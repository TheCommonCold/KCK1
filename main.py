import matplotlib.pyplot as plt
import csv
import numpy
from matplotlib import rc


nazwy=('2cel-rs.csv','rsel.csv','2cel.csv','cel-rs.csv','cel.csv')
symbole=('o','v','D','s','d')
def czytacz(nazwa):
    dane = []
    effort = []
    with open(nazwa, newline='') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            templist = []
            effort.append(float(row[1]))
            for str in row[2:]:
                templist.append(float(str))
            dane.append(numpy.mean(templist))
    return dane,effort

plt.figure(figsize=(6,6))

plt.title('Pokolenie')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
plt.xlabel('Rozegranych gier (×1000)',**{'family': 'serif', 'serif': ['Computer Modern']})
plt.ylabel('Odsetek wygranych gier [%]',**{'family': 'serif', 'serif': ['Computer Modern']})
dana,effort = czytacz(nazwy[1])
i=0

for nazwa in nazwy:
    dana, effort = czytacz(nazwa)
    plt.plot(effort, dana, marker=symbole[i], label=nazwa)
    i=i+1
plt.legend(numpoints=3)
plt.legend()
plt.savefig('test.pdf')
plt.close()

