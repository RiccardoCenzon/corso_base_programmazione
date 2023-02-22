
lista_operazioni=["Somma","somma","Differenza","differenza","Moltiplicazione","moltiplicazione","Divisione","divisione"]
operazione:str=""
calcolo:int=0
errore1:str="Errore: hai inserito un'operazione inesistente."
errore2:str="Errore: non puoi dividere per zero."
errore3:str="Non hai risposto con Y o N."
n1:int=0
n2:int=0
i:str=""
while True:
    def calcolatrice (a,b):
        if(operazione in lista_operazioni):
            if(operazione=="Somma" or operazione=="somma"):
                calcolo=a+b
            if(operazione=="Differenza" or operazione=="differenza"):
                calcolo=a-b
            if(operazione=="Moltiplicazione" or operazione=="moltiplicazione"):
                calcolo=a*b
            if(operazione=="Divisione" or operazione=="divisione"):
                if(b==0):
                    calcolo=errore2
                else:
                    calcolo=a/b
            print("Il risultato dell'operazione è: " +str(calcolo))
        else:
            print(errore1)
    operazione:str=input("Inserisci il tipo di operazione che vuoi fare (somma, differenza, moltiplicazione, divisione): ")
    n1=int(input("Inserisci il primo numero: "))
    n2=int(input("Inserisci il secondo numero: "))
    calcolatrice (n1,n2)
    while True:    
        i=input("Vuoi fare un'altra operazione? Rispondi con 'Y' (Yes) oppure 'N' (No). ")
        if(i=="Y" or i=="N"):
            break
        else:
            print(errore3)
    if(i=="Y"):
        continue
    if(i=="N"):
        break

        
   





