# korea-kospi-news-dataframe
simple python code which create data frame that contains news airticles about kospi stocks

# usage

> import kospi as kospi
> df = kospi.getArticles($STOCK_NAME_LIST, $PAGE_COUNT_TO_CRAWL_EACH_STOCK)

> kospi.getArticles(['삼성전자','SK텔레콤'], 3 )

crawl the list of news articles related to Samsung Electronics and SK Telecom by 3 pages and return to the dataframe.

# example 

```python
Python 2.7.5 (default, Nov  6 2016, 00:28:07) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> #-*- coding: utf-8 -*-                                                             
... import kospi as kospi                                                              
       
print 'SK텔레콤의 title 4개 출력'                                                  
print sk_df.title[0:4]                                                             
print '=============================='                                             
print '전체에서 뉴스메체별 count'                                                  
print df.groupby(['stock','source']).agg('count')>>>                                                                                    
... df = kospi.getArticles(['삼성전자','SK텔레콤'], 3 )                                

>>>                                                                                    
... samsung_df =  df[df.stock == '삼성전자']                                           
>>> sk_df = df[df.stock == 'SK텔레콤']                                                 
>>>                                                                                    
... print '=============================='                                             
==============================
>>> print '삼성전자의 title 2개 출력'                                                  
삼성전자의 title 2개 출력
>>> print samsung_df.title[0:2]                                                        
0    삼성전자, C랩 노하우로 500개 스타트업 육성
1             韓유니콘 기업 삼성전자가 키운다
Name: title, dtype: object
>>> print '=============================='                                             
==============================
>>> print 'SK텔레콤의 title 4개 출력'                                                  
SK텔레콤의 title 4개 출력
>>> print sk_df.title[0:4]                                                             
68         SK텔레콤, 개발문턱 낮춘 누구 오픈플랫폼 공개..데이터도 공유해요
69             SKT, 개발 문턱 낮춘 오픈플랫폼 '누구 디벨로퍼스' 공개
70    NH농협카드, SKT단말기 및 통신요금 할인 'NH농협 T라이트카드' ...
71             NH농협카드, SKT 단말기요금 할인 NH농협 T라이트 출시
Name: title, dtype: object
>>> print '=============================='                                             
==============================
>>> print '전체에서 뉴스메체별 count'                                                  
전체에서 뉴스메체별 count
>>> print df.groupby(['stock','source']).agg('count')
              date  title  url
stock source                  
SK텔레콤 매일경제      13     13   13
      머니투데이      9      9    9
      서울경제       1      1    1
      아시아경제      7      7    7
      이데일리       4      4    4
      조선비즈       1      1    1
      조세일보       2      2    2
      파이낸셜뉴스    15     15   15
      한국경제       4      4    4
      헤럴드경제      6      6    6
삼성전자  매일경제      11     11   11
      머니투데이      6      6    6
      서울경제       3      3    3
      아시아경제      6      6    6
      이데일리      11     11   11
      조선비즈       1      1    1
      조세일보       1      1    1
      파이낸셜뉴스     6      6    6
      한국경제      16     16   16
      헤럴드경제      7      7    7
>>> print(df.to_string())
                 date  source  stock                                       title                                                url
0    2018.10.17 18:44    서울경제   삼성전자                  삼성전자, C랩 노하우로 500개 스타트업 육성  https://finance.naver.com/item/news_read.nhn?a...
1    2018.10.17 17:01    이데일리   삼성전자                           韓유니콘 기업 삼성전자가 키운다  https://finance.naver.com/item/news_read.nhn?a...
2    2018.10.17 17:02    매일경제   삼성전자            삼성전자, 5년간 500개 사내외 스타트업 과제 본격 육성  https://finance.naver.com/item/news_read.nhn?a...
3    2018.10.17 17:01    한국경제   삼성전자             삼성전자, 신생 스타트업에 '6년산 창업 비결' 전수한다  https://finance.naver.com/item/news_read.nhn?a...
4    2018.10.17 17:00   머니투데이   삼성전자              삼성전자, C랩 외부 개방5년간 500개 스타트업 육성  https://finance.naver.com/item/news_read.nhn?a...
5    2018.10.17 17:00  파이낸셜뉴스   삼성전자                      삼성전자, 5년간 스타트업 500개 육성  https://finance.naver.com/item/news_read.nhn?a...
6    2018.10.17 17:00   헤럴드경제   삼성전자      삼성전자, 사내 스타트업 육성 C랩 외부로 확대스타트업 생태계 ...  https://finance.naver.com/item/news_read.nhn?a...
7    2018.10.17 17:01    조선비즈   삼성전자      스마트벤처 스타트업 서큘러스모인, 삼성전자 C-Lab 프로그램에 선정  https://finance.naver.com/item/news_read.nhn?a...
8    2018.10.17 16:43   머니투데이   삼성전자                      NIPA 신임원장에 김창용 삼성전자 고문  https://finance.naver.com/item/news_read.nhn?a...
9    2018.10.17 15:42    한국경제   삼성전자              코스피, 미국 증시 급등에 상승삼성전자SK하이닉스 1%  https://finance.naver.com/item/news_read.nhn?a...
10   2018.10.17 09:14    한국경제   삼성전자                코스피, 미국발 훈풍에 상승삼성전자SK하이닉스 1%  https://finance.naver.com/item/news_read.nhn?a...
11   2018.10.17 13:30  파이낸셜뉴스   삼성전자            에이스침대, 삼성전자와 콜라보 행사 롯데하이마트몰에서 진행  https://finance.naver.com/item/news_read.nhn?a...
12   2018.10.17 10:24   아시아경제   삼성전자                에이스침대, 하이마트쇼핑몰서 삼성전자와 공동 기획전  https://finance.naver.com/item/news_read.nhn?a...
13   2018.10.17 09:33    서울경제   삼성전자                 혼수 고민 그만 에이스침대삼성전자 '컬래버 행사'  https://finance.naver.com/item/news_read.nhn?a...
14   2018.10.17 09:05    이데일리   삼성전자                에이스침대삼성전자, 신혼부부 겨냥 콜래보레이션 진행  https://finance.naver.com/item/news_read.nhn?a...
15   2018.10.17 11:27   아시아경제   삼성전자       종 잡을 수 없는 삼성전자 목표주가, 최대 2만원 격차 '천차만별'  https://finance.naver.com/item/news_read.nhn?a...
16   2018.10.17 11:03    매일경제   삼성전자         삼성전자, 차세대 네트워크 서비스 분석 솔루션 기업 지랩스 인수  https://finance.naver.com/item/news_read.nhn?a...
```

