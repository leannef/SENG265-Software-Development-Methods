import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			print L
			rotate L counter clockwise about the origin by angle a
preconditions
	stdin contains a legal lines file
'''

try:
	angle = sys.argv[1]
	count = sys.argv[2]
	if type(angle) != float or type(count)!=int :		
		raise ValueError
except ValueError:
	print >> sys.stderr,'Syntax: rotate.py angle count'

'''
for line in sys.stdin:
	L = line.split()
	point0 = Line_Point.Point(L[1],L[2])
	point1 = Line_Point.Point(L[3],L[4])
	Line=Line_Point.Line(point0,point1)
	print 'line'+ ' '+ Line
	Line.rotate(a)
'''
	
