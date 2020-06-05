class ContinueError(Exception):
    def __init__(self):
        self.error_message = "Kod 105: Unesena vrijednost je pogrešna,treba unijeti d ili n."
        print("\n Opis greške: {}".format(self.error_message))
        