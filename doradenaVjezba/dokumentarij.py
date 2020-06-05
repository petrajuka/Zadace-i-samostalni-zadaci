# Dokumentarij je aplikacija za ispis i unos studenata
# na kolegiju Razvoj poslovnih aplikacija

from dokError import DokError

class Dokumentarij:

    def __init__(self, names=''):
        self.names = names

    def display_title_bar(self):
        print("\t**************************************************")
        print("\t*** Dokumentarij - Razvoj poslovnih aplikacija ***")
        print("\t**************************************************")

    def get_user_choice(self):
        # ispisujemo korisniku meni što može raditi u aplikaciji
        # na kraju ga pitamo i uzimamo njegov odabir te taj odabir vracamo 
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenta.")
        print("[x] Izlaz.")

        return input("Što želite napraviti u dokumentariju?")

    def show_names(self):
        # prikazuje imena svih studenata dodanih u listu
        print("\n Ovo je popis studenata na kolegiju Razvoj poslovnih aplikacija: \n")
        for name in self.names:
            print(name.title())

    def get_new_name(self):
        # uzimamo kroz input od korisnika novo  ime te ga dodajemo u listu, ako to ime već nije u listi
        new_name = input("\n Unesite ime studenta: ")
        if new_name in self.names:
            print("\n{} je već upisan/a u dokumentariju.".format(new_name.title()))
        else:
            self.names.append(new_name)
            print("\n Dobrodošao/la {}!\n".format(new_name.title()))

    def play(self):
        self.names = []
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.show_names()
            elif choice == '2':
                self.get_new_name()
            elif choice == 'x':
                print("\nHvala na pregledu/uređivanju dokumentarija.Pozdrav!")
            else:
                raise DokError(101)
            
if __name__ == '__main__':
    game = Dokumentarij()
    game.play()            

