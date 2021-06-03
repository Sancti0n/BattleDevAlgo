#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
sapin = 0
for i in lines:
    if(int(i) <= 250 and int(i) >= sapin):
        sapin = int(i)
print(sapin)
