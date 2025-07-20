def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    try:
        # Open and read the lines of both files
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = [line.strip() for line in f1.readlines()]  # Strip newlines in file1
            lines2 = [line.strip() for line in f2.readlines()]  # Strip newlines in file2

        # Check if lines in file1 match those in file2
        if lines1 == lines2:  # Exact match of content and length
            return "Equal"
        elif len(lines1) < len(lines2) and lines1 == lines2[:len(lines1)]:
            return "Subset"  # file1 matches the prefix of file2
        else:
            return "No Relation"

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return "No Relation"