#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

#initial list of favourite foods
favourite_foods = [" pizza", "bargar", "chicken" ," rolex", "rice"]

favourite_foods.append("salad")
favourite_foods.append("irish")
print(favourite_foods)

favourite_foods.remove("irish")
print(favourite_foods)






#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers = [ 2 ,5 , 8 , 10 , 3 ,6 ]
first =(2)
last =(6)
print( first,last)
numbers.sort(reverse = True)
print(numbers)

sum = 0
sum_of_numbers =(2, 5, 8, 3 ,6)
print(sum_of_numbers)

