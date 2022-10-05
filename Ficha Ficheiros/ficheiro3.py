from os import write


def invert(file1, file2):
    with open(file1, 'r') as file1:
        with open(file2, 'w') as file2:
            lines = reversed(file1.readlines())
            for line in lines:
                file2.write(line)

invert('teste.txt', 'segundo.txt')