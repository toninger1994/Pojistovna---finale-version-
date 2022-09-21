"""stringová reprezentace pro uživatele"""
def moznost():
    head = (26*"_"+"\n""Evidence pojíštených\n" +26*"_")
    volba = ["Vyberte si akci:","1 - Přidat nového pojíštence","2 - Vypsat všechny pojíštěnce","3 - Vyhledat pojíštence","4 - Konec"]
    print(f"{head}\n{volba[0]}\n{volba[1]}\n{volba[2]}\n{volba[3]}\n{volba[4]}")

