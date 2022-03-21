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
# pyplot.plot(inputs, output)
# pyplot.show()

########## SIGMOID FUNCTION ###############3

# output varies in between 0 to 1
#The larger the input (more positive), the closer the output value will be to 1.0,
# the smaller the input (more negative), the closer the output will be to 0.0

from math import exp
def sigmoid(x):
    #exp(-x) is same as pow(2.71828, x) as exp is euler number whose value is equal to 2.718
    return 1.0 / (1 + exp(-x))

# there are 2 problem with sigmoid function
# 1. vanishing gradient (same in tanh also)
# 2. value which are smaller are getting value close to zero , there is loss of all negative values (fixed using tanh)

#################### Tanh function ########################

# output values between -1 to +!
# The larger the input (more positive), the closer the output value will be to 1.0,
# the smaller the input (more negative), the closer the output will be to -1.0.
def tanFunction(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))






