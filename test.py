

def array_string(letterend, letterstart, text):
    main_str = ""
    while letterstart != letterend:
        main_str += text[letterstart]
        letterstart += 1

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
    letterstarter = keyWord_finder("me", filter_text, 2)
    print(array_string(len(filter_text), letterstarter, filter_text))

talkBack()