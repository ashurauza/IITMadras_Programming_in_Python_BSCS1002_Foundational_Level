import random

# Heterogeneous values in multiple lines
def display_student_details(name: str, age: int, rollno: int):
    '''
    Given name, age, and rollno of a student, print them over multiple lines.
    '''
    print(name)
    print(age)
    print(rollno)

# Heterogeneous values - single line
def display_student_details_same_line(name: str, age: int, rollno: int):
    '''
    Given name, age, and rollno of a student, print them in the same line separated by a comma.
    '''
    print(f"{name},{age},{rollno}")

# Homogeneous values - single line
def display_comma_separated_integers(nums: list):
    '''
    Given a list of integers, print them in the same line separated by commas.
    '''
    print(",".join(map(str, nums)))

# Homogeneous values - multi-line with floating-point precision
def display_float_nums_over_multiple_lines(nums: list):
    '''
    Given a list of floating point numbers, print them over multiple lines with 3 digits after the decimal.
    '''
    for num in nums:
        print(f"{num:.3f}")

# Homogeneous values - indefinite sequence with random integers
def display_random_ints(seed: int):
    '''
    Given a random seed, set the random seed and generate multiple random integers in the range [0,100]
    until a 0 is encountered, printing a maximum of 10 comma-separated integers per line.
    '''
    random.seed(seed)
    count = 0
    line = []
    while True:
        num = random.randint(0, 100)
        line.append(str(num))
        count += 1
        if count == 10 or num == 0:
            print(",".join(line))
            line = []
            count = 0
        if num == 0:
            break

# Hybrid data - single line
def display_batsman_runs(name: str, number: int, runs: list):
    '''
    Given name, number, and runs scored by a batsman, display the name, number, and runs in the same line separated by commas.
    '''
    runs_str = ",".join(map(str, runs))
    print(f"{name},{number},{runs_str}")

# Key-Value pairs - multi-line, sorted by keys
def display_course_scores(course_scores: dict):
    '''
    Given a dictionary of course scores, display each course and its score separated by a colon on each line,
    sorted by course name.
    '''
    for course in sorted(course_scores):
        print(f"{course}:{course_scores[course]}")

# Nested list of tuples - multi-line with hyphen and comma-separated values
def display_all_batsman_runs(batsman_runs: list):
    '''
    Given a list of tuples containing batsman names and runs, print the batsman name followed by runs separated by hyphens and commas.
    '''
    for batsman, runs in batsman_runs:
        runs_str = ",".join(map(str, runs))
        print(f"{batsman}-{runs_str}")

# List of dictionaries - single line per dictionary entry
def display_student_marks(student_marks: list):
    '''
    Given student details in a list of dictionaries, print each student's attributes in a single line, comma-separated.
    '''
    for student in student_marks:
        print(f"{student['rollno']},{student['city']},{student['age']},{student['course1']},{student['course2']},{student['course3']}")

# List of dictionaries - multiple lines per dictionary entry
def display_student_marks_over_multiple_lines(student_marks: list):
    '''
    Given student details in a list of dictionaries, print each student's attributes over multiple lines.
    '''
    for student in student_marks:
        print(student['rollno'])
        print(student['city'])
        print(student['age'])
        print(student['course1'])
        print(student['course2'])
        print(student['course3'])

# this basically reads the input and executes it as code
import sys
exec(sys.stdin.read())