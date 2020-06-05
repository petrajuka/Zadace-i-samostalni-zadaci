class HutError000(Exception):
    def __init__(self):
        self.error_message = "Kod 000: Nespecificirana greška u programskom kodu za klasu Hut"
        print("\n Opis greške: {}".format(self.error_message))

class HutError101(Exception):
    def _init_(self):
        self.error_message = "Kod 101: Uneseni broj je izvan zadanog raspona: Broj > 5"
        print("\n Opis greške: {}".format(self.error_message))

class HutError102(Exception):
    def _init_(self):
        self.error_message = "Kod 102: Uneseni broj je izvan zadanog raspona: Broj < 0"
        print("\n Opis greške: {}".format(self.error_message))

class HutError103(Exception):
    def _init_(self):
        self.error_message = "Kod 103: Uneseni broj je izvan zadanog raspona: Broj = 0"
        print("\n Opis greške: {}".format(self.error_message))

class HutError104(Exception):
    def _init_(self):
        self.error_message = "Kod 104: Unesena vrijednost nije broj"
        print("\n Opis greške: {}".format(self.error_message))

      
        