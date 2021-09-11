import os
from file_helper import get_file_contents

cwd = os.getcwd()

numbers = get_file_contents(cwd + '/day_1_input.txt')

numbers = [int(num) for num in numbers]

for num in numbers:
    diff = 2020 - num
    if diff in numbers:
        print(num * diff)
        break
