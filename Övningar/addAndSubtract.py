num = randint(0, 9)

def on_button_pressed_a():
    global num
    num -= 1

def on_button_pressed_b():
    global num
    num +=1

def on_gesture_shake():
    global num
    basic.clear_screen()
    num = randint(0, 9)

def on_forever():
    basic.show_number(num)
    
input.on_gesture(Gesture.Shake, on_gesture_shake)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
basic.forever(on_forever)
