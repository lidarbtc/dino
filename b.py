import a
import json

result = a.a
product_id = str(result['item']['num_iid']) # 상품번호
title = result['item']['title'] # 상품제목
price = result['item']['price'] # 상품 가격(할인 적용)
original_price = result['item']['orginal_price'] # 상품 가격 (할인 미적용)
product_imgurl = result['item']['item_imgs']#[0]['url'] # 상품 사진 링크
#prop = result['item']['prop_imgs']['prop_img'][0]['properties'] # 옵션
prop_price = result['item']['skus']['sku']#[0]['price'] # 옵션 가격 (할인 적용)
prop_originalprice = result['item']['skus']['sku']#[0]['orginal_price'] # 옵션 가격 (할인 미적용)
prop_imgurl = result['item']['prop_imgs']['prop_img']#[0]['url'] # 옵션 사진 링크
propname = result['item']['skus']['sku']#[0]['properties_name'] # 옵션 이름
propid = str(result['item']['skus']['sku'])#[0]['sku_id']) # 옵션 id
desc_imgurl = result['item']['desc_img']

#for i in prop_imgurl:
#    print(i["url"])

b = r'{"item":{"num_iid":"600448952765","title":"新款多功能活氧微雾机焗油机家用蒸发机蒸汽机护发机超声波臭氧机","desc_short":"","price":"580","total_price":0,"suggestive_price":0,"orginal_price":"580.00","nick":"亲亲爱尚潮流","num":"200","min_num":0,"detail_url":"https:\/\/item.taobao.com\/item.htm?id=600448952765","pic_url":"\/\/img.alicdn.com\/imgextra\/i2\/2491925690\/O1CN01BOljSm1ru4AQ8wuoW_!!2491925690.jpg","brand":"","brandId":null,"rootCatId":"50002768","cid":"50024628","crumbs":[],"created_time":"","modified_time":"","delist_time":"","desc":"<p><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2PcozkdRopuFjSZFtXXcanpXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2vl2YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB26.j7kbBnpuFjSZFGXXX51pXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2il6YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2frEwkd0opuFjSZFxXXaDNVXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB23AGfiMxlpuFjSszgXXcJdpXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2ze5CiMJlpuFjSspjXXcT.pXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB20LB4iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2pxSfiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2qN00iM0kpuFjSspdXXX4YXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2j6eXiHXlpuFjSszfXXcSGXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2lc0ViSXlpuFjy0FeXXcJbFXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2xuKFiHFkpuFjy1XcXXclapXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2mECliR4lpuFjy1zjXXcAKpXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2uWGniHtlpuFjSspoXXbcDpXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2.0ytiHVkpuFjSspcXXbSMVXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2OCiXiH0kpuFjy0FjXXcBbVXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2B49fiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2ShitiMFkpuFjSspnXXb4qFXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2N204iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB24mwwkipnpuFjSZFIXXXh2VXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2FSDYkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2aAookohnpuFjSZFpXXcpuXXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2e5G5edhvOuFjSZFBXXcZgFXa_!!2341974772.jpg\"  \/><img align=\"absmiddle\" src=\"http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2AqobkbJmpuFjSZFwXXaE4VXa_!!2341974772.jpg\"  \/><\/p><img src=\"https:\/\/www.o0b.cn\/i.php?t.png&rid=gw-1.6314322f94ee5&p=237260441&k=25423&t=1662267954\" style=\"display:none\" \/>","desc_img":["http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2PcozkdRopuFjSZFtXXcanpXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2vl2YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB26.j7kbBnpuFjSZFGXXX51pXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2il6YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2frEwkd0opuFjSZFxXXaDNVXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB23AGfiMxlpuFjSszgXXcJdpXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2ze5CiMJlpuFjSspjXXcT.pXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB20LB4iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2pxSfiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2qN00iM0kpuFjSspdXXX4YXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2j6eXiHXlpuFjSszfXXcSGXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2lc0ViSXlpuFjy0FeXXcJbFXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2xuKFiHFkpuFjy1XcXXclapXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2mECliR4lpuFjy1zjXXcAKpXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2uWGniHtlpuFjSspoXXbcDpXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2.0ytiHVkpuFjSspcXXbSMVXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2OCiXiH0kpuFjy0FjXXcBbVXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2B49fiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2ShitiMFkpuFjSspnXXb4qFXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB2N204iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i2\/2341974772\/TB24mwwkipnpuFjSZFIXXXh2VXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i1\/2341974772\/TB2FSDYkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i4\/2341974772\/TB2aAookohnpuFjSZFpXXcpuXXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2e5G5edhvOuFjSZFBXXcZgFXa_!!2341974772.jpg","http:\/\/img.alicdn.com\/imgextra\/i3\/2341974772\/TB2AqobkbJmpuFjSZFwXXaE4VXa_!!2341974772.jpg"],"item_imgs":[{"url":"\/\/img.alicdn.com\/imgextra\/i2\/2491925690\/O1CN01BOljSm1ru4AQ8wuoW_!!2491925690.jpg"},{"url":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01ZAhmaC1ru4AQ8uZJ5_!!2491925690.jpg"},{"url":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg"},{"url":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01ZNWdbI1ru4ANT9Org_!!2491925690.jpg"},{"url":"\/\/img.alicdn.com\/imgextra\/i3\/2491925690\/O1CN01ZjJNri1ru4AOlWbeT_!!2491925690.jpg"}],"item_weight":"","item_size":"","location":"广东广州","post_fee":0,"express_fee":null,"ems_fee":"","shipping_to":"","has_discount":"false","video":[],"is_virtual":"","sample_id":"","is_promotion":"false","props_name":"1627207:949304607:颜色分类:A款-珍珠白;1627207:228941177:颜色分类:B款-双头微雾机","prop_imgs":{"prop_img":[{"properties":"1627207:949304607","url":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg"},{"properties":"1627207:228941177","url":"\/\/img.alicdn.com\/imgextra\/i2\/2491925690\/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg"}]},"property_alias":"","props":[{"name":"颜色分类","value":"A款-珍珠白,B款-双头微雾机"},{"name":"款式","value":"立式"}],"total_sold":"12","skus":{"sku":[{"price":"980","total_price":0,"orginal_price":"980","properties":"1627207:949304607","properties_name":"1627207:949304607:颜色分类:A款-珍珠白","quantity":"200","sku_id":"4368671370175"},{"price":"580","total_price":0,"orginal_price":"580","properties":"1627207:228941177","properties_name":"1627207:228941177:颜色分类:B款-双头微雾机","quantity":"200","sku_id":"4368671370176"}]},"seller_id":"2491925690","sales":6,"shop_id":"118690644","props_list":{"1627207:949304607":"颜色分类:A款-珍珠白","1627207:228941177":"颜色分类:B款-双头微雾机"},"seller_info":{"nick":"亲亲爱尚潮流","item_score":"4.9 ","score_p":"4.9 ","delivery_score":"4.9 ","shop_type":"C","user_num_id":"2491925690","sid":"118690644","title":"天芝美容美发机构","zhuy":"https:\/\/shop118690644.taobao.com\/","shop_name":"天芝美容美发机构"},"tmall":false,"error":"","warning":"","url_log":[],"fav_count":"60","fans_count":"4779","freight":"快递: 免运费","props_imgs":{"prop_img":[{"properties":"1627207:949304607","url":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg"},{"properties":"1627207:228941177","url":"\/\/img.alicdn.com\/imgextra\/i2\/2491925690\/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg"}]},"_ddf":"xdl","promo_type":null,"props_img":{"1627207:949304607":"\/\/img.alicdn.com\/imgextra\/i4\/2491925690\/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg","1627207:228941177":"\/\/img.alicdn.com\/imgextra\/i2\/2491925690\/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg"},"format_check":"ok","shop_item":[],"relate_items":[]},"error":"","secache":"3ac1f936bffbca8c157ec625084997cf","secache_time":1662267954,"secache_date":"2022-09-04 13:05:54","translate_status":"","translate_time":0,"language":{"default_lang":"cn","current_lang":"cn"},"reason":"","error_code":"0000","cache":0,"api_info":"today:7 max:30000 all[7=7+0+0];expires:2022-10-11","execution_time":"2.746","server_time":"Beijing\/2022-09-04 13:05:54","client_ip":"14.36.78.153","call_args":{"num_iid":"600448952765","is_promotion":"1"},"api_type":"taobao","server_memory":"5.89MB","request_id":"gw-1.6314322f94ee5","last_id":"1194882664"}'

