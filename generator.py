import random

    

ph_gr = [x.rstrip().split('\t') for x in open('phonème_graphème.txt', 'r', encoding='UTF-8')]

voyelles = {}
consonnes = {}
semi = {}

rules = ['cv', 'csv', 'ccv']


for element in ph_gr:
    if element[1] == 'Voyelle':
        voyelles[element[0]] = element[2].split('|')
    
    if element[1] == 'Consonne':
        consonnes[element[0]] = element[2].split('|')
    
    if element[1] == 'Semi-voyelle':
        semi[element[0]] = element[2].split('|')


#print(random.choice(list(voyelles.items())))

logatomes = []

ccv = 0
cv = 0
csv = 0

for i in range(0,100):
    
    logatome = ''
    lenght = random.randint(2,6)

    for j in range(lenght):
        forme = random.choice(rules)
        if forme == 'cv':
            cv += 1
            syllabe = random.choice(list(consonnes.items()))[1][0]
            syllabe += random.choice(list(voyelles.items()))[1][0]
        if forme == 'csv':
            csv += 1
            syllabe = random.choice(list(consonnes.items()))[1][0]
            syllabe += random.choice(list(semi.items()))[1][0]
        if forme == 'ccv':
            ccv += 1
            syllabe = random.choice(list(consonnes.items()))[1][0]
            syllabe = random.choice(list(consonnes.items()))[1][0]
            syllabe += random.choice(list(voyelles.items()))[1][0]
        logatome += syllabe
    
    logatomes.append(logatome)

print('cv =', cv, '\ncsv =', csv, '\ncsv =', ccv)

with open('logatomes.txt', 'w', encoding='UTF-8') as out:
    out.write('\n'.join(logatomes))
