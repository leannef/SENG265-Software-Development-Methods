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

# process the command line arguments
if len(sys.argv) != 4:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' delta_x delta_y count'
	sys.exit(1)
try:
	delta_x = float(sys.argv[1])
	delta_y = float(sys.argv[2])
	count = int(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' delta_x delta_y count'
	sys.exit(2)

for line in sys.stdin:
	# convert L to a Line object
	L = line.split()
	point0 = Line_Point.Point(float(L[1]), float(L[2]))
	point1 = Line_Point.Point(float(L[3]), float(L[4]))
	line = Line_Point.Line(point0, point1)

	# translate and write line count times
	for i in range(count):
		line.translate(delta_x, delta_y)
		print 'line', line
