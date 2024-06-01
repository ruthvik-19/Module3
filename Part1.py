
# Customer inputs the total charge of their food
food_charge = float(input("What was the total charge on your meal today? "))

# Calculate 18% gratuity and 7% sales tax on the food charge 
gratuity = round(food_charge * .18, 2)
sales_tax = round(food_charge * .07, 2)

# Calculate the final amount 
final_amount = food_charge + gratuity + sales_tax

# Print the input and all calculated values
print("The charge for all the food is: {}".format(food_charge))
print("The gratuity for the food charge is: {}".format(gratuity))
print("The sales tax on the food is: {}".format(sales_tax))
print("The total amount you owe today is: {}".format(final_amount))


