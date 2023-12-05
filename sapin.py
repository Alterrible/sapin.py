# cristmas update de maths.py
# sage=str(input("avez vous été sage cette année ?  ")) # Christmas update
# sapin = [
#     [None, None, None, "*", None, None, None],
#     [None, None, None, "-", None, None, None],
#     [None, None, "-", "-", "-", None, None],
#     [None, "-", "-", "-", "-", "-", None],
#     ["-", "-", "-", "-", "-", "-", "-"],
#     [None, None, None, "-", None, None, None]
# ]

# if sage=="oui" or "OUI" or "Oui":
#     for row in sapin:
#         print(' '.join(str(e) if e else ' ' for e in row))
#     print("joyeux noël")
# else:
#     print("RIP")

a=int(input("sapin (nb impaire): "))
def sapin(largeur): #la largeur est impaire
    dl=largeur//2
    for i in range(dl+1):
        ligne=" "*(dl-i)+"^"*i+"^"+"^"*i
        print(ligne)
sapin(a)