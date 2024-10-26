import json
import numpy as np

listPath = ["../bench/3/q1/rand/randrw_",  "../bench/3/q1/seq/rw_", "../bench/3/q2/randrw_", "../bench/3/q3/randrw", "../bench/3/q4/randrw_"]
listeQ1 = [ "0.0", "12.5" , "25.0", "37.5", "50.0" , "62.5", "75.0", "87.5","100.0"]
listeQ2 = [str(i) for i in range(10,21)]
listeQ2bis = ["1ko", "2ko", "4ko", "8ko", "16ko", "32ko", "64ko", "128ko", "256ko", "512ko", "1Mo"]
listeQ3 = [""]
listeQ4 = ["1","2","4","6","8"]

listes = [listeQ1, listeQ1, listeQ2, listeQ3, listeQ4]

# bw_read_randrw = (bw_read_randrw - np.min(bw_read_randrw)) / (np.max(bw_read_randrw) - np.min(bw_read_randrw))
# bw_read_rw = (bw_read_rw - np.min(bw_read_rw)) / (np.max(bw_read_rw) - np.min(bw_read_rw))
# bw_write_randrw = (bw_write_randrw - np.min(bw_write_randrw)) / (np.max(bw_write_randrw) - np.min(bw_write_randrw))
# bw_write_rw = (bw_write_rw - np.min(bw_write_rw)) / (np.max(bw_write_rw) - np.min(bw_write_rw))

def import_data():
	data = [ [] for i in range(len(listPath))]
	i = 0

	for liste in listes:
		for L in liste:
			strPath = listPath[i] + L + ".json"
			with open(strPath, 'r' ) as file:    
				tmp = json.load(file)
				data[i].append( tmp)
		
		i+=1
	
	return data

def extract_data(data, index_q, section, datatype):
	"""
	index_q\n
	0 => "../mesures/q1/rand/randrw_" \n
	1 => "../mesures/q1/seq/rw_" \n
	2 => "../mesures/q2/randrw_" \n
	3 => "../mesures/q3/randrw_" \n
	4 = > "../mesures/q4/randrw_" \n
	"""

	d = []

	for i in range(len(listes[index_q])):
		nb_threads = int(data[index_q][i]['jobs'][0]['job options']['numjobs'])
		ds = np.array([])

		for tid in range(nb_threads):
			ds = np.append(ds, data[index_q][i]['jobs'][tid][section][datatype])

		if (type(ds[0]) != dict):
			d.append(np.mean(ds))
		else:
			d.append(ds)
	return d