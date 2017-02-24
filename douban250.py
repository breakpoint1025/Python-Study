import urllib.request 
import re
from bs4 import BeautifulSoup


#设置代理
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http" : 'http://coliu:Amazon!3@sdcwsa01.commscope.com:80',
                                             "https" : 'http://coliu:Amazon!3@sdcwsa01.commscope.com:80'})
null_proxy_handler = urllib.request.ProxyHandler({})

#设置登录信息
#authinfo = urllib.request.HTTPBasicAuthHandler()
#authinfo.add_password(realm='PDQ Application',
#                      uri='https://mahler:8092/site-updates.py',
#                      user='klem',
#                      passwd='geheim$parole')

if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)

urllib.request.install_opener(opener)


#封装url请求 伪装成浏览器请求
url = 'https://movie.douban.com/top250'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
req = urllib.request.Request(url, headers = headers)

#抽取主页面是所有的分页链接
response = urllib.request.urlopen(req)
soup = BeautifulSoup(response, "html.parser")
urllist = ['https://movie.douban.com/top250']
for url in soup.findAll("a"):
    if re.match(r'.*?start=\d{2,3}&filter=.*', url['href']):
        print(url['href'])
        urllist.append('https://movie.douban.com/top250'+url['href'])


#逐页打印电影信息
def printmovieinfo(urllist, headers):
    for url in urllist:
        req = urllib.request.Request(url, headers = headers)
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response, "html.parser")
        content = soup.find('ol')
        for child in content.children:
            if child.name == 'li':
                a = child.find('em')
                b = child.find('span', class_='title')
                c = child.find('span', class_='rating_num')
                d = child.find('span', class_='inq')
                print (a.text + '. <<' + b.text + '>> ' + c.text + ' \"' + d.text + '\"')


printmovieinfo(urllist, headers)

