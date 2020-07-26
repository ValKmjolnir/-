from selenium import webdriver
from lxml import etree

# path of chromedriver,need to be changed by yourself
drive_path=r"E:\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=drive_path)
driver.get('https://tieba.baidu.com/f?kw=%BD%E4%C9%AB')

html_src=driver.page_source
xml_src=etree.HTML(html_src)
article_xpath='//*[@id="thread_list"]/li'
title_xpath='./div/div[2]/div[1]/div[1]/a/text()'
content_xpath='./div/div[2]/div[2]/div[1]/div/text()'

articles=xml_src.xpath(article_xpath)
print(articles)
article_titles=[]
article_contents=[]
for i in range(1,len(articles)):
    article_titles.append(articles[i].xpath(title_xpath))
    article_contents.append(articles[i].xpath(content_xpath))

for i in range(len(article_titles)):
    print("title: "+article_titles[i][0])
    print("content: "+article_contents[i][0].replace("\n","").strip())
driver.close()
driver.quit()