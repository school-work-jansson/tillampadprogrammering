from math import *

personnummer = input("Skriv in ett personnummer i formatet (ÅÅÅÅMMDD-XXXX) > ")

def formatera(personnummer):
    personnummerLista = [char for char in personnummer]
    if len(personnummerLista) == 13 or len(personnummerLista) == 12: # Om det är formatet (ÅÅÅÅMMDD-XXXX) eller (ÅÅÅÅMMDDXXXX)
        del personnummerLista[:2] # Ta bort de 2 första ÅÅ
    del personnummerLista[-1] # Tar bort sista siffran i personnummret (inte nödvändigt)
    
    tmp = [] # en tmp lista som används för att hålla i personnumret minus ev bindesträck
    for elem in personnummerLista: # letar efter element i listan som inte är en siffra och struntar i att lägga den i tmp listan       
        if elem.isdigit():
            tmp.append(elem)
    
    return tmp

def kontrollSiffra(personnummer):
    siffersumma = 0 # Variabel för att hålla kontroll siffran
    
    for idx, elem in enumerate(personnummer): # En enumerate loop som har ett count och en value, loopar igenom hela personnummret
        if not (((idx + 1)&1) == 0): # Kollar ifall indexet är udda för att "multiplcera varannan med 2"
            if int(elem) * 2 > 9: # Ifall talet * 2 är större en 10
                for n in str(int(elem) * 2):
                    siffersumma += int(n) # Addera varje siffrorna till siffersumman
            else:
                siffersumma += int(elem) * 2 # addera till siffersumman plus multiplicera siffran med 2
        else:
            siffersumma += int(elem)

    kSiffra = (ceil(siffersumma/10) * 10) - siffersumma # Avrunda upp siffersumman till närmaste tiotal - siffersumman

    return kSiffra

kontroll = kontrollSiffra(formatera(personnummer))

print(f"Räknade ut kontrollsiffran {kontroll}")

if kontroll == int(personnummer[-1]):
    print(f"Kontrollsiffran {personnummer[-1]} stämmer.")
else:
    print(f"Kontrollsiffran {personnummer[-1]} stämmer inte.")
