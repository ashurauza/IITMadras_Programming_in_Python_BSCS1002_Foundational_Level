age = int(input())  # Read age as integer from standard input
dob = input()       # Read DOB in format dd/mm/yy from standard input

# Extract day, month, year as integers
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:])

# Calculate fifth birthday
fifth_birthday = f"{day}/{month}/{year + 5}"

# Calculate last birthday (based on age)
last_birthday = f"{day}/{month}/{year + age}"

# Calculate 10 months after birth date
if month + 10 > 12:
    month = (month + 10) - 12
    year += 1
else:
    month = month + 10

tenth_month = f"{day}/{month}/{year}"

# Print all dates in one line, separated by comma and space
print(f"{tenth_month}, {fifth_birthday}, {last_birthday}")

# Read weight in kg as float and convert to grams
weight = float(input()) * 1000  # Convert kg to grams

# Convert weight to string and format nicely
weight_str = str(int(weight))
weight_readable = f"{weight_str[:2]} kg {weight_str[2:5]} grams"

# Print formatted weight
print(weight_readable)
