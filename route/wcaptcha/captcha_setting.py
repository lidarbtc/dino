# -*- coding: UTF-8 -*-
import os

# string.digits + string.ascii_uppercase
NUMBER = ['2', '3', '4', '5', '6', '7', '8']
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'm', 'n', 'p', 'r', 'v', 'w', 'x', 'y']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 5

IMAGE_HEIGHT = 60
IMAGE_WIDTH = 300

TRAIN_DATASET_PATH = 'dataset' + os.path.sep + 'train'
TEST_DATASET_PATH = 'dataset' + os.path.sep + 'test'
PREDICT_DATASET_PATH = 'dataset' + os.path.sep + 'predict'