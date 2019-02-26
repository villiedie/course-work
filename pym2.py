import pymorphy2
morph = pymorphy2.MorphAnalyzer()
inlo = input("Введите слово:")
p = morph.parse(inlo)[0]
if p.tag.POS in ['NOUN', 'ADJF', 'PRTF', 'NUMR', 'NPRO']:
    print("Падеж слова ")
    if p.tag.case == 'nomn':
        print("Именительный")
    elif p.tag.case == 'gent':
        print("Родительный")
    elif p.tag.case == 'datv':
        print("Дательный")
    elif p.tag.case == 'accs':
        print("Винительный")
    elif p.tag.case == 'ablt':
        print("Творительный")
    elif p.tag.case == 'loct':
        print("Предложный")
    elif p.tag.case == 'voct':
        print("Звательный")
    elif p.tag.case == 'gen2':
        print("Второй родительный(частичный)")
    elif p.tag.case == 'acc2':
        print("Второй винительный")
    elif p.tag.case == 'loc2':
        print("Второй предложный(местный)")
if p.tag.number == 'sing':
    print("Единственное число")
else:
    print("Множественное число")
print("Нормальная форма слова: ", p.normal_form)
