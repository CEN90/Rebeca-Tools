import os
import sys
import subprocess

# Check if no arguments were passed
if len(sys.argv) == 1:
    print("No arguments provided. Please provide an .aut file as an argument.")
    sys.exit(1)

# Get the file name and extension
file = sys.argv[1]
filename, extension = os.path.splitext(file)

# Check if the file extension is 'aut'
if extension != ".aut":
    print("Invalid file type. Please provide an .aut file.")
    sys.exit(1)

# Run the commands
subprocess.run(["ltsconvert", file, "--out=dot", filename + ".dot"])
subprocess.run(["dot", "-Tpdf", filename + ".dot", "-o", filename + ".pdf"])

if os.path.isfile(filename + ".dot"):
    os.remove(filename + ".dot")

print("Converted the reduced statespace.")