import csv

def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    num_players = 0
    num_goals = 0
    
    try:
        # Open and read the CSV file
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)  # Read as a dictionary using headers
            for row in reader:
                # Check if the country matches
                if row['Country'] == country:
                    num_players += 1
                    num_goals += int(row['Goals'])
        
        # If no players are found for the country, return (-1, -1)
        if num_players == 0:
            return (-1, -1)
        
        return (num_players, num_goals)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return (-1, -1)
    except KeyError:
        print("Error: File format is incorrect. Missing required headers.")
        return (-1, -1)