from PyDictionary import PyDictionary
from prettytable import PrettyTable

dictionary=PyDictionary()

def translate():
    
    word = input("Enter your word: ").capitalize()
    t = PrettyTable([word, 'Meaning'])
    meaning = dictionary.meaning(word)
    
    count = 1
    
    for x in meaning:
        for i in meaning[x]:
            t.add_row([count, i])
            count += 1
    print(t)
    
    
if __name__ == '__main__':
    translate()