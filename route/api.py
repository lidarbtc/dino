from urllib.parse import urlparse, parse_qs
import requests
import json

def taobao(url):
    headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
    }
    params = parse_qs(urlparse(url).query)
    id = params['id'][0]
    result = requests.get('https://api-gw.onebound.cn/taobao/item_get/?key=t_821022925423&secret=20211011&num_iid={}&is_promotion=1'.format(id), headers=headers)
    result = r"{}".format(result)
    return json.loads(result)