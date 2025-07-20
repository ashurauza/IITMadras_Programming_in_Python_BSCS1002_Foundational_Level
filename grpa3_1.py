# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:  # the terminal condition
        total += n  # add n to the total
        n = int(input())  # take the next n from the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # repeat forever since we are breaking inside
        line = input()
        if line == "END":  # The terminal condition
            break
        quantity, price = line.split()  # split uses space by default
        quantity, price = int(quantity), int(price)  # convert to ints
        total_price += quantity * price  # accumulate the total price
    print(total_price)

elif task == "only_ed_or_ing":
    result = []
    while True:
        word = input().strip()
        if word.lower() == "stop":
            break
        if word.endswith("ed") or word.endswith("ing"):
            result.append(word)
    print("\n".join(result))  # Print each word on a new line

elif task == "reverse_sum_palindrome":
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    result = []
    while True:
        number = int(input())
        if number == -1:
            break
        reversed_number = int(str(number)[::-1])
        if is_palindrome(number + reversed_number):
            result.append(number)
    print("\n".join(map(str, result)))  # Print each number on a new line

elif task == "double_string":
    while True:
        text = input().strip()
        if text == "":
            break
        print(text * 2)

elif task == "odd_char":
    result = []
    while True:
        text = input().strip()
        if text.endswith("."):
            result.append(text[::2])  # Extract characters at even indices (0-based)
            break
        result.append(text[::2])  # Extract characters at even indices (0-based)
    print(" ".join(result))

elif task == "only_even_squares":
    result = []
    while True:
        number = input().strip()
        if number.lower() == "nan":
            break
        number = int(number)
        if number % 2 == 0:
            result.append(number ** 2)
    print("\n".join(map(str, result)))  # Print each square on a new line

elif task == "only_odd_lines":
    result = []
    line_count = 1
    while True:
        line = input().strip()
        if line == "END":
            break
        if line_count % 2 != 0:
            result.insert(0, line)  # prepend the line
        line_count += 1
    print("\n".join(result))