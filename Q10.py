import numpy
import matplotlib.pyplot

#x axes
x = numpy.array([0, 1, 2, 3, 4])

#y axes
y = numpy.array([0, 1, 2, 3, 4])

# RO is X
matplotlib.pyplot.plot(x,y, 'r-')

# BO is X^2
matplotlib.pyplot.plot(numpy.square(x), y, 'b-')

# YO is 2^X
matplotlib.pyplot.plot(2**x, y, 'y-')

matplotlib.pyplot.show();

