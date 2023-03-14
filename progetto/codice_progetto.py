
import random
lunghezza:int=0
maiuscole:str=""
minuscole:str=""
numeri:str=""
simboli:str=""
rimuovi:str=""
rimuovi_carattere:str=""
i:int=0
password:str=""
carattere:str=""
lista_maiuscole=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lista_minuscole=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lista_numeri=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lista_simboli=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ';', ':', ',', '<', '.', '>', '/', '?', '~']
lista_indice=["maiuscole", "minuscole", "numeri", "simboli" ]
risposte_possibili=["s","n"]
errore:str="Errore: non hai digitato come richiesto, riprova."
conta_maiuscole:int=0
conta_minuscole:int=0
conta_numeri:int=0
conta_simboli:int=0

#30 psw più usate al mondo
lista_psw=["123456","password","123456789","12345","12345678","qwerty","1234567","111111","1234567890","123123","abc123","1234","password1","iloveyou","1q2w3e4r","000000","qwerty123","zaq12wsx","dragon","sunshine","princess","letmein","654321","monkey","27653","1qaz2wsx","123321","qwertyuiop","superman","asdfghjkl"]
attenzione:str="La tua password NON è sicura!"
consiglio:str="Per rendere la password più sicura inserisci anche: "
while True:
     print("Benvenuto!")
     print("Se vuoi generare una password, digita 'GENERA'.")
     print("Se vuoi verificare la sicurezza di una password, digita 'VERIFICA'.")
     input_utente=input()
     if(input_utente=="GENERA"):
          print("Ottimo, hai scelto di generare una password.")
          print("Ora ti verrà posta una serie di domande per configurare al meglio la tua password.")
          print("Per rispondere digita 's' o 'n'")
          lunghezza=input("Inserisci il numero di caratteri della password: ")
          if(lunghezza.isnumeric()==False):
             print(errore)
             break
          maiuscole=input("Vuoi una password con lettere maiuscole? ")
          if(maiuscole not in risposte_possibili):
             print(errore)
             break
          if(maiuscole=="n"):
             lista_indice.remove("maiuscole")
          minuscole=input("Vuoi una password con lettere minuscole? ")
          if(minuscole not in risposte_possibili):
             print(errore)
             break
          if(minuscole=="n"):
             lista_indice.remove("minuscole")
          numeri=input("Vuoi una password con numeri? ")
          if(numeri not in risposte_possibili):
             print(errore)
             break
          if(numeri=="n"):
             lista_indice.remove("numeri")
          simboli=input("Vuoi una password con simboli? ")
          if(simboli not in risposte_possibili):
             print(errore)
             break
          if(simboli=="n"):
             lista_indice.remove("simboli")
          while True:
               rimuovi=input("Vuoi escludere un carattere dalla password? ")
               if(rimuovi not in risposte_possibili):
                    print(errore)
               if(rimuovi=="s"):
                    rimuovi_carattere=input("Inserisci il carattere da escludere: ")
                    if(rimuovi_carattere in lista_maiuscole):
                         lista_maiuscole.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_minuscole):
                         lista_minuscole.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_numeri):
                         lista_numeri.remove(rimuovi_carattere)
                    if(rimuovi_carattere in lista_simboli):
                         lista_simboli.remove(rimuovi_carattere)
                    if(rimuovi=="n"):
                         break
                    if(len(lista_maiuscole)==0):
                         lista_indice.remove("maiuscole")
                    if(len(lista_minuscole)==0):
                         lista_indice.remove("minuscole")
                    if(len(lista_numeri)==0):
                         lista_indice.remove("numeri")
                    if(len(lista_simboli)==0):
                         lista_indice.remove("simboli")
               if(rimuovi=="n"):
                    break    
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
                         carattere=password[i]
                         if(carattere in lista_maiuscole):
                                   conta_maiuscole=conta_maiuscole+1
                         if(carattere in lista_minuscole):
                                   conta_minuscole=conta_minuscole+1
                         if(carattere in lista_numeri):
                                   conta_numeri=conta_numeri+1
                         if(carattere in lista_simboli):
                                   conta_simboli=conta_simboli+1
                         if(conta_maiuscole!=0 and maiuscole!="s"):
                              break
                         if(conta_minuscole!=0 and minuscole!="s"):
                              break
                         if(conta_numeri!=0 and numeri!="s"):
                              break
                         if(conta_simboli!=0 and simboli!="s"):
                              break
                         i=i+1
          print("La tua password è: "+str(password))
     
     if(input_utente=="VERIFICA" or input_utente=="Verifica" or input_utente=="verifica"):
          print("Ottimo, hai scelto di verificare la sicurezza di una password.")
          password=input("Inserisci la password: ")
          lunghezza=len(password)
          while i<lunghezza:
               carattere=password[i]
               if(carattere in lista_maiuscole):
                    conta_maiuscole=conta_maiuscole+1
               if(carattere in lista_minuscole):
                    conta_minuscole=conta_minuscole+1
               if(carattere in lista_numeri):
                    conta_numeri=conta_numeri+1
               if(carattere in lista_simboli):
                    conta_simboli=conta_simboli+1
               i=i+1  
          if(conta_maiuscole==0 or conta_minuscole==0 or conta_numeri==0 or conta_simboli==0 or lunghezza<8):
               print(attenzione)         
          if(conta_maiuscole==0):
                    print(str(consiglio)+"maiuscole.")
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
          if(password in lista_psw):
               print(str(attenzione))
               print("La tua password è una delle più utilizzate al mondo!")
          if(lunghezza<8):
               print("La tua password è troppo corta.") 
     print("Desideri continuare? ")
     continuare=input()
     if(continuare not in risposte_possibili):
          print(errore)
     if(continuare=="n"):
         quit()
    

    