import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			scale L about the origin by factor
			print L
preconditions
	stdin contains a legal lines file
'''

# process the command line arguments
if len(sys.argv) != 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' factor count'
	sys.exit(1)
try:
	factor = float(sys.argv[1])
	count = int(sys.argv[2])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' factor count'
	sys.exit(2)

for line in sys.stdin:
	# convert L to a Line object
	L = line.split()
	point0 = Line_Point.Point(float(L[1]), float(L[2]))
	point1 = Line_Point.Point(float(L[3]), float(L[4]))
	line = Line_Point.Line(point0, point1)

	# scale and write line count times
	for i in range(count):
		line.scale(factor)
		print 'line', line
