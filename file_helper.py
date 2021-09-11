def get_file_contents(file_name):
    opened_file = open(file_name)

    lines = opened_file.readlines()
    stripped_lines = []
    for x in lines:
        stripped_lines.append(x.strip())
    return stripped_lines
