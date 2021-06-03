#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
arr = []
arrDay = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
arrDay = list(map(int, lines[0].split()))
arr = list(map(int, lines[1].split()))
if arrDay[0] == max(arr):
    print('OK')
else:
    print('ERREUR')
