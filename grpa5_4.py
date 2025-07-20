# mapping
def is_greater_than_5(numbers:list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    return list(map(lambda x: x > 5, numbers))
    
# filtering
def filter_less_than_5(numbers:list)->list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''
    return list(filter(lambda x: x < 5, numbers))
    
# aggregation with filtering
def sum_of_two_digit_numbers(numbers:list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''
    return sum(filter(lambda x: 10 <= x <= 99, numbers))

# aggregation with mapping
def is_all_has_a(words: list) -> bool:
    '''Given a list of words, check if all words have the letter 'a' (case insensitive).'''
    return all(map(lambda word: 'a' in word.lower(), words))

# enumerate
def print_with_numbering(items):
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''
    print('\n'.join(map(lambda index_item: f"{index_item[0]}. {index_item[1]}", enumerate(items, start=1))))

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple lines separated by a hyphen with space around it.
    '''
    print('\n'.join([f"{country} - {capital}" for country, capital in zip(countries, capitals)]))

# key value list to dict
def make_dict(keys, values):
    '''Create a dictionary with keys and values'''
    return dict(map(lambda kv: (kv[0], kv[1]), zip(keys, values)))

# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words (length greater than 5).'''
    return list(map(lambda i: i[0], filter(lambda x: len(x[1]) > 5, enumerate(words))))
    
# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''
    return ''.join(map(lambda pair: pair[0] * pair[1], zip(chars, repeats)))