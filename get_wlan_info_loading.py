#import ssl
import requests
import json
import time
import random
import os
from selenium import webdriver

from requests.packages.urllib3.exceptions import InsecureRequestWarning

__metaclass__ = type
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#global User_agent, IP


class WlanGet:

  def __init__(self):

        #def init_Ip_Useragent():
      
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
        
        #global User_agent
        #global IP

        self.User_agent = random.choice(USER_AGENTS)
        self.IP = {"http":random.choice(IP_AGENTS)} 
        self.cookie_handle = open('C://Users/hanyh_/Desktop/cookie.txt', mode = 'a+')
        self.REREAD = False
        self.info = { }


  def get_Cookie(self):

          print("Simulated Firefox browser...")
          browser = webdriver.Firefox()
          
          print("Finished")

          print("Connect the Webpage and Login...")
          browser.get('https://192.168.1.20/survey.json.cgi')

          elem_Username = browser.find_element_by_id('username')
          elem_Username.send_keys('ubnt')

          elem_Password = browser.find_element_by_id('password')
          elem_Password.send_keys('ubnt')

          elem_Login = browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/input")
          elem_Login.click()


          print("Finished,then get Cookie...")
          cookie_temp = browser.get_cookies()
          Cookie = (cookie_temp[0]['name'] + '=' + cookie_temp[0]['value'])

          browser.close()
          os.system(r'taskkill /F /IM geckodriver.exe')
          print(Cookie)
          print("All Preparations are Completed.")
      
          self.cookie_handle.write(Cookie)

          print(Cookie)
          

  
  '''
  def check_cookie(self):

          if(self.cookie_handle.read() == ''):
            self.REREAD = TRUE
  '''
        
  def get_WlanInfo(self,url):
        
        #print("Get Wlan Information and Ignore the SSL Warning. ")
        #ssl._create_default_https_context = ssl._create_unverified_context  #Cancel SSL

        url_record = url

        Cookie = self.cookie_handle.read()
        print("________")
        print(Cookie)
        
        headers = {
          'User_agent': self.User_agent, 
          'Cookie': Cookie,
          'Connection': 'keep-alive',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Host': '192.168.1.20',
          'Referer': 'https://192.168.1.20/survey.cgi?mode=tool',
          'X-Requested-With': 'XMLHttpRequest'
          }

        
        req = requests.get(url_record, headers = headers, proxies = self.IP, verify = False)
        
        try:
          self.info = json.loads(req.text)
          print(type(self.info))
          print("The get_WlanInfo has done.")
          #print(req.text)
          #return(json_data)
        except Exception:
          print("Exception!!!!")
          self.REREAD = True

      
def write_WlanInfo(information):

      print("Record Wlan Data to Text File")

      with open('C://Users/hanyh_/Desktop/data.txt', mode = 'w') as information:
        for info in information:
              list = [info['mac'], '\t', info['essid'], '\t', \
                  info['frequency'],'\t',info['channel'],'\t',info['signal_level']]
              file_handle.writelines(list)
              file_handle.write('\n')

      time.sleep(1)
      print("Write Finished")

      

if __name__ == "__main__":

      url = "https://192.168.1.20/survey.json.cgi"

      wlanget = WlanGet()  #define an instance of a  WlanGet class and initialiazation

      #wlanget.check_cookie()  # check if there already is cookie information

      wlanget.get_WlanInfo(url)
      
      if(wlanget.REREAD == True):  #whether need reread the cookie information
        wlanget.get_Cookie()
        wlanget.get_WlanInfo(url)  #get the wlan information use cookie


      write_WlanInfo(wlanget.info)
      time.sleep(1)
      
      print("All Finished")
      print("Please enter any key to close.")




         



