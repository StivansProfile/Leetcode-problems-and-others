def reverse_integer(integer):
	int_arr = list(str(integer))
	lenght_of_num = len(int_arr)
	reversed_integer = ""

	if "-" in int_arr:
		int_arr.remove("-")
		int_arr.insert(len(int_arr),"-")

	while lenght_of_num > 0:
		reversed_integer += int_arr[-1]
		int_arr.remove(int_arr[-1])
		lenght_of_num -= 1

	print(f"Given int: {integer}")
	print(f"Reversed: {int(reversed_integer)}")

reverse_integer(115)