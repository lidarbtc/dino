import os

def imgpt(url, path, index):
    link = "https:"+url
    os.system("curl {} > ./static/taobao_img/{}_{}.png".format(link, path, index))

def imgpp(url, path):
    link = "https:"+url
    os.system("curl {} > ./static/prop_img/{}.png".format(link, path))

def imgdc(url, path, index):
    link = "https:"+url
    os.system("curl {} > ./static/desc_img/{}_{}.png".format(link, path, index))
