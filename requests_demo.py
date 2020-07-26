import requests
from lxml import etree


response=requests.get('https://tieba.baidu.com/f?kw=%BD%E4%C9%AB')
xml_src=etree.HTML(response.content.decode("utf-8"))

article_xpath='//*[@id="thread_list"]/li'
title_xpath='./div/div[2]/div[1]/div[1]/a/text()'
content_xpath='./div/div[2]/div[2]/div[1]/div/text()'

articles=xml_src.xpath(article_xpath)
article_titles=[]
article_contents=[]
for i in range(1,len(articles)):
    article_titles.append(articles[i].xpath(title_xpath))
    article_contents.append(articles[i].xpath(content_xpath))
for i in range(len(article_titles)):
    print("title: "+article_titles[i][0])
    print("content: "+article_contents[i][0].replace("\n","").strip())