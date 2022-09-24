# create a word dictionary

def dictionary():
    word = input("Masukkan perkataan: ")
    wordDictionary = {
        'makan': 'perbuatan untuk memasukkan makanan ke dalam mulut',
        'berlari': 'perbuatan untuk bergerak dengan cepat',
        'berenang': 'perbuatan untuk bergerak dengan menggunakan tangan di dalam air',
        'mencarut': 'perbuatan memaki-maki',
        'telefon bimbit': 'peranti untuk membuat panggilan telefon',
    }
    
    if word in wordDictionary:
        print(wordDictionary[word])
    elif word not in wordDictionary:
        print("Perkataan tidak wujud dalam kamus")
        
    dictionary()

if __name__ == '__main__':
    dictionary()