import itertools

class Pojistovna:
    """application serves as a database 
    for storing, listing, searching people"""
    firstname_list = []  
    surname_list = []
    telnumber_list = []
    age_list = []
    birth_number_list = []    
    #konstruktor
    def __init__(self,first_name = None,second_name = None, telnum = None, age = None,birth_number=None):
        self.first_name = first_name
        self.second_name = second_name
        self.telnum = telnum
        self.age = age
        self.birth_number = birth_number #bude efektivnější při vyhledávání v seznamu,problém s duplicitou jmén či přijmení
    
    def __str__(self):
        """Reprezentační zprává této třídy"""
        return f"Zdraví Vás aplikace pro ukládání dat našich klientů."
    
        
    """tyto dvě následující metody jako alternativa pro iteraci pro objekt, pokud nebude funovat cyklus for in range """
    #kontrola pro iteraci přes seznam
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        pass
    
    def add_new_data(self):
        #data se budou postupně ukládat do kolekce list, název odpovídá typu charakteru požadujícího data    
        self.first_name = str(input("Zadejte jméno pojíštěnce:\n"))
        if self.first_name !="":
            #dodatečné ošetření pro délku slova a byl to string a ne číslo, případně ještě errorvallue když zbyde čas
            self.firstname_list.append(self.first_name)
            """self.incID.append(str(self.nextID+1))"""
            """self.id_list.append(str(self.id+1))"""
             
        self.second_name = str(input("Zadejte příjmení pojíštěnce\n"))
        self.surname_list.append(self.second_name)
        
        self.telnum = (input("Zadej telefonní číslo:\n").strip())
        self.telnumber_list.append(self.telnum)
        
        self.age = int(input("Zadejte svůj věk:\n"))
        self.age_list.append(self.age)
        
        #vhodné ošetřit na oficiální povolenou délku RČ v ČR skrz f-ci len()
        self.birth_number = int(input("Zadej svého rodné číslo\n").strip())
        self.birth_number_list.append(self.birth_number)
        print("Data byla uložena uložena.")
        input("Zmáčkni libovolnou klávesu pro ukončení.")
        return self
    
    def vycet_dat(self):
        #chtělo by to ještě přidat autoinc. id pro lepší orientaci v případě delšího listu - zatím fail
        #našel jsem způsob jak iterovat jednotlivé prvky ve všech seznamech, error nezjišten, except není nutno přidat
        #pokud by nefungovalo, tak byl zkusil __iter__ a __next__ - nebylo nutné
        for (a,b,c,d,rc) in itertools.zip_longest(self.firstname_list,self.surname_list,self.telnumber_list,self.age_list,self.birth_number_list):
            print(f"{a}    {b}    {c}    {d}    ID:{rc}")
            #print(f"\t{a}\t{b}\t{c}\t{d}") \t zlobí potom estetika výsledku
        return
            #return Pojistovna() návrat ke konstruktorovi varianta ??
            
    def hledacek_dat(self):
        cycle = True
        """metoda sloužící k vyhledání uživatele v databázi(listu)"""
        #first name searcher
        self.fnsearcher = str(input("Zadejte křestní jméno:\n")).strip().capitalize() 
        #second name searcher
        self.snsearcher = str(input("Zadejte přijmení:\n")).strip().capitalize()
        #id searcher - nejdůležitější
        self.idsearcher = int(input("Zadejte své rodné číslo pro kontrolu:\n").strip())
        
        cycle = True
        while cycle:
            try:
                if (self.fnsearcher in self.firstname_list) and (self.second_name in self.surname_list) and (self.idsearcher in self.birth_number_list):
                    self.xid = self.birth_number_list.index(self.idsearcher)
                    if self.xid >=0:
                        #s \t zlobí estetika na výčtu v konzoli, raději 4x space
                        print("\nZáznam nalezen:\n")
                        print(f"{self.firstname_list[self.xid]}    {self.surname_list[self.xid]}    {self.telnumber_list[self.xid]}\
                                {self.age_list[self.xid]}    ID{self.birth_number_list[self.xid]}")
                        cycle = False
                    
                    else:
                        print("Bohužel, takovýto uživatel v naší databázi neexistuje.")
                        cycle = False
                else:
                    print("Zadané informace jsou nesprávné, zkuste to prosím znovu.")
                    self.hledacek_dat() #zůstaneme v možnosti 3
            except ValueError: #pro případ, že by input od usera nebyl správný
                print("Zadané číslo nemá platný formát.")
            self.ask =str(input("Chcete zůstat ve vyhledávání ANO/NE:\n").lower().strip())
            if self.ask =="ano":
                self.hledacek_dat()
            elif self.ask =="ne":
                cycle = False
                break

            else:
                print("Platí pouze ANO/NE!")
                cycle = False
                