def generate_clusters(data,columns,number,column):
	kmeans_data=data[columns]
	X=np.array(kmeans_data)
	kmeans=KMeans(n_clusters=number).fit(X)
	data[column]=kmeans.labels_
	return data

