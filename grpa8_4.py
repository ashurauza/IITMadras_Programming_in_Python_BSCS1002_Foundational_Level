def num_to_words(mat):
    """
    Convert matrix of single-digit numbers to a file with words

    Argument: 
        mat: list of lists
    Return:
        None
    """
    # Dictionary to map numbers to words
    num_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    
    try:
        # Open the file in write mode
        with open("words.csv", "w") as file:
            for i, row in enumerate(mat):
                # Convert row of numbers to their word equivalents
                word_row = [num_to_word[num] for num in row]
                # Join words with commas
                line = ",".join(word_row)
                
                # Write to file; add newline except for the last row
                if i < len(mat) - 1:
                    file.write(line + "\n")
                else:
                    file.write(line)
    except Exception as e:
        print(f"An error occurred: {e}")