import urllib.request 


#设置代理
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http" : 'http://coliu:Amazon!3@sdcwsa01.commscope.com:80'})
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
#url = 'http://www.baidu.com'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
#values = {'username' : 'cqc',  'password' : 'XXXX' }  
#headers = { 'User-Agent' : user_agent }  
#data = urllib.urlencode(values)  
url = 'http://www.baidu.com/'
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})

oper = urllib.request.urlopen(req)
data = oper.read()
print(data.decode())