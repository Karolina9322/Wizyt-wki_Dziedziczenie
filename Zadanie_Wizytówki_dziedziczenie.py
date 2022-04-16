#Klasa podstawowa Card:
class Card:
    def __init__(self, name, surname, email_adress):
        self.name = name
        self.surname = surname
        self.email_adress = email_adress
    
        self._label_length = len(self.name + " " + self.surname)

    def __str__(self):
        return f"{self.name} {self.surname}, {self.email_adress}"
    
    def __repr__(self):
        return self.__str__()
    
    def __contact__(self):
        return f"Kontaktuję się z: {self.name} {self.surname}, {self.email_adress}"

    @property
    def label_length(self):
        return self._label_length

    

person_1 = Card("Wiktoria", "Olszewska", "WiktoriaOlszewska@armyspy.com")
person_2 = Card("Eugeniusz", "Kowalski", "EugeniuszKowalski@armyspy.com")
person_3 = Card("Frydrych", "Tomaszewski", "FrydrychTomaszewski@armyspy.com")
person_4 = Card("Franciszka", "Kucharska", "FranciszkaKucharska@armyspy.com")
person_5 = Card("Klementyna", "Czarnecka", "KlementynaCzarnecka@armyspy.com")

persons = [person_1, person_2, person_3, person_4, person_5]

#Wypisanie listy 5 wizytówek:
for i in persons:
    print(i)

print()

#Sortowanie po imieniu, nazwisku i adresie email:
by_name = sorted(persons, key = lambda Card: Card.name)
by_surname = sorted(persons, key = lambda Card: Card.surname)
by_email_adress = sorted(persons, key = lambda Card: Card.email_adress)

print(by_name)
print()
print(by_surname)
print()
print(by_email_adress)

print()

#Sumowanie długości imienia i nazwiska:
print(f"""Suma długości imienia i nazwiska oddzielonych spacją to:
Osoba 1: {person_1.label_length}
Osoba 2: {person_2.label_length}
Osoba 3: {person_3.label_length}
Osoba 4: {person_4.label_length}
Osoba 5: {person_5.label_length}""")

print()

#Zastosowanie metody contact():
print(
    person_1.__contact__(),"\n", 
    person_2.__contact__(),"\n",
    person_3.__contact__(),"\n",
    person_4.__contact__(),"\n",
    person_5.__contact__()
    )

print()

#DZIEDZICZENIE
#Wizytówka bazowa, dziedziczenie z klasy podstawowej Card:
class BaseContact(Card):
    def __init__(self, private_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone = private_phone

    def __contact__(self):
        return f"Wybieram numer: {self.private_phone} i dzownię do: {self.name} {self.surname}"

person_1 = BaseContact("+48 555-666-888", "Wiktoria", "Olszewska", "WiktoriaOlszewska@armyspy.com")
person_2 = BaseContact("+48 535-444-789", "Eugeniusz", "Kowalski", "EugeniuszKowalski@armyspy.com")
person_3 = BaseContact("+48 666-098-765", "Frydrych", "Tomaszewski", "FrydrychTomaszewski@armyspy.com")
person_4 = BaseContact("+48 456-789-234", "Franciszka", "Kucharska", "FranciszkaKucharska@armyspy.com")
person_5 = BaseContact("+48 565-789-456", "Klementyna", "Czarnecka", "KlementynaCzarnecka@armyspy.com")

persons = [person_1, person_2, person_3, person_4, person_5]

#Zastosowanie metody contact() w klasie bazowej BaseContact:
print(
    person_1.__contact__(),"\n", 
    person_2.__contact__(),"\n",
    person_3.__contact__(),"\n",
    person_4.__contact__(),"\n",
    person_5.__contact__()
    )

print()


#Wizytówka biznesowa, dziedziczenie z klasy bazowej BaseContact:
class BusinessContact(BaseContact):
    def __init__(self, business_phone, company, occupation,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone
        self.company = company
        self.occupation = occupation
        
    
    def __contact__(self):
        return f"Wybieram numer: {self.business_phone} i dzownię do: {self.name} {self.surname}"

person_1 = BusinessContact("+48 777-897-654","FPUH Hołysz", "Charakteryzatorka", "+48 555-666-888", "Wiktoria", "Olszewska", "WiktoriaOlszewska@armyspy.com")
person_2 = BusinessContact("+48 999-456-787", "Grupa Andrukiewicz-Gorol Sp.j.", "Żołnierz", "+48 535-444-789", "Eugeniusz","Kowalski", "EugeniuszKowalski@armyspy.com")
person_3 = BusinessContact("+48 345-666-999", "Urynowicz S.A.", "Inżynier", "+48 666-098-765", "Frydrych", "Tomaszewski", "FrydrychTomaszewski@armyspy.com")
person_4 = BusinessContact("+48 567-666-987", "PPUH Leks Sp.j.", "Agent literacki", "+48 456-789-234", "Franciszka", "Kucharska","FranciszkaKucharska@armyspy.com")
person_5 = BusinessContact("+48 555-333-444", "Spółdzielnia Baszak-Klęczar s.c.", "Księgowa","+48 565-789-456", "Klementyna", "Czarnecka", "KlementynaCzarnecka@armyspy.com")


#Zastosowanie mwtody contact() w klasie biznesowej BusinessContact:
print(
    person_1.__contact__(),"\n", 
    person_2.__contact__(),"\n",
    person_3.__contact__(),"\n",
    person_4.__contact__(),"\n",
    person_5.__contact__()
    )

print()


#Funkcja generująca losowe wizytówki prywatne lub służbowe:


from faker import Faker
fake = Faker("pl_PL")

def create_contacts(how_many, type):

    if type == 'Prywatna':
        for i in range(how_many):
            print(BaseContact(fake.phone_number(), fake.first_name(), fake.last_name(), fake.email()))
    if type == 'Biznesowa':
        for i in range(how_many):
            print(BusinessContact(fake.phone_number(), fake.company(), fake.job(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.email()))

if __name__ == "__main__":
    (create_contacts(5,'Biznesowa'))