class TankError(Exception):
    def __init__(self, code):
        self.error_message = ''
        self.error_message = '~'*50+'\n'
        self.error_dict = {
            000: 'ERROR-000: Nespecificirana pogreška',
            101: 'ERROR-101: Uneseni broj je jednak 0!',
            102: 'ERROR-102: Uneseni broj je negativan',
            103: 'ERROR-103: Unesena vrijednost nije broj',
            104: 'ERROR-104: Greška povezana s neispravnim unosom u glavnom izborniku!'
        }
        try:
            self.error_message += self.error_dict[code] 
        except KeyError:
            self.error_message += self.error_dict[000]
            self.error_message += '\n'
       