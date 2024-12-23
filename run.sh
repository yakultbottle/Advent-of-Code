#!/bin/bash

# Check for correct arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: run <1|2> <small|test>"
    exit 1
fi

# Map arguments to script and file names
script="part$1.py"  # Converts 1/2 to part1.py/part2.py
if [[ "$2" == small* ]]; then
    number=${2#small}
    if [[ -z "$number" ]]; then
	file="small_test.txt"
    else
        file="small_test${number}.txt"
    fi
elif [[ "$2" == test* ]]; then
    number=${2#test}
    if [[ -z "$number" ]]; then
	file="test.txt"
    else
        file="test${number}.txt"
    fi
else
    echo "Invalid input: $2"
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

