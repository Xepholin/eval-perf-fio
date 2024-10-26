import matplotlib.pyplot as plt
from const import *

def read_part(data, output_path):
    bw_rw = extract_data(data, 1, 'read','bw')
    bw_randrw = extract_data(data, 0, 'read', 'bw')

    bw_rw = [value/10**3 for value in bw_rw]
    bw_randrw = [value/10**3 for value in bw_randrw]

    _, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_box_aspect(1)

    X_axis = np.arange(len(listeQ1)) 
        
    plt.bar(X_axis - 0.2, bw_randrw, 0.4, label="BP lecture aléatoire")
    plt.bar(X_axis + 0.2, bw_rw, 0.4, label="BP lecture séquentielle")

    plt.title("Lecture Sequentielle Vs. Aléatoire wrt. % d'écriture")
    plt.xticks(X_axis, listeQ1)
    plt.xlabel("Pourcentage d'écriture")
    plt.ylabel("Bande Passante en Mo/s")
    plt.legend(loc='best')
    plt.grid(True)

    plt.xlim(left=-0.8)
    plt.ylim(bottom=0)

    plt.savefig(output_path)

def write_part(data, output_path):
    bw_rw = extract_data(data, 1, 'write','bw')
    bw_randrw = extract_data(data, 0, 'write', 'bw')

    bw_rw = [value/10**3 for value in bw_rw]
    bw_randrw = [value/10**3 for value in bw_randrw]

    _, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_box_aspect(1)

    X_axis = np.arange(len(listeQ1)) 

    plt.bar(X_axis - 0.2, bw_randrw, 0.4, label="BP écriture aléatoire")
    plt.bar(X_axis + 0.2, bw_rw, 0.4, label="BP écriture séquentielle")

    plt.title("Écriture Sequentielle Vs. Aléatoire wrt. % d'écriture")
    plt.xticks(X_axis, listeQ1)
    plt.xlabel("Pourcentage d'écriture")
    plt.ylabel("Bande Passante en Mo/s")
    plt.legend(loc='best')
    plt.grid(True)

    plt.xlim(left=-0.8)
    plt.ylim(bottom=0)

    plt.savefig(output_path)
    
def bw_sum_part(data, output_path):
    bw_read_rw = extract_data(data, 1, 'read','bw')
    bw_write_rw = extract_data(data, 1, 'write','bw')

    bw_read_rw = [value/10**3 for value in bw_read_rw]
    bw_write_rw = [value/10**3 for value in bw_write_rw]

    bw_read_randrw = extract_data(data, 0, 'read', 'bw')
    bw_write_randrw = extract_data(data, 0, 'write', 'bw')

    bw_read_randrw = [value/10**3 for value in bw_read_randrw]
    bw_write_randrw = [value/10**3 for value in bw_write_randrw]

    bw_rw = []
    bw_randrw = []

    for i in range(len(bw_read_rw)):
        bw_rw.append((bw_read_rw[i] + bw_write_rw[i]) / 2)
        bw_randrw.append((bw_read_randrw[i] + bw_write_randrw[i]) / 2)

    _, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_box_aspect(1)

    X_axis = np.arange(len(listeQ1))
        
    plt.bar(X_axis - 0.2, bw_rw, 0.4, label="BP Moyenne Séquentielle")
    plt.bar(X_axis + 0.2, bw_randrw, 0.4, label="BP Moyenne Aléatoire")

    plt.title("Bande Passante Moyenne wrt. % d'écriture")
    plt.xlabel("Pourcentage d'écriture")
    plt.ylabel("Bande Passante en Mo/s")
    plt.legend(loc='best')
    plt.grid(True)

    plt.xlim(left=-0.8)
    plt.ylim(bottom=0)

    plt.savefig(output_path)

data = import_data()

read_part(data, "../plots/bw_read_part.png")
write_part(data, "../plots/bw_write_part.png")

bw_sum_part(data, "../plots/bw_sum_part.png")