import csv, sys
rows = list(csv.reader(open(sys.argv[1])))
widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
fmt = ' | '.join('{{:<{}}}'.format(w) for w in widths)
print('| ' + fmt.format(*rows[0]) + ' |')
print('| ' + ' | '.join('-'*w for w in widths) + ' |')
for row in rows[1:]: print('| ' + fmt.format(*row) + ' |')
