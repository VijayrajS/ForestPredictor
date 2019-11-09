fp = open('deforest_data.csv', 'r')
op = open('deforest_data_cl.csv', 'w+')

lines = fp.read().split('\n')
csv_lines = [line.split(',') for line in lines]

for line in csv_lines:
    op.write(','.join(line[0:2] + line[34:]) + '\n')
