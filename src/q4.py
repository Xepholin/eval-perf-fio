import matplotlib.pyplot as plt
from const import *

def rand_rw_parallel(data, output_path):
	bw_read_randrw = extract_data(data, 4, 'read', 'bw')
	bw_write_randrw = extract_data(data, 4, 'write', 'bw')

	_, ax = plt.subplots(1, 1, figsize=(10, 8))
	ax.set_box_aspect(1)

	plt.plot(listeQ4, bw_read_randrw, lw=2, label="Read BW Random")
	plt.plot(listeQ4, bw_write_randrw, lw=2, label="Write BW Random")

	plt.title("Read & Write Random wrt. nb threads")
	plt.xlabel("Nb threads")
	plt.ylabel("Bandwidth")
	plt.legend(loc='best')
	plt.grid(True)

	plt.savefig(output_path)
    
data = import_data()
rand_rw_parallel(data, "../plots/bw_rw_rand_parallel.png")