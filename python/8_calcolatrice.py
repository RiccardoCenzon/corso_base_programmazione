numero_1=int(input("Inserisci il primo numero:"))
numero_2=int(input("Inserisci il secondo numero:"))
numero_operazione=int(input("Inserisci il numero dell'operazione:"))
if(numero_operazione==1):
    output=numero_1+numero_2
if(numero_operazione==2):
    output=numero_1-numero_2
if(numero_operazione==3):
    if(numero_2==0):
        output=("Non puoi dividere per zero!")
    else:
        output=numero_1/numero_2
if(numero_operazione==4):
    output=numero_1*numero_2
if(numero_operazione<1):
    output=numero_1+numero_2
if(numero_operazione>4):
    output=numero_1+numero_2
print(output) 