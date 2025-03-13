



from bs4 import BeautifulSoup
import requests

url = "https://www.baidu.com"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content)

print(soup.prettify())

# 获取所有class='entry-title'的h2标签
tags = soup.find_all('a', class_='mnav')
print(tags)
# for tag in tags:
#     a_tag = tag.find('a')
#     print('Title:[%s], URL:[%s]' %(tag.text, a_tag['href']))