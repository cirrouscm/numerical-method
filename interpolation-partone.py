
print('------------------------ UJIAN TENGAH SEMESTER PRAKTIK METODE NUMERIK ------------------------')
print('\nThe downward velocity of rain droplet which is observed by rocket given in this table:')

import numpy as np
import pandas as pd

df = pd.read_csv('data-interpolasi.csv') 
print(df.head(10))
print()
ref = int(input('Input t(s) =  ')) #menginput niali t yang akan dicari (reference)
#------------------------------------------ SOAL NOMOR 1 ------------------------------------------------

print('\n1. Find the value for downward velocity at t = 16s using Direct Method')
print('\na. For first order/linear,second,third, and fourth order polynomial\n')

class Interpolasi1:

	def index_range(self, data, ref): #mencari 2 titik terdekat, ref adalah data yang dibutuhkan
		low = min([i for i in data if i <= ref], #batas bawah
				key= lambda x:abs(x-ref))
		high = min([i for i in data if i >= ref], #batas atas
				key= lambda x:abs(x-ref))
		return (data.index(low), data.index(high))

	def gauss_elimination(self, A, b): #perhitungan menggunakan gaus elimination
		n = len(A)
		ab = np.column_stack((A, b))
		#looping eliminasi gauss, forward elimination
		for k in range(0, n-1):
			ab[k] = ab[k] / ab[k, k]
			for i in range(k+1, n):
				pivot = ab[k, k] / ab[i, k]
				ab[i] = ab[k] - pivot * ab[i]
		#backward substitusi untuk mencari nilai a0,a1,..,an
		for k in range(n-1, -1, -1):
			ab[k] = ab[k] / ab[k, k]
			for i in range(k-1, -1, -1):
				pivot2 = ab[k, k] / ab[i, k]
				ab[i] = ab[k] - pivot2 * ab[i]
		x = ab[:, n]
		return x

	def linear_order(self, file, ref, col1, col2): #ref : reference, col1 dan col2 merupakan tabel kolom excel
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))] 
		y = [data[col2][i] for i in range(len(data))] 
		range_idx = self.index_range(x, ref) #mencari 2 titik yang akan digunakan (2 titik terdekat)
		ma = np.array([ #matriks x
				[1, x[range_idx[0]]],
				[1, x[range_idx[1]]]
			])
		mb = np.array([ #matriks y
				y[range_idx[0]], 
				y[range_idx[1]]
			])
		a = self.gauss_elimination(ma, mb) #perhitungan menggunakan gauss eliminasi
		self.lin = round((a[0] + a[1]*ref),3) #perhitungan hasil linear order method
		print('Direct Linear Order Method= %.2f + %.2fx\nV(t)=%.2f mm/s'%(a[0], a[1], self.lin))

	def second_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))]
		y = [data[col2][i] for i in range(len(data))]
		range_idx = self.index_range(x, ref) #mencari 3 titk terdekat
		if x.index(x[range_idx[0]]) == 0:
			high = x[x.index(x[range_idx[1]])+1]
			borders = [x[range_idx[0]], x[range_idx[1]], high]
		else:
			low = x[x.index(x[range_idx[0]])-1]
			borders = [low, x[range_idx[0]], x[range_idx[1]]]
		ma = np.array([ #matriks x
				[1, borders[0], borders[0]**2],
				[1, borders[1], borders[1]**2],
				[1, borders[2], borders[2]**2]
			])
		mb = np.array([ #matriks y
				y[x.index(borders[0])],
				y[x.index(borders[1])],
				y[x.index(borders[2])]
			])
		a = self.gauss_elimination(ma, mb) #menghitung matriks dengan gauss eliminasi
		self.scd = round((a[0] + a[1]*ref + a[2]*pow(ref, 2)),3)
		print('Direct Second Order Method = %.2f + %.2fx + %.2fx^2\nVt = %.2f mm/s'%(a[0],a[1],a[2], self.scd))

	def third_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data
		x = [data[col1][i] for i in range(len(data))]
		y = [data[col2][i] for i in range(len(data))]
		range_idx = self.index_range(x, ref) #mencari 4 titik terdekat
		if x.index(x[range_idx[0]]) == 0 or x.index(x[range_idx[0]]) == 1:
			borders = x[:4]
		elif x.index(x[range_idx[0]]) == len(x)-1 or x.index(x[range_idx[0]])-2:
			borders = x[-4:]
		else: 
			high = x[x.index(x[range_idx[1]])+1]
			low = x[x.index(x[range_idx[0]])-1]
			borders = [low, x[range_idx[0]], x[range_idx[1]], high]
		ma = np.array([ #matriks x
				[1, borders[0], borders[0]**2, borders[0]**3],
				[1, borders[1], borders[1]**2, borders[1]**3],
				[1, borders[2], borders[2]**2, borders[2]**3],
				[1, borders[3], borders[3]**2, borders[3]**3],
			])
		mb = np.array([ #matriks y
				y[x.index(borders[0])],
				y[x.index(borders[1])],
				y[x.index(borders[2])],
				y[x.index(borders[3])]
			])
		a = self.gauss_elimination(ma, mb) #menghitung matriks dengan gauss eliminasi
		self.thd = round((a[0] + a[1]*ref + a[2]*pow(ref,2) + a[3]*pow(ref,3)),3)
		print('Direct Third Order Method = %.2f + %.2fx + %.2fx^2+ %.2fx^3\nVt = %.2f mm/s'%
			(a[0],a[1],a[2],a[3], self.thd))

	def fourth_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))]
		y = [data[col2][i] for i in range(len(data))]
		range_idx = self.index_range(x, ref) #mencari 5 titik terdekat
		if x.index(x[range_idx[0]]) == 0 or x.index(x[range_idx[0]]) == 1:
			borders = x[:5]
		elif x.index(x[range_idx[0]]) == len(x)-1 or x.index(x[range_idx[0]])-3:
			borders = x[-5:]
		else: 
			high = x[x.index(x[range_idx[1]])+1]
			low = x[x.index(x[range_idx[0]])-1]
			borders = [low, x[range_idx[0]], x[range_idx[1]], high]
		ma = np.array([ #matriks x
				[1, borders[0], borders[0]**2, borders[0]**3, borders[0]**4],
				[1, borders[1], borders[1]**2, borders[1]**3, borders[1]**4],
				[1, borders[2], borders[2]**2, borders[2]**3, borders[2]**4],
				[1, borders[3], borders[3]**2, borders[3]**3, borders[3]**4],
				[1, borders[4], borders[4]**2, borders[4]**3, borders[4]**4]
			])
		mb = np.array([ #matriks y
				y[x.index(borders[0])],
				y[x.index(borders[1])],
				y[x.index(borders[2])],
				y[x.index(borders[3])],
				y[x.index(borders[4])]
			])
		a = self.gauss_elimination(ma, mb) #menghitung matriks dengan gauss eliminasi
		self.fth = round((a[0] + a[1]*ref + a[2]*pow(ref,2) + a[3]*pow(ref,3) + a[4]*pow(ref,4)),3)
		print('Direct Fourth Order Method = %.2f + %.2fx + %.2fx^2 + %.2fx^3 + %.2fx^4\nVt = %.2f mm/s'%
			(a[0],a[1],a[2],a[3],a[4],self.fth))

	def error (self): #mencari relative approximate error
		error_scd = abs((self.scd-self.lin)/self.scd*100) #mencari ea dari second order 
		error_thd = abs((self.thd-self.scd)/self.thd*100) #mencari ea dari third order
		error_fth = abs((self.fth-self.thd)/self.fth*100) #mencari ea dari fourth order
		print('\nb.What are their absolute relative approximate errors?')
		print('Error Direct Second Order Method = %.5f'%(error_scd))
		print('Error Direct Third Order Method = %.5f'%(error_thd))
		print('Error Direct Fourth Order Method = %.5f'%(error_fth))


