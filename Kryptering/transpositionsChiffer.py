import math

def fillArray(txt, arr):
    currentChar = 0
    
    rCount = 0
    cCount = 0
    
    # För varje karaktär, fyll ut listan
    while currentChar <= len(txt) - 1:
        # Om raden är slut gå till nästa rad kolumn 0
        if len(arr[0]) - 1 < cCount:
            rCount += 1
            cCount = 0
        
        arr[rCount][cCount] = txt[currentChar]
        cCount += 1
        currentChar += 1
    
    return arr


def matrixToString(arr):
    output = ""
    
    # För varje bokstav i matrisen så ska den lägga till det i strängen
    for idx in range(len(arr)):
        for val in arr[idx]:
            output += val
    
    return output


def transposeMatrix(inArr, outArr):
    for r in range(len(inArr)):
        # Varje kolumn
        for c in range(len(inArr[0])):
            # Byt platsen på Kolumnen och raden från arry till outArr
            outArr[c][r] = inArr[r][c]

    return outArr


def transpositionEncrypt(txt, cAmount, encrypt):
    cols = cAmount
    rows = math.ceil(len(txt) / cols)
    
    if encrypt: 
        arr = fillArray(txt, [["" for n in range(cols)] for m in range(rows)]) # fyller en lista med en sträng
        print("Fyll listan: ", arr)
        outArr = transposeMatrix(arr, [["" for n in range(rows)] for m in range(cols)])  # Vänder på listan
        print("Vända listan", outArr)
    else: # Meddelandet ska avkrypteras då så börjar arrayen som omvänd jämfört med den orginella
        arr = fillArray(txt, [["" for n in range(rows)] for m in range(cols)])
        outArr = transposeMatrix(arr, [["" for n in range(cols)] for m in range(rows)])
    
    return matrixToString(outArr)


def traspositionBruteForce(string, comparing):
    tests = [] 
    n = 1

    while n < 100:
        current = transpositionEncrypt(string, n, False)
        tests.append(current)

        if current == comparing:
            return tests

        n += 1
    else:
        return "Kunde inte hitta rätt lösenord"
    

def main():
    crack = input("Vill du knäcka ett lösenord? (1 / True) eller (0 / False) > ")

    if crack == "True" or crack == "true" or crack == "1":
        inText = input("Skriv in ett ord eller en mening som ska knäckas > ")
        comparison = input("Skriv ett ord eller en mening som du vill jämföra mo > ")

        outList = traspositionBruteForce(inText, comparison)
        
        for n in outList:
            print(n)
            
    elif crack == "False" or crack == "false" or crack == "0":
        rows = int(input("Hur många rader ska det vara i matrisen? "))
        
        inText = input("Skriv in ett ord eller en mening ska hanteras > ")
        
        encrypt = input("Ska texten krypteras (1 / True) eller avkrypteras (0 / False) > ")

        if encrypt == "True" or encrypt == "true" or encrypt == "1":
            outText = transpositionEncrypt(inText, rows, True)
            print(f"Texten '{inText}' krypterades till '{outText}'")
        elif encrypt == "False" or encrypt == "false" or encrypt == "0":
            outText = transpositionEncrypt(inText, rows, False)
            print(f"Texten '{inText}' avkrypterades till '{outText}'")
    else:
        crack = input("Vill du knäcka ett lösenord? (1 / True) eller (0 / False) > ")

if __name__ == "__main__":
    main()