# let say this is a function defined in the core library and we dont have access to edit it

def div(a,b):
    print(a/b)

div(4,2)

# but this function have 1 loose end according to our requirement which is
# if a is smaller than b , than we need to swap a, b value

# to handle this we will use decorator at our code
# which will take div function as an input

def smart_div(div):              # include core library function
    def inner(a, b):              # input same as core function param
        if a<b :
            a,b = b,a
        return div(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)