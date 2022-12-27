import pyautogui
#import time

f = open('name.txt', 'r')
screen = pyautogui.size()
startButton = (10, screen.height - 10)
message_num = 0
name = "boxDroid"

pyautogui.PAUSE = 1.25
message = [
    "hi",
    "how are you",
    "my name is " + name,
    "what is your name"
]


def array_string(letterend, letterstart, text):
    main_str = ""
    while letterstart != letterend:
        main_str += text[letterstart]
        letterstart += 1
        print(main_str)
    return main_str


def msg_filter(msg, filter1, filter2,):
    filter_one = msg.replace(filter1, " ")
    filter_two = filter_one.replace(filter2, "")
    return filter_two


def keyWord_finder(keyword, text, space):
    return text.index(keyword) + space


def talkBack():
    #msg = pyautogui.prompt("Text", "Talk to me")
    msg = "my name is michael"
    filter_text = msg_filter(msg, "is", " ")
    print(filter_text)
    letterstarter = keyWord_finder("me", filter_text, 2)
    print(letterstarter)
    print(array_string(len(msg)-1, letterstarter, filter_text))


#pyautogui.moveTo(startButton)
#pyautogui.rightClick()
#pyautogui.typewrite("NotePad")
#pyautogui.press("Enter")
#time.sleep(5)
pyautogui.countdown(5)
while True:
    pyautogui.typewrite(message[message_num], interval=0.15)
    pyautogui.press("Enter")
    message_num += 1
    print(message_num)
    if message_num > len(message) - 1:
        talkBack()
