#-------------------- METODE JACOBI----------------------
print("------------ METODE ITERASI JACOBI -----------")

import numpy as np

#mendefinisikan persamaan/fungsi
#mencari setiap nilai a,b, dan c
#menggunakan round untuk memberikan hasil pembulatan

def find_x1(a, b, x2=None, x3=None, iter=0):

	a1 = round((b[0]/a[0][0]),3)
	a2 = round((-a[0][1]/a[0][0]),3)
	a3 = round((-a[0][2]/a[0][0]),3)

	x1 = a1 + (a2*x2) + (a3*x3)

	iter+=1

	return list_x1.append(x1), iter

def find_x2(a, b, x1=None, x3=None, iter=0):

	b1 = round((-a[1][0]/a[1][1]),3)
	b2 = round((b[1]/a[1][1]),3)
	b3 = round((-a[1][2]/a[1][1]),3)

	x2 = b2 + (b1*x1) + (b3*x3)

	iter+=1

	return list_x2.append(x2), iter

def find_x3(a, b, x1=None, x2=None, iter=0):

	c1 = round((-a[2][0]/a[2][2]),3)
	c2 = round((-a[2][1]/a[2][2]),3)
	c3 = round((b[2]/a[2][2]),3)

	x3 = c3 + (c1*x1) + (c2*x2)

	iter=i
	return list_x3.append(x3), iter

def app_error(x) :
	
	x_new = x[len(x)-1]
	x_prev = x[len(x)-2]

	rel_app_err= np.abs(((x_new-x_prev)/x_new)*100)

	return rel_app_err

#menyimpan hasil perhitungan atau  rumus ke dalam list
list_x1 = [0]
list_x2 = [0]
list_x3 = [0]
error_list= [0]

#masukkan matriks a,b, iterasi
a = [[2, -1, 7], [-3, 9, 1], [5, -2, -3]]
b = [3, 2, -1]
n = 10
#looping metode iterasi jacobi
for i in range(0,n):
	#mencari nilai x1,x2,x3
	x1=list_x1[len(list_x1)-1]
	x2=list_x2[len(list_x2)-1]
	x3=list_x3[len(list_x3)-1]

	#mencari nilai (x1,x2,x3) pada setiap persamaan
	iter = i+1
	find_x1(a, b, x2=x2, x3=x3)
	find_x2(a, b, x1=x2, x3=x3)
	find_x3(a, b, x1=x1, x2=x2)

	#mencari nilai relatife approximate error
	EA1= app_error(list_x1)
	EA2= app_error(list_x2)
	EA3= app_error(list_x3)

	error_list.append([[EA1],[EA2],[EA3]])

	#membuat colom/tabel hasil dari perhitungan
	array = np.column_stack([list_x1,list_x2,list_x3])
	
	#mencetak jumlah iterasi
	print('Iterasi ke %s '%i)
	i+=1

print()
print(array)
print ()
print (error_list)
