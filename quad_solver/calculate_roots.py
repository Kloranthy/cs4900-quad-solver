
from math import sqrt



def calculate_roots(
	a, b, c
):

	roots = []


	discriminant = b * b - 4 * a * c


	if (
		( discriminant < 0 )
		or (
			( a == 0 )
			and ( c == 0 )
		)
	):

		print( 'discim < 0' )
		return roots
	# no real roots



	if ( discriminant > 0 ):

		x1 = (
			( -b + sqrt( discriminant ) )
			/ ( 2 * a ) 
		)

		x2 = (
			( -b - sqrt( discriminant ) )
			/ ( 2 * a ) 
		)

		roots = [ x1, x2 ]

		roots.sort()

	# discriminant > 0
	elif ( ( discriminant == 0 ) and ( a != 0 ) ):

		x1 = (
			-b
			/ ( 2 * a ) 
		)

		roots = [ x1, x1 ]

	# discriminant == 0 and a != 0


	return roots
# calculate_roots

