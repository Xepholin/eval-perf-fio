import matplotlib.pyplot as plt
from const import *

def rand_rw_size(data, output_path):
	bw_read_randrw = extract_rw_rand(data, 3, 'read', 'bw')
	bw_write_randrw = extract_rw_rand(data, 3, 'write', 'bw')

	bw_read_percentile = extract_rw_rand(data, 3, 'read', 'clat_ns')
	bw_write_percentile = extract_rw_rand(data, 3, 'write', 'clat_ns')

	print(bw_read_percentile[0][0]['percentile'])
	exit()

	_, ax = plt.subplots(1, 1, figsize=(10, 8))
	ax.set_box_aspect(1)

	plt.plot(listeQ, bw_read_randrw, lw=2, label="Read BW Random")
	plt.plot(listeQ2, bw_write_randrw, lw=2, label="Write BW Random")

	plt.title("Read & Write Random wrt. split")
	plt.xlabel("Split")
	plt.ylabel("Bandwidth")
	plt.legend(loc='best')
	plt.grid(True)

	plt.savefig(output_path)
    
data = import_data()
rand_rw_size(data, "../plots/bw_rw_rand_split.png")