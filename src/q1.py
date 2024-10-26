import matplotlib.pyplot as plt
from const import *

def rand_rw_part(data, output_path):
    bw_read_rw = extract_data(data, 1, 'read','bw')
    bw_write_rw = extract_data(data, 1, 'write','bw')

    bw_read_randrw = extract_data(data, 0, 'read', 'bw')
    bw_write_randrw = extract_data(data, 0, 'write', 'bw')

    bw_read_rw = [value/10**3 for value in bw_read_rw]
    bw_write_rw = [value/10**3 for value in bw_write_rw]

    bw_read_randrw = [value/10**3 for value in bw_read_randrw]
    bw_write_randrw = [value/10**3 for value in bw_write_randrw]

    _, axs = plt.subplots(1, 2, figsize=(14,7))
    axs = axs.ravel()
        
    axs[0].plot(listeQ1, bw_read_randrw, lw=2, label="BP lecture aléatoire")
    axs[0].plot(listeQ1, bw_read_rw, lw=2, label="BP lecture séquentielle")

    axs[1].plot(listeQ1, bw_write_randrw, lw=2, label="BP écriture aléatoire")
    axs[1].plot(listeQ1, bw_write_rw, lw=2, label="BP écriture séquentielle")

    axs[0].set_title("Lecture Sequentielle Vs. Aléatoire wrt. % d'écriture")
    axs[0].set_xlabel("Pourcentage d'écriture")
    axs[0].set_ylabel("Bande Passante en Mo/s")
    axs[0].legend(loc='best')
    axs[0].grid(True)

    axs[1].set_title("Écriture Sequentielle Vs. Aléatoire wrt. % d'écriture")
    axs[1].set_xlabel("Pourcentage d'écriture")
    axs[1].set_ylabel("Bande Passante en Mo/s")
    axs[1].legend(loc='lower right')
    axs[1].grid(True)

    axs[0].set_xlim(left=-0.5)
    axs[0].set_ylim(bottom=-0.5)

    axs[1].set_xlim(left=-0.5)
    axs[1].set_ylim(bottom=-0.5)

    plt.tight_layout()
    plt.savefig(output_path)
    
def bw_part(data, output_path):
    bw_read_rw = extract_data(data, 1, 'read','bw')
    bw_write_rw = extract_data(data, 1, 'write','bw')

    bw_read_randrw = extract_data(data, 0, 'read', 'bw')
    bw_write_randrw = extract_data(data, 0, 'write', 'bw')

    bw_read_rw = [value/10**3 for value in bw_read_rw]
    bw_write_rw = [value/10**3 for value in bw_write_rw]

    bw_read_randrw = [value/10**3 for value in bw_read_randrw]
    bw_write_randrw = [value/10**3 for value in bw_write_randrw]

    bw_rw = []
    bw_randrw = []

    for i in range(len(bw_read_randrw)):
        bw_rw.append((bw_read_rw[i] + bw_write_rw[i]) / 2)
        bw_randrw.append((bw_read_randrw[i] + bw_write_randrw[i]) / 2)

    _, axs = plt.subplots(1, 2, figsize=(19,7))
    axs = axs.ravel()
        
    axs[0].scatter(listeQ1, bw_rw, label="BP Moyenne Séquentielle")
    axs[1].scatter(listeQ1, bw_randrw, label="BP Moyenne Aléatoire")

    axs[0].set_title("Bande Passante Moyenne wrt. % d'écriture")
    axs[0].set_xlabel("Pourcentage d'écriture")
    axs[0].set_ylabel("Bande Passante en Mo/s")
    axs[0].legend(loc='best')

    axs[1].set_title("Bande Passante Moyenne wrt. % d'écriture")
    axs[1].set_xlabel("Pourcentage d'écriture")
    axs[1].set_ylabel("Bande Passante en Mo/s")
    axs[1].legend(loc='lower right')

    axs[0].set_xlim(left=-0.5)
    axs[0].set_ylim(bottom=-0.5)

    axs[1].set_xlim(left=-0.5)
    axs[1].set_ylim(bottom=-0.5)

    plt.tight_layout()
    plt.savefig(output_path)

data = import_data()
rand_rw_part(data, "../plots/bw_rw_rand_part.png")
bw_part(data, "../plots/bw_part.png")