#Quadratic equation (ax**2 + bx + c = 0)
import cmath

def find_roots(a, b, c):

#calculate the discriminant
	d = (b**2) - (4*a*c)

#find two solutions
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)

print(find_roots(2, 10, 8));
