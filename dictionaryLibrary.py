from PyDictionary import PyDictionary
from prettytable import PrettyTable

dictionary=PyDictionary()

def translate():
    
    word = input("Enter your word: ")
    t = PrettyTable([word, 'Meaning'])
    
    try:
        word = word.capitalize()
        meaning = dictionary.meaning(word)
        count = 1
    
        for x in meaning:
            for i in meaning[x]:
                t.add_row([count, i])
                count += 1
        print(t)
    except:
        print("Word not found in dictionary")
        translate()
    
    
if __name__ == '__main__':
    translate()