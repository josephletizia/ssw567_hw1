#Joseph Letizia
#SSW 567
#HW 01: Testing Triangle Classification

def classify_triangle(a, b, c):
	if type(a) != (int or float) or type(b) != (int or float) or type(c) != (int or float):
		output = "An input(s) is not valid"
	elif (a or b or c) == 0:
		output = "Invalid Triangle"
	elif (a+b) < c or (a+c) < b or (b+c) < a:
		output = "Invalid Triangle"
	else:
		if  a == b and b == c:
			output = "Equlateral Triangle"
		elif a == b or b == c or a == c:
			output = "Isosceles Triangle"
		elif (a**2 + b**2 == c**2) and a != b and a != c and b != c:
			output = "Right and Scalene Triangle"
		else:
			output = "Scalene Triangle"

	return output