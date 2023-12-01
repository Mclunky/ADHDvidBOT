
import subprocess
import os

# Path to the directory containing the scripts
scripts_path = 'C:/Users/Ohio/Documents/Shorts Scraper/'

# Path to the flag file
flag_file = os.path.join(scripts_path, 'flag.txt')

# Check if the flag file exists, if it does, exit the script.
if os.path.exists(flag_file):
    print("Script already running. Exiting.")
    exit()
# If not, create it and proceed.
else:
    with open(flag_file, 'w') as file:
        file.write("running")

# Get list of .py files in the directory
script_files = [f for f in os.listdir(scripts_path) if f.endswith('.py')]

# Sort the files based on the initial number in the file name
script_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else float('inf'))

# Execute scripts sequentially
for script in script_files:
    print(f"Running {script}...")
    subprocess.run(['python', os.path.join(scripts_path, script)])
    print(f"{script} completed.\n")

# Delete the flag file at the end of script execution.
os.remove(flag_file)
