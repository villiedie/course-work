import json


def categories(filename):
    massiv = []
    for lines in filename:
        pik = json.loads(lines)
        if pik['cat2'] != '':
            massiv.append(pik['cat3'])
    return massiv


def alls(filename):
    a = {}
    c = {}
    d = {}
    for line in filename:
        a.clear()
        c.clear()
        d.clear()
        pik = json.loads(line)
        for i in range(0, len(pik['text_tags']) - 1):
            if pik['text_tags'][i][2] == "A" and pik['text_tags'][i+1][2] == "S":
                a[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
            if pik['text_tags'][i][2] == "S" and pik['text_tags'][i+1][2] == "S" \
                    and pik['text_tags'][i+1][3] == "Genitive":
                c[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
            if pik['text_tags'][i][2] == "S" and pik['text_tags'][i+1][2] == "S" \
                    and pik['text_tags'][i+1][3] == "Instrumental":
                d[str(pik['text_tags'][i])+str(pik['text_tags'][i+1])] = 1
        x = pik['cat3']
        with open("%s.txt" % x, 'a', encoding='utf-8') as g:
            g.write(str(a))
            g.write(str(c))
            g.write(str(d))
    return


file = open("C:/Users/User/Desktop/al/учёба/курсовая/all_reviews_texts_with_tags.txt", encoding='UTF8')
filenames = categories(file)
for fname in filenames:
    with open('%s.txt' % fname, 'w', encoding='UTF8') as infile:
        infile.truncate(0)
file.close()
filea = open("C:/Users/User/Desktop/al/учёба/курсовая/all_reviews_texts_with_tags.txt", encoding='UTF8')
alls(filea)
with open('result.txt', 'w', encoding='utf-8') as out:
    for fname in filenames:
        with open('%s.txt' % fname, encoding='UTF8') as infile:
            for line1 in infile:
                out.write(line1)
filea.close()
