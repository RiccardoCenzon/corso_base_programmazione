tot=0
i=0
while True:
    numero=int(input("Inserisci un numero:"))
    if(numero==0):
        break
    else:
        tot=tot+numero
    i=i+1
print(tot/i)