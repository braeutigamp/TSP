from stadt import Stadt
from random import shuffle
from random import random
class Tour(object):
    def __init__(self,liste,maxDist):
        self.liste=liste
        self.distance=0
        self.laenge=0
        self.generiereTour()
        self.getLaenge()
        self.mutation_rate=0.01
        self.maxDist=maxDist

    def generiereTour(self):
        shuffle(self.liste)

    """fuegt Stadt an postion ein, geaendert von Jan am 06.02."""
    def setStadt(self,Stadt,position):
        self.liste[position]=Stadt

    def getStadt(self,position):
        return self.liste[position]

    def getTourSize(self):
        return len(self.liste)

    def istStadtvorhanden(self,Stadt):
        for i in self.liste:
            if i == Stadt:
                return True
        return False


    """gibt die Laenge der Tour zurueck"""
    def getLaenge(self):

        tourLaenge = 0
        for Stadtindex in range(len(self.liste)):
            fromStadt = self.getStadt(Stadtindex);
            if Stadtindex+1 < self.getTourSize():
                zielStadt = self.getStadt(Stadtindex+1)
            else:
                zielStadt = self.getStadt(0)
            tourLaenge += fromStadt.berechneAbstand(zielStadt)
            #print(str(Stadtindex)+' ', end='')
        #print()
        self.laenge = tourLaenge

        """Wenn self.laenge nicht 0 ist gib direkt self.laenge zurueck"""
        return self.laenge


    def getFitness(self):
        return 1-self.getLaenge()/self.maxDist

    def mutieren(self):
        mutated=False
        for i in range(self.getTourSize()-2):
            if random()<=self.mutation_rate:
                #print("yes,",i, i+1)
                self.liste[i],self.liste[i+1]=self.liste[i+1],self.liste[i]
                mutated=True
        if mutated:
            self.laenge=self.getLaenge()

    def getStaedte(self):
        for i in self.liste:
            print(i.getXY())

