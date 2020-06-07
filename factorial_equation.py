n=2

array=list(map(int,input().split()))
new_array=array[0:n]
# print(new_array[0])
# print(new_array[1])


factorial=1
if new_array[1]<0:
	print(f'cannot be be valid number as the number entered is  a negative one !!!')

elif new_array[1]==0:
	print(f'the factorial is 1')

else :
	for value in range(1,new_array[1]+1):
		factorial=factorial*value
# print(factorial)


number_whose_last_digit_has_to_be_extracted=pow(new_array[0],factorial)

# print(number_whose_last_digit_has_to_be_extracted)


if number_whose_last_digit_has_to_be_extracted<10:
	print(number_whose_last_digit_has_to_be_extracted)
else :
	print(number_whose_last_digit_has_to_be_extracted%10)
