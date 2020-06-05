import random
from vjezba7Error import Karte2Error
class Karte2:
    def __init__(self):
        self.SPIL = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'Decko':10, 'Dama':10, 'Kralj':10, 'Kec':1}
        self.num_round = 1
        self.player_round_win = 0
        self.computer_round_win = 0   

    
    def display_title_bar(self):
        print("\t**************************************")
        print("\t***  Kartaška igra 2 - izvlačenje  ***")
        print("\t**************************************")
    
    def get_user_choice(self):
        print("\n[1] Pokreni kartašku igru 2.")
        print("[x] Izlaz")
        return input("Što želite napraviti?")

    def start_game(self):
        deck = (['2', '3', '4', '5', '6', '7', '8', '9', '0', 'Decko', 'Dama', 'Kralj', 'Kec'])*4
        random.shuffle(deck)
        while self.num_round < 4:
            player = [deck.pop() for _ in range(2)]
            computer = [deck.pop() for _ in range(2)]
            print("Igračeva (Vaša) ruka: {}".format(player))
            print("Računalov odabir: {}".format(computer))
            player.append(deck.pop())
            computer.append(deck.pop())
            player_score = sum(self.SPIL[card]for card in player)
            computer_score = sum(self.SPIL[card]for card in computer)
            if player_score > computer_score:
                print("Igrač dobiva ovu rundu. Rezultat: Igrač {} vs Računalo {}".format(player_score, computer_score))
                self.num_round +=1
                self.player_round_win +=1
            elif player_score < computer_score:
                print("Računalo dobiva ovu rundu. Rezultat: Računalo {} vs Igrač {}".format(computer_score, player_score))
                self.num_round +=1
                self.computer_round_win +=1
            elif player_score == computer_score:
                print("Neriješeno!")
            
        if self.player_round_win > self.computer_round_win:
            print("Igrač pobjeđuje. Rezultat: Igrač {} vs Računalo {}".format(self.player_round_win, self.computer_round_win))      
        elif self.player_round_win < self.computer_round_win:
            print("Računalo pobjeđuje. Rezultat: Računalo {} vs Igrač {}".format(self.computer_round_win, self.player_round_win))
        else:
            raise Karte2Error(000)
               
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("Hvala na igranju Kartaške igre. Pozdrav!")
            else:
                raise Karte2Error(101)

if __name__ == '__main__':
    game = Karte2 ()
    game.play()

        


    
