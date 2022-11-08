# -*- coding: UTF-8 -*-
import os
from torch.utils.data import DataLoader,Dataset
import torchvision.transforms as transforms
from PIL import Image
from route.wcaptcha import one_hot_encoding as ohe
from route.wcaptcha import captcha_setting

class mydataset(Dataset):

    def __init__(self, folder, cname, transform=None):
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        self.filepath = cname
        self.transform = transform
 
    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, idx):
        cname = self.filepath
        image_root = self.train_image_file_paths[idx]
        #image_name = image_root.split(os.path.sep)[-1]
        #print(image_root)
        image = Image.open("./wcaptcha/dataset/predict/{}.png".format(cname))
        if self.transform is not None:
            image = self.transform(image)
        label = ohe.encode(cname.split('.')[0])
        return image, label

transform = transforms.Compose([
    # transforms.ColorJitter(),
    transforms.Grayscale(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def O0oo0o0O0o(cname, transform=None):
    image = Image.open("./route/wcaptcha/dataset/predict/{}.png".format(cname))
    label = ohe.encode(cname.split('.')[0])
    if transform is not None:
        image = transform(image)
    return image, label
    

def get_train_data_loader():

    dataset = mydataset(captcha_setting.TRAIN_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=64, shuffle=True)

def get_test_data_loader():
    dataset = mydataset(captcha_setting.TEST_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)

def get_predict_data_loader(ccname):
    cname = ccname
    dataset = O0oo0o0O0o(cname, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)