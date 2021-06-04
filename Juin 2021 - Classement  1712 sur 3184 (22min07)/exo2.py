#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import collections

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
arr = collections.Counter(lines)
for k, v in arr.items():
    if v == 2:
        print(k)
