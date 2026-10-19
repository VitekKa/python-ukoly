# Program pro prodej lístků do divadla

zakladni_cena = 500

pocet_osob = int(input("Zadejte počet osob: "))

# pcet osob
if pocet_osob >= 4:
    typ_slevy = "Skupinová sleva (25 %)"
    cena_za_jednu = zakladni_cena * 0.75

else:
    vek = float(input("Zadejte věk návštěvníka: "))
    
    # senior
    if vek >= 65:
        typ_slevy = "Sleva pro seniory (20 %)"
        cena_za_jednu = zakladni_cena * 0.80
        
    # student
    elif vek < 26:
        je_student = input("Jste student? (ano/ne): ")
        
        if je_student == "ano":
            typ_slevy = "Studentská sleva (30 %)"
            cena_za_jednu = zakladni_cena * 0.70
        elif je_student == "ne":
            typ_slevy = "Bez slevy (základní cena)"
            cena_za_jednu = zakladni_cena
        else:
            typ_slevy = "Chybná odpověď (zadejte ano nebo ne)"
            cena_za_jednu = zakladni_cena
            
    # ostatni
    else:
        typ_slevy = "Bez slevy (základní cena)"
        cena_za_jednu = zakladni_cena

# celkova cena
celkova_cena = cena_za_jednu * pocet_osob

print("Typ slevy:", typ_slevy)
print("Cena za jednu vstupenku:", cena_za_jednu, "Kč")
print("Celková cena:", celkova_cena, "Kč")