import math

'''
Purpose
	Provide an exception class for Point and Line.
Exceptions
	None
Preconditions
	Message is a string.
'''
class Error(Exception):
	def __init__(self, message):
		self.message = message

'''
Purpose
	Store a point as an x, y pair.
	Provide functions to rotate, scale and translate the point.
Preconditions
	After instantiation, a Point object is modified only by
	rotate, scale and translate.
'''
class Point:
	'''
	Purpose
		Create a Point instance from x and y.
	Exceptions
		Raise Error if x or y are not of type float.
	Preconditions
		None
	'''
	def __init__(self, x, y):	
		self.x = x 
		self.y = y
		isfloat1 = float(x)
		isfloat2 = float(y)
		if isfloat1 != x:
			raise Error('caught: Parameter "x" illegal.')
		elif isfloat2 != y:
			raise Error('caught: Parameter "y" illegal.')
		
	
	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.
	Preconditions
		None
	'''
	def rotate(self, a): 
		x0 = cos(a) * x - sin(a) * y
		y0 = sin(a) * x + cos(a) * y
		isfloat = float(a)
		if isfloat != a:
			raise Error('caught: Parameter "a" illegal.')
		
		

	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, f):
		x0 = f * x
		y0 = f * y
		isfloat = float(f)
		if isfloat != f:
			raise Error('caught: Parameter "f" illegal.')
	'''
	Purpose
		Translate point by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		x0 = x + delta_x
		y0 = y + delta_y
		isfloat1 = float(delta_x)
		isfloat2 = float(delta_y)
		if isfloat != delta_x:
			raise Error('caught: Parameter "delta_x" illegal.')
		elif isfloat2 != delta_y:
			raise Error('caught: Parameter "delta_y" illegal.')
	
	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):	
		isfloat = float(self)		
		if isfloat == self:
			return int(float(self) + 0.5)

'''
Purpose
	Store a Line as a pair of Point instances.
	Provide functions to rotate, scale and translate the line.
Preconditions
	After instantiation, a Line object is modified only by
	rotate, scale and translate.
'''
class Line:
	'''
	Purpose
		Create a Line instance from point0 and point1.
	Exceptions
		None
	Preconditions
		None
	'''
	def __init__(self, point0, point1):
		point0  = Point._init_(point0,x,y)
		point1  = Point._init_(point1,x,y)
		self.point0 = point0	
		self.point1 = point1
		line = Line(point0, point1)
	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.
		Raise Error if self.point0 or self.points1 is not legal.
	Preconditions
		None
	'''
	def rotate(self, a):
		line = Line(point0,point1)
		line.rotate(a)
		'''		
		Point.rotate(point0,a)
		Point.rotate(point1,a)
		'''

	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, factor):
		line = Line(point0,point1)
		line.scale(factor)

	'''
	Purpose
		Translate Line by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		line = Line( point0, point1 )
		line.translate(delta_x, delta_y)

	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):
		isfloat = float(self)		
		if isfloat == self
			return int(float(self) + 0.5)


