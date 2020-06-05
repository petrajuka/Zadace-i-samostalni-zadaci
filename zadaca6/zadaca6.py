import random
from zadaca6Error import GameEror
class Game:
    def __init__(self):
        self.ranks = ["Kec","2","3","4","5","6","7","8","9","10","Decko","Dama","Kralj"]
        self.suits = ["Tref","Srce","Karo","Pik"]
        self.deck = []
        value = 1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank + " iz " + suit + " boje ", value])
            value = value + 1
        random.shuffle(self.deck)
        self.scoreplayer = 0
        self.scorecomputer = 0



    def display_title_bar(self):
        print("\t*************************************")  
        print("\t****  Dobrodošli u kartašku igru !***")  
        print("\t*************************************")  

    def get_user_choice(self):
        print("\n[1]Igraj kartašku igru.")
        print("[x] Izlaz.")

        return input("Odaberite što želite napraviti?")

    

    def igra(self):
        player = int(input("Odaberite broj između 1 i 200:"))
        computer = random.randint(1,200)
        while True:
            self.card1 = self.deck.pop(0) # card1 je Igrac                
            self.card2 = self.deck.pop(0) # card2 je Racunalo
            self.scoreplayer += self.card1[1]
            self.scorecomputer += self.card2[1]
            
            if self.card1 == 0:
                print("sve karte su podijeljene")
                break
            elif self.scoreplayer >= player:
                print("Igrac je pobjedio. Igrac - {} vs Racunalo - {}- {}:{}".format(player, computer, self.scoreplayer, self.scorecomputer))
                break
            elif self.scorecomputer >= computer:
                print("Računalo je pobjedilo. Racunalo - {} vs Igrac - {}- {}:{}".format(computer, player, self.scorecomputer, self.scoreplayer))
                break
            elif self.scoreplayer >= player and self.scorecomputer >= computer:
                print("Igrac i racunalo su prešli. Igrac - {} vs Racunalo- {}-{}:{}".format(player, computer, self.scoreplayer, self.scorecomputer))
                break
            elif self.scoreplayer == self.scorecomputer:
                print("Igrac i racunalo imaju iste bodove.Igrac - {} vs Racunalo - {}-{}:{}".format(player, computer, self.scoreplayer, self.scorecomputer))
                break
            else:
                raise GameEror(102)
        
            
            
    

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            # na temelju korisnikova odabira izvršavamo programsku logiku naše igrice ovisno o tome
            #što je korisnik odabrao
            self.display_title_bar()
            if choice == '1':
                self.igra()
            elif choice == 'x':
                print("\nHvala na igri. Pozdrav.")
            else:
                raise GameEror(101)

                    
                    
if __name__ == '__main__':
    game = Game()
    game.play()


        


    

