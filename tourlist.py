from tour import Tour
from stadt import Stadt
from quicksort import quicksort
from quicksort import compare_fitness
from random import randint
from copy import deepcopy
class Tourlist(object):
    def __init__(self,tourcount,stadtcount):
        self.tourlist=[]
        self.stadtlist=[]
        self.stadtcount=stadtcount
        self.createStadtlist()
        self.minTour=self.minDist()
        self.maxTour=self.maxDist()
        for i in range(tourcount):
            self.addTour(Tour(deepcopy(self.stadtlist),self.maxTour))

    def addTour(self,tour):
        self.tourlist.append(tour)

    def createStadtlist(self):
        stadtlist=[]
        for a in range(self.stadtcount):
            self.stadtlist.append(Stadt())

    def mutiere(self):
        for i in self.tourlist:
            i.mutieren()

    def sort(self):
        self.tourlist= quicksort(self.tourlist,compare_fitness)

    def getTour(self,position):
        return self.tourlist[position]

    def minDist(self):
        minTour=0
        slist=self.stadtlist
        for stadt in slist:
            mindist=1500
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if mindist > Dist :
                         mindist= Dist
            minTour=minTour +mindist

        return minTour

    def maxDist(self):

        maxTour=0
        slist=self.stadtlist
        for stadt in slist:
            maxdist=0
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if maxdist < Dist :
                         maxdist= Dist
            maxTour=maxTour +maxdist

        return maxTour
    def createNewGen(self,prozent):
        list =self.shortTourlist(prozent)
        newlist = []
        for i in range(len(self.tourlist)):
            a = randint(0,len(list)-1)
            b = randint(0,len(list)-1)
            newlist.append(self.crossover(list[a],list[b]))
        self.tourlist=quicksort(newlist,compare_fitness)
        self.mutiere()

    def shortTourlist(self,prozent):
        return quicksort(self.tourlist,compare_fitness)[:len(self.tourlist)-1*int(prozent/100)]


    """von Daniel K. und Mats / Schranken zum ausrechnen der Fitness"""
    def Schranken(self):
        maxTour=0
        minTour=0
        slist=self.stadtlist
        for stadt in slist:
            mindist=1500
            maxdist=0
            for stadt2 in slist:
                if stadt != stadt2:
                   Dist= stadt.berechneAbstand(stadt2)
                   if mindist > Dist :
                         mindist= Dist
                   if maxdist < Dist :
                         maxdist= Dist
            minTour=minTour +mindist
            maxTour=maxTour +maxdist

        return maxTour,minTour

    def crossover(self,parent1,parent2):
        child = Tour(deepcopy(parent1.liste),self.maxTour)
        for i in range(child.getTourSize()):
        	child.setStadt(None,i )

        startPos = randint(0,parent1.getTourSize()-1)
        endPos = randint(0,parent1.getTourSize()-1)


        for i in range(parent1.getTourSize()):
        	if startPos < endPos and i > startPos and i < endPos:
        		child.setStadt(parent1.getStadt(i),i)
        	elif startPos > endPos:
        		if not i < startPos and i > endPos:
        			child.setStadt(parent1.getStadt(i),i)
        for i in range(parent2.getTourSize()):
        	if not child.istStadtvorhanden(parent2.getStadt(i)):
        		for ii in range(parent1.getTourSize()):
        			if child.getStadt(ii) == None:
        				child.setStadt(parent2.getStadt(i),ii)
        				break
        return child





t =Tourlist(100,20)
print(quicksort(t.tourlist,compare_fitness)[0].laenge)
for i in range(10):
    t.createNewGen(20)
    print(quicksort(t.tourlist,compare_fitness)[0].laenge)


