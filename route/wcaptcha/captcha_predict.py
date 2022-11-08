# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
#from visdom import Visdom # pip install Visdom
from route.wcaptcha import captcha_setting
from route.wcaptcha import my_dataset
from route.wcaptcha.captcha_cnn_model import CNN

def main(cname):
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load('./route/wcaptcha/model.pkl'))
    #print("load cnn net.")
    ccname = cname

    predict_dataloader = my_dataset.get_predict_data_loader(ccname)

    #vis = Visdom()
    for images in predict_dataloader:
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 0:captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c1 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, captcha_setting.ALL_CHAR_SET_LEN:2 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c2 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 2 * captcha_setting.ALL_CHAR_SET_LEN:3 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c3 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 3 * captcha_setting.ALL_CHAR_SET_LEN:4 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
        c4 = captcha_setting.ALL_CHAR_SET[np.argmax(predict_label[0, 4 * captcha_setting.ALL_CHAR_SET_LEN:5 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]

        c = '%s%s%s%s%s' % (c0, c1, c2, c3, c4)
        print(c)
        return c
        #vis.images(image, opts=dict(caption=c))

if __name__ == '__main__':
    main()