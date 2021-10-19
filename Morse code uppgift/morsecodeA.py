alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

radio.set_group(255)
radio.send_number(1)

randomNum = randint(0, len(alphabet) - 1)

messagePart = ""
message: List[str] = []

sender = True
idx = 0 # For pagenation

# Splittar array till text
def split(string, delimiters = ' \t\n'):
    result = []
    word = ''
    
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result


# Konverterar en array till string för att sen kunna skicka meddelandet som en sträng
def sendMessage(msg = [""]): 
    m = ''

    # ["ABBA", "BB", "AA"] --> ABBA;BB;AA
    for i in msg:
        m += i + ';'

    radio.send_string(m)


# Konverterar morsecode till klartext
def translateMessage(msg):
    output = ""

    for m in msg:
        if m in morseAlphabet:
            output += alphabet[morseAlphabet.index(m)]
    
    return output


def showMorse(string):
    Y = 0 # Sätter radnumret till 0
    basic.clearScreen()

    # Loopar igenom strängen "string" och plottar lång eller kort
    for n in string:
        if Y < 5:
            if n == ".":
                led.plot(0, Y)
                led.plot(1, Y)
            elif n == "-":
                led.plot(0, Y)
                led.plot(1, Y)
                led.plot(2, Y)
                led.plot(3, Y)

        Y += 1


# Check if morse is valid
def checkMessage(msgPart):
    showMorse(msgPart)
    
    # Kollar msgPart ifall den finns med i morsecode alphabetet
    if not (msgPart in morseAlphabet):
        basic.show_leds("""
            . . # # .
            . # . . #
            . . . # .
            . . . . .
            . . # . .
            """, 1000)
        return False

    return True


def on_button_pressed_a():
    global messagePart, sender, idx

    if sender: 
        
        messagePart += "."

        showMorse(messagePart)
        
    else: 
        # Subtraherar 1 till index 
        idx -= 1
        
        # Sätter idx till max ifall man går under det lägsta
        if idx < 0:
            idx = len(message) - 1

        # Visar tecknet
        showMorse(message[idx])


def on_button_pressed_b():
    global messagePart, sender, idx

    if sender:
        messagePart += "-"
        showMorse(messagePart)

    else: 
        # Adderar 1 till index för att visa nästa tecknet
        idx += 1

        # Sätter idx till det minsta ifall man passerar det högsta
        if idx > len(message) - 1:
            idx = 0
        
        # Visar tecknet
        showMorse(message[idx])


def on_button_pressed_ab():
    global messagePart, message, sender

    if sender: 
        
        # Om man är skickaren så ska den pusha tecknet till message listan. 
        # Om "messagePart" är tom så ska den skicka meddelandet ifall meddelandet är större än 0
        if messagePart == "":
            if len(message) > 0:

                basic.show_string(translateMessage(message))
                sendMessage(message)

                basic.clearScreen()

                basic.show_string("S>" + str(len(message)) )

                message = []
            else:
                basic.show_icon(IconNames.NO)
        else:    

            if checkMessage(messagePart) == True:
                message.append(messagePart) # push to the main message array

            messagePart = "" 
  
    else: 

        # Visa morsecoden som klartext
        basic.show_string(translateMessage(message))

        sender = True
        message = []
    
    basic.clearScreen()
    

def on_gesture_shake():
    global messagePart, sender
    
    # Tömmer tecknet
    if sender:
        messagePart = ""
        basic.clearScreen()


def on_received_string(receivedString):
    global message, sender

    # Check if received message is larger than 0; to prevent crash
    if len(split(receivedString, ';')) > 0 :
        sender = False
        message = split(receivedString, ';') # "-..;--;-.-." --> ["-..", "--", "-.-."] 

        basic.show_string("R<" + str(len(message)) )

        # Visar första tecknet som användaren för lite snygghet
        showMorse(message[idx])


def light_on():
    display = 0
    
    for x in range(5):
        for y in range(5):
            if led.point(x, y):
                display += 1
 
    while display <= 24:
        xNum = randint(0, 4)
        yNum = randint(0, 4)
        
        if not ( led.point(xNum, yNum) ):
            led.plot(xNum, yNum)
            display += 1
            basic.pause(25)
 

def light_off():
    display = 24
    
    while display >= 0:
        xNum = randint(0, 4)
        yNum = randint(0, 4)
        
        if led.point(xNum, yNum):
            led.unplot(xNum, yNum)
            display -= 1
            basic.pause(25)


def playIntro(letter):
    basic.show_string(letter)
    basic.pause(500)
    light_on()
    
    basic.pause(1000)
    light_off()


# Function calls
playIntro("M")

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

radio.on_received_string(on_received_string) 




