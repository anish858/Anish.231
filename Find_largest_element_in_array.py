user_input = input("Enter numbers separated by space: ")
num_list = list(map(int, user_input.split()))
print(f"The lagest element in the list is {max(num_list)}")
