import pyautogui
import time
import os


f = open('name.txt', 'r')
screen = pyautogui.size()
startButton = (10, screen.height - 10)
response_num = 0
Botname = "boxDroid"
verification_bool = 0
user_name = ""
user_age = 0
gender = " "

pyautogui.PAUSE = 1.25
inbox_responses = [

]
response = [
    "hi",
    "my name is " + Botname
]
positive_reponses = [
    "yes"
    "okay"
    "fine"
    "you too"
]


class Person:
    def __init__(self, name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender



def array_filter(removed_array, filtered_array):
    for r in removed_array:
        for f in filtered_array:
            if r == f:
                removed_array.remove(r)
            else:
                pass


def array_string(letterend, letterstart, text):
    main_str = ""
    while letterstart != letterend:
        main_str += text[letterstart]
        letterstart += 1

    return main_str


def msg_filter(msg, filter1, filter2,):
    filter_one = msg.replace(filter1, " ")
    filter_two = filter_one.replace(filter2, "")
    if " " not in  filter_two:
        return filter_one
    else:
        return filter_two


def keyWord_finder(keyword, text, space):
    return text.index(keyword) + space

def verification(verification):
    pyautogui.press("Enter")
    pyautogui.typewrite("Verification process")
    pyautogui.press("Enter")
    pyautogui.typewrite(f"verifcation {verification}")
    pyautogui.press("Enter")
    response.append("What is your name?")
    inbox_responses.append("What is your name?")
    msg = pyautogui.prompt(response[len(response)-1], "Response")
    if "name" in response[len(response)-1]:
        if "my name " in msg or "call me " in msg:
            filter_text = msg_filter(msg.lower(), "is", " ")
            letterstarter = keyWord_finder("me", filter_text, 2)
            user_name = array_string(len(filter_text), letterstarter, filter_text)
            response.append("Nice to meet you " + user_name)
            time.sleep(3)
            response.append("How old are you")
            inbox_responses.append("How old are you")
        else:
            user_name = msg
            response.append("Nice to meet you " + user_name)
            time.sleep(3)
            response.append("How old are you")
            inbox_responses.append("How old are you")
        msg = pyautogui.prompt(response[len(response)-1], "Response")

    if "old " in response[len(response)-1]:
        if "years" in msg and "old" in msg and "i am" in msg:
            filter_text = msg_filter(msg.lower(), "i", "years old")
            letterstarter = keyWord_finder("am", filter_text, 2)
            user_age = array_string(len(filter_text), letterstarter, filter_text)
            response.append(f"okay {user_age}")
        else:
            user_age = msg
            response.append(f"okay {user_age}")
        response.append("Male or female")
        inbox_responses.append("Male or female")
        msg = pyautogui.prompt(response[len(response)-1], "Response")

    if "male" in response[len(response)-1]:
        if "m" in msg or "f" in msg:
          response.append("Verification process done")
          array_filter(response,inbox_responses)
          print(response)
          return 1

if verification(verification_bool) == 1:
    verification_bool = 1

def operation():
    command_keywords=  {
        "open": {
            "notepad" : [
                "type",
                "write"
            ]
        }
    }
    pyautogui.press("Enter")
    response.append("What can i do for you")
    command = pyautogui.prompt("Assistant","What can i do for You")
    if "open" in command:
        removal_conjonctions = msg_filter(command, "and", " ")
        application = msg_filter(removal_conjonctions, "open", " ")
        if "type" or "write" in command_keywords["open"][application]:
            type_removal = application.find("ty")
            application_name = msg_filter(application,array_string(len(application)-1,type_removal,application), " ")
            print(application_name)
            os.system(application_name.lower() + ".exe")
            function_msg = msg_filter(application,application_name," ")
            message_finder = keyWord_finder("pe",function_msg,2)
            print(array_string(len(function_msg),message_finder,function_msg))
        else:
            print(application)
            os.system(application.lower() + ".exe")
            command = pyautogui.prompt("Assistant", "What can i do for You")


    pyautogui.countdown(5)
while True:
    pyautogui.press("Enter")
    pyautogui.typewrite(response[response_num], interval=0.15)
    response_num += 1
    print(response_num)
    if response_num > len(response) - 1:

        if verification_bool == 0:
            verification(verification_bool)
        else:
            operation()