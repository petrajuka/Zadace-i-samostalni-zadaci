class PogadanjeEror(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: "Kod 000: Nespecificirana greška",
            101: "Kod 101: krivi unos u pogađanju broja.",
            102: "Kod 102: Krivi unos u glavnom izborniku.",
            103: "Kod 103: Vaš broj nije u zadanom opsegu."
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))
        