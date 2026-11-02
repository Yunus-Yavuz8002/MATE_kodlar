import random
rnd=random.randint(0,100)
while True:
    i=int(input("Sayı tut:"))
    if i<rnd:
        print("Yukarı çık")
    if i>rnd:
        print("Aşağı in")
    if i==rnd:
        print("Doğru buldunuz")
        break