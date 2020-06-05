class GameEror(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_dict = {
            000: "Kod 000: Nespecificirana greška",
            101: "Kod 101: Greška povezana s neispravnim unosom u glavnom izborniku.",
            102: "Kod 102: Greška povezana s neispravnim korisnikovim unosom."
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))