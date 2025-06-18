# Import the ntplib library to access internet time servers using NTP
import ntplib

# Import ctime from the time module to convert time from timestamp to readable format
from time import ctime


# Define a function to get the current internet time
def get_internet_time():
    try:
        # Create an NTP client object
        client = ntplib.NTPClient()

        # Send a request to an internet time server (pool.ntp.org)
        response = client.request('time.google.com')

        # Print the current time received from the server in a readable format
        print("Current time from Internet Time Server:")
        print(ctime(response.tx_time))

    # Catch and print any errors that occur (e.g., no internet connection)
    except Exception as e:
        print("Could not retrieve time from internet. Reason:", e)


# Call the function to run the code
get_internet_time()
