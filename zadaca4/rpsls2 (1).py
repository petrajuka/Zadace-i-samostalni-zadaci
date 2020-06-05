# Igra Rock Paper Scissors Lizard Spock, korisnik protiv računala
#igra se do 3 dobivena nakon čega se proglašava pobjednik

import random
from rpslsError import RpslsError

class Rpsls2:
    def __init__(self):
        self.player_input = None
        self.player_number = -1
        self.computer_number = -1
        self.computer_choice_name = None
        self.player_points = 0
        self.computer_points = 0
        self.num_round = 0

    def display_title_bar(self):
        print("\t***********************************************************")
        print("\t*** Dobrodošli u igru Rock Paper Scissors Lizard Spock! ***")
        print("\t***********************************************************")

    def get_user_choice(self):
        # ispisujemo korisniku meni što može raditi u aplikaciji
        # na kraju ga pitamo i uzimamo njegov odabir te taj odabir vracamo 
        print("\n[1] Započni igru Rock Paper Scissors Lizard Spock.")
        print("[x] Izlaz.")
    
        return input("Što želite napraviti?")

    def broj_u_string(self):
        """
        pretvara brojeve (0, 1, 2, 3, 4) u nazive/tekst (rock, Spock, paper, lizard, scissors)
        """
        if self.computer_number == 0:
            self.computer_choice_name = "rock"
        elif self.computer_number == 1:
            self.computer_choice_name = "Spock"
        elif self.computer_number == 2:
            self.computer_choice_name = "paper"
        elif self.computer_number == 3:
            self.computer_choice_name = "lizard"
        elif self.computer_number == 4:
            self.computer_choice_name = "scissors"
        else:
            self.computer_choice_name = None
            raise RpslsError(103)
        return self.computer_choice_name
    
       
    def string_u_broj(self):
        """
        pretvara naziv/tekst (rock, Spock, paper, lizard, scissors) u broj (0, 1, 2, 3, 4)
        """
        if self.player_input == "rock":
            self.player_number = 0
        elif self.player_input == "spock":
            self.player_number = 1
        elif self.player_input == "paper":
            self.player_number = 2
        elif self.player_input == "lizard":
            self.player_number = 3
        elif self.player_input == "scissors":
            self.player_number = 4
        else:
            self.player_number = -1
            raise RpslsError(102)
        return self.player_number

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.num_round = 0
            self.display_title_bar()
            while self.num_round < 3:
                if choice == '1':
                    # unos korisnikovog tekst
                    self.player_input = input("Odaberite rock, spock, paper, lizard ili scissors: ").lower()
                    # pretvorba korisnikovog tekst u broj
                    self.player_number = self.string_u_broj()
                    # racunalo odabire pomocu random metode
                    self.computer_number = random.randrange(0,5)
                    ostatak = (self.player_number - self.computer_number)%5
                    if(self.player_number == -1):
                        winner = "Greška"
                        raise RpslsError(101)
                    else:
                        if ostatak == 0:
                            winner = "Neriješeno"
                            self.num_round +=1
                        elif ostatak == 1 or ostatak == 2:
                            winner = "Vi (čovjek) pobjeđujete ovu rundu"
                            self.num_round +=1
                            self.player_points += 1
                        elif ostatak == 3 or ostatak == 4:
                            winner = "Računalo pobjeđuje ovu rundu"
                            self.num_round +=1
                            self.computer_points += 1
                    self.computer_choice_name = self.broj_u_string()
                    print("Vi (čovjek) ste odabrali: {}".format(self.player_input.title()))
                    print("Računalo je odabralo: {}".format(self.computer_choice_name.title()))
                    print(winner)
                    print("Igrač ima {} bodova:".format(self.player_points))
                    print("Komp ima {} bodova:".format(self.computer_points))
                elif choice == 'x':
                    print("\nHvala na pregledu/uređivanju dokumentarija.Pozdrav!")
                else:
                    raise RpslsError(104)
            if self.player_points>self.computer_points:
                print("Igrač pobijedio s {}:{} ".format(self.player_points, self.computer_points))
            elif self.computer_points>self.player_points:
                print("Računalo pobijedilo s {}:{} ".format(self.computer_points, self.player_points))

    def show_user_choice(self):
        # ispisujemo korisniku meni što može raditi u aplikaciji
        # na kraju ga pitamo i uzimamo njegov odabir te taj odabir vracamo 
        print("\n[1] Započni igru Rock Paper Scissors Lizard Spock.")
        print("[x] Izlaz.")

        return input("Što želite napraviti?")
        
if __name__ == "__main__":
    game = Rpsls2()
    game.play()



    

