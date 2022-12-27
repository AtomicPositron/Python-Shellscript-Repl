relation = open("relation.txt",  'r')

msg= "my brother namedavid"
v1_msg = msg.replace("is", "")
new_msg = v1_msg.replace(" ", "")
firstLetterNumber = new_msg.index("me")+2
for t in relation:
    if t in msg and t not in msg :
        while firstLetterNumber != len(new_msg):
            print(f"{t}: {new_msg[firstLetterNumber]}")
            firstLetterNumber += 1
        break
    else:
        print("none \n")
        while firstLetterNumber != len(new_msg):
            print(new_msg[firstLetterNumber])
            firstLetterNumber += 1
        break
