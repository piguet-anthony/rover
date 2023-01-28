from . import RoverCommandes

class RoverAvancer(RoverCommandes):
    def __init__(self, orientation, posX, posY):
        RoverCommandes.__init__(self,orientation, posX, posY)

    def avancer(self):
        match self.orientation:
            case "N":
                self.posY += 1
            case "S":
               self.posY -= 1
            case "O":
                self.posX -= 1
            case "E":
                self.posX += 1
            case _:
                print("error de direction")