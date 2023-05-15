import time

def focus_timer(minutes):
    """Function to run the focus timer for a specified number of minutes"""
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time remaining: {seconds//60} minutes {seconds%60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time is up! Focus session is over.")

if __name__ == "__main__":
    focus_timer(25) # run a 25 minute focus session
