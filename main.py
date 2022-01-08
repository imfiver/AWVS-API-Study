import requests
import json

# Disable SSL warnings关闭https 证书警告
try:
    import requests.packages.urllib3

    requests.packages.urllib3.disable_warnings()
except Exception:
    pass

"""
curl 写法
curl "https://192.168.1.95/api/v1/me"
 -H 'Content-Type: application/json;charset=utf8' 
 -H 'X-Auth: 1986ad8c0a5b3df4d7028d5f3c06e936c655a098a7a1146fcbfe78d7b46cfc7c4' -k
"""

api_key = "1986ad8c0a5b3df4d7028d5f3c06e936c655a098a7a1146fcbfe78d7b46cfc7c4"
api_urls = "https://192.168.1.95/api/v1/"
headers = {
    'X-Auth': api_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json;charset=utf8'
}
print(headers)
"""
查看账户信息: /api/v1/me            GET
证书信息: /api/v1/me               GET
节点引擎信息: /api/v1/workers       GET
通知信息: /api/v1/notifications     GET
Dashboard信息:  /api/v1/me/stats    GET
/api/v1/targets
"""


def get_me():
    """
    查看账户信息
    Method:GET
    URL: /api/v1/me
    """
    url = api_urls + "me"
    print(url)
    try:
        r = requests.get(url=url, headers=headers, verify=False)
        print(r.text)

    except:
        pass


def get_info():
    """
    证书信息
    Method:GET
    URL: /api/v1/info
    :return:
    """
    url = api_urls + "info"
    try:
        r = requests.get(url=url, headers=headers, verify=False)
        print(r.text)
    except:
        pass


def api_get_test(test):
    url = api_urls + test
    print(url)
    try:
        r = requests.get(url=url, headers=headers, verify=False)
        print(r, r.text)
    except:
        pass


def api_post_test(test="targets"):
    url = api_urls + test
    print(url)

    data = {
        "address": "https://blog.ryzezr.com",
        "description": "xxxxx",
        "criticality": 30
    }
    data = json.dumps(data)
    print(data)
    try:
        r = requests.post(url, data=data, headers=headers, verify=False)
        print(r, r.text)
    except:
        pass


# api_get_test(test="targets")
api_post_test()

