import random
import os
filename = input("Enter the filename containing payloads (default: payloads.txt): ")

# Use default filename if no input is given
if filename == "":
    filename = "payloads.txt"

# Check if the file exists
if not os.path.exists(filename):
    print(f"Error: File {filename} not found.")
    exit()

# Open a text file containing payloads for reading
with open(filename, "r") as f:
    # Read the payloads into a list
    payloads = f.read().splitlines()

# Initialize empty lists of strings to filter out and to keep
filter_strings = []
keep_strings = []

# Prompt the user to specify whether or not to filter out payloads
while True:
    filter_out = input("Filter out payloads? (y/n) ").lower()
    if filter_out in ["y", "n"]:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if filter_out == "y":
    # Loop until the user is done specifying strings to filter out
    while True:
        # Prompt the user to specify a string to filter out
        filter_string = input("Enter a string to filter out (or leave blank to finish): ")

        # Check if the user is done specifying strings
        if filter_string == "":
            # Break out of the loop if the user is done
            break
        else:
            # Add the specified string to the list of strings to filter out
            filter_strings.append(filter_string)

# Prompt the user to specify whether or not to specify strings that should be present in the payloads
while True:
    keep = input("Specify strings that should be present in the payloads? (y/n) ").lower()
    if keep in ["y", "n"]:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if keep == "y":
    # Loop until the user is done specifying strings to keep
    while True:
        # Prompt the user to specify a string to keep
        keep_string = input("Enter a string to keep (or leave blank to finish): ")

        # Check if the user is done specifying strings
        if keep_string == "":
            # Break out of the loop if the user is done
            break
        else:
            # Add the specified string to the list of strings to keep
            keep_strings.append(keep_string)

# Filter out payloads that contain any of the specified strings to filter out
if filter_strings:
    filtered_payloads = [payload for payload in payloads if not any(s in payload for s in filter_strings)]
else:
    filtered_payloads = payloads

# Keep only payloads that contain any of the specified strings to keep
if keep_strings:
    filtered_payloads = [payload for payload in filtered_payloads if any(s in payload for s in keep_strings)]

# Prompt the user to specify how many payloads to display
while True:
    try:
        num_payloads = int(input("How many payloads do you want to see? "))
        if num_payloads <= 0:
            print("Invalid input. Please enter a positive integer.")
        elif num_payloads > len(filtered_payloads):
            print(f"Sorry, there are only {len(filtered_payloads)} payloads available after filtering.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Choose the specified number of payloads at random
chosen_payloads = random.sample(filtered_payloads, num_payloads)

# Display the chosen payloads
for payload in chosen_payloads:
    print(payload)
