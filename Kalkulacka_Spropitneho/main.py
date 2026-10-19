print("--- Kalkulačka spropitného ---")

celkova_cena = float(input("Zadej celkovou cenu účtu (Kč): "))

procenta_dyska = float(input("Kolik procent chceš dát jako dýško? (např. 3.5): "))
procenta_dyska = round(procenta_dyska, 2)

pocet_lidi = int(input("Mezi kolik lidí se účet dělí? "))

castka_dyska = celkova_cena * (procenta_dyska / 100)
celkova_s_dyskem = celkova_cena + castka_dyska

celkova_s_dyskem_zaokrouhlena = round(celkova_s_dyskem)
castka_na_osobu = round(celkova_s_dyskem / pocet_lidi)

print("\n--- Výsledek ---")
print(f"Zvolené dýško: {procenta_dyska} %")
print(f"Celková cena včetně dýška: {celkova_s_dyskem_zaokrouhlena} Kč")
print(f"Každý člověk má zaplatit: {castka_na_osobu} Kč")