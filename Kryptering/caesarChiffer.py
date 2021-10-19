
def shift(char, shiftAmount):
    # EXAMPLE -> chr((ord(char) + shiftAmount - 97) % 26 + 97) 
    # 122(z) + 1(shiftAmount) = 123
    # 123 - 97 = 26 
    # 26 % 26 = 0 + 97 = 97 = a

    # Hanterar icke ascii tecken
    if char == 'å':
        return 'å'
    elif char == 'ä':
        return 'ä'
    elif char == 'ö':
        return 'ö'
    else:
         # Hanterar gemener och versaler
        if char.isupper():
            return chr((ord(char) + shiftAmount - 65) % 26 + 65)
        elif char.islower():
            return chr((ord(char) + shiftAmount - 97) % 26 + 97)    
        elif ord(char) == 0 or ord(char) == 32: # hanterar mellanslag
            return chr(32)
        else:
            return ''

    
def caesarEncrypt(txt, shiftAmount):
    out = ""
    
    for n in txt:
        out = shift(n, shiftAmount)
    return out


# Genom "bruteforce" så testar den att shifta tecknerna med alla ascii nummer av tecken i alfabetet
def caesarBruteForce(txt):
    attemps = [] # lista som håller alla försök
    
    tmp = "" # en temporär sträng

    for num in range(1, 26): 
        for n in txt:
            tmp += shift(n, num)
        attemps.append(tmp) # lägger till det forcerade försöket i listan
        tmp = "" # Tömmer den temporära strängen
    
    return attemps

def main():
    crack = input("Vill du knäcka ett lösenord? Ja (1 / True) eller Nej (0 / False) > ")

    if crack == "True" or crack == "true" or crack == "1":
        inText = input("Skriv in ett ord eller en mening som ska knäckas > ")
        outList = caesarBruteForce(inText)

        for n in outList:
            print(n)

    elif crack == "False" or crack == "false" or crack == "0":
        shiftAmount = int(input("Hur många steg ska varje bokstav skiftas med? > "))
        encrypt = input("Ska texten krypteras Ja (1 / True) eller avkrypteras Nej (0 / False)")

        if encrypt == "True" or encrypt == "true" or encrypt == "1":
            inText = input("Skriv in ett ord eller en mening ska krypters > ")
        elif encrypt == "False" or encrypt == "false" or encrypt == "0":
            inText = input("Skriv in ett ord eller en mening ska avkrypteras > ")
            shiftAmount *= -1

        outText = caesarEncrypt(inText, shiftAmount)

        print(f"Texten '{inText}' krypterades till '{outText}'")

    else:
        crack = input("Vill du knäcka ett lösenord? Ja (1 / True) eller Nej (0 / False) > ")

if __name__ == "__main__":
    main()