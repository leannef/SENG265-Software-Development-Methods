import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			translate L horizontally by delta_x
			translate L vertically by delta_y
			print L
preconditions
	stdin contains a legal lines file
'''
try:
	delta_x = sys.argv[1]
	delta_y = sys.argv[2]
	count = sys.argv[3]
	if type(delta_x) != float or type(delta_y) != float or type(count)!=int:
		raise ValueError
except ValueError:
	print >> sys.stderr,'Syntax: translate.py delta_x delta_y count'
'''
delta_x = sys.argv[1]
delta_y = sys.argv[2]
count = sys.argv[3]
for line in sys.stdin:
	L = line.split()
'''


