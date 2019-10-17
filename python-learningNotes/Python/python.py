import requests
import re
url = 'https://www.biqugex.com/book_139/47639799.html'
html = requests.get(url)
html.encoding = 'gb2312'

#print(html.text)
content = re.findall(r'<div id="content" class="showtxt">(.*?)<br /><br />　　',html.text)
#print(content)
content2 = re.findall(r'\u3000\u3000\u3000\u3000(.*?)<br />',content[0])
page = ''
for i in content2:
    page += i
print(page)
f = open('元尊.txt')
f.write(page)