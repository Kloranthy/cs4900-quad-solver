


acceptable_digits_of_precision = 4

epsilon = 1e-16


def has_acceptable_digits_of_precision( value ) :

  rounded_value = round( value, acceptable_digits_of_precision )

  abs_diff = abs( value - rounded_value )

  return ( abs_diff <= epsilon )
# has_acceptable_digits_of_precision




def check_abc_values( a, b, c ) :

  result = {
    'valid' : True,
    'a_is_not_zero' : True,
    'acceptable_digits_of_precision' : True
  }


  if ( a == 0.0 ) :

    result[ 'valid' ] = False
    result[ 'a_is_not_zero' ] = False
  # a is zero


  if (
    ( not has_acceptable_digits_of_precision( a ) )
    or ( not has_acceptable_digits_of_precision( b ) )
    or ( not has_acceptable_digits_of_precision( c ) )
  ) :

    result[ 'acceptable_digits_of_precision' ] = False
  # too many digits of precision
  

  return result
# check_abc_values


