def add_line_numbers(input_file, output_file):
    with open(input_file, "r") as infile:
        lines = infile.readlines()
    with open(output_file, "w") as outfile:
        for line_number, line in enumerate(lines, start=1):
            outfile.write(f"{line_number:4}: {line}")
input_file = "program.txt"
output_file = "numbered_program.txt"
add_line_numbers(input_file, output_file)
print("Line numbers added successfully.")
