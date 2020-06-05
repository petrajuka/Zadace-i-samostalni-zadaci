# igra kamen, papir, škare

from kpsError import KpsError

class Kps:
    def __init__(self):
        self.i1_input = None
        self.i2_input = None


    def play(self):

        # unos teksta igrača 1
        self.i1_input = input("Odaberite k, p ili s: ").lower()
        # unos teksta igrača 2
        self.i2_input = input("Odaberite k, p ili s: ").lower()
        if self.i1_input=='k':
            if self.i2_input=='k':
                print('Neriješeno.')
            elif self.i2_input=='p':
                print('Igrač2 je pobijedio (p>k).')
            else:
                print('Igrač1 je pobijedio (k>s).')
        elif self.i1_input=='p':
            if self.i2_input=='p':
                print('Neriješeno.')
            elif self.i2_input=='k':
                print('Igrač1 je pobijedio (p>k).')
            else:
                print('Igrač2 je pobijedio (s>p).')
        elif self.i1_input=='s':
            if self.i2_input=='s':
                print('Neriješeno.')
            elif self.i2_input=='p':
                print('Igrač1 je pobijedio (s>p).')
            else:
                print('Igrač2 je pobijedio (k>s).')
        else:
            raise KpsError(101)
            
if __name__ == "__main__":
    game = Kps ()
    game.play()



