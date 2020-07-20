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

try:
	factor = sys.argv[1]
	count = sys.argv[2]
	if type(factor) != float or type(count)!=int :
		raise ValueError
except ValueError:
	print >> sys.stderr,'Syntax: scale.py factor count'
'''
factor = sys.argv[1]
count = sys.argv[2]
for line in sys.stdin:
	L = line.split()
	point0 = Line_Point.Point(L[1],L[2])
	point1 = Line_Point.Point(L[3],L[4])
	Line=Line_Point.Line(point0,point1)
	print 'line'+ ' '+ Line
	Line.rotate(a)
'''