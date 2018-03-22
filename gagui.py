from tkinter import *
from tourlist import *

class Gagui():
    def __init__(self,tourlist):
        self.tourlist=tourlist
        self.master=Tk()
        self.counter=0
        self.frame = Canvas(self.master, width=1200, height= 550, background="#5C0815")
        self.frame.pack()
        self.tourlist.sort()
        self.button = Button(self.master, text="NEUE ROUTE GENERIEREN", command=self.buttonclicked)
        self.button.pack()
        self.label = Label(self.master, text="")
        self.label.pack()
        self.tourzeichnen(self.tourlist.getTour(self.counter))

    #def buttonclicked(self):
       # self.counter = self.counter + 1
       # self.frame.delete(ALL)
       # self.tourzeichnen(self.tour.getTour(self.counter))

    def buttonclicked(self):
        for i in range(1):
            self.tourlist.createNewGen(10)
        self.frame.delete(ALL)
        self.tourlist.getTour(0).getStaedte()
        self.tourzeichnen(self.tourlist.getTour(0))



    def tourzeichnen(self,tour):

        self.frame.create_text(30, 10, fill="#FFFFFF", text=str(round(tour.getLaenge(), 2)))
        for i in range(tour.getTourSize()-1):
            stadt1=tour.getStadt(i)
            stadt2=tour.getStadt(i+1)
            x1=stadt1.x
            y1=stadt1.y
            x2=stadt2.x
            y2=stadt2.y

            los1=(x1-4,y1-4)
            rus1=(x1+4,y1+4)
            los2=(x2-4,y2-4)
            rus2=(x2+4,y2+4)
            if i == 0:
                start = [stadt1.x, stadt1.y]
                self.frame.create_line(x1, y1, x2, y2, fill="#000000", width="5")
                self.frame.create_line(x1, y1, x2, y2, fill="#FFFFFF", width="2")

            if i > 0:
                self.frame.create_line(x1, y1, x2, y2, fill="#000000", width="5")
                self.frame.create_line(x1, y1, x2, y2, fill="#FFFFFF", width="2")
                self.frame.create_rectangle(los1[0]-3, los1[1]-3, rus1[0]+3, rus1[1]+3, fill="#000000", width="0")
                self.frame.create_rectangle(los1[0], los1[1], rus1[0], rus1[1], fill="#dd0000", width="0")

            if i==tour.getTourSize()-2:
                ende = [stadt2.x, stadt2.y]
                self.frame.create_line(start[0], start[1], ende[0], ende[1], fill="#000000", width="5")
                self.frame.create_line(start[0], start[1], ende[0], ende[1], fill="#FFFFFF", width="2")
                self.frame.create_rectangle(start[0]-7, start[1]-7, start[0]+7, start[1]+7, fill="#000000", width="0")
                self.frame.create_rectangle(start[0]-4, start[1]-4, start[0]+4, start[1]+4, fill="#0000dd", width="0")
                self.frame.create_rectangle(los2[0]-3, los2[1]-3, rus2[0]+3, rus2[1]+3, fill="#000000", width="0")
                self.frame.create_rectangle(los2[0], los2[1], rus2[0], rus2[1], fill="#00dd00", width="0")

        #mainloop()



t=Tourlist(100,20)
gui=Gagui(t)

