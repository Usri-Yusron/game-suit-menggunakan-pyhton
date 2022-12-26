import random
print("---------------------------")
print("GAME GUNTING-BATU-KERTAS  |")
print("silihkan pilih salah satu |")
print("1.Gunting                 |")
print("2.Batu                    |")
print("3.kertas                  |")
print("---------------------------")

tipe = input("Kamu pilih      : ")

if tipe in ("gunting", "batu", "kertas"):
    choice = ("gunting", "batu", "kertas")
    komputer_random = random.choice(choice)
    print("komputer pilih  :", komputer_random)
    print(tipe, "Lawan", komputer_random)
    
    #logic
    if tipe == komputer_random:
        print("tidak ada yang menang, SERI")
    else:
        if tipe == 'batu':
            if komputer_random == 'gunting':
                print("batu menang")
                print ("komputer kalah")
            if komputer_random == 'kertas':
                print("kertas menang")
                print ("anda kalah")
                
        if tipe == 'kertas':
            if komputer_random == 'gunting':
                print("gunting menang")
                print ("anda kalah")
            if komputer_random == 'batu':
                print("kertas menang")
                print ("komputer kalah")
                
        if tipe == 'gunting':
            if komputer_random == 'batu':
                print("batu menang")
                print ("anda kalah")
            if komputer_random == 'kertas':
                print("gunting menang")
                print ("komputer kalah")
    print("---------------------------")
    
    