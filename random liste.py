from random import randint
def random_list(length):
    liste=[]
    a=0
    while a <=length:
        random =randint(0,length)
        if not random in liste:
            a = a+1
            liste.append(random)
    return liste

def mutieren(liste,mutation_rate):
    neue_liste=liste
    for i in range(len(neue_liste)-1):
        if randint(0,10000)/10000<=mutation_rate:
            print("mutiert")
            neue_liste[i],neue_liste[i+1]=neue_liste[i+1],neue_liste[i]
    return neue_liste
