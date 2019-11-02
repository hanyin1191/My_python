'''-------------PYTHON request------------'''

#导入库
import urllib.request		#python3 use "urllib.request" replace "urllib2"

urllib.requset.Request(url, data = None, headers ={}, origin_req_host = None, unverifiable = False, method = None)
												#headers is a dict.
												#Request is a class.

urllib.request.urlopen(url, data = None, [timeout,]*, cafile = None, capath = None, context = None)
												#data -->  POST request. type is bytes flow, can use bytes() to translate. 
												#cafile & capath --> CA, when use the HTTPS
												#context --> set SSL 

'''-----------------requests----------------------'''
import requests

Response_get = requests.get(url, params = None, **Kwargs)
Response_post = requests.post(url, data = None,json = None, *kwargs)

Response_get.text	#---> string type
Response_get.content#--->bytes type
Response_get.json	#--->json type
r.status_code		#return 200 means succcess.
r.encoding 			#从HTTP header中猜测的响应内容编码方式。
r.apparent_encoding	#从内容中分析处的响应内容编码方式（备选编码方式）

'''------------------urlparse----------------'''
import urllib.parse 				#this model uesd to analysis url.

urllib.parse.urlparse(URL)			#return a ParseResult object.

from urllib.parse import *

# 解析URL字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
# 通过属性名和索引来获取URL的各部分
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())

result = urlunparse(('http', 'www.crazyit.org:80', 'index.php',		#urlunparse() used to combine to get a URL.
    'yeeku', 'name=fkit', 'frag'))
print('URL为:', result)

parse_qs()			#this two func used to analysis require string(bytes type),return a dict.
parse_qsl()			#return a list.
					#and the urlencode() is Inverse func.

urllib.parse.urlencode(query)		#translate the dict or list parameter to require string.


#  urljoin() used to combine two url 
#被拼接URL不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result) # http://www.crazyit.org/users/help.html
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result) # http://www.crazyit.org/users/book/list.html
# 被拼接URL以斜线（代表根路径path）开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result) # http://www.crazyit.org/help.html
# 被拼接URL以双斜线（代表绝对URL）开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result) # http://help.html



'''----------------BeautifulSoup----------------------'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')		#use BeautifulSoup model Analysis the html Object.

findAll(tag, attributes, recursive, text, limit, keywords)		#return a list of all matching results.
find(tag, attributes, recursive, text, keywords)				#return the first matching result.


name_box = soup.find('h1', attrs = {'class' : 'name'})
name = name_box.text.strip()					#strip() used to remove the beginning and ending character of string.

ul = find_all('ul')






#导入python csv和datatime模块
import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file:		#write into excel.
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])


data.append((name, price))		#append tuple.

str.split(str ='', num = string.count(str))		#split string using str.return a sting list.

data = bytes(string, encoding = 'utf-8')		#using bytes() translate the string to byte flow.