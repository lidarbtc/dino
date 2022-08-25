import os

def imgpt(url, path):
    link = "https:"+url
    os.system("curl " + link + " > ./static/taobao_img/"+path+".png")

def imgpp(url, path):
    link = "https:"+url
    os.system("curl " + link + " > ./static/prop_img/"+path+".png")
