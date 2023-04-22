import random


def password():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 10
    password1 = ''
    for i in range(length):
        password1 += random.choice(chars)
    return password1
