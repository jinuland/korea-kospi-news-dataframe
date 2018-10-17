#-*- coding: utf-8 -*-
import requests
import kospi_dic
import re
import pandas as pd
article = re.compile( r'.*<a href="(.*)" class="tit".*target=_top>(?:<span class="ico_reply"></span>)?(.*)</a>.*')
date = re.compile( r'.*<td class="date"> (.*)</td>.*')
source = re.compile(r'.*<td class="info">(.*)</td>.*')

titleList = []
urlList = []
dateList = []
sourceList = []
itemList = []
kospi_dic =  kospi_dic.get_kospi_dic()
def getArticles( kospi_list, pages ) :
    for item in kospi_list :
        for page in range(pages) :
            page +=1
            r = requests.get("https://finance.naver.com/item/news_news.nhn?code={}&page={}&sm=title_entity_id.basic&clusterId=".format(kospi_dic[item], page))
            lines = str(r.content).decode(r.encoding).splitlines()
            for line in lines :
                articleMatch = article.match(line)
                if articleMatch :
                    titleList.append(re.sub('&[a-z]+;','',articleMatch.group(2)))
                    urlList.append('https://finance.naver.com' + articleMatch.group(1))
                dateMatch = date.match(line)
                if dateMatch :
                    dateList.append(dateMatch.group(1))
                sourceMatch = source.match(line)
                if sourceMatch :
                    sourceList.append(sourceMatch.group(1))
                    itemList.append(item)
    data = {
        "stock" : itemList,
        "title" : titleList,
        "url" : urlList,
        "date" : dateList,
        "source" : sourceList
    }
    return pd.DataFrame(data)

