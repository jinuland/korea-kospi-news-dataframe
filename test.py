#-*- coding: utf-8 -*-
import kospi as kospi

df = kospi.getArticles(['삼성전자','SK텔레콤'], 3 )

samsung_df =  df[df.stock == '삼성전자']
sk_df = df[df.stock == 'SK텔레콤']

print '=============================='
print '삼성전자의 title 2개 출력'
print samsung_df.title[0:2]
print '=============================='
print 'SK텔레콤의 title 4개 출력'
print sk_df.title[0:4]
print '=============================='
print '전체에서 뉴스메체별 count'
print df.groupby(['stock','source']).agg('count')


