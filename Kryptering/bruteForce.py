import time
import random

def passerad_tid():
    return time.time()

# Knäcka lösenord med en rekrussiv funktion
def bruteForce(current, passwordToCrack, alfabet):
    # Om längden på försök strängen är längre än lösenordet så ska den avsluta     
    if len(current) >= len(passwordToCrack):
        return None
 
    # För varje karaktär i alfabetet     
    for char in alfabet:
        # Lägg på nuvarande test med bokstaven den är på i for-loopen
        newTest = current + char
        # Kolla ifall testet är lika med lösenordet
        if newTest == passwordToCrack:
            return {"password": newTest, "p_time": passerad_tid()}
        # Annars gör samma sak igen och spara de den returnerar
        isPassword = bruteForce(newTest, passwordToCrack, alfabet)

        # Kollar ifall det funktionen returnerar inte är lika med if-statsen jag kollar över
        # Antingen så är det None eller så är det det knäckta lösenordet
        if isPassword is not None:
            return isPassword


# Ett annat sätt att knäcka lösenord. Genom att bara testa sig fram slumpmässigt
def randomBruteForce(passwordToCrack, alfabet):
    test = ""
    while passwordToCrack != test:
        test = ''.join(random.choice(alfabet) for _ in range(len(passwordToCrack)))
    return {"password": test, "p_time": passerad_tid()}

def randomPassword(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def main():

    alfabetShort = "abcdefghijklmnopqrstuvwxyz"
    alfabetLong = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!_-" 

    
    length = int(input("Hur många karaktärer ska det slumpmässiga lösenordet vara? > "))

    if length > 4:
        print(f">> Detta kan ta väldigt lång tid då datorn behöver göra {len(alfabetLong) ** length} permutationer för lösenordet med fler tecken")

    print(f"Påbörjar test 1 med följande tecken ({alfabetShort})...")
    passwordToCrack = randomPassword(length, alfabetShort) 
    start_time1 = time.time()
    response1 = bruteForce("", passwordToCrack, alfabetShort)

    print(f"Påbörjar test 2 med följande tecken ({alfabetLong})...")
    passwordToCrack = randomPassword(length, alfabetLong) 
    start_time2 = time.time()
    response2 = bruteForce("", passwordToCrack, alfabetLong)
    
    if response1 is not None or response2 is not None:
        print(f">> Att knäcka lösenordet '{response1['password']}' tog programmet {round(response1['p_time'] - start_time1, 5)} sekunder")
        print(f">> Att knäcka lösenordet '{response2['password']}' tog programmet {round(response2['p_time'] - start_time2, 5)} sekunder")            
    else:
        print(">> Kunde inte hitta lösenordet")


if __name__ == "__main__":
    main()