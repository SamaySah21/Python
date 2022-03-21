# practicing activation function

# relu activation function

from matplotlib import pyplot

def rectifiedLinearUnit(x):
    return max(0.0, x)

# print(rectifiedLinearUnit(-4))

# define input data
inputs = [x for x in range(-10, 10)]
print(inputs)

#getoutput
output = [rectifiedLinearUnit(x) for x in inputs]

print(output)
# plot input vs output
pyplot.plot(inputs, output)
pyplot.show()