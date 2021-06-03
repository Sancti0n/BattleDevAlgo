lines = [
        '..........',
        '..........', 
        '..........', 
        '..........', 
        '..........', 
        '..#...####', 
        '##......#.', 
        '#.#....###', 
        '####..#.#.', 
        '.#...#.###', 
        '##.#....#.', 
        '####.#####', 
        '####.#####', 
        '####.#####', 
        '####.#####', 
        '#...##..#.', 
        '..###....#', 
        '#..#..####', 
        '...#....#.', 
        '..#..#..##']
#print(len(lines))
#print(lines)
longueur = len(lines[0])
arrtab = []
'''
arrRang = []
for i in lines:
    #print(i)
    #for a in range(len(i)):
    #print(i.count('#'))
    if i.count('#') == 9:
        rang = i
        arrRang.append(rang)
        print(i)
        index = i.index('.')
        print(index)
print(arrRang)
for i in lines:
    print()
    if i[arrRang[0][4]]== '.':
        print(i)
'''
value = ''
#print(range(len(lines)))
   
b = 0
i = 0
while b<longueur:
    while i<len(lines):
        value += lines[i][b]
        i+=1
    b+=1
    arrtab.append(value)
    i=0
    value = ''

#print(arrtab)

maxO = 0
tabmax = []
b=0
for i in range(len(arrtab)):
    while arrtab[i][b] == '.':
        #maxO += 1
        b+=1
    tabmax.append(b)
    #max0 = 0
    b=0
print(max(tabmax))