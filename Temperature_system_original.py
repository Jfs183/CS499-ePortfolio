import time

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

def main():

    while True:
        temp = read_temperature()
        state = determine_state(temp, setpoint)

        display_lcd(f"Temp: {temp}F", f"State: {state}")

        time.sleep(3)

if __name__ == "__main__":
    main()
