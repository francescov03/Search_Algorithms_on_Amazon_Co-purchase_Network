import random

input_file = "Uninformed-Search-Algorithms-Analysis-main/dataset/amazon0312.txt"
output_file = "Uninformed-Search-Algorithms-Analysis-main/dataset/amazon0312-weighted.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if line.startswith("#"):
            continue  # Skip the comments
        parts = line.strip().split()
        if len(parts) == 2:
            from_node, to_node = parts
            weight = random.randint(1, 10)
            outfile.write(f"{from_node}\t{to_node}\t{weight}\n")
