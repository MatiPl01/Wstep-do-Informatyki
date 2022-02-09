# More flexible solution that can be used in variety of examples
# Returns only one solution (not all possible if more are present)
from decimal import Decimal


def parse_domain_str(domain: str) -> tuple:
	"""Parses the domain given as an argument of the function
	domain  - the domain of the function in which results will be searched (can't be infinite)
		'(a, b)'  -  a < x < b
		'[a, b]'  -  a <= x <= b
		'[a, b)'  -  a <= x < b
		'(a, b]'  -  a < x <= b
	"""
	if domain[0] not in '([' or domain[-1] not in ')]':
		raise ValueError(f'The domain {domain} is invalid. Please use the valid syntax.')
	a, b = (Decimal(n) for n in domain[1:-1].split(','))
	a_included = domain[0] == '['
	b_included = domain[-1] == ']'
	return a, b, a_included, b_included


def find_solution(f_x: 'the function itself', y: 'the value of the function', domain: str, *, eps=Decimal('.0000001')):
	"""Finds solution of the function given (with the result specified) using bisection
	f_x     - function which we look for solutions of
	y       - the result of the function
	domain  - the domain of the function in which results will be searched (can't be infinite)
		'(a, b)'  -  a < x < b
		'[a, b]'  -  a <= x <= b
		'[a, b)'  -  a <= x < b
		'(a, b]'  -  a < x <= b
	"""
	# Parse the domain
	a, b, a_included, b_included = parse_domain_str(domain)
	y = Decimal(y)

	while True:
		x = (a + b) / 2
		result = f_x(x)
		if abs(result - y) <= eps:
			return x
		if result < y:
			a = x
		else:
			b = x


if __name__ == '__main__':
	function = lambda x: x**x
	value = 2020
	domain = '[0, 100]'
	result = find_solution(function, value, domain)
	print(result)
