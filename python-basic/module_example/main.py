# import test_package.test as circle
# import test_package.test_module

from test_package import *

# print(circle.get_circumference(10))
# print(circle.get_circle_area(10))
print(test.get_circumference(10))
print(test.get_circle_area(10))

# test_package.test_module.say_hello("kimrasng")
# test_package.test_module.whoareyou()
test_module.say_hello("kimrasng")
test_module.whoareyou()