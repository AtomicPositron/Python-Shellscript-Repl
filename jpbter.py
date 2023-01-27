import nltk 

string ="search for ms-dos"
nltk.download('averaged_perceptron_tagger')
# install punkt
y = nltk.word_tokenize(string)
x = nltk.pos_tag(y)
for r in x:
    print(r)
    print(r[1])
    
print(x)
