import matplotlib.pyplot as plt
from const import *

def rand_rw_size(data, output_path):
	bw_read_randrw, bw_write_randrw = extract_rw_rand(data, 2, 0, 'bw')
	
	_, ax = plt.subplots(1, 1, figsize=(10, 8))
	ax.set_box_aspect(1)

	plt.plot(listeQ2, bw_read_randrw, lw=2, label="Read BW Random")
	plt.plot(listeQ2, bw_write_randrw, lw=2, label="Write BW Random")

	plt.title("Read & Write Random wrt. request size")
	plt.xlabel("Request size")
	plt.ylabel("Bandwidth")
	plt.legend(loc='best')
	plt.grid(True)

	plt.savefig(output_path)
    
data, data2 = import_data()
rand_rw_size(data, "../plots/bw_rw_rand_size.png")
rand_rw_size(data2, "../plots/bw_rw_rand_size2.png")