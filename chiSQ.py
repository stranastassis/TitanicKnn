from numpy import *

def chiSQ(x, y):
	cl = unique(y)
	rows = x.shape[0]
	dim = x.shape[1]
	valCHI = zeros(dim)
	
	for d in range(dim):
		feature = x[:,d]
		vals = unique(feature)
		total = 0
		for i in range(len(vals)):
			samples_val_i = where(feature==vals[i])[0]
			for j in range(len(cl)):
				ytmp = y[samples_val_i]
				Oij = len(where(ytmp==cl[j])[0])
				samples_cl_j = where(y==cl[j])[0]
				Eij = float(len(samples_val_i)*len(samples_cl_j))/rows
				total = total + pow((Oij-Eij),2)/Eij

		valCHI[d] = total

	chisq = valCHI	
	
	return chisq
