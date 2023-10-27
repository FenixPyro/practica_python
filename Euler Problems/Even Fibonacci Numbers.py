"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms"""
i = 0
fib = [1, 1]
sum_even_numbers = 0

# Bucle while que crea una lista con 300 términos de la sucesión de Fibonacci
while i <= 300:
    fib.append(fib[i]+fib[i+1])
    i = i + 1

# Bucle para iterar en cada elemento de la lista y agregarlo a la suma total, diferenciando a los valores impares y menores que 4 millones   
for word in fib:
    if word <= 4000000 and word % 2 != 0:
        sum_even_numbers += word

#Imprimo la suma
print(sum_even_numbers)
#Final del código
