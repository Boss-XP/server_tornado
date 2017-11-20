import urllib3
import django

def getRequest(url):
    hhttp = urllib3.PoolManager()
    resp = hhttp.request('GET', url)
    print("get response==")
    print(resp.data)



def postRequest(url, data):
    hhttp = urllib3.PoolManager()
    resp = hhttp.request('POST',
                         url,
                         fields={'body':data},
                         )
    print("post response==")
    print(resp.data)



# getRequest('http://localhost:8000')
# getRequest('http://localhost:8000/login')
# getRequest('http://localhost:8000/')
# getRequest('http://localhost:8000/login')
# getRequest('http://localhost:8000/login')
# getRequest('http://localhost:8000/login')
#
# postRequest('http://localhost:8000','d')
# postRequest('http://localhost:8000/login','d')
# postRequest('http://localhost:8000','d')
# postRequest('http://localhost:8000/login','d')
# postRequest('http://localhost:8000/login','d')






# print(getRequest('http://localhost:8000'))
# print(getRequest('http://localhost:8000/login'))
# print(getRequest('http://localhost:8000/'))
# print(getRequest('http://localhost:8000/login'))
# print(getRequest('http://localhost:8000/login'))
# print(getRequest('http://localhost:8000/login'))
#
# print(postRequest('http://localhost:8000','d'))
# print(postRequest('http://localhost:8000/login','d'))
# print(postRequest('http://localhost:8000','d'))
# print(postRequest('http://localhost:8000/login','d'))
# print(postRequest('http://localhost:8000/login','d'))