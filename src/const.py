import json
import numpy as np

listPath = ["../mesures/q1/rand/randrw_",  "../mesures/q1/seq/rw_", "../mesures/q2/randrw_" , "../mesures/q3/randrw"  , "../mesures/q4/randrw_"]
listPath2 = ["../mesures2/q1/rand/randrw_",  "../mesures2/q1/seq/rw_", "../mesures2/q2/randrw_" , "../mesures2/q3/randrw"  , "../mesures2/q4/randrw_"]
listeQ1 = [ "0.0", "12.5" , "25.0", "37.5", "50.0" , "62.5", "75.0", "87.5","100.0"]
listeQ2 = [str(i) for i in range(10,21)]
listeQ3 = [""]
listeQ4 = ["1","2","4","6","8"]

listes = [listeQ1, listeQ1, listeQ2, listeQ3, listeQ4]

# bw_read_randrw = (bw_read_randrw - np.min(bw_read_randrw)) / (np.max(bw_read_randrw) - np.min(bw_read_randrw))
# bw_read_rw = (bw_read_rw - np.min(bw_read_rw)) / (np.max(bw_read_rw) - np.min(bw_read_rw))
# bw_write_randrw = (bw_write_randrw - np.min(bw_write_randrw)) / (np.max(bw_write_randrw) - np.min(bw_write_randrw))
# bw_write_rw = (bw_write_rw - np.min(bw_write_rw)) / (np.max(bw_write_rw) - np.min(bw_write_rw))

def import_data():
	data = [ [] for i in range(len(listPath))]
	data2 = [ [] for i in range(len(listPath2))]
	i = 0

	for liste in listes:
		for L in liste:
			strPath = listPath[i] + L + ".json"
			strPath2 = listPath2[i] + L + ".json"
			with open(strPath, 'r' ) as file:    
				tmp = json.load(file)
				data[i].append( tmp)

			with open(strPath2, 'r' ) as file:    
				tmp = json.load(file)
				data2[i].append( tmp)
		
		i+=1
	
	return data, data2

def extract_rw_rand(data, index_q, tid, datatype):
	"""
	index_q\n
	0 => "../mesures/q1/rand/randrw_" \n
	1 => "../mesures/q1/seq/rw_" \n
	2 => "../mesures/q2/randrw_" \n
	3 => "../mesures/q3/randrw" \n
	4 = > "../mesures/q4/randrw_" \n
	"""

	read = np.array([])
	write = np.array([])

	for i in range (len(listes[index_q])):
		read = np.append(read, data[index_q][i]['jobs'][tid]['read'][datatype])
		write = np.append(write, data[index_q][i]['jobs'][tid]['write'][datatype])

	return read, write