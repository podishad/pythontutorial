
# Errors and exception

x = -5
#if x < 0:
#    raise Exception("X should be greater than 0 always")

#y = -5
#assert (y > 0), "y is not positive"

#ZeroDivisionError: division by zero
#a = 5 / 0


try:
    a = 5 / 0
#except:
#    print ("It cannot be devided by 0")
#except Exception as e:
#    print(e)
except ZeroDivisionError as e:
    print (e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("This is for clean up operations - close all streams etc")

class value_too_high_error(Exception):
    pass

class value_too_small(Exception):

    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
   if x > 10:
       raise value_too_high_error("Value is too high check ")
   if x < 5:
       raise value_too_small("VALUE IS TOO SMALL CHECK IT", x)

#test_value(30)

try:
    test_value(3)
except value_too_high_error as e:
    print(e)
except value_too_small as e:
    print(e.message, e.value)



