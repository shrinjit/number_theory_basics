def find_the_cycles_of_polygon(value_of_the_side_of_the_polygon):
	if value_of_the_side_of_the_polygon <2:
		return 0
	else :
		return value_of_the_side_of_the_polygon*(value_of_the_side_of_the_polygon-1)+1














test_cases=int(input('enter the test cases over here ---->>>>>>'))
while test_cases>0:
	number_of_sides_of_polygon=int(input('Enter the side of the POLYGON   !!!!!'))
	print(find_the_cycles_of_polygon(number_of_sides_of_polygon))
	test_cases=test_cases - 1