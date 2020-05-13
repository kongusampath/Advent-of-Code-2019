
import functools as ft

with open("inputday1.txt", "r") as file:

   weights =  file.readlines()
   print(weights)
   weights = [ int(i.strip("\n")) for i in weights ]

   fuelSum = ft.reduce(lambda x,y: x+y, list(map(lambda x: int(x/3) - 2, weights)))
   print(fuelSum)

   #weights=[654]
   for i in range(0, len(weights)):

    recursiveFuel = int(weights[i]/3) - 2
    weights[i] = 0

    while recursiveFuel > 0:

        weights[i] += recursiveFuel
        recursiveFuel = int(recursiveFuel / 3) - 2


recursiveFuelSum = ft.reduce(lambda x,y: x+y, weights)

print (recursiveFuelSum)


