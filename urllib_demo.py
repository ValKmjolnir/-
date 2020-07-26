import urllib
import urllib.request
from lxml import etree


url='https://tieba.baidu.com/f?kw=%BD%E4%C9%AB'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)

html_src=response.read().decode("utf-8")
# 百度贴吧你妈死了，主页内容用注释括起来，傻逼东西
html_src=html_src.replace("<!--","")
html_src=html_src.replace("-->","")
xml_src=etree.HTML(html_src)

article_xpath='//*[@id="thread_list"]/li'
title_xpath='/div/div[2]/div[1]/div[1]/a/text()'
content_xpath='/div/div[2]/div[2]/div[1]/div/text()'

article_titles=xml_src.xpath(article_xpath+title_xpath)
article_contents=xml_src.xpath(article_xpath+content_xpath)
for i in range(len(article_titles)):
    print("title: "+article_titles[i])
    print("content: "+article_contents[i].replace("\n","").strip())