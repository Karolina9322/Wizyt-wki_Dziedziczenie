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

    @label_length.setter
    def label_length(self,value):
        if value == len(self.name + " " + self.surname):
            self._label_length = value
    

person_1 = Card(name = "Wiktoria", surname = "Olszewska", email_adress = "WiktoriaOlszewska@armyspy.com")
person_2 = Card(name = "Eugeniusz", surname = "Kowalski", email_adress = "EugeniuszKowalski@armyspy.com")
person_3 = Card(name = "Frydrych", surname = "Tomaszewski", email_adress = "FrydrychTomaszewski@armyspy.com")
person_4 = Card(name = "Franciszka", surname = "Kucharska", email_adress = "FranciszkaKucharska@armyspy.com")
person_5 = Card(name = "Klementyna", surname = "Czarnecka", email_adress = "KlementynaCzarnecka@armyspy.com")

persons = [person_1, person_2, person_3, person_4, person_5]

#Wypisanie listy 5 wizytówek:
for i in persons:
    print(i)

print()

#Sortowanie po imieniu, nazwisku i adresie email:
by_name = sorted(persons, key = lambda Business_card: Business_card.name)
by_surname = sorted(persons, key = lambda Business_card: Business_card.surname)
by_email_adress = sorted(persons, key = lambda Business_card: Business_card.email_adress)

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

person_1 = BaseContact(name = "Wiktoria", surname = "Olszewska", email_adress = "WiktoriaOlszewska@armyspy.com", private_phone = "+48 555-666-888")
person_2 = BaseContact(name = "Eugeniusz", surname = "Kowalski", email_adress = "EugeniuszKowalski@armyspy.com", private_phone = "+48 535-444-789")
person_3 = BaseContact(name = "Frydrych", surname = "Tomaszewski", email_adress = "FrydrychTomaszewski@armyspy.com", private_phone = "+48 666-098-765")
person_4 = BaseContact(name = "Franciszka", surname = "Kucharska", email_adress = "FranciszkaKucharska@armyspy.com", private_phone = "+48 456-789-234")
person_5 = BaseContact(name = "Klementyna", surname = "Czarnecka", email_adress = "KlementynaCzarnecka@armyspy.com", private_phone = "+48 565-789-456")

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

person_1 = BusinessContact(name = "Wiktoria", surname = "Olszewska", private_phone = "+48 555-666-888", business_phone = "+48 777-897-654", company = "FPUH Hołysz", occupation = "Charakteryzatorka", email_adress = "WiktoriaOlszewska@armyspy.com")
person_2 = BusinessContact(name = "Eugeniusz", surname = "Kowalski", private_phone = "+48 535-444-789", business_phone = "+48 999-456-787", company = "Grupa Andrukiewicz-Gorol Sp.j.", occupation = "Żołnierz", email_adress = "EugeniuszKowalski@armyspy.com")
person_3 = BusinessContact(name = "Frydrych", surname = "Tomaszewski", private_phone = "+48 666-098-765", business_phone = "+48 345-666-999", company = "Urynowicz S.A.", occupation = "Inżynier", email_adress = "FrydrychTomaszewski@armyspy.com")
person_4 = BusinessContact(name = "Franciszka", surname = "Kucharska", private_phone = "+48 456-789-234", business_phone = "+48 567-666-987", company = "PPUH Leks Sp.j.", occupation = "Agent literacki", email_adress = "FranciszkaKucharska@armyspy.com")
person_5 = BusinessContact(name = "Klementyna", surname = "Czarnecka", private_phone = "+48 565-789-456", business_phone = "+48 555-333-444", company = "Spółdzielnia Baszak-Klęczar s.c.", occupation = "Księgowa", email_adress = "KlementynaCzarnecka@armyspy.com")


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

def create_contacts():
    
    type = input(f"Jaki rodzaj wizytówki chcesz wygenerować: Prywatna / Biznesowa: ")
    how_many = int(input(f"Podaj ile wizytówek chcesz wygenerować: "))

    if type == "Prywatna":
        for i in range(how_many):
            print(f"Prywatna wizytówka: {fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}")
    if type == "Biznesowa":
        for i in range(how_many):
            print(f"Biznesowa wizytówka: {fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}, {fake.company()}, {fake.job()}")


if __name__ == "__main__":
    create_contacts()