message: str = 'Inserisci un numero: '
number: int = int(input(message))
max = number
min = number
count = 0
while True:    
    if (count != 0):
        number: int = int(input(message))
    if (number == 0):
        break
    if (number > max):
        max = number
    if (number < min):
        min = number 
    count = count + 1
print("Max: ", max)
print("Min: ", min)