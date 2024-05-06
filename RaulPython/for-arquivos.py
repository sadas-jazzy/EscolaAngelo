import os
i = 1
while i <= 5:
    nome = str(i)
    os.rename(nome +".txt", nome + ".py")
    i = i + 1