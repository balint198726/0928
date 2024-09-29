# Generáljunk 5 lottószámot!( nem baj, ha van köztük egyforma)
import random


def lottoszamok():
    lottoszamok = []

    for _ in range(5):
        szam = random.randint(1,90)
        lottoszamok.append(szam)
        print(lottoszamok)