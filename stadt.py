from random import randint

class Stadt(object):
    def __init__(self,x=None,y=None):
        if x ==None:
            self.x=randint(0,1000)
        else:
            self.x=x
        if y ==None:
            self.y=randint(0,1000)
        else:
            self.y=y

    """gibt Abstand zwischen 2 Staedten zurueck"""
    def berechneAbstand(self, stadt):
        x=abs(self.x-stadt.x)
        y=abs(self.y-stadt.y)
        """Satz des pythagoras"""
        abstand=(x**2+y**2)**0.5
        return abstand

    def getXY(self):
        return (self.x,self.y)

    def equals(self,Stadt):
        if Stadt == None:
            return False
        return self.getXY()== Stadt.getXY()



