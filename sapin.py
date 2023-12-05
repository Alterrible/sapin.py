# cristmas update de maths.py
sage=str(input("avez vous été sage cette année ?  ")) # Christmas update
sapin = [
    [None, None, None, "*", None, None, None],
    [None, None, None, "-", None, None, None],
    [None, None, "-", "-", "-", None, None],
    [None, "-", "-", "-", "-", "-", None],
    ["-", "-", "-", "-", "-", "-", "-"],
    [None, None, None, "-", None, None, None]
]

if sage=="oui" or "OUI" or "Oui":
    for row in sapin:
        print(' '.join(str(e) if e else ' ' for e in row))
    print("joyeux noël")
else:
    print("RIP")