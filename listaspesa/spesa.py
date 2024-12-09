#1.Inizializza la lista della spesa vuota
lista_della_spesa = []
#2.Crea un metodo che aggiunge elementi alla lista
def aggiungi_elemento(lista, elemento):
    lista.append(elemento)
    print(f"{elemento} è stato aggiunto alla lista.")
#3.Crea un metodo che visualizza gli elementi della lista
def visualizza_lista(lista):
    if lista:
        print("Ecco gli elementi della tua lista della spesa:")
        for elemento in lista:
            print(f"- {elemento}")
    else:
        print("La lista della spesa è vuota.")
   #4.Crea un metodo che rimuove l’elemento selezionato dall’utente dalla lista
        def rimuovi_elemento(lista, indice):
            if 0 <= indice < len(lista):
                elemento_rimosso = lista.pop(indice)
        print(f"{elemento_rimosso} è stato rimosso dalla lista.")
    else:
        print("Indice non valido. Impossibile rimuovere l'elemento.")
        #5.Aggiungere un menu tramite un ciclo while che permettere all’utente di decidere a quale metodo accedere o se terminare
        def menu():
   while True:
print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per
visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare
gli elementi della lista,\n premi 5 per eliminare un elemento")
x=int(input(""))
if x == 0:
break
elif x == 1:
aggiungi()
elif x == 2:
visualizza()
elif x == 3:
rimuovi()
elif x == 4:
conta()
elif x == 5:
svuota_lista()