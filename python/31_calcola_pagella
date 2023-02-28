i=1
primo_voto=0
secondo_voto=0
somma_voti=0
somma_totale=0
materie_insufficienti=0
while i<6:
    if(i==1):
        materia="Matematica"
    if(i==2):
        materia="Italiano"
    if(i==3):
        materia="Storia"
    if(i==4):
        materia="Inglese"
    if(i==5):
        materia="Informatica"
    primo_voto=input("Inserisci il primo voto di "+str(materia)+": ")
    secondo_voto=input("Inserisci il secondo voto di "+str(materia)+": ")
    somma_voti=int(primo_voto)+int(secondo_voto)
    if (int(somma_voti)/2)<=6:
        materie_insufficienti=materie_insufficienti+1
    somma_totale=somma_voti+somma_totale
    i=i+1
media_totale=int(somma_totale)/10
if(media_totale>=6 and materie_insufficienti<=1):
    esito="promosso"
else:
    esito="bocciato"
print("La tua media totale è: "+str(media_totale))
print("Il numero di materie insufficienti è: "+str(materie_insufficienti))
print("Sei... "+str(esito))
    


    
