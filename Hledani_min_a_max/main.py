
a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))
c = float(input("Zadej třetí číslo: "))

if a <= b and a <= c:
    nejmensi = a
    if b <= c:
        prostredni = b
        nejvetsi = c
    else:
        prostredni = c
        nejvetsi = b
elif b <= a and b <= c:
    nejmensi = b
    if a <= c:
        prostredni = a
        nejvetsi = c
    else:
        prostredni = c
        nejvetsi = a
else:
    nejmensi = c
    if a <= b:
        prostredni = a
        nejvetsi = b
    else:
        prostredni = b
        nejvetsi = a

print(f"Seřazená čísla od nejmenšího po největší: {nejmensi}, {prostredni}, {nejvetsi}")