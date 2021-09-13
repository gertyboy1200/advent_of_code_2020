import os
from file_helper import get_file_contents

cwd = os.getcwd()

numbers = get_file_contents(cwd + '/day_1_input.txt')

adj = get_file_contents(cwd + '/day_1_input.txt')

numbers = [int(num) for num in numbers]

adj = [int(sub) for sub in adj]

found = False

for num in numbers:
    for sub in adj:
        if (2020 - num - sub) in numbers:
            print(num * (2020 - num - sub) * sub)
            found = True
            break
    if found == True:
        break
