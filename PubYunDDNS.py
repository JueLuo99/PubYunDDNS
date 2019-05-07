import requests
import base64


# 需要更新的帐号密码和域名
username = ""
password = ""
hostname = ""




def update(auth):

    url = "http://members.3322.net/dyndns/update?hostname="+hostname
    headers = {"Host": "members.3322.net", "Authorization": "Basic "+auth.decode(), "User-Agent": "myclient/1.0 me@null.net"}
    print(requests.get(url=url, headers=headers).text)

auth = base64.b64encode((username+":"+password).encode())
update(auth)