import pyautogui
import time

f = open('name.txt', 'r')
screen = pyautogui.size()
startButton = (10, screen.height-10)
message_num = 0
name = "boxDroid"
personsName = ""
pyautogui.PAUSE = 1.25
message = [
    "hi",
    "how are you",
    "my name is "+name,
    "what is your name"
]

def talkBack():
    msg = pyautogui.prompt("Text", "Talk to me")
    for name in f:
        if msg.__contains__(("my name is" + name).lower()):
            print("found")
            message.append("nice to meet you too")


pyautogui.moveTo(startButton)
pyautogui.rightClick()
pyautogui.typewrite("NotePad")
pyautogui.press("Enter")
time.sleep(3)
while True:
    pyautogui.typewrite(message[message_num],interval=0.15)
    pyautogui.press("Enter")
    message_num += 1
    print(message_num)
    if message_num > len(message)-1:
       talkBack()

