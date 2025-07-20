# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

new_word = word  # do not remove this line

# remove the "ing" suffix from new_word if it is there
if new_word.endswith("ing"):
    new_word =new_word.rstrip("ing")  # remove the last 3 characters

# add the suffix "ing" to new_word if continuous_tense is True
if continuous_tense:
    new_word += "ing"

# Part 2 - If Else Pattern
# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age >= 18:
    age_group = "Adult"
else:
    age_group = "Child"

# applicant_type:str should be age group with the member status like "Adult Member" or "Child Non-member"
if age_group == "Adult":
    applicant_type = "Adult Member" if is_member else "Adult Non-member"
else:
    applicant_type = "Child Member" if is_member else "Child Non-member"

# Part 3 - If Elif Else
# based on the value of color_code assign the color value in lower case and "black" if color_code is none of R, B and G
if color_code == "R":
    color = "red"
elif color_code == "G":
    color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

# Time validation and conversion
# is_time_valid = bool: True if time is valid (should be ranging from 1 - 12 both including) else False 
is_time_valid = time[:-3].isdigit() and 1 <= int(time[:-3]) <= 12 and time[-2:] in ["AM", "PM"]

# time_in_hrs:int should have the time in 24 hrs format. Try to do this in a single expression
time_in_hrs = (int(time[:-3]) % 12) + (12 if time[-2:] == "PM" else 0)

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range
if is_time_valid:
    if time_in_hrs < 12:
        time_of_day = "Morning" if time_in_hrs >= 6 else "Night"
    elif time_in_hrs < 17:
        time_of_day = "Afternoon"
    else:
        time_of_day = "Evening"
else:
    time_of_day = "Invalid"