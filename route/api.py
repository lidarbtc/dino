from urllib.parse import urlparse, parse_qs
import requests
import json

def taobao(url):
    headers = {
    "Accept-Encoding": "gzip",
    "Connection": "close"
    }
    result = requests.get('https://api-gw.onebound.cn/taobao/item_get/?key=t_821022925423&secret=20211011&num_iid={}&is_promotion=1'.format(url), headers=headers)
    
    return result.json()