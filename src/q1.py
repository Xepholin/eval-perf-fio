import matplotlib.pyplot as plt
from const import *

def rand_rw_part(data, output_path):
	bw_read_rw = extract_rw_rand(data, 1, 'read','bw')
	bw_write_rw = extract_rw_rand(data, 1, 'write','bw')

	bw_read_randrw = extract_rw_rand(data, 0, 'read', 'bw')
	bw_write_randrw = extract_rw_rand(data, 0, 'write', 'bw')

	_, axs = plt.subplots(1, 2, figsize=(14,7))
	axs = axs.ravel()
		
	axs[0].plot(listeQ1, bw_read_randrw, lw=2, label="Read BW Random")
	axs[0].plot(listeQ1, bw_read_rw, lw=2, label="Read BW")

	axs[1].plot(listeQ1, bw_write_randrw, lw=2, label="Write BW Random")
	axs[1].plot(listeQ1, bw_write_rw, lw=2, label="Write BW")

	axs[0].set_title("Read Sequential Vs. Random wrt. % of write")
	axs[0].set_xlabel("Pourcentage of write")
	axs[0].set_ylabel("Bandwidth")
	axs[0].legend(loc='best')
	axs[0].grid(True)

	axs[1].set_title("Write Sequential Vs. Random wrt. % of write")
	axs[1].set_xlabel("Pourcentage of write")
	axs[1].set_ylabel("Bandwidth")
	axs[1].legend(loc='lower right')
	axs[1].grid(True)

	plt.tight_layout()
	plt.savefig(output_path)
    
data = import_data()
rand_rw_part(data, "../plots/bw_rw_rand_part.png")