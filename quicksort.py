def quicksort(liste,function):
    if len(liste) <=1:
        return liste
    else:
        pivot=liste[0]
        kleiner=[x for x in liste[1:] if function(x,pivot)==True]
        groesser=[x for x in liste[1:] if function(x,pivot)==False]
        return quicksort(groesser,function) + [pivot] + quicksort(kleiner,function)

def compare_fitness(e1,e2):
    if e1.getFitness()<e2.getFitness():
        return True
    else:
        return False