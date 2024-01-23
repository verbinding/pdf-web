#!/bin/bash

# Define the output file name
output_file="specific_files_and_folders_contents.txt"

# List of files and folders for which to print contents
declare -a files_and_folders=(
    "./backend/app/__init__.py"
    "./backend/app/main.py"
    "./backend/app/models/company_enrichment_request.py"
    "./backend/app/models/person_identify_request.py"
    "./backend/app/routers/__init__.py"
    "./backend/app/routers/company_enrichment.py"
    "./backend/app/routers/person_identify.py"
    "./backend/requirements.txt"
)

# Function to print the contents of specified files and folders
print_specific_contents() {
    for item in "${files_and_folders[@]}"; do
        if [ -f "$item" ]; then
            # If it's a file, print its contents
            echo "Contents of $item:" >> "$output_file"
            cat "$item" >> "$output_file"
            echo "" >> "$output_file"
        elif [ -d "$item" ]; then
            # If it's a directory, print the directory structure
            echo "Directory Structure of $item:" >> "$output_file"
            tree "$item" >> "$output_file"
            echo "" >> "$output_file"
        fi
    done
}

# Call the function to append specific file and folder contents to the output file
print_specific_contents

# Display a message about where the contents were saved
echo "Specific files and folders contents saved to $output_file"
