from optionfunkce import moznost
from pojistovnaclass import Pojistovna

  
#instance
customer01 = Pojistovna()
print(customer01)
cyklus = True  
while cyklus:
    moznost() #úvodní stringová prezetenace nabídky a možnostmi volby
    vstup = int(input().strip())
    #1. funguje + návrat zpětně do úvodní konzole 
    if vstup == 1:
        customer01.add_new_data()
    #2. funguje, několikrát odzkoušeno
    elif vstup == 2:
        customer01.vycet_dat()
    elif vstup ==3:
        customer01.hledacek_dat()
    elif vstup ==4:
        print("Děkujeme za použití naší aplikace, hezký den.")
        cyklus = False #ukončí se cyklus zmáčknutím 4
    else:  
        pass #jednoduché ošetření, aby se při překliknutí neukončila aplikace předčasně/ odzkoušeno


#                           __Poznámky od autora ke kódu__:
# 1. chybí ošetření minimální délka jména, pevně stanové délky telefonního a rodného čísla podle určitách pravivdel
# 2. zvážit udělat metodu třídy, který by se volala ano/ne zůstat, ušetřilo by to řádky
# 3. zcela jistě nejsou vychytány všechny chyby, snažil jsem se zaměřit na ty nejčastější
# 4. zkusit místo 4 a více lístu, udělat nested list, kdy by se vyhledával jen pomocí id/RČ a všechny další prvky by se automaticky při splnění podmínky vypsali - neodzkoušeno
# 5. potřeba vícero tříd, které by dědily od rodič. třídy metody a atributy nebyla nutná, pokud by byl projekt databáze(pojistovna,banka,posta) - tam by se dali podtřídy jistě uplatnit