c = json.loads(b)

pp = c['item']['item_imgs']

for i in desc_imgurl:
    print(i)

{
    "item": {
        "num_iid": "600448952765",
        "title": "\xe6\x96\xb0\xe6\xac\xbe\xe5\xa4\x9a\xe5\x8a\x9f\xe8\x83\xbd\xe6\xb4\xbb\xe6\xb0\xa7\xe5\xbe\xae\xe9\x9b\xbe\xe6\x9c\xba\xe7\x84\x97\xe6\xb2\xb9\xe6\x9c\xba\xe5\xae\xb6\xe7\x94\xa8\xe8\x92\xb8\xe5\x8f\x91\xe6\x9c\xba\xe8\x92\xb8\xe6\xb1\xbd\xe6\x9c\xba\xe6\x8a\xa4\xe5\x8f\x91\xe6\x9c\xba\xe8\xb6\x85\xe5\xa3\xb0\xe6\xb3\xa2\xe8\x87\xad\xe6\xb0\xa7\xe6\x9c\xba",
        "desc_short": "",
        "price": "580",
        "total_price": 0,
        "suggestive_price": 0,
        "orginal_price": "580.00",
        "nick": "\xe4\xba\xb2\xe4\xba\xb2\xe7\x88\xb1\xe5\xb0\x9a\xe6\xbd\xae\xe6\xb5\x81",
        "num": "200",
        "min_num": 0,
        "detail_url": "https://item.taobao.com/item.htm?id=600448952765",
        "pic_url": "//img.alicdn.com/imgextra/i2/2491925690/O1CN01BOljSm1ru4AQ8wuoW_!!2491925690.jpg",
        "brand": "",
        "brandId": None,
        "rootCatId": "50002768",
        "cid": "50024628",
        "crumbs": [],
        "created_time": "",
        "modified_time": "",
        "delist_time": "",
        "desc": '<p><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2PcozkdRopuFjSZFtXXcanpXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i3/2341974772/TB2vl2YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB26.j7kbBnpuFjSZFGXXX51pXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2il6YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i3/2341974772/TB2frEwkd0opuFjSZFxXXaDNVXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB23AGfiMxlpuFjSszgXXcJdpXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB2ze5CiMJlpuFjSspjXXcT.pXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB20LB4iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2pxSfiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB2qN00iM0kpuFjSspdXXX4YXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i3/2341974772/TB2j6eXiHXlpuFjSszfXXcSGXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB2lc0ViSXlpuFjy0FeXXcJbFXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB2xuKFiHFkpuFjy1XcXXclapXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB2mECliR4lpuFjy1zjXXcAKpXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2uWGniHtlpuFjSspoXXbcDpXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB2.0ytiHVkpuFjSspcXXbSMVXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB2OCiXiH0kpuFjy0FjXXcBbVXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB2B49fiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2ShitiMFkpuFjSspnXXb4qFXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB2N204iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i2/2341974772/TB24mwwkipnpuFjSZFIXXXh2VXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i1/2341974772/TB2FSDYkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i4/2341974772/TB2aAookohnpuFjSZFpXXcpuXXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i3/2341974772/TB2e5G5edhvOuFjSZFBXXcZgFXa_!!2341974772.jpg"  /><img align="absmiddle" src="http://img.alicdn.com/imgextra/i3/2341974772/TB2AqobkbJmpuFjSZFwXXaE4VXa_!!2341974772.jpg"  /></p><img src="https://www.o0b.cn/i.php?t.png&rid=gw-1.6314322f94ee5&p=237260441&k=25423&t=1662267954" style="display:none" />',
        "desc_img": [
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2PcozkdRopuFjSZFtXXcanpXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i3/2341974772/TB2vl2YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB26.j7kbBnpuFjSZFGXXX51pXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2il6YkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i3/2341974772/TB2frEwkd0opuFjSZFxXXaDNVXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB23AGfiMxlpuFjSszgXXcJdpXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB2ze5CiMJlpuFjSspjXXcT.pXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB20LB4iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2pxSfiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB2qN00iM0kpuFjSspdXXX4YXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i3/2341974772/TB2j6eXiHXlpuFjSszfXXcSGXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB2lc0ViSXlpuFjy0FeXXcJbFXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB2xuKFiHFkpuFjy1XcXXclapXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB2mECliR4lpuFjy1zjXXcAKpXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2uWGniHtlpuFjSspoXXbcDpXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB2.0ytiHVkpuFjSspcXXbSMVXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB2OCiXiH0kpuFjy0FjXXcBbVXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB2B49fiR0kpuFjy1zdXXXuUVXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2ShitiMFkpuFjSspnXXb4qFXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB2N204iHBkpuFjy1zkXXbSpFXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i2/2341974772/TB24mwwkipnpuFjSZFIXXXh2VXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i1/2341974772/TB2FSDYkkqvpuFjSZFhXXaOgXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i4/2341974772/TB2aAookohnpuFjSZFpXXcpuXXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i3/2341974772/TB2e5G5edhvOuFjSZFBXXcZgFXa_!!2341974772.jpg",
            "http://img.alicdn.com/imgextra/i3/2341974772/TB2AqobkbJmpuFjSZFwXXaE4VXa_!!2341974772.jpg",
        ],
        "item_imgs": [
            {
                "url": "//img.alicdn.com/imgextra/i2/2491925690/O1CN01BOljSm1ru4AQ8wuoW_!!2491925690.jpg"
            },
            {
                "url": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01ZAhmaC1ru4AQ8uZJ5_!!2491925690.jpg"
            },
            {
                "url": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg"
            },
            {
                "url": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01ZNWdbI1ru4ANT9Org_!!2491925690.jpg"
            },
            {
                "url": "//img.alicdn.com/imgextra/i3/2491925690/O1CN01ZjJNri1ru4AOlWbeT_!!2491925690.jpg"
            },
        ],
        "item_weight": "",
        "item_size": "",
        "location": "\xe5\xb9\xbf\xe4\xb8\x9c\xe5\xb9\xbf\xe5\xb7\x9e",
        "post_fee": 0,
        "express_fee": None,
        "ems_fee": "",
        "shipping_to": "",
        "has_discount": "false",
        "video": [],
        "is_virtual": "",
        "sample_id": "",
        "is_promotion": "false",
        "props_name": "1627207:949304607:\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:A\xe6\xac\xbe-\xe7\x8f\x8d\xe7\x8f\xa0\xe7\x99\xbd;1627207:228941177:\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:B\xe6\xac\xbe-\xe5\x8f\x8c\xe5\xa4\xb4\xe5\xbe\xae\xe9\x9b\xbe\xe6\x9c\xba",
        "prop_imgs": {
            "prop_img": [
                {
                    "properties": "1627207:949304607",
                    "url": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg",
                },
                {
                    "properties": "1627207:228941177",
                    "url": "//img.alicdn.com/imgextra/i2/2491925690/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg",
                },
            ]
        },
        "property_alias": "",
        "props": [
            {
                "name": "\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb",
                "value": "A\xe6\xac\xbe-\xe7\x8f\x8d\xe7\x8f\xa0\xe7\x99\xbd,B\xe6\xac\xbe-\xe5\x8f\x8c\xe5\xa4\xb4\xe5\xbe\xae\xe9\x9b\xbe\xe6\x9c\xba",
            },
            {"name": "\xe6\xac\xbe\xe5\xbc\x8f", "value": "\xe7\xab\x8b\xe5\xbc\x8f"},
        ],
        "total_sold": "12",
        "skus": {
            "sku": [
                {
                    "price": "980",
                    "total_price": 0,
                    "orginal_price": "980",
                    "properties": "1627207:949304607",
                    "properties_name": "1627207:949304607:\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:A\xe6\xac\xbe-\xe7\x8f\x8d\xe7\x8f\xa0\xe7\x99\xbd",
                    "quantity": "200",
                    "sku_id": "4368671370175",
                },
                {
                    "price": "580",
                    "total_price": 0,
                    "orginal_price": "580",
                    "properties": "1627207:228941177",
                    "properties_name": "1627207:228941177:\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:B\xe6\xac\xbe-\xe5\x8f\x8c\xe5\xa4\xb4\xe5\xbe\xae\xe9\x9b\xbe\xe6\x9c\xba",
                    "quantity": "200",
                    "sku_id": "4368671370176",
                },
            ]
        },
        "seller_id": "2491925690",
        "sales": 6,
        "shop_id": "118690644",
        "props_list": {
            "1627207:949304607": "\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:A\xe6\xac\xbe-\xe7\x8f\x8d\xe7\x8f\xa0\xe7\x99\xbd",
            "1627207:228941177": "\xe9\xa2\x9c\xe8\x89\xb2\xe5\x88\x86\xe7\xb1\xbb:B\xe6\xac\xbe-\xe5\x8f\x8c\xe5\xa4\xb4\xe5\xbe\xae\xe9\x9b\xbe\xe6\x9c\xba",
        },
        "seller_info": {
            "nick": "\xe4\xba\xb2\xe4\xba\xb2\xe7\x88\xb1\xe5\xb0\x9a\xe6\xbd\xae\xe6\xb5\x81",
            "item_score": "4.9 ",
            "score_p": "4.9 ",
            "delivery_score": "4.9 ",
            "shop_type": "C",
            "user_num_id": "2491925690",
            "sid": "118690644",
            "title": "\xe5\xa4\xa9\xe8\x8a\x9d\xe7\xbe\x8e\xe5\xae\xb9\xe7\xbe\x8e\xe5\x8f\x91\xe6\x9c\xba\xe6\x9e\x84",
            "zhuy": "https://shop118690644.taobao.com/",
            "shop_name": "\xe5\xa4\xa9\xe8\x8a\x9d\xe7\xbe\x8e\xe5\xae\xb9\xe7\xbe\x8e\xe5\x8f\x91\xe6\x9c\xba\xe6\x9e\x84",
        },
        "tmall": False,
        "error": "",
        "warning": "",
        "url_log": [],
        "fav_count": "60",
        "fans_count": "4779",
        "freight": "\xe5\xbf\xab\xe9\x80\x92: \xe5\x85\x8d\xe8\xbf\x90\xe8\xb4\xb9",
        "props_imgs": {
            "prop_img": [
                {
                    "properties": "1627207:949304607",
                    "url": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg",
                },
                {
                    "properties": "1627207:228941177",
                    "url": "//img.alicdn.com/imgextra/i2/2491925690/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg",
                },
            ]
        },
        "_ddf": "xdl",
        "promo_type": None,
        "props_img": {
            "1627207:949304607": "//img.alicdn.com/imgextra/i4/2491925690/O1CN01VkvSX61ru4AN9AF49_!!2491925690.jpg",
            "1627207:228941177": "//img.alicdn.com/imgextra/i2/2491925690/O1CN01rrulmU1ru4AFrTiZZ_!!2491925690.jpg",
        },
        "format_check": "ok",
        "shop_item": [],
        "relate_items": [],
    },
    "error": "",
    "secache": "3ac1f936bffbca8c157ec625084997cf",
    "secache_time": 1662267954,
    "secache_date": "2022-09-04 13:05:54",
    "translate_status": "",
    "translate_time": 0,
    "language": {"default_lang": "cn", "current_lang": "cn"},
    "reason": "",
    "error_code": "0000",
    "cache": 0,
    "api_info": "today:7 max:30000 all[7=7+0+0];expires:2022-10-11",
    "execution_time": "2.746",
    "server_time": "Beijing/2022-09-04 13:05:54",
    "client_ip": "14.36.78.153",
    "call_args": {"num_iid": "600448952765", "is_promotion": "1"},
    "api_type": "taobao",
    "server_memory": "5.89MB",
    "request_id": "gw-1.6314322f94ee5",
    "last_id": "1194882664",
}
