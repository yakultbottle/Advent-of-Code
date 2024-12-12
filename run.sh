#!/bin/bash

# Check for correct arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: run <1|2> <small|test>"
    exit 1
fi

# Map arguments to script and file names
script="part$1.py"  # Converts 1/2 to part1.py/part2.py
if [ "$2" == "small" ]; then
    file="small_test.txt"
elif [ "$2" == "test" ]; then
    file="test.txt"
else
    echo "Error: Second argument must be 'small' or 'test'."
    exit 1
fi

# Check if the script and file exist
if [[ ! -f $script ]]; then
    echo "Error: $script not found in $(pwd)!"
    exit 1
fi

if [[ ! -f $file ]]; then
    echo "Error: $file not found in $(pwd)!"
    exit 1
fi

# Execute the command
cat "$file" | python3 "$script"

