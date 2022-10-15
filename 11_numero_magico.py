numero_magico = 7
i=1
while i <= 10:
        i=i+1
        numero_utente=int(input("Inserisci il numero magico:"))
        if(numero_utente == numero_magico): 
            print("Complimenti, hai indovinato!")
            break
        else:
            print("Game over!")
A=input("Press any key to exit.")

