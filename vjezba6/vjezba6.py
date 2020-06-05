import random
from vjezba6Error import PogadanjeEror
class Pogadanje:
    def __init__(self):
        self.num_round = 1

    def display_title_bar(self):
        print("\t******************************")  
        print("\t**** Igra- Pogađanje broja ***")  
        print("\t******************************")  

    def get_user_choice(self):
        print("\n[1]Igraj igru pogađanje broja.")
        print("[x] Izlaz.")
        return input("Odaberite što želite napraviti?")

    def start_game(self):
        computer = random.randint(1, 100)
        while self.num_round <= 10:
            player = int(input("Unesite broj između 1 i 100: "))
            if player > computer:
                print("Vaš broj je veći od traženog broja.")
                self.num_round += 1
            elif player < computer:
                print("Vaš broj je manji od traženog broja.")
                self.num_round += 1
            elif player == computer:
                print("Pogodili ste broj!")
                break
            else:
                raise PogadanjeEror(103)
            
            if self.num_round > 10:
                print("Potrošili ste sve pokušaje, traženi broj je: {}".format(computer))
                break
        
           
            
    
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igri. Pozdrav.")
            else:
                raise PogadanjeEror(102)

if __name__ == "__main__":
    game = Pogadanje()
    game.play() 

    