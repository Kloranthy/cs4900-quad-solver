#!/bin/bash



for test_dir in */
do
  echo $test_dir

  test_input_file="${test_dir}test_input.txt"
  #echo $test_input_file
  #cat $test_input_file
  #echo ""

  expect_output_file="${test_dir}expect_output.txt"
  #echo $expect_output_file
  #cat $expect_output_file
  #echo ""

  actual_output_file="${test_dir}actual_output.txt"

  cd ..
  #pwd

  #cat "./system_testing/$test_input_file"

  python3 -m quad_solver < "./system_testing/$test_input_file" > "./system_testing/$actual_output_file"

  #cat "./system_testing/$actual_output_file"

  cd ./system_testing
  pwd

  #echo $actual_output_file
  #cat $actual_output_file
  #echo ""

  # todo check if diff is empty string
  #diff $expect_output_file $actual_output_file
done
