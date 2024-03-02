# Read the first file and extract binary strings
with open('11.txt', 'r') as file1:
    binary_strings1 = {line.split()[1] for line in file1}

# Read the second file and get binary strings
with open('11NEW.txt', 'r') as file2:
    binary_strings2 = {line.strip() for line in file2}

# Find strings that are in file1 but not in file2
in_file1_not_file2 = binary_strings1.difference(binary_strings2)

# Find strings that are in file2 but not in file1
in_file2_not_file1 = binary_strings2.difference(binary_strings1)

# Print the results
print("In file1 but not in file2:", in_file1_not_file2)
print("In file2 but not in file1:", in_file2_not_file1)
