# Check if the digits of a number are sorted in ascending order
def is_num_sorted(num: int) -> bool:
    digits = str(num)
    return digits == ''.join(sorted(digits))

# Count the numbers that are sorted in a given list
def sorted_num_count(nums: list) -> int:
    return sum(1 for num in nums if is_num_sorted(num))

# Check if there exists a common substring among words
def common_substring(words: list) -> str:
    smallest_word = min(words, key=len)
    if all(smallest_word in word for word in words):
        return smallest_word
    return None

# Check if a phone number is valid based on specified criteria
def is_valid_phone_number(phone_no: int) -> bool:
    phone_str = str(phone_no)
    if len(phone_str) != 10 or not phone_str.startswith("98123"):
        return False
    return all(phone_str.count(digit) <= 5 for digit in phone_str)

# Validate multiple phone numbers and return a dictionary of results
def validate_phone_numbers(phone_nos: list) -> dict:
    return {phone: "VALID" if is_valid_phone_number(phone) else "INVALID" for phone in phone_nos}

# Determine the winner of an election based on vote counts
def get_election_winner(votes: dict) -> str:
    return max(votes, key=votes.get)

# Identify misspelt words from a sentence not in a given vocabulary
def misspelt_words(vocab: str, sentence: str) -> list:
    vocab_set = set(vocab.split(","))
    sentence_words = sentence.split()
    return [word for word in sentence_words if word not in vocab_set]

# Count the number of sock pairs by color
def count_sock_pairs(sock_colors: list) -> int:
    from collections import Counter
    color_counts = Counter(sock_colors)
    return sum(count // 2 for count in color_counts.values())

# Determine if a word is "vowely" (contains all vowels in ascending order)
def is_vowely(word: str) -> bool:
    # Extract vowels in order of appearance
    vowels_in_word = ''.join([char for char in word if char in "aeiou"])
    return vowels_in_word == "aeiou"


# Count the number of "vowely" words in a list
def vowely_count(words: list) -> int:
    return sum(1 for word in words if is_vowely(word))

# Format a name with proper capitalization
def format_name(first: str, middle: str, last: str) -> str:
    parts = [first.capitalize(), last.capitalize()]
    if middle:
        parts.insert(1, middle.capitalize())
    return " ".join(parts)

# Find all "double palindromes" up to a given number n
def double_palindromes(n: int) -> list:
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    
    return [x for x in range(1, n+1) if is_palindrome(x) and is_palindrome(x**2)]

# Calculate scores in a Stone-Paper-Scissor game
def scores_spx(kakashi_moves: list, guy_moves: list):
    rules = {"S": "X", "X": "P", "P": "S"}
    k_score, g_score = 0, 0
    for k_move, g_move in zip(kakashi_moves, guy_moves):
        if k_move != g_move:
            if rules[k_move] == g_move:
                k_score += 1
            else:
                g_score += 1
    return k_score, g_score