import json


def categories(filename):
    massiv = []
    for lines in filename:
        pik = json.loads(lines)
        if pik['cat2'] != '':
            massiv.append(pik['cat3'])
    return list(set(massiv))


def alls(filename):
    a = {}
    c = {}
    d = {}
    lengtha = 0
    lengthc = 0
    lengthd = 0
    lengthall = 0
    for line in filename:
        a.clear()
        c.clear()
        d.clear()
        pik = json.loads(line)
        for i in range(0, len(pik['text_tags']) - 1):
            if pik['text_tags'][i][2] == "A" and pik['text_tags'][i+1][2] == "S":
                lengtha += 1
                if str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) not in a:
                    a[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
                elif str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) in a:
                    a[str(pik['text_tags'][i]) + str(pik['text_tags'][i + 1])] += 1
            if pik['text_tags'][i][2] == "S" and pik['text_tags'][i+1][2] == "S" \
                    and pik['text_tags'][i+1][3] == "Genitive":
                lengthc += 1
                if str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) not in c:
                    c[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
                elif str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) in c:
                    c[str(pik['text_tags'][i]) + str(pik['text_tags'][i + 1])] += 1
            if pik['text_tags'][i][2] == "S" and pik['text_tags'][i+1][2] == "S" \
                    and pik['text_tags'][i+1][3] == "Instrumental":
                lengthd += 1
                if str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) not in d:
                    d[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
                elif str(pik['text_tags'][i])+str(pik['text_tags'][i+1]) in d:
                    d[str(pik['text_tags'][i]) + str(pik['text_tags'][i + 1])] += 1
        cat = pik['cat3']
        lengthall += len(pik['text_tags'])
        with open("%s.txt" % cat, 'a', encoding='utf-8') as g:
            g.write(str(a))
            g.write('\n')
            g.write(str(c))
            g.write('\n')
            g.write(str(d))
            g.write('\n')
    lengthallmin = lengthall - lengtha - lengthc - lengthd
    return lengthall, lengthallmin, lengtha, lengthc, lengthd


def sorting(dictionary):
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    for r in sorted_keys:
        out.write(str(r))
        out.write('\t')
        out.write(str(dictionary[r]))
        out.write('\n')
    return


with open("C:/Users/User/Desktop/al/учёба/курсовая/all_reviews_texts_with_tags.txt", encoding='UTF8') as file:
    filenames = categories(file)
for fname in filenames:
    with open('%s.txt' % fname, 'w', encoding='UTF8') as infile:
        infile.truncate(0)
filea = open("C:/Users/User/Desktop/al/учёба/курсовая/all_reviews_texts_with_tags.txt", encoding='UTF8')
tupla = alls(filea)
ab = {}
cd = {}
de = {}
with open('result.txt', 'w', encoding='utf-8') as out:
    out.write("Всего словосочетаний %d\r\n" % tupla[0])
    out.write("Осталось после обработки %d\r\n" % tupla[1])
    out.write("Словосочетаний типа А %d\r\n" % tupla[2])
    out.write("Словосочетаний типа С %d\r\n" % tupla[3])
    out.write("Словосочетаний типа D %d\r\n" % tupla[4])
    for fname in filenames:
        with open('%s.txt' % fname, encoding='UTF8') as infile:
            ab.clear()
            cd.clear()
            de.clear()
            out.write('\n')
            for x, line1 in enumerate(infile):
                pay = json.loads(line1)
                if x % 3 == 0:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in ab:
                            ab[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in ab:
                            ab[list(pay.keys())[j]] += 1
                elif x % 3 == 1:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in cd:
                            cd[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in cd:
                            cd[list(pay.keys())[j]] += 1
                elif x % 3 == 2:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in de:
                            de[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in de:
                            de[list(pay.keys())[j]] += 1
            out.write("Категория:  %s\r\n" % fname)
            out.write('Словосочетания типа A\n')
            sorting(ab)
            out.write('\nСловосочетания типа C\n')
            sorting(cd)
            out.write('\nСловосочетания типа D\n')
            sorting(de)

ab.clear()
cd.clear()
de.clear()
with open('resultall.txt', 'w', encoding='utf-8') as out:
    for fname in filenames:
        with open('%s.txt' % fname, encoding='UTF8') as infile:
            for x, line1 in enumerate(infile):
                pay = json.loads(line1)
                if x % 3 == 0:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in ab:
                            ab[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in ab:
                            ab[list(pay.keys())[j]] += 1
                elif x % 3 == 1:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in cd:
                            cd[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in cd:
                            cd[list(pay.keys())[j]] += 1
                elif x % 3 == 2:
                    for j in range(0, len(pay)):
                        if list(pay.keys())[j] not in de:
                            de[list(pay.keys())[j]] = 1
                        elif list(pay.keys())[j] in de:
                            de[list(pay.keys())[j]] += 1
    out.write('Словосочетания типа A\n')
    sorting(ab)
    out.write('\nСловосочетания типа C\n')
    sorting(cd)
    out.write('\nСловосочетания типа D\n')
    sorting(de)
filea.close()

