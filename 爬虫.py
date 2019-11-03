import re
import requests
import random
import time
from bs4 import BeautifulSoup
#from itertools import *

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
        "http://101.231.50.154:8000", 
        "http://221.178.232.130:8080",
        "http://106.52.181.184:80",
        "http://101.231.50.154:8000"
        ]
     
proxies={"http":random.choice(IP_AGENTS)}

headers = {

    'User-Agent' : random.choice(USER_AGENTS)
    #'cookie' : "lastCity=101010100; __a=84598353.1572346493.1572356566.1572750546.57.3.44.44; _uab_collina=157234649310747432600103; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1572750546,1572763137,1572763733,1572763901; sid=sem_pz_bdpc_dasou_title; __c=1572750546; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0luu-0KZEgsZrwQ4I0000079yiNC00000X5wJqM.THdBULP1doZA8QMu1x60UWdVUv4_py4-g1wxuAT0T1d-uj0LnW6znj0snjndmHfk0ZRqwHwjPRcvfRRLPRfzwbnswjNDfHuaPj7DrH04n1Rdn1n0mHdL5iuVmv-b5HnzrHnkPWm4nHbhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1YdPjf1nf%26tpl%3Dtpl_11534_19968_16032%26l%3D1514755672%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3293166919_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D136%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_4_dg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26oq%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26rqlang%3Dcn&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1572766282; __zp_stoken__=6f43LeglXM%2Bh7Q21OR3dIA%2BSkF%2FbrsxxjMRHINYvPGzd81gW6k3fxmgqOzMKCfer%2BDDktYrc0uY9LqoCSIpAFZVUuQ%3D%3D; JSESSIONID=""; __zp_sseed__=G2Jtn0OhKZ9/lNEp+Yp1IEIX8oYwVbbKrdvY/4NkqJE=; __zp_sname__=f53019a5; __zp_sts__=1572766562179"
    
    }

cookie_dict = {
    
    'Cookie' : "lastCity=101010100; __a=84598353.1572346493.1572356566.1572750546.75.3.62.62; _uab_collina=157234649310747432600103; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1572750546,1572763137,1572763733,1572763901; sid=sem_pz_bdpc_dasou_title; __c=1572750546; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0luu-0KZEgsZrwQ4I0000079yiNC00000X5wJqM.THdBULP1doZA8QMu1x60UWdVUv4_py4-g1wxuAT0T1d-uj0LnW6znj0snjndmHfk0ZRqwHwjPRcvfRRLPRfzwbnswjNDfHuaPj7DrH04n1Rdn1n0mHdL5iuVmv-b5HnzrHnkPWm4nHbhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1YdPjf1nf%26tpl%3Dtpl_11534_19968_16032%26l%3D1514755672%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3293166919_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D136%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_4_dg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26oq%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26rqlang%3Dcn&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1572769983; __zp_stoken__=6f43LeglXM%2Bh7Q21OR3dIA%2BSkGyO3%2BHtnLMSYC6THRz3F0tNrqdmFpQXXL4P%2B1qOnVGQqnNhedhDReDXr65LFJ9Egw%3D%3D; JSESSIONID=""; __zp_sseed__=G2Jtn0OhKZ9/lNEp+Yp1IPDJfoa9v+b8FWC0AtfHUKw=; __zp_sname__=f53019a5; __zp_sts__=1572770129854"
    
    }

cookie = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar = None, overwrite = True)

s = requests.Session()
s.cookies = cookie
 

url = "https://www.zhipin.com"

job_list = []

def jobs(page):

    for i in range(1, page+1):
        
        
        try:
            print("第%s页数据" % i)
            uri = "/c101010100/?query=python&page=%s" % i
            print(url + uri)
            
            #response = requests.get(url + uri, headers = headers, proxies = proxies)
            response = s.get(url + uri, headers = headers, proxies = proxies)
            print(response.status_code)
            if(i == 1):
                print(response.text)

            content = BeautifulSoup(response.text, 'html.parser')
            
            ul = content.find_all('ul')

            jobs = ul[12].find_all('li')

            rege = r'<p>([\u4e00-\u9fa5 ]+)<em class="vline"></em>([\d+-年]+|[\u4e00-\u9fa5]+)<em class="vline"></em>([\u4e00-\u9fa5]+)'

            pattern = re.compile(rege)

            for job in jobs:
                
                job_dict = {}
                job_details_uri = job.find('h3', attrs = {'class' : 'name'}).find('a')['href']
                job_company = job.find('div', attrs = {'class' : 'company-text'}).find('h3', attrs = {'class' : 'name'}).find('a').text
                job_salary = job.find('h3', attrs = {'class' : 'name'}).find('span', attrs = {'class' : 'red'}).text
                job_details = str(job.find('p'))
                job_rege = pattern.match(job_details)
                
                
                job_dict['name'] = job_company
                job_dict['uri'] = job_details_uri
                job_dict['salary'] = job_salary
                try:
                    job_dict['site'] = job_rege.group(1)
                    job_dict['year'] = job_rege.group(2)
                    job_dict['edu'] = job_rege.group(3)
                except:
                    continue

                job_list.append(job_dict)
            time.sleep(1)
        except:
            continue

    #for job in job_list:
            #print(job)

def get_job_details(job_list):
    
    job_details = []

    for job_dict in job_list:

        company_uri = job_dict['uri']
        company_name = job_dict['name']
        print(url + company_uri)
        try:
            #res = requests.get(url + company_uri, headers = headers, proxies = proxies)
            res = s.get(url + company_uri, headers = headers, proxies =proxies)
            
            content = BeautifulSoup(res.text, 'html.parser')
            temp = content.find('div', attrs = {'class' : 'text'})
            print(temp.prettify())
            text = temp.text.strip() 
            result = {'name' : company_name, 'details' : text}
            
            job_details.append(result)
                
        except:
            continue

    for job in job_details:
        print(job)
    


if __name__ == "__main__":
    
    jobs(2)
    get_job_details(job_list)
    