test1 = Interpolasi1() #untuk memanggil setiap fungsi yang ada dalam class
test1.linear_order('data-interpolasi.csv', ref, 't(s)', 'v(mm/s)')
test1.second_order('data-interpolasi.csv',ref, 't(s)', 'v(mm/s)')
test1.third_order('data-interpolasi.csv', ref, 't(s)', 'v(mm/s)')
test1.fourth_order('data-interpolasi.csv', ref,'t(s)', 'v(mm/s)')
test1.error()

#----------------------------------------- SOAL NOMOR 2 -------------------------------------------------

print('\n2. Find the value for downward velocity at t = 16s using Newton Method')
print('\na. For first order/linear,second,third, and fourth order polynomial')

class Interpolasi2():

	def index_range(self, data, ref): #untuk mencari range atau titik (x) pada setiap order
		low = min([i for i in data if i <= ref], #batas bawah
				key= lambda x:abs(x-ref))
		high = min([i for i in data if i >= ref], #batas atas
				key= lambda x:abs(x-ref))
		return (data.index(low), data.index(high))
	def newton (self,x,y): #perhitungan metode newton
		n = len(y) #banyak data y
		matriks = np.zeros([n,n]) #membuat matriks untuk menampung hasil perhitungan
		matriks[:,0] = y #kolom pertama adalah nilai y
		for i in range (1,n): #looping perhitungan interpolasi newton
			for j in range (n-i):
				matriks[j][i] = (matriks[j+1][i-1] - matriks[j][i-1])/(x[j+i]-x[j]) 
		return matriks[0]

	def linear_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import x dan y
		x = [data[col1][i] for i in range(len(data))] #nilai x
		y = [data[col2][i] for i in range(len(data))] #nilai y
		range_idx = self.index_range(x, ref) #mencari 2 titik terdekat dengan data referensi
		x = np.array([ #nilai x
				[x[range_idx[0]]],
				[x[range_idx[1]]]
			])
		y = np.array([ #nilai y
				y[range_idx[0]], 
				y[range_idx[1]]
			])
		a = self.newton(x, y) #perhitungan metode newton
		result_linear = (a[0] + a[1]*(ref-(x[0]))) #hasil perhitungan metode newton order linear
		print('\nNewton Linear Order Method = %2f mm/s'% (result_linear))

	def second_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))] #data x
		y = [data[col2][i] for i in range(len(data))] #data y
		range_idx = self.index_range(x, ref) #mencari 3 titik terdekat dengan data referensi
		if x.index(x[range_idx[0]]) == 0:
			high = x[x.index(x[range_idx[1]])+1]
			borders2 = [x[range_idx[0]], x[range_idx[1]], high]
		else:
			low = x[x.index(x[range_idx[0]])-1]
			borders2 = [low, x[range_idx[0]], x[range_idx[1]]] #borders berguna sebagai nilai x (titik)
		y = np.array([ #nilai y
				y[x.index(borders2[0])],
				y[x.index(borders2[1])],
				y[x.index(borders2[2])]
			])
		a = self.newton(borders2,y) #perhitungan menggunakan metode newton
		result_second = a[0] + a[1]*(ref-(borders2[0])) + a[2]*((ref-(borders2[0]))*(ref-(borders2[1])))
		print('Newton Second Order Method = %2f mm/s'% (result_second))

	def third_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))] #data x
		y = [data[col2][i] for i in range(len(data))] #data y
		range_idx = self.index_range(x, ref) #mencari 4 titik terdekat dengan data referensi
		if x.index(x[range_idx[0]]) == 0 or x.index(x[range_idx[0]]) == 1:
			borders3 = x[:4]
		elif x.index(x[range_idx[0]]) == len(x)-1 or x.index(x[range_idx[0]])-2:
			borders3 = x[-4:]
		else: 
			high = x[x.index(x[range_idx[1]])+1]
			low = x[x.index(x[range_idx[0]])-1]
			borders3 = [low, x[range_idx[0]], x[range_idx[1]], high] #borders berguna sebagai nilai x (titik)
		self.borders3 = borders3
		y = np.array([ #nilai y
				y[x.index(borders3[0])],
				y[x.index(borders3[1])],
				y[x.index(borders3[2])],
				y[x.index(borders3[3])]
			])
		self.a = self.newton(borders3, y) #perhitungan menggunakan metode newton
		a0 = self.a[0]
		a1 = self.a[1]*(ref-(borders3[0]))
		a2 = self.a[2]*((ref-(borders3[0]))*(ref-(borders3[1])))
		a3 = self.a[3]*((ref-(borders3[0]))*(ref-(borders3[1]))*(ref-(borders3[2])))
		result_third = a0 + a1 + a2 + a3 #hasil dari perhitungan metode newton order third
		print('Newton Third Order Method = %2f mm/s'% (result_third))

	def fourth_order(self, file, ref, col1, col2):
		data = pd.read_csv(file) #import data x dan y
		x = [data[col1][i] for i in range(len(data))] #data x
		y = [data[col2][i] for i in range(len(data))] #data y
		range_idx = self.index_range(x, ref) #mencari 5 titik terdekat dengan data referensi
		if x.index(x[range_idx[0]]) == 0 or x.index(x[range_idx[0]]) == 1:
			borders4 = x[:5]
		elif x.index(x[range_idx[0]]) == len(x)-1 or x.index(x[range_idx[0]])-3:
			borders4 = x[-5:]
		else: 
			high = x[x.index(x[range_idx[1]])+1]
			low = x[x.index(x[range_idx[0]])-1]
			borders4 = [low, x[range_idx[0]], x[range_idx[1]], high] #borders berguna sebagai nilai x (titik)
		y = np.array([
				y[x.index(borders4[0])],
				y[x.index(borders4[1])],
				y[x.index(borders4[2])],
				y[x.index(borders4[3])],
				y[x.index(borders4[4])]
			])
		a = self.newton(borders4,y) #perhitungan menggunakan metode newton
		a0_a1 = a[0] + a[1]*(ref-(borders4[0])) 
		a2 = a[2]*((ref-(borders4[0]))*(ref-(borders4[1])))
		a3 = a[3]*((ref-(borders4[0]))*(ref-(borders4[1]))*(ref-(borders4[2])))
		a4 = a[4]*((ref-(borders4[0]))*(ref-(borders4[1]))*(ref-(borders4[2]))*(ref-(borders4[3])))
		result_fourth = a0_a1 + a2 + a3 + a4 #hasil perthitungan metode newton order fourth
		print('Newton Fourth Order Method = %2f mm/s'% (result_fourth))

	def deriv_integ (self): #menghitung integral dan turunan dari order third 
		x = self.borders3 #Nilai x0,x1,x2
		a0 = int(self.a[0]) #mendefinisikan hasil perhitungan newton a0
		a1 = int(self.a[1]) #mendefinisikan hasil perhitungan newton a1
		a2 = int(self.a[2]) #mendefinisikan hasil perhitungan newton a2
		a3 = int(self.a[3]) #mendefinisikan hasil perhitungan newton a3
		p1 = np.poly1d([x[0]],True) #mendefinisikan (x-x0)
		p2 = np.poly1d([x[0],x[1]],True) #mendefinisikan (x-x0)(x-x1)
		p3 = np.poly1d([x[0],x[1],x[2]],True) #mendefinisikan (x-x0)(x-x1)(x-x2)

		p = a0 + a1*p1 + a2*p2 + a3*p3 #persamaan order third
		intg = p.integ() #pengintegralan
		distance = (intg(16))-(intg(11)) #mencari selisih jarak dari v16 dan v11
		diff = p.deriv() #penurunan
		diff_16 = diff(16) #mencari percepatan dari v16

		print('\nb. Use the third order of Newton method to find the distance of droplet observed by rocket at t=11s and t=16s')
		print('The answer is = %s mm'% distance)
		print('\nc. What is droplet acceleration at t = 16s?')
		print('The answer is = %s mm/s^2'% diff_16)

test2 = Interpolasi2() #untuk memanggil setiap fungsi yang ada dalam class
test2.linear_order('data-interpolasi.csv', ref, 't(s)', 'v(mm/s)')
test2.second_order('data-interpolasi.csv',ref, 't(s)', 'v(mm/s)')
test2.third_order('data-interpolasi.csv', ref, 't(s)', 'v(mm/s)')
test2.fourth_order('data-interpolasi.csv', ref,'t(s)', 'v(mm/s)')
test2.deriv_integ()

print('\nFinished.')
