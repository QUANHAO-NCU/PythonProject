import requests,re
url = 'http://longzu5.net/post/334.html'
html = requests.get(url)
html.encoding = 'utf-8'
print(html.text)
# content = re.findall(r'<div id="content" name="content">(.*?)</div>\
#          <center><script>yuedu_bottom1();</script></center>',html.text)
# print(content)
# content2 = re.findall(r'\u3000\u3000\u3000\u3000(.*?)<br />',content[0])
# page = ''
# for i in content2:
#     page += i
# print(page)
# f = open('元尊.txt')
# f.write(page)