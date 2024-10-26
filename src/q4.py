import matplotlib.pyplot as plt
from const import *

def rand_rw_parallel(data, output_path):
	bw_read_randrw = extract_data(data, 4, 'read', 'bw')
	bw_write_randrw = extract_data(data, 4, 'write', 'bw')

	bw_read_randrw = [value/10**3 for value in bw_read_randrw]
	bw_write_randrw = [value/10**3 for value in bw_write_randrw]

	_, ax = plt.subplots(1, 1, figsize=(10, 8))
	ax.set_box_aspect(1)

	X_axis = np.arange(len(listeQ4)) 

	plt.bar(X_axis - 0.2, bw_read_randrw, 0.4, label="BP lecture aléatoire")
	plt.bar(X_axis + 0.2, bw_write_randrw, 0.4, label="BP écriture aléatoire")

	plt.title("Lecture & Écriture Aléatoire wrt. Nombre de threads")
	plt.xticks(X_axis, listeQ4)
	plt.xlabel("Nombre de threads")
	plt.ylabel("Bande Passante en Mo/s")
	plt.legend(loc='best')
	plt.grid(True)

	plt.xlim(left=-0.8)
	plt.ylim(bottom=0)

	plt.savefig(output_path)
    
data = import_data()
rand_rw_parallel(data, "../plots/bw_rw_rand_parallel.png")