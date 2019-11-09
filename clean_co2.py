fp = open('edg_co2.csv', 'r')
op = open('edg_co2_cl.csv', 'w+')

lines = fp.read().split('\n')[1:-1]
csv_lines = [line.split(',') for line in lines]

temp = []

for line in csv_lines:
    if temp and temp[0] == line[0]:
        t1 = [float(u) for u in line[4:]]
        for i in range(len(t1)):
            temp[i+2] += t1[i]
    
    else:
        op.write(','.join([str(u) for u in temp]) + '\n')
        temp = line[0:2] + [float(u) for u in line[4:]]

op.write(','.join([str(u) for u in temp]) + '\n')
