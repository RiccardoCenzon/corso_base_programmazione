#aggiungere la possibilità di rimuovere un carattere dalla generazione casuale
#inizializzare le variabili 
#if psw sicura

import random
i=0
password=""
lista_maiuscole=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lista_minuscole=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lista_numeri=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lista_indice=["maiuscole", "minuscole", "numeri", "simboli" ]
risposte_possibili=["Sì","Si","si","SI","No","no","NO"]
lista_simboli=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ';', ':', ',', '<', '.', '>', '/', '?', '`', '~']
errore="Errore: non hai digitato come richiesto, riprova."
#30 psw più usate al mondo
lista_psw=["123456","password","123456789","12345","12345678","qwerty","1234567","111111","1234567890","123123","abc123","1234","password1","iloveyou","1q2w3e4r","000000","qwerty123","zaq12wsx","dragon","sunshine","princess","letmein","654321","monkey","27653","1qaz2wsx","123321","qwertyuiop","superman","asdfghjkl"]
consiglio="Per rendere la password più sicura inserisci anche: "
while True:
    print("Benvenuto!")
    print("Se vuoi generare una password, digita '1'.")
    print("Se vuoi verificare la sicurezza di una password, digita '2'.")
    input_utente=int(input(""))
    if(input_utente==1):
        print("Ottimo, hai scelto di generare una password.")
        print("Ora ti verrà posta una serie di domande per configurare al meglio la tua password.")
        print("Per rispondere digita 'Sì' o 'No'")
        lunghezza=input("Inserisci il numero di caratteri della password: ")
        if(lunghezza.isnumeric()== False):
             print(errore)
             break
        maiuscole=input("Vuoi una password con lettere maiuscole? ")
        if(maiuscole not in risposte_possibili):
             print(errore)
             break
        if(maiuscole=="No"):
             lista_indice.remove("maiuscole")
        minuscole=input("Vuoi una password con lettere minuscole? ")
        if(minuscole not in risposte_possibili):
             print(errore)
             break
        if(minuscole=="No"):
             lista_indice.remove("minuscole")
        numeri=input("Vuoi una password con numeri? ")
        if(numeri not in risposte_possibili):
             print(errore)
             break
        if(numeri=="No"):
             lista_indice.remove("numeri")
        simboli=input("Vuoi una password con simboli? ")
        if(simboli not in risposte_possibili):
             print(errore)
             break
        if(simboli==""):
             lista_indice.remove("simboli")
        while i<int(lunghezza):
                carattere=random.choice(lista_indice)
                if(carattere=="maiuscole"):
                     password=str(password)+random.choice(lista_maiuscole)
                if(carattere=="minuscole"):
                     password=str(password)+random.choice(lista_minuscole)
                if(carattere=="numeri"):
                     password=str(password)+random.choice(lista_numeri)
                if(carattere=="simboli"):
                     password=str(password)+random.choice(lista_simboli)
                i=i+1
        print("La tua password è: "+str(password))
    if(input_utente==2):
        print("Ottimo, hai scelto di verificare la sicurezza di una password.")
        password=input("Inserisci la password: ")
        lunghezza=len(password)
        while i<lunghezza:
            carattere=password[i]
            if(carattere not in lista_maiuscole):
                consiglio=str(consiglio)+"maiuscole"
            if(carattere not in lista_minuscole):
                consiglio=str(consiglio)+", minuscole"
            if(carattere not in lista_numeri):
                consiglio=str(consiglio)+", numeri"
            if(carattere not in lista_simboli):
                consiglio=str(consiglio)+", simboli"
            print(consiglio)
            if(password in lista_psw or lunghezza<8):
                print("La password non è sicura.")
                print("Ecco a te 5 suggerimenti per rinforzare la tua password.")
                print("1. Scegli una lunghezza adeguata. Si consigliano almeno 8 caratteri.")
                print("2. Cerca di includere il più possibile lettere maiuscole e minuscole, numeri e simboli.")
                print("3. Non utilizzare la stessa password per più servizi online.")
                print("4. Non includere informazioni personali come il proprio nome, cognome, data di nascita, città in cui si vive...")
                print("5. Utilizza questo programma per verificare la sicurezza della tua password.")
    print("Desideri continuare? Rispondi con 'Sì' o 'No'. ")
    input_utente=input()
    if(input_utente not in risposte_possibili):
         print(errore)
    if(input_utente=="No" or input_utente=="no" or input_utente=="NO"):
         quit()
    

    