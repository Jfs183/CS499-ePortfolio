import time
from datetime import datetime 

setpoint = 70

# Read the current temperature
def read_temperature():
    return 72

# Determine system state based on temperature
def determine_state(temp, setpoint):
    if temp < setpoint:
        return "HEAT"
    elif temp > setpoint:
        return "COOL"
    else:
        return "OFF"

# Display information on the LCD
def display_lcd(line1, line2):
    print(line1)
    print(line2)
    print("----------------")

# Get current date and time
def get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d %H:%M")

# Show welcome message
def show_welcome():
    display_lcd("Welcome to", "CS 499")
    time.sleep(2)
    display_lcd("Jonathan Skop", "System Ready")
    time.sleep(2)

# Log temperature and state to a file
def log_data(temp, state, current_time):
    with open("temp_log.txt", "a") as file:
        file.write(f"{current_time} - Temp: {temp}, State: {state}\n")

def main():
    show_welcome()

    while True:
        temp = read_temperature()
        state = determine_state(temp, setpoint)
        current_time = get_datetime()

        display_lcd(f"Temp: {temp}F", f"{state} {current_time}")
        log_data(temp, state, current_time)

        time.sleep(3)

if __name__ == "__main__":
    main()