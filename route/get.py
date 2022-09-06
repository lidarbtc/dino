import os

def imgpt(url, path, index):
    os.system("curl {} > ./static/taobao_img/{}_{}.png".format(url, path, index))

def imgpp(url, path):
    os.system("curl {} > ./static/prop_img/{}.png".format(url, path))

def imgdc(url, path, index):
    os.system("curl {} > ./static/desc_img/{}_{}.png".format(url, path, index))
