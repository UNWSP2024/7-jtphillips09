# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    # --- Added code starts here ---
    print("Enter state population data. Type 'done' when finished.\n")

    while True:
        year_input = input("Enter year (or 'done' to stop): ")
        if year_input.lower() == 'done':
            break
        try:
            year = int(year_input)
        except ValueError:
            print("Please enter a valid year.")
            continue

        state = input("Enter state name: ")

        try:
            population = int(input("Enter population: "))
        except ValueError:
            print("Please enter a valid number for population.")
            continue

        all_entered_values.append([year, state, population])

    if not all_entered_values:
        print("\nNo data entered. Exiting program.")
        return

    print("\nData entered:")
    for entry in all_entered_values:
        print(entry)

    # Now have the user enter a year. 
    try:
        year_to_sum = int(input("\nEnter a year to total the population for: "))
    except ValueError:
        print("Invalid year. Exiting program.")
        return

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, year_to_sum)
    # --- Added code ends here ---


def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population

    # --- Added code starts here ---
    total_population = 0
    for entry in all_entered_values:
        if entry[0] == year_to_sum:
            total_population += entry[2]

    print(f"\nTotal population for {year_to_sum}: {total_population:,}")
    # --- Added code ends here ---


# Call the main function.
if __name__ == '__main__':
    main()
