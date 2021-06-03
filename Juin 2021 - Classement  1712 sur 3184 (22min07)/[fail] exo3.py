#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
longueur = len(lines[0])
arrtab = []
value = ''
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
tabmax = []
b=0
for i in range(len(arrtab)):
    while arrtab[i][b] == '.':
        b+=1
    tabmax.append(b)
    b=0
print("BOOM "+str(max(tabmax)))
