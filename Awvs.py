import requests
import json

# 关闭https证书警告
try:
    import requests.packages.urllib3

    requests.packages.urllib3.disable_warnings()
except Exception:
    print("SSL 警告关闭失败")
    pass


# 调用Awvs的类
class Awvs:
    r"""

    """

    def __init__(self, api_url: str, api_key: str):
        r"""
        :param api_url: AWVS提供的API URL
        :param api_key: AWVS提供的API KEY
        """
        # 判断用户输入的URL结尾是否有 "/"
        self.api_url = api_url + "/" if api_url[-1] != "/" else api_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "X-Auth": api_key,
        }

    def info(self):
        r"""
        证书信息 License
        Method: GET
        URL: /api/v1/info
        :return:
        """
        url = self.api_url + "info"

        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)

        except Exception:
            print("链接失败")

    def me(self):
        r"""
        账户信息
        Method:GET
        URL: /api/v1/me
        :return:
        """
        url = self.api_url + "me"
        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)
        except Exception:
            print("链接失败")

    def workers(self):
        r"""
        节点引擎信息
        Method:GET
        URL: /api/v1/workers
        :return:
        """
        url = self.api_url + "workers"
        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)
        except Exception:
            print("链接失败")

    def notifications(self):
        r"""
         通知信息
         Method:GET
         URL: /api/v1/notifications
         :return:
         """
        url = self.api_url + "notifications"
        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)
        except Exception:
            print()

    def stats(self):
        r"""
        Dashboard 信息
        Method:GET
        URL: /api/v1/me/stats
        :return:
        """
        url = self.api_url + "me/stats"
        # print(url)
        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)
        except Exception:
            print("链接失败")

    def targets(self):
        r"""
        所有目标信息
        Method:GET
        URL: /api/v1/targets
        :return: 
        """
        url = self.api_url + "targets"
        try:
            r = requests.get(url=url, headers=self.headers, verify=False, timeout=30)
            print(r.text)
        except Exception:
            print("获取所有目标信息失败")

    def targets_threat(self, _threat, _criticality):
        r"""
        筛选目标信息
        :param _threat:
        :param _criticality:
        Method:GET
        URL: /api/v1/targets?q=threat:{list};criticality:{list};
        :return:
        """
        url = self.api_url + "targets"

        r"""
        _threat                  _criticality
        3: High                  30: Critical
        2: Medium                20: High
        1: Low                   10: Normal
        0: Informational         0: Low                        
        """
        query = {
            "threat": _threat,
            "criticality": _criticality,
        }
        try:
            r = requests.get(url=url, headers=self.headers, params=query, verify=False, timeout=30)
            print(r.url)
            print(r.text)
        except Exception as e:
            print(e)

    def add_target(self, address: str, criticality, description):
    # test
    def get_api_url(self):
        print(self.api_url)

    def get_api_key(self):
        print(self.api_key)

    def get_headers(self):
        print(self.headers)


# TEST
api_url = "https://192.168.1.95/api/v1"
api_key = "1986ad8c0a5b3df4d7028d5f3c06e936c655a098a7a1146fcbfe78d7b46cfc7c4"

awvs = Awvs(api_url, api_key)

# awvs.targets_threat("1,3", "10,30")
# awvs.targets()
# awvs.stats()
# awvs.notifications()
# awvs.workers()
# awvs.me()
# awvs.info()
# awvs.get_headers()
# awvs.get_api_url()
# awvs.get_api_key()
