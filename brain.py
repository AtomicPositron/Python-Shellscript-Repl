import os
import webbrowser as wb
import nltk as nl

primary_Command = " "
secondary_Command = " "

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
    if "null" not in  filter_two:
        return filter_one
    else:
        return filter_two


def keyWord_finder(keyword, text, space):
    if keyword is False or text is False:
        return "nothing"
    else:
        return text.index(keyword) + space


def application_Filter(msg):  
    preposition_list = []
    token = nl.word_tokenize(msg)
    pos_token = nl.pos_tag(token)
    for l in pos_token:
      
        if l[1] in "IN":
            preposition_list.append(l[0])
    
    for p in preposition_list:
         if primary_Command == token[0] and  token[1] == p:
             new_message = msg_filter(msg, p, " ")     
             
    #parameter for no preposition
    
    if len(preposition_list) == 0:
        print("empty")
        new_message = msg
    
    print(msg_filter(new_message, primary_Command, " "))
    
def secondry_command_finder():
    pass
             
    
def search_filter(msg):
    query = msg_filter(msg, primary_Command," ")
   # for s in search_conjunctions:
   #     if s in query and s[0] in query[0]:
   #         print("found or")        
    return query
    # note log filter out for in the beginning after serch command
    
tasks=[
"weather",
"timer",
"time",
"Navigation",
"Traffic",
"reminders",
"calender events",
"Flights"
"Image search"
]  
    
command = "open notepad"

if "open" in command:
    primary_Command = "open"
    application = application_Filter(command)
    #print(application)
  #  os.system(application)
    #print(application.capitalize())
    #os.system("microsoft"+application.capitalize())

if "search" in command:
    primary_Command="search"
    query = search_filter(command)
    wb.open("https://www.google.com/search?q="+ query)
    
#elif "type" or "write" in command_keywords["open"][application]:
#    type_removal = application.find("ty")
# #   application_name_space_filter = msg_filter(application,array_string(len(application),type_removal,application), " ")
#    application_name = msg_filter(application_name_space_filter, " ", " ")
#    print(application_name)
#    os.system(application_name.lower())
#    function_msg = msg_filter(application,application_name," ")
#    message_finder = keyWord_finder("pe",function_msg,2)
 #   print(array_string(len(function_msg),message_finder,function_msg))
    
    
    