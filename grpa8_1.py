def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    result = {}
    
    try:
        # Open the file and process each line
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()  # Remove leading/trailing whitespace and newline
                # Update frequency count
                result[word] = result.get(word, 0) + 1
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return result