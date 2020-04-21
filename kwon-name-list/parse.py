with open('Kwon.txt', 'r') as f:
    for (i, line) in enumerate(f.readlines()):
        with open('{}.txt'.format(i), 'w') as outf:
            outf.write(line[:-1])