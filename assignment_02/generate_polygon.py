import sys
import math
import Line_Point

'''
purpose
	write to stdout a regular polygon with s sides and first vertex at (x0,y0)
preconditions
	None
'''
try:
	x0 = sys.argv[1]
	y0 = sys.argv[2]
	count = sys.argv[3]
	if type(x0) != float or type(y0)!=float or type(count)!=int:
		raise ValueError
	elif type(x0) == float and type(y0)==float and type(count)==int:
		print >> sys.stderr,'hi'
		F = []
		point0 = Line_Point.Point(x0,y0)
		F.append(point0)
		print >> sys.stderr,F
		for i in range(1,count):	
			point0.rotate(2*math.pi/count)
			F.append(point0)
		B = []
		for j in range(0,count-1):
			L1 = Line_Point.Line(F[j], F[j+1])
			B.append(L1)
			print >> sys.stderr,'line'+ ' '+ B[j]
	
except ValueError:
	print >> sys.stderr,'Syntax: generate_polygon.py x0 y0 s'










