class SomeClass():
	a = 1
	def __init__(self):
	    b = 2

some_var = SomeClass()
another_var = SomeClass()


for var, classs in vars(SomeClass).items():
    print(var, classs)