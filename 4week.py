import ast


def tonalnost(filename):
    minu = []
    plu = []
    for lines in filename:
            if lines[0] != '!':
                if 'negative' in lines:
                    parts = lines.split(',')
                    minu.append(parts[0])
                if 'positive' in lines:
                    parts = lines.split(',')
                    plu.append(parts[0])
    return minu, plu


file = open('rusentilex_2017.txt', encoding='utf8')
minus, plus = tonalnost(file)
ishfile = open('resultall.txt', encoding='utf8')
print(ishfile.readline(), 'done')
a = {}
b = {}
posi = open('positive.txt', 'w', encoding='utf8')
nega = open('negative.txt', 'w', encoding='utf8')
for line in ishfile:
    a.clear()
    b.clear()
    if line == '\n':
        break
    temp = ast.literal_eval(line.split('\t')[0])
    if temp[0][1] in plus:
        posi.write(line)
    if ast.literal_eval(line.split('\t')[0])[0][1] in minus:
        nega.write(line)
file.close()
ishfile.close()
posi.close()
nega.close()
