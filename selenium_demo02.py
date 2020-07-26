from selenium import webdriver
from lxml import etree

# path of chromedriver,need to be changed by yourself
drive_path=r"E:\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=drive_path)
driver.get('https://tieba.baidu.com/f?kw=%BD%E4%C9%AB')

article_xpath='//*[@id="thread_list"]/li'
title_xpath='/div/div[2]/div[1]/div[1]/a'
content_xpath='/div/div[2]/div[2]/div[1]/div'

article_titles=driver.find_elements_by_xpath(article_xpath+title_xpath)
article_contents=driver.find_elements_by_xpath(article_xpath+content_xpath)

for i in range(len(article_titles)):
    print("title:   "+article_titles[i].text)
    print("content: "+article_contents[i].text)

driver.close()
driver.quit()