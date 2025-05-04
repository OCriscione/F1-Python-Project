import requests  # Importing the requests library to make HTTP requests to the API.

F1Url = "https://ergast.com/api/f1/2024"  # This is the base URL for the Ergast API to fetch race results for the 2024 F1 season.

def raceResults(roundNumber):
    # Construct the full URL to fetch results for a specific round (e.g., round=1).
    url = f"{F1Url}/{roundNumber}/results.json"  # Updated to query for a specific round.
    response = requests.get(url)  # Make an HTTP GET request to the constructed URL.

    if response.status_code == 200:  # If the status code of the response is 200, it means the request was successful.

        data = response.json()  # Convert the response (which is in JSON format) into a Python dictionary.

        # The response structure in the Ergast API has the following hierarchy: 'MRData' -> 'RaceTable' -> 'Races' -> 'Results'.
        # Extract the race data for the first race in the list (index 0).
        race = data['MRData']['RaceTable']['Races'][0]

        # Extract the race name and the date of the race.
        raceName = race.get("raceName", "Unknown Race")  # Use .get() to safely fetch the value, fallback to 'Unknown Race' if not found.
        date = race.get("date", "Unknown Date")  # Same for the date.
        
        # Extract the list of results for the race.
        results = race.get("Results", [])  # If no results are found, an empty list is used.

        # Print the race name and date as a header.
        print(f"\n{raceName} - {date}")
        print("Position | Driver               | Team")
        print("---------------------------------------------")

        # Loop through each result in the 'Results' list to display position, driver, and team.
        for result in results:
            position = result.get("position", "N/A")  # Get the position of the driver. If not found, default to "N/A".
            driver = result.get("Driver", {})  # The driver info is stored under the "Driver" key in the result.
            driverName = f"{driver.get('givenName', '')} {driver.get('familyName', '')}".strip()  # Construct the driver's full name.

            # Extract the team's name from the 'Constructor' data.
            teamName = result.get("Constructor", {}).get("name", "Unknown Team")  # Use .get() to avoid KeyError if the team data is missing.

            # Print the result: position, driver's full name, and the team's name.
            print(f"{position:<8} | {driverName:<20} | {teamName}")

    else:
        # If the status code is not 200 (i.e., the request failed), print an error message.
        print(f"Failed to retrieve data for round {roundNumber}. Status code: {response.status_code}")

def mainf1():
    totalRounds = 24  # The 2024 F1 season has 24 races (rounds).

    # Loop through each round number (from 1 to 24) and fetch the race results for that round.
    for roundNumber in range(1, totalRounds + 1):
        raceResults(roundNumber)  # Call the 'raceResults' function for each round.

mainf1()  # Start the program by calling 'mainf1'.
