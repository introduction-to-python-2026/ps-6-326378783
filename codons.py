def create_codon_dict(file_path):
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()
    empty_dict = {}
    for row in rows:
        row = row.strip().split("\t")
        empty_dict[row[0]] = row [2]
    return empty_dict

