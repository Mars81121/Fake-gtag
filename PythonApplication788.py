import time
import random
import msvcrt
import sys
import os

def set_blue_background():
    print("\x1b[44m", end="")  # ANSI escape code for blue background

def reset_color():
    print("\x1b[0m", end="")  # Reset ANSI escape code to default

def loading_screen(seconds):
    set_blue_background()  # Set blue background
    print("Welcome to the Gorilla Tag Anti-Cheat Terminal")
    print("Loading...")
    reset_color()  # Reset color

    for _ in range(seconds):
        print(".", end="", flush=True)
        time.sleep(1)

    set_blue_background()  # Set blue background
    print("\nLoading complete!")
    reset_color()  # Reset color

def display_ip_addresses():
    set_blue_background()  # Set blue background
    print("\nIP Addresses:")
    reset_color()  # Reset color

    for _ in range(5):
        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        print(ip_address)

def display_additional_ip_addresses():
    set_blue_background()  # Set blue background
    print("\nAdditional IP Addresses:")
    reset_color()  # Reset color

    for _ in range(5):
        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        print(ip_address)

def display_player_codes():
    set_blue_background()  # Set blue background
    print("\nGorilla Tag Player Codes:")
    reset_color()  # Reset color

    for _ in range(9):
        player_code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=13))
        print(player_code)

def is_gorilla_tag_installed():
    steam_apps_path = os.path.join(os.getenv("ProgramFiles(x86)"), "Steam", "steamapps", "common")
    gorilla_tag_path = os.path.join(steam_apps_path, "Gorilla Tag")

    return os.path.exists(gorilla_tag_path)

if __name__ == "__main__":
    if not is_gorilla_tag_installed():
        print("Error: Gorilla Tag is not installed on your system.")
        sys.exit(1)

    loading_time = 5
    loading_screen(loading_time)

    # Flags to disable options
    options_disabled = {'K': False, 'R': False, 'C': False}

    while True:
        key = msvcrt.getch().decode().upper()
        if key == 'K' and not options_disabled['K']:
            print("\nPress 'K' to display IP addresses.")
            display_ip_addresses()
            options_disabled['K'] = True
        elif key == 'R' and not options_disabled['R']:
            print("\nPress 'R' to display additional IP addresses.")
            display_additional_ip_addresses()
            options_disabled['R'] = True
        elif key == 'C' and not options_disabled['C']:
            print("\nPress 'C' to display Gorilla Tag Player Codes.")
            display_player_codes()
            options_disabled['C'] = True
        elif key == 'X':
            print("\nPress 'X' again to exit...")
            key = msvcrt.getch().decode().upper()
            if key == 'X':
                print("\nExiting the terminal...")
                reset_color()  # Reset color before exiting
                sys.exit()
