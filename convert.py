import os
import sys
import subprocess

# Check if no arguments were passed
if len(sys.argv) == 1:
    print("No arguments provided. Please provide a .statespace file as an argument.")
    sys.exit(1)

# Get the file name and extension
file = os.path.realpath(sys.argv[1])
filename, extension = os.path.splitext(file)

# Check if the file extension is 'statespace'
if extension != ".statespace":
    print("Invalid file type. Please provide an .statespace file.")
    sys.exit(1)

# Extract project name and base directory
projectname = os.path.basename(filename)
basedir = os.path.dirname(os.path.dirname(filename))

# Define paths based on the base directory and project name
outlocation = os.path.join(basedir, "Rebeca", "statespaces") + "/"
observable = os.path.join(outlocation, "observable_actions.txt")
tau = os.path.join(outlocation, "tau_transitions.txt")

# Path to helper programs
tools_dir = os.path.dirname(os.path.realpath(__file__))
cast = os.path.join(tools_dir, "Cast", "cast")
extraction = os.path.join(tools_dir, "Extraction", "extraction")
reduce = os.path.join(tools_dir, "convert.sh")

autfile = projectname + "_reduced.aut"

# Replace .aut-file
if os.path.isfile(outlocation + autfile):
    os.remove(outlocation + autfile)
open(outlocation + autfile, 'a').close()

subprocess.run([cast, file], stdout=open(outlocation + autfile, 'w'))
testautfile = len(open(outlocation + autfile, 'r').read().split())

# Check that something was written out to the .aut-file
if testautfile == 0:
    print("Something went wrong during casting")

# Extraction
subprocess.run([extraction, outlocation + autfile, tau, "-s", observable])
testextraction = len(open(tau, 'r').read().split())
if testextraction == 0:
    print("Something went wrong during extraction")

# Reduce using convert.sh
subprocess.run(["python", outlocation + autfile])
# subprocess.run([reduce, outlocation + autfile])