
import random

#liste 
#lista_maiuscole comprende tutte le lettere maiuscole che possono essere utilizzate per generare la psw
lista_maiuscole=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#lista_minuscole comprende tutte le lettere minuscole che possono essere utilizzate per generare la psw
lista_minuscole=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#lista_numeri comprende tutte i numeri che possono essere utilizzati per generare la psw
lista_numeri=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#lista_simboli comprende tutte i simboli che possono essere utilizzati per generare la psw
lista_simboli=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ';', ':', ',', '<', '.', '>', '/', '?', '~']
#lista_indice comprende tutti i tipi di carattere che possono essere utilizzati per generare la psw
lista_indice=["maiuscole", "minuscole", "numeri", "simboli" ]
#risposte_possibili comprende tutte quelle risposte accettate dal programma
#lista_psw comprende le 30 psw più usate al mondo
lista_psw=["123456","password","123456789","12345","12345678","qwerty","1234567","111111","1234567890","123123","abc123","1234","password1","iloveyou","1q2w3e4r","000000","qwerty123","zaq12wsx","dragon","sunshine","princess","letmein","654321","monkey","27653","1qaz2wsx","123321","qwertyuiop","superman","asdfghjkl"]

#variabili str
maiuscole:str=""
minuscole:str=""
numeri:str=""
simboli:str=""
rimuovi:str=""
rimuovi_carattere:str=""
password:str=""
carattere:str=""
errore_1:str="Errore: non hai digitato come richiesto, riprova."
errore_2:str="Errore. Riprova."
attenzione:str="La tua password NON è sicura!"
consiglio:str="Per rendere la password più sicura inserisci anche: "
#variabili int
lunghezza:int=0
i:int=0
conta_maiuscole:int=0
conta_minuscole:int=0
conta_numeri:int=0
conta_simboli:int=0
password_sicura:int=1
password_stampata:int=0
print("Benvenuto")
while True:
    #chiediamo all'utente se vuole generare o verificare una psw
    print("Se vuoi generare una password, digita 'G'.")
    print("Se vuoi verificare la sicurezza di una password, digita 'V'.")
    input_utente=input()
    #l'utente sceglie di generare una psw
    if(input_utente!="G" and input_utente!="V"):
        print(errore_1)
        break
    if(input_utente=="G"):
          print("Ottimo, hai scelto di generare una password.")
          print("Ora ti verrà posta una serie di domande per configurare al meglio la tua password.")
          print("Per rispondere digita 'S' o 'N'")
          #chiediamo all'utente la lunghezza della psw che vuole generare
          lunghezza=input("Inserisci il numero di caratteri della password: ")
          #controlliamo che la lunghezza inserita sia realmente un numero e se non lo è stampiamo un errore
          if(lunghezza.isnumeric()==False):
             print(errore_1)
             break
          #chiediamo se nella password devono esserci maiuscole
          maiuscole=input("Vuoi una password con lettere maiuscole? ")
          #se la risposta dell'utente è sbagliato, stampiamo un errore
          if(maiuscole!="S" and maiuscole!="N"):
             print(errore_1)
             break
          #se la risposta dell'utente è no, togliamo 'maiuscole' dalla lista_indice. In questo modo nessuna lettera maiuscola può essere estratta per la formazione della psw.
          if(maiuscole=="N"):
             lista_indice.remove("maiuscole")
          #ripetiamo i passaggi precedenti con le minuscole
          minuscole=input("Vuoi una password con lettere minuscole? ")
          if(minuscole!="S" and minuscole!="N"):
             print(errore_1)
             break
          if(minuscole=="N"):
             lista_indice.remove("minuscole")
          #ripetiamo i passaggi precedenti con i numeri
          numeri=input("Vuoi una password con numeri? ")
          if(numeri!="S" and numeri!="N"):
             print(errore_1)
             break
          if(numeri=="N"):
             lista_indice.remove("numeri")
          #ripetiamo i passaggi precedenti con i simboli
          simboli=input("Vuoi una password con simboli? ")
          if(simboli!="S" and simboli!="N"):
             print(errore_1)
             break
          if(simboli=="N"):
             lista_indice.remove("simboli")
          #in questo ciclo chiediamo all'utente se vuole escludere un carattere dalle varie liste
          while True:
               rimuovi=input("Vuoi escludere un carattere dalla password? ")
               #verifichiamo se la risposta dell'utente è accettabile
               if(rimuovi!="S" and rimuovi!="N"):
                    print(errore_1)
               #l'utente sceglie di escludere un carattere
               if(rimuovi=="S"):
                    #l'utente inserisce il carattere da escludere
                    rimuovi_carattere=input("Inserisci il carattere da escludere: ")
                    #se il carattere inserito dall'utente è presente in una delle nostre liste, lo rimuoviamo. In questo verrà escluso durante l'estrazione.
                    if(rimuovi_carattere in lista_maiuscole):
                         lista_maiuscole.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_minuscole):
                         lista_minuscole.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_numeri):
                         lista_numeri.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_simboli):
                         lista_simboli.remove(rimuovi_carattere)
                    #l'utente sceglie di non rimuovere altri caratteri
                    if(rimuovi=="N"):
                         break
                    #se l'utente decide di eliminare tutti i caratteri di una lista, togliamo direttamente il tipo di carattere dalla lista_indice. Es: l'utente rimuove tutti i numeri (0,1,2,3,4,5,6,7,8,9). Rimuoviamo 'numeri' dalla lista_indice.
                    if(len(lista_maiuscole)==0):
                         lista_indice.remove("maiuscole")
                    if(len(lista_minuscole)==0):
                         lista_indice.remove("minuscole")
                    if(len(lista_numeri)==0):
                         lista_indice.remove("numeri")
                    if(len(lista_simboli)==0):
                         lista_indice.remove("simboli")
               #l'utente sceglie di tenere tutti i caratteri
               if(rimuovi=="N"):
                    break    
                #procediamo con la generazione della psw
    while i<int(lunghezza):
            #estraiamo il tipo di carattere da inserire
            carattere=random.choice(lista_indice)
            #in base al tipo di carattere, estraiamo il carattere dalla lista corrispondente
            if(carattere=="maiuscole"):
                password=str(password)+random.choice(lista_maiuscole)
            if(carattere=="minuscole"):
                password=str(password)+random.choice(lista_minuscole)
            if(carattere=="numeri"):
                password=str(password)+random.choice(lista_numeri)
            if(carattere=="simboli"):
                password=str(password)+random.choice(lista_simboli)
            carattere=password[i]
                         #contiamo quanti e quali caratteri presenta la psw
            if(carattere in lista_maiuscole):
                                   conta_maiuscole=conta_maiuscole+1
            if(carattere in lista_minuscole):
                                   conta_minuscole=conta_minuscole+1
            if(carattere in lista_numeri):
                                   conta_numeri=conta_numeri+1
            if(carattere in lista_simboli):
                                   conta_simboli=conta_simboli+1
                         #se l'utente aveva detto di voler un certo carattere nella sua password ma questo non risulta esserci, rigeneriamo la password.
            if(conta_maiuscole!=0 and maiuscole!="S"):
                              break
            if(conta_minuscole!=0 and minuscole!="S"):
                              break
            if(conta_numeri!=0 and numeri!="S"):
                              break
            if(conta_simboli!=0 and simboli!="S"):
                              break
            i=i+1
            #stampiamo la password generata
    print("La tua password è: "+str(password))
    password_stampata=1
    #l'utente sceglie di verificare la sicurezza di una psw
    if(input_utente=="V"):
        print("Ottimo, hai scelto di verificare la sicurezza di una password.")
        #l'utente inserisce la password da controllare
        password=input("Inserisci la password: ")
        #controlliamo la lunghezza della password inserita
        lunghezza=len(password)
        #in questo ciclo controlliamo tutti i caratteri della password, usando come parametro la lunghezza.
        while i<lunghezza:
               carattere=password[i]
               #contiamo quanti e quali caratteri presenta la psw
               if(carattere in lista_maiuscole):
                    conta_maiuscole=conta_maiuscole+1
               if(carattere in lista_minuscole):
                    conta_minuscole=conta_minuscole+1
               if(carattere in lista_numeri):
                    conta_numeri=conta_numeri+1
               if(carattere in lista_simboli):
                    conta_simboli=conta_simboli+1
               i=i+1  
        #se la psw non presenta tutti i tipi di carattere o è lunga meno di 8 caratteri, la consideriamo non sicura
        if(conta_maiuscole==0 or conta_minuscole==0 or conta_numeri==0 or conta_simboli==0 or lunghezza<8):
               print(attenzione)
               password_sicura=0
        #in base a quale tipo di carattere manca, stampiamo un suggerimento
        if(conta_maiuscole==0):
            print(str(consiglio)+"maiuscole.")
        #poniamo nuovamente i contatori = 0
        conta_maiuscole=0   
        if(conta_minuscole==0):
            print(str(consiglio)+"minuscole.")     
        conta_minuscole=0  
        if(conta_numeri==0):
            print(str(consiglio)+"numeri.")
        conta_numeri=0 
        if(conta_simboli==0):
            print(str(consiglio)+"simboli.")
        conta_simboli=0
        #controlliamo se la psw rientra in quelle più utilizzate al mondo
        if(password in lista_psw):
               print("La tua password è una delle più utilizzate al mondo!")
               password_sicura=0
        #consideriamo come lunghezza minima per considerare una psw sicura quella di 8 caratteri
        if(lunghezza<8):
               print("La tua password è troppo corta.") 
               password_sicura=0
        if(password_sicura==1):
            print("La tua password è sicura.")
    if(password_stampata==0):
        print(errore_2)
    #chiediamo all'utente se vuole riutilizzare il programma
    print("Desideri continuare? ")
    continuare=input()
    if(continuare!="S" and continuare!="N"):
          print(errore_1 )
    if(continuare=="N"):
         quit()
