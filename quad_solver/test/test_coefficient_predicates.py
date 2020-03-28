
import unittest


from quad_solver.predicates.abc import has_acceptable_digits_of_precision



good_values = [
  3.14
]

bad_values = [
  3.14159265359
]




class TestCalculateRoots( unittest.TestCase ):


  def test_good_values( self ):

    for value in good_values :

      expected_result = True

      actual_result = has_acceptable_digits_of_precision( value )

      print( f"value : {value}  expected_result : {expected_result}  actual_result : {actual_result}" )


      self.assertEqual( expected_result, actual_result )

    # loop through good values

    return
  # test_good_values



  def test_bad_values( self ):

    for value in bad_values :

      expected_result = False

      actual_result = has_acceptable_digits_of_precision( value )

      print( f"value : {value}  expected_result : {expected_result}  actual_result : {actual_result}" )


      self.assertEqual( expected_result, actual_result )

    # loop through bad values

    return
  # test_bad_values


# TestCalculateRoots






if ( __name__ == "__main__" ):

  unittest.main()


