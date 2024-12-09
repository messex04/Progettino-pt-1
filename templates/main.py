
lista_spesa = []



def aggiungi():
    x = str(input("Aggiungi un elemento alla lista \n"))
    lista_spesa.append(x)  


def visualizza():
    for i in range(len(lista_spesa)):  
        print(f"{i + 1}. {lista_spesa[i]}")  



def rimuovi():
    x = input("Inserisci elemento da rimuovere\n")  
    if x in lista_spesa: 
        lista_spesa.remove(x) 
        print(f"L'elemento '{x}' è stato rimosso.") 
    else:
        print(f"L'elemento '{x}' non è presente nella lista.")  


def conta():
    x = set(lista_spesa) 
    for i in x: 
        occorrenze = lista_spesa.count(i)  
        if occorrenze > 1:
            print(f"L'elemento '{i}' appare {occorrenze} volte.")
        else:
            print(f"L'elemento '{i}' appare {occorrenze} volta.")



def svuota_lista():
    lista_spesa.clear()  
    print("La lista è stata svuotata.") 


while True:

    print(" premi 0 per uscire,")
    print(" premi 1 per aggiungere un elemento,")
    print(" premi 2 per visualizzare la lista,")
    print(" premi 3 per eliminare un elemento,")
    print(" premi 4 per contare gli elementi della lista,")
    print(" premi 5 per svuotare la lista")

    x = int(input(""))
    
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
    else:
        print("Opzione non valida. Riprova.")  