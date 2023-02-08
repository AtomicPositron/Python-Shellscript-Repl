import os
import pyttsx3
import webbrowser
import time 

_main_memory = []

COMMAND_REFRENCE = [
    "open",
    "quit",
    "search",
    "help"
]
def response(text:str, command:str):
        engine = pyttsx3.init()
        print(command + " "+ text)
        engine.say(command +" "+text)
        engine.runAndWait()

def handle_open(input:str):
    response(input, "opening")
    
    if os.system(input):
        os.system("microsoft"+input)
    

def handle_quit():
    quit()

def handle_search(query:str):
    response(" ", "alright")
    webbrowser.open(f"https://www.google.com/search?q={query}")  

def handle_help():
    print(f"list of commands \n {COMMAND_REFRENCE}")


#def handle_restart(type:str):
#    os.system(f" cmd /{type.lower()} C:/Users/Mars/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Mars/OneDrive/Documents/Language/Python/ShellProject/main.py")

def input_fun(command:str) -> list:
    global index_one
    global index_two
    global _sleeptimer
    index_one = 0
    index_two = 0
    _sleeptimer = 0
    if "and" in command or "then" in command:
        if "and" in command and "then" in command:
            _split_layer_one = command.split("and")
            _split_layer_two = [substring.split('then') for substring in _split_layer_one]
            for item in _split_layer_two:
                index_one += 1
                for _item_command in item:
                    index_two += 1
                    print(len(_item_command)-1+len(item)-1, " length")
                    if index_two+index_one != len(_item_command)-1+len(item)-1 :
                        _sleeptimer += 1
                        print(_sleeptimer)
                    else:
                        _sleeptimer = 0
                    
                    print(len(item))
                    print(_item_command)
                    _command  = _item_command.strip()
                    argument, *text =  _command.split()
                    arg = argument
                    txt = text
                    command_object = {
                        "_command_type": arg,
                        "_command_text":  txt
                    }
                                                            
                    # Timing function
                                        
                    
                    #_main_memory.append(command_object)
                    #print(_main_memory)
                    #return arg, txt
        
    else:
        command  =command.strip()
        argument, *text =  command.split()
        arg = argument
        txt = text
        command_object = {
            "_command_type": arg,
            "_command_text":  txt
        }
        _main_memory.append(command_object)
        
        return arg, txt
    
def run_command(list:list):
    for x in list:
        if x["_command_type"] in COMMAND_REFRENCE:
            command = x["_command_type"].lower()
            text = " ".join(x["_command_text"])
            match command:
                case "open":
                    handle_open(text)   
                    list.remove(x)  
                case "quit":
                    handle_quit()
                case "search":
                    handle_search(text)
                    list.remove(x)
                #case "restart":
                #      handle_restart(text)
                case _:
                    raise NotImplementedError(f"The command {command} dosen't exist")
        else:
            command = x["_command_type"]
            list.remove(x)           
            print(f"The command {command} dosen't exist")
        
            
    
def run():
    while True:
        try:
           command  = input("input: ")
           input_fun(command)
        except TypeError:
            print("error")
        except ValueError:
            print("empty string")
        except NotImplementedError:
            print("command dosen't exist")
        except KeyboardInterrupt:
            print("\n quiting program")
            quit()
        finally:
            if len(_main_memory) > 0:
                time.sleep(_sleeptimer)
                try:
                     run_command(_main_memory)     
                except IndexError:
                    print("Bye")
                    quit()
                finally:
                   pass


if __name__ == "__main__":
    run()