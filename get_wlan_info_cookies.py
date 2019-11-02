# -*- coding: utf-8 -*-


import requests
import random
import json
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def GetWlanInfo():
    
    USER_AGENTS = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
            ]

    IP_AGENTS = [
            "http://58.240.53.196:8080", 
            "http://219.135.99.185:8088",
            "http://117.127.0.198:8080",
            "http://58.240.53.194:8080"
            ]
         
    proxies={"http":random.choice(IP_AGENTS)}

    time.sleep(1)

    
     
    url = "https://192.168.1.20/survey.json.cgi"
    
    Cookie = "AIROS_SESSIONID = 672281f83ae11e6277ced79f1a3525ab"

    
    '''
    session = requests.Session()
    headers = {'user-agent':'Mozilla/5.0'}
    req = session.get(url, headers = headers, verify = False)
    temp_Dict = session.cookies.get_dict()
    temp_Cookie = temp_Dict['AIROS_SESSIONID']
    Cookie = 'AIROS_SESSIONID=' + temp_Cookie
    print(temp_Dict)
    
    '''
    header = {
        'User-agent': random.choice(USER_AGENTS), 
        'Cookie': Cookie,
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Host': '192.168.1.20',
        'Referer': 'https://192.168.1.20/survey.cgi?mode=tool',
        'X-Requested-With': 'XMLHttpRequest'
    }


    #设置url get请求的参数
    data={
          "iface" : "ath0"
          }


    req=requests.get(url,data,headers = header,proxies = proxies,verify = False)

    print(req.status_code)

    print(req.text)


    return(json.loads(req.text))




    


def WriteTxt(info):
    
    file_handle = open('D://c++/data.txt', mode = 'w')

    for dir in info:
        
        list = [dir['mac'], '\t', dir['essid'], '\t', \
                dir['frequency'],'\t',dir['channel'],'\t',dir['signal_level']]
        file_handle.writelines(list)
        file_handle.write('\n')
        
    file_handle.close()

    print("finish")
    time.sleep(1)


if __name__ == "__main__":

    info = GetWlanInfo()

    #WriteTxt(info)

    print("OK")

    enter = input("please enter any key to close:")





