from scu_captcha import imgLoader, Predict



with open("captcha.jpg", "wb") as f: 
    f.write(byte_Captcha)
img = imgLoader("captcha.jpg")
res = Predict(img)

print(res)