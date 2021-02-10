import random

opcje = ["1", "2", "3"]
wybor = ()
nr_gracza = 0

def wybor_broni(opcje):
    for wybor in opcje:
        if wybor == opcje[0]:
            print("Wybrałeś Papier")
            

        if wybor == opcje[1]:
            print("Wybrałeś Kamień")
            

        if wybor == opcje[2]:
            print("Wybrałeś Nożyce")
            
def komputer():
    for wybor in opcje:
        if nr_gracza == 1:
            random.randint(0, 2)
            wybor = random.randint(0, 2)

            if wybor == 0:
                print("Komputer: Papier")
                wybor == opcje[0]
                

            if wybor == 1:
                print("Komputer: Kamień")
                wybor == opcje[1]
                

            if wybor == 2:
                print("Komputer: Nożyce")
                wybor == opcje[2]
                
        
def gracz(nr_gracza):
    if nr_gracza == 1:
        return ()
    else:
        print("Papier-1, Kamień-2, Nożyce-3")
        return wybor
    
while wybor != 'q':
    wybor = gracz(nr_gracza)  
    wybor = input("Wybierz swoja bron: ")

    if (wybor != "1" or wybor != "2" or wybor != "3"):
            print("Podałeś nieprawidłową wartość!")
            continue
    
    
    nr_gracza = (nr_gracza + 1) % 2 

wybor_broni(opcje)