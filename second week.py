import json
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import pymorphy2
import time
start = time.process_time()
morph = pymorphy2.MorphAnalyzer()
speech = []
typeA = []
typeB = []
typeC = []
typeD = []
k = 0
file = open("all_reviews_texts_318352.txt", encoding='UTF8')
line = file.readline()


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def processing(lines):
    pik = json.loads(lines)
    a = [word_tokenize(t) for t in sent_tokenize(pik['description'])]
#     for word, i in zip(a, range(len(a))):
#         speech.append([])
#        for more in word:
#            p = morph.parse(more)[0]
#            speech[i].append(more)
#            speech[i].append(p.tag.POS)
    return a


def bigrammy(assa):
    for word in assa:
        bigram = nltk.bigrams(word)
        for bi in list(bigram):
            for more in bi:
                p = morph.parse(more)[0]
                speech.append(more)
                speech.append(p.tag.POS)
                speech.append(p.tag.case)
    return split(speech, 6)


# print(bigrammy(processing(line)))

f = open("res.txt", 'w')
for line, i in zip(file, range(100)):
    for bigr in bigrammy(processing(line)):
        k += 1
        print(i)
        if bigr[1] == 'ADJF' and bigr[4] == 'NOUN':
            typeA.append(bigr)
        elif bigr[1] == 'PRTF' and bigr[4] == 'NOUN':
            typeB.append(bigr)
        elif bigr[1] == 'NOUN' and bigr[4] == 'NOUN' and bigr[5] == 'gent':
            typeC.append(bigr)
        elif bigr[1] == 'NOUN' and bigr[4] == 'NOUN' and bigr[5] == 'ablt':
            typeD.append(bigr)
f.write("Количество словосочетаний всего " + str(k) + "\n")
f.write("Количество оставшихся словосочетаний " + str(k-len(typeA)-len(typeB)-len(typeC)-len(typeD)) + "\n")
f.write("Тип 3А " + str(len(typeA)) + "; Тип 3В " + str(len(typeB)) + "; Тип 3С " + str(len(typeC)) +
        "; Тип 3D " + str(len(typeD)) + "\n")
f.write(str(typeA))
f.write(str(typeB))
f.write(str(typeC))
f.write(str(typeD))
f.close()
print(time.process_time()-start)
