import os
import sys
import subprocess

# Funkar

# Check if no arguments were passed
if len(sys.argv) == 1:
    print("No arguments provided. Please provide an .aut file as an argument.")
    sys.exit(1)

# Get the file name and extension
file = os.path.realpath(sys.argv[1])
filename, extension = os.path.splitext(file)

# Check if the file extension is 'aut'
if extension != ".aut":
    print("Invalid file type. Please provide an .aut file.")
    sys.exit(1)

# Define paths based on the base directory and project name
tau = os.path.join(os.path.dirname(filename), "tau_transitions.txt")
filename_reduced = filename + "_reduced" + extension

# Read the content of tau file
with open(tau, 'r') as f:
    tau_content = f.read().strip()

# Run the ltsconvert command
subprocess.run(["ltsconvert", "--equivalence=weak-trace", "--tau=" + tau_content, file, filename_reduced])