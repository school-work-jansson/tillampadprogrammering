ID = 0
targetedID = 0

radio.set_group(255)
radio.send_number(ID)

def send(text = "", id = 0):
    radio.send_string(text)
    radio.send_number(id)

def on_button_pressed_AB():
    send("Hello World", targetedID)

# Väljer mellan IDt som man ska få
def on_button_pressed_a():
    global targetedID
    # Sänk target ID med 1
    if targetedID <= 0:
        targetedID = 0
    else:
        targetedID -= 1

def on_button_pressed_b():
    global targetedID
    # Ökar target ID med 1
    targetedID += 1
    
def on_received_number(receivedNumber):
    global ID
    
    # Söker efter ett ledigt nummer 
    if receivedNumber == ID:
        ID += 1
        radio.send_number(ID)

    # Kollar nummret som den får ifall det är targetID
    
def on_received_string(receivedString):
    # Om ID är lika med targetID så ska den hantera meddelandet
    if ID == targetedID:
        basic.show_string(receivedString)

def on_forever():
    basic.show_number(ID)
basic.forever(on_forever)

input.on_button_pressed(Button.AB, on_button_pressed_AB)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.on_received_string(on_received_string)
radio.on_received_number(on_received_number)