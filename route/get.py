import os

def imgpt(url, path, index):
    if url.find("http") == -1:
        url = "http:"+url
    os.system("wget {} -q -O ./static/taobao_img/{}_{}.png".format(url, path, index))

def imgpp(url, path, index):
    if url.find("http") == -1:
        url = "http:"+url
    os.system("wget {} -q -O ./static/prop_img/{}_{}.png".format(url, path, index))

def imgdc(url, path, index, l):
    if url.find("http") == -1:
        url = "http:"+url
    if url.find("o0b") == -1:
        os.system("wget {} -q -O ./static/desc_img/{}_{}.png".format(url, path, index))
