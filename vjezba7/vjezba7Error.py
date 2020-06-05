class Karte2Error(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: "Kod 000: Nespecificirana greška",
            101: "Kod 101: Krivi unos u glavnom izborniku."
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))