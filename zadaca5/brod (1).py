import random
from rocket import Rocket
from brodError import BrodError
class Ship(Rocket):
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route


    def fight(self):
        
        shipNum = int(input("Unesite broj brodova na moru: ")) 
        if shipNum > 0:
            ships = []
            rockets = []
            for x in range(0, shipNum):# for petlja se vrti od 0 do 5
                x = random.randint(0, 100)
                y = random.randint(1, 100)
                self.route = random.randint(0,10)
                ships.append(Ship(x,y,self.route))
        
            for x in range(0, shipNum):     # for petlja se vrti od 0 do 5
                x = random.randint(0,100)
                y = random.randint(1,100)
                rockets.append(Rocket(x, y))
        elif shipNum == 0:
            raise BrodError(101)
        elif shipNum < 0:
            raise BrodError(102)
        elif (type(shipNum) != int):
            raise BrodError(103)

        for index, ship in enumerate(ships):
            print("Brod  {} je napravio {} rutu/e.".format(index+1, ship.route))

        print("\n")
        yourShip = int(input("od {} brodova, vaš brod je pod brojem: ".format(shipNum)))

        chosenShip = ships[yourShip-1]
       
        for index, tank in enumerate(ships):
            distance = chosenShip.get_distance(tank)
            print("Vaš brod je udaljen {} km od broda broj {}.".format(distance, index+1))

        print("\n")
        
        for index, rocket in enumerate(rockets):
            distance = chosenShip.get_distance(rocket)
            print("Vaš brod je udaljen {} km od rakete broj {}.".format(distance, index+1))

    
                    
            