import pandas as pd
from datetime import datetime

def check_formatting(file_path, output_file_path):
    """
    Checks the formatting of a data file for common issues such as invalid dates
    and incorrectly formatted data lines.

    Parameters:
        file_path (str): The path to the data file to be checked.
        output_file_path (str): The path to the output file where issues will be marked.

    Returns:
        int: The number of issues found.
    """
    issues_count = 0
    with open(file_path, 'r') as file:
        with open(output_file_path, 'w') as output_file:
            for line_number, line in enumerate(file, start=1):
                original_line = line  # Store the original line
                line = line.strip()
                if not line or line == '---':
                    output_file.write(original_line)  # Write original line to output file
                    continue  # Skip empty lines and separators
                # Check for date format
                if line.count('-') == 2 and len(line) == 10 and line[4] == '-' and line[7] == '-':
                    try:
                        datetime.strptime(line, '%Y-%m-%d')
                    except ValueError:
                        line += ' #####'  # Mark invalid line
                        issues_count += 1
                else:
                    parts = line.split(',')
                    if len(parts) < 2 or not parts[1].strip().isdigit():
                        line += ' #####'  # Mark invalid line
                        issues_count += 1
                output_file.write(line + '\n')  # Write line to output file
    return issues_count

def main():
    """
    Main function to run the check_formatting function and mark any issues found in the output file.
    """
    input_file_path = 'Data/SourceFiles/RussianLosses/ByUkraine/russian_losses_by_ukraine.txt'
    output_file_path = 'marked_invalid_lines.txt'
    issues_count = check_formatting(input_file_path, output_file_path)
    print(f"{issues_count} issues found. Invalid lines marked in '{output_file_path}'.")

if __name__ == "__main__":
    main()
