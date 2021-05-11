#----------------------------METODE SEIDEL-----------------------------

print("--------------------- ITERASI SEIDEL ---------------------------")

def seidel(a, x ,b): 
#Menentukan panjang dari matrik	 
	n = len(a)
	k = 0				 
	# Looping itu mencari x1,x2,x3
	for i in range(0, n):		  
		d = b[i]				 
		
	# untuk menghitung persamaan x1,x2,x3
		for j in range(0, n):
			if(i != j):
				d-=a[i][j] * x[j]
		# untuk mencari x baru
		x[i] = round(d / a[i][i],4)

		k=+1
		rae = np.abs((x[i]-x[i-1])/(x[i])*100/100)
		print('Relative Approximate Error =',rae)
		
	return x

#------------- input matrik ------------				 
n = 3							
x = [0, 0, 0] #tebakan pertama						 
a = [[5,-2,3],[-3,9,1],[2,-1,-7]] #matriks dari persamaan/fungsi
b = [-1,2,3] #matriks dari hasil masing-masing persamaan/fungsi
iterasi = 6
print('x0 =',x) 

#looping untuk mencari iterasi 
for k in range (0, iterasi+1):			 
	find = seidel(a, x, b)
	print ('Iterasi ke-',k , '|', find)
	print()
	k+=1
