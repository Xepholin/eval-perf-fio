import matplotlib.pyplot as plt
from const import *

def rand_rw_size(data, output_path):
	bw_read_percentile = extract_data(data, 3, 'read', 'clat_ns')
	bw_write_percentile = extract_data(data, 3, 'write', 'clat_ns')

	percentiles = list((bw_read_percentile[0][0]['percentile'].keys()))
	percentile_split_read = list(bw_read_percentile[0][0]['percentile'].values())
	percentile_split_write = list(bw_write_percentile[0][0]['percentile'].values())

	percentiles = [float(value) for value in percentiles]

	percentile_split_read = np.array([float(value) for value in percentile_split_read])
	percentile_split_write = np.array([float(value) for value in percentile_split_write])

	# percentile_default_read = list(bw_read_percentile[1][0]['percentile'].values())
	# percentile_default_write = list(bw_write_percentile[1][0]['percentile'].values())
	# percentile_default_read = np.array([float(value) for value in percentile_default_read])
	# percentile_default_write = np.array([float(value) for value in percentile_default_write])
	
	_, ax = plt.subplots(1, 1, figsize=(10, 8))
	ax.set_box_aspect(1)

	X_axis = np.arange(len(percentile_split_read[2:11])) 

	plt.bar(X_axis - 0.2, percentile_split_read[2:11], 0.4, label = 'CLat of Read Bssplit') 
	plt.bar(X_axis + 0.2, percentile_split_write[2:11], 0.4, label = 'CLat of Write Bssplit') 

	plt.title("Complete Latency of Read/Write Bssplit wrt. Percentiles")
	plt.xticks(X_axis, percentiles[2:11]) 
	plt.xlabel("Percentiles")
	plt.ylabel("CLat")
	plt.legend(loc='best')
	plt.grid(True)

	plt.savefig(output_path)
    
data = import_data()
rand_rw_size(data, "../plots/bw_rw_rand_split.png")