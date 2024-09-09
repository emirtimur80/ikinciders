import random 
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
hane = int(input("Şifreniz kaç haneli olsun:"))
sifre = ""
for i in range(hane):
    y = random .choice(x)
    sifre += y 
print(sifre)
