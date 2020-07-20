import sys

from Line_Point import *

print '********** Point'

print '*** constructor'
try:
	p0 = Point(1,1.0) # x illegal
except Error as e:
	print 'caught:', e.message
try:
	p0 = Point(1.0,'y') # y illegal
except Error as e:
	print 'caught:', e.message

print Point(0.0,1.0)

print '*** rotate'
# a illegal
try:
	p0 = Point(0.0, 0.0)
	p0.rotate(1)
except Error as e:
	print 'caught:', e.message

# normal case
p0 = Point(0.0, 1.0)
p0.rotate(math.pi)
print p0

print '*** scale'
# a illegal
try:
	p0 = Point(0.0, 0.0)
	p0.scale(1)
except Error as e:
	print 'caught:', e.message

# normal case
p0 = Point(2.0, 3.0)
p0.scale(2.3)
print p0

print '*** translate'
# delta_x illegal
try:
	p0 = Point(0.0, 0.0)
	p0.translate(1, 2.0)
except Error as e:
	print e.message

# delta_y illegal
try:
	p0 = Point(0.0, 0.0)
	p0.translate(1.0, 2)
except Error as e:
	print e.message

# normal case
p0 = Point(3.0, 5.0)
p0.translate(1.1, -2.2)
print p0

print '********** Line'
print '*** constructor'
p0 = Point(0.0, 1.0)
p1 = Point(2.0, 3.0)
line = Line(p0,p1)
print line

# check for shallow copy
p0.scale(2.0)
p1.scale(2.0)
print line

print '*** rotate'
# a illegal
try:
	line = Line( Point(1.0,1.0), Point(1.0,1.0) )
	line.rotate(1)
except Error as e:
	print e.message

# normal case
line = Line( Point(0.0,0.0), Point(0.0,1.0) )
line.rotate(math.pi)
print line

print '*** scale'
# f illegal
try:
	line = Line( Point(1.0,1.0), Point(1.0,1.0) )
	line.scale(1)
except Error as e:
	print e.message

# normal case
line = Line( Point(1.0,2.0), Point(3.0,4.0) )
line.scale(2.3)
print line

print '*** translate'
# delta_x illegal
try:
	line = Line( Point(1.0,1.0), Point(1.0,1.0) )
	line.translate(1, 2.0)
except Error as e:
	print e.message

# delta_y illegal
try:
	line = Line( Point(1.0,1.0), Point(1.0,1.0) )
	line.translate(1.0, 2)
except Error as e:
	print e.message

# normal case
line = Line(Point(0.0,0.0), Point(1.0,2.0))
line.translate(1.0, 2.0)
print line
