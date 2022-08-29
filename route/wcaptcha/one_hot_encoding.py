# -*- coding: UTF-8 -*-
import numpy as np
from wcaptcha import captcha_setting


def encode(text):
    vector = np.zeros(captcha_setting.ALL_CHAR_SET_LEN * captcha_setting.MAX_CAPTCHA, dtype=float)
    def char2pos(c):
        if c == "2":
            return 0
        elif c == "3":
            return 1
        elif c == "4":
            return 2
        elif c == "5":
            return 3
        elif c == "6":
            return 4
        elif c == "7":
            return 5
        elif c == "8":
            return 6
        elif c == "a":
            return 7
        elif c == "b":
            return 8
        elif c == "c":
            return 9
        elif c == "d":
            return 10
        elif c == "e":
            return 11
        elif c == "f":
            return 12
        elif c == "g":
            return 13
        elif c == "h":
            return 14
        elif c == "k":
            return 15
        elif c == "m":
            return 16
        elif c == "n":
            return 17
        elif c == "p":
            return 18
        elif c == "r":
            return 19
        elif c == "v":
            return 20
        elif c == "w":
            return 21
        elif c == "x":
            return 22
        elif c == "y":
            return 23
        else:
            print(c)
            print("error")
            quit()
        

        """
        if c =='_':
            k = 62
            return k
        k = ord(c)-48
        if k > 9:
            k = ord(c) - 65 + 10
            if k > 35:
                k = ord(c) - 97 + 26 + 10
                if k > 61:
                    raise ValueError('error')
        return k
        """
    for i, c in enumerate(text):
        idx = i * captcha_setting.ALL_CHAR_SET_LEN + char2pos(c)
        vector[idx] = 1.0
    return vector

def decode(vec):
    char_pos = vec.nonzero()[0]
    text=[]
    for i, c in enumerate(char_pos):
        c = c % 24
        if c == 0:
            char_code = "2"
        elif c == 1:
            char_code = "3"
        elif c == 2:
            char_code = "4"
        elif c == 3:
            char_code = "5"
        elif c == 4:
            char_code = "6"
        elif c == 5:
            char_code = "7"
        elif c == 6:
            char_code = "8"
        elif c == 7:
            char_code = "a"
        elif c == 8:
            char_code = "b"
        elif c == 9:
            char_code = "c"
        elif c == 10:
            char_code = "d"
        elif c == 11:
            char_code = "e"
        elif c == 12:
            char_code = "f"
        elif c == 13:
            char_code = "g"
        elif c == 14:
            char_code = "h"
        elif c == 15:
            char_code = "k"
        elif c == 16:
            char_code = "m"
        elif c == 17:
            char_code = "n"
        elif c == 18:
            char_code = "p"
        elif c == 19:
            char_code = "r"
        elif c == 20:
            char_code = "v"
        elif c == 21:
            char_code = "w"
        elif c == 22:
            char_code = "x"
        elif c == 23:
            char_code = "y"
        else:
            print(c)
            print("error")
            quit()
        text.append(char_code)
    return "".join(text)

if __name__ == '__main__':
    e = encode("BK7H")
    print(decode(e))