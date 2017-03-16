import numpy as np

def generate_clusters(data,columns,number,column):
	""" Takes a dataframe and generates clusters based on a
		user input subset of columns.

		Parameters
		----------
		data: DataFrame with data
		columns: subset of columns to use for clustering
		number: number of clusters
		column: new column to be added to dataframe with cluster assignment

		Returns
		-------
		Updated dataframe with column with cluster assignment
	"""

	kmeans_data = data[columns]
	X = np.array(kmeans_data)
	kmeans = KMeans(n_clusters=number).fit(X)
	data[column] = kmeans.labels_
	return data
