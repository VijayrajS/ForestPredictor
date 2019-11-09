fp = open('Metadata_Country_API_AG.LND.FRST.ZS_DS2_en_csv_v2_180602.csv', 'r')
op = open('metadata_cl.csv', 'w+')

import csv
spamreader = csv.reader(fp, delimiter=',', quotechar='\"')
for row in spamreader:
    op.write(','.join([row[0],row[2],row[4]])+'\n')
