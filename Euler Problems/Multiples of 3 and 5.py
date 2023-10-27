"""" Find the sum of all the multiples of 3 or 5 below 1000."""
#Creo una lista con los primeros 999 números naturales, una variable para iterar y una variable para asignar la suma"
natural_numbers = list()
i = 0
sum_multiples = 0

#Agrego los elementos a la lista
while i < 1000:
    natural_numbers.append(i)
    i = i + 1

#Itero en la lista para encontrar los múltiplos de 3 o 5, y añadirlos a la suma total    
for number in natural_numbers:
    if number % 5 == 0 or number % 3 == 0:
        sum_multiples += number

print(sum_multiples)