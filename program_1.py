# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

# List of month names for reference
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Empty list to store rainfall amounts
rainfall = []

# Get rainfall input from user
for month in months:
    while True:
        try:
            amount = float(input(f"Enter the total rainfall for {month}: "))
            if amount < 0:
                print("Rainfall cannot be negative. Please try again.")
            else:
                rainfall.append(amount)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculate total and average
total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12

# Find highest and lowest rainfall
max_rainfall = max(rainfall)
min_rainfall = min(rainfall)
max_month = months[rainfall.index(max_rainfall)]
min_month = months[rainfall.index(min_rainfall)]

# Display results
print("\n--- Rainfall Summary ---")
print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print(f"Highest rainfall: {max_rainfall:.2f} inches in {max_month}")
print(f"Lowest rainfall: {min_rainfall:.2f} inches in {min_month}")
