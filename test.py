import requests
import json
base_url='http://127.0.0.1:8000/'
endpoint='fullthrottle/'


def resoure():
    resp=requests.get(base_url+endpoint)
    print(resp.status_code)
    print(json.dumps(resp.json(),indent=4))
resoure()