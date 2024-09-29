# Írjuk ki a 10x10-es szorzótáblát
def szorzotabla():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i*j}\t", end="")
