import random


def get_number():
    result = []
    while len(result) != 3:
        number = random.randint(1, 9)
        if number in result:
            continue
        else:
            result.append(number)
    return result



def calcul(number, input_number):
    strike, ball = 0, 0
    for i in range(len(number)):
        if input_number[i] == number[i]:
            strike += 1
        elif input_number[i] in number:
            ball += 1
    return strike, ball