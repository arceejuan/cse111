# I added a feature where a user can input a country of interest. After which, it will give you the minimum, maximum, and average life
# expectancy for the specific country of choice.

# Define the file path of the CSV dataset
file_path = 'life-expectancy.csv'

# Initialize variables to store the lowest and highest life expectancy values
lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')
year_data = {}  # Dictionary to store life expectancy data for each year
country_data = {}  # Dictionary to store life expectancy data for each country

# Read the CSV file and iterate through its rows
with open(file_path, newline='', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    header = lines[0].strip().split(',')  # Get the header row
    data = [line.strip().split(',') for line in lines[1:]]  # Extract data rows

    # Iterate through each row in the data
    for row in data:
        year = int(row[2])
        country = row[0]  
        life_expectancy = float(row[3])  
        
        # Update lowest and highest values if necessary
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_country = country
            lowest_year = year
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_country = country
            highest_year = year
        
        # Store life expectancy data for each year
        if year in year_data:
            year_data[year].append((country, life_expectancy))
        else:
            year_data[year] = [(country, life_expectancy)]
        
        # Store life expectancy data for each country
        if country in country_data:
            country_data[country].append(life_expectancy)
        else:
            country_data[country] = [life_expectancy]

# Display the lowest and highest life expectancy values with corresponding year and country
print(f"The overall max life expectancy is: {highest_life_expectancy} from {highest_country} in {highest_year}")
print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_country} in {lowest_year}")

# Allow the user to input a year of interest
year_of_interest = int(input("Enter the year of interest: "))

# Calculate the average life expectancy for the year of interest
if year_of_interest in year_data:
    life_expectancies = [data[1] for data in year_data[year_of_interest]]
    average_life_expectancy = sum(life_expectancies) / len(life_expectancies)
    
    # Find the country with the minimum and maximum life expectancies for the year of interest
    min_country, min_life_expectancy = min(year_data[year_of_interest], key=lambda x: x[1])
    max_country, max_life_expectancy = max(year_data[year_of_interest], key=lambda x: x[1])
    
    # Display the results
    print(f"\nThe average life expectancy across all countries in {year_of_interest} was: {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life_expectancy:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life_expectancy:.3f}")
else:
    print(f"No data available for the year {year_of_interest}")

# Allow the user to input a country of interest
country_of_interest = input("Enter the country of interest: ")

# Calculate the minimum, maximum, and average life expectancy for the country of interest
if country_of_interest in country_data:
    country_life_expectancies = country_data[country_of_interest]
    min_country_life_expectancy = min(country_life_expectancies)
    max_country_life_expectancy = max(country_life_expectancies)
    average_country_life_expectancy = sum(country_life_expectancies) / len(country_life_expectancies)
    
    # Display the results
    print(f"\nThe minimum life expectancy for {country_of_interest} is: {min_country_life_expectancy:.2f}")
    print(f"The maximum life expectancy for {country_of_interest} is: {max_country_life_expectancy:.2f}")
    print(f"The average life expectancy for {country_of_interest} is: {average_country_life_expectancy:.2f}")
else:
    print(f"No data available for the country {country_of_interest}")
