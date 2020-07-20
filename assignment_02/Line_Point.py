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
		if type(x) != float:
			raise Error('caught: Parameter "x" illegal.')
		elif type(y) != float:
			raise Error('caught: Parameter "y" illegal.')
		self.x = x 
		self.y = y
		
	
	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.
	Preconditions
		None
	'''
	def rotate(self, a): 
		if type(a) != float:
			raise Error('caught: Parameter "a" illegal.')
		self.x0 = math.cos(a) * self.x - math.sin(a) * self.y
		self.y0 = math.sin(a) * self.x + math.cos(a) * self.y
		
		

	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, f):
		if type(f) != float:
			raise Error('caught: Parameter "f" illegal.')
		self.x0 = f * self.x
		self.y0 = f * self.y
	'''
	Purpose
		Translate point by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		if type(delta_x) != float:
			raise Error('caught: Parameter "delta_x" illegal.')
		elif type(delta_y) != float:
			raise Error('caught: Parameter "delta_y" illegal.')
		self.x0 = self.x + delta_x
		self.y0 = self.y + delta_y
	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):
		x1 = int(round(self.x))
		y1 = int(round(self.y))
		back_string=str(x1)+' '+str(y1)
		return back_string

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
		Raise Error if self.point0 or self.points1 is not legal.
	'''
	def __init__(self, point0, point1):
		if type(self.point0.x) != float or type(self.point0.y) != float :
			raise Error('caught: Parameter "point0" illegal.')
		elif type(self.point1.x) != float or type(self.point1.y) != float :
			raise Error('caught: Parameter "point1" illegal.')
		self.point0 = Point(point0.x,point0.y)	
		self.point1 = Point(point1.x,point1.y)
		
	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.

	Preconditions
		None
	'''
	def rotate(self, a):
		if type(a) != float:
			raise Error('caught: Parameter "a" illegal.')
		self.point0.rotate(a)
		self.point1.rotate(a)	
	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, factor):
		if type(factor) != float:
			raise Error('caught: Parameter "factor" illegal.')
		self.point0.scale(factor)
		self.point1.scale(factor)


	'''
	Purpose
		Translate Line by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		if type(delta_x) != float:
			raise Error('caught: Parameter "delta_x" illegal.')
		elif type(delta_y) != float:
			raise Error('caught: Parameter "delta_y" illegal.')
		self.point0.translate(delta_x, delta_y)
		self.point1.translate(delta_x, delta_y)

	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):
		x1 = int(round(self.point0.x))
		x2 = int(round(self.point1.x))
		y1 = int(round(self.point0.y))
		y2 = int(round(self.point1.y))
		back_string=str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)
		return back_string


