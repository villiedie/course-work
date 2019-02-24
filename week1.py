import re
import json
from collections import Counter
file = open("all_reviews_texts_318352.txt", encoding='UTF8')
reg = []
massiv = []
massivCat2 = []
goda = []
for line in file:
    res = re.search(r'\d\d.\d\d.\d{4}', line)
    if res:
        reg.append(res.group()[6:])
    pik = json.loads(line)
    if pik['cat2'] != '':
        massiv.append(pik['cat3'])
    if pik['cat2'] != '':
        massivCat2.append(pik['cat2'])
print("Года, извлеченные из поля review_date", reg)
print("Количество уникальных категорий из поля 'cat3':", len(list(set(massiv))))
print("Количество отзывов по категориям из поля 'cat3'", Counter(massiv))
print("Количество уникальных категорий из поля 'cat2':", len(list(set(massivCat2))))
print("Количество отзывов по категориям из поля 'cat2", Counter(massivCat2))
print("Количество отзывов по годам", Counter(reg))
file.close()
