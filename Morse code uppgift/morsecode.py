alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

randomNum = randint(0, len(alphabet) - 1)
guess = ""
nRights = 0

def showCurrentChar():
    basic.show_string(alphabet[randomNum])

def showMorse(input):
    Y = 0
    basic.clearScreen()
    for n in input:
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
        
def checkAwnser(guess):
    global nRights
    showMorse(guess)
    if (guess in morseAlphabet):
        if (guess == morseAlphabet[randomNum]):
            basic.show_icon(IconNames.YES)
            nRights += 1
            return True
        else:
            basic.show_icon(IconNames.NO)
            return False
    else:
        basic.show_leds("""
            . # # . .
            # . . # .
            . . # . .
            . . . . .
            . . # . .
            """, 1000)
        return False

def on_button_pressed_a():
    global guess
    guess += "."

    # Visa det man skriver in medan man skriver in det
    showMorse(guess)

def on_button_pressed_b():
    global guess
    guess += "-"
    
    # Visa det man skriver in medan man skriver in det
    showMorse(guess)

def on_button_pressed_ab():
    global guess
    global randomNum


    if checkAwnser(guess) == True:
        randomNum = randint(0, len(alphabet) - 1)
    else:
        if nRights >= 3:
            basic.show_string(str(nRights) + " STREAK")
        
    guess = ""
    showCurrentChar()

def on_gesture_shake():
    global guess
    guess = ""
    showCurrentChar()

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

playIntro("M")
showCurrentChar()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)  
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
