#memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('----------------------- METODE LINEAR REGRESSION | Soal No.1 -------------------')

#mengolah/input data excel
df = pd.read_csv('Linear_Regression.csv')
print('Data =')
print(df.head(6))

#mendefinisikan nilai x dan y
X = df['x'].values
Y = df['y'].values

#menghitung rata-rata x dan y
x_mean = np.mean(X)
y_mean = np.mean(Y)

#jumlah data
n = len(df)

#Looping menghitung a0 dan a1
a = 0
b = 0

for i in range (n):
    a += (X[i]-x_mean)*(Y[i]-y_mean)
    b += (X[i]-x_mean)**2
    a1 = a/b
    a0 = y_mean - (a1*x_mean)

#Menghitung nilai RMSE
fx = a0 +a1*X
sfx=sum((fx-Y)**2)
MSE= 1/n*sfx

R_MSE = np.sqrt(MSE)

#menghitung nilai y, jika x = 1
x = 1 
hasil_x = a0 + a1*x

print()
print('The best value of a1 and a2 =')
print('a0 =', a0, 'a1 =', a1)
print()
print('The fucntion of Linear Regression')
print("y = %f + %fx"%(a0,a1))
print()
print('Finding root mean square error')
print('RMSE = %f'%(R_MSE))
print('if x=1, the result is =', hasil_x)

#---------------------------------------------------------------------------

#memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('----------------- METODE MULTIPLE REGRESSION | Soal No.2 ----------------------')

#mengolah/input data excel
df=pd.read_csv('Multiple_Regression.csv')
print('Data =')
print(df.head(10))

#mencari jumlah dari nilai x,y,z
sum_x = sum(df['X'])
sum_y = sum(df['Y'])
sum_z = sum(df['Z'])

#membuat list array hasil perhitungan dari looping
x_pow= []
y_pow= []
list_xy = []
list_xz = []
list_yz = []

#looping regresi multiple linear

n= len(df)
for i in range (n):
    x_2 = df['X'][i]**2
    y_2 = df['Y'][i]**2
    xy = df['X'][i]*df['Y'][i]
    xz = df['X'][i]*df['Z'][i]
    yz = df['Y'][i]*df['Z'][i]
    x_pow.append(x_2)
    y_pow.append(y_2)
    list_xy.append(xy)
    list_xz.append(xz)
    list_yz.append(yz)
    i+=1

#menyimpan data hasil looping ke dalam data frame
result = pd.DataFrame({'x2':x_pow,
                       'y2':y_pow,
                       'xy':list_xy,
                       'xz':list_xz,
                       'yz':list_yz})

#menghitung nilai sigma dari x^2,y^2,xy,xz,yz
sum_x2 = sum(result['x2'])
sum_y2 = sum(result['y2'])
sum_xy = sum(result['xy'])
sum_xz = sum(result['xz'])
sum_yz = sum(result['yz'])

#membuat matriks
A = np.array([[n, sum_x, sum_y], [sum_x, sum_x2, sum_xy], [sum_y, sum_xy, sum_y2]])
b = np.array([sum_z,sum_xz,sum_yz])

#mencari nilai invers dan nilai x (a0,a1,a2)
A_inv = np.linalg.inv(A)
x = np.dot(A_inv,b)

print()
print('The value of a0, a1, and a2')
print('a0 =', (round((x[0]))), 'a1 =',(round((x[1]))), 'a2 =', (round((x[2]))))
print()
print('The function of Multiple Regression')
print('z = %s + %s x + %s x^2'% (round((x[0])) ,round((x[1])) ,round((x[2]))))

#-----------------------------------------------------------------------------

#Memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('------------------- METODE NON LINEAR REGRESSION | Soal No.3 -------------------')

#mengolah/input data excel
df = pd.read_csv('NonLinear_Regression.csv')
print('Data =')
print(df.head(6))

#Permisalan x dan y menggunakan list comprehension
x = [round((1/df['x'][i]),3) for i in range(len(df['x']))]
y = [round((1/df['y'][i]),3) for i in range(len(df['y']))]

#mencari rata-rata x dan y
x_mean = np.mean(x)
y_mean = np.mean(y)

#menghitung sigma x dan sigma y
sum_x = sum(x)
sum_y = sum(y)

#menghitung xy, x^2, sigma_x^2
xy = [round((x[i]*y[i]),3) for i in range(len(x))]
x_pow = [round((x[i]**2),3) for i in range(len(x))]
sx_pow = sum_x**2

#mencari nilai a0 dan a1
n = len(df)
a1 = ((n*sum(xy))-(sum_x*sum_y))/((n*sum(x_pow))-sx_pow)
a0 = y_mean-(a1*x_mean)

print()
print('The function of Non Linear Regression')
print('z = a0 + a1x')
print('z = %f + %f x'%(a0,a1))

#------------------------------------------------------------------------------

#memasukkan modul yang akan digunakan
import numpy as np
import pandas as pd

print('--------------------- METODE POLYNOMIAL REGRESSION | Soal No.4 -----------------')

#mengolah/input data excel
df=pd.read_csv('Polynomial_Regression.csv')
print('Data =')
print(df.head(6))

#mencari jumlah dari nilai x,y
sum_x = sum(df['x'])
sum_y = sum(df['y'])

#membuat list array hasil perhitungan dari looping
x_pow= []
x3_pow= []
x4_pow = []
list_xy = []
list_x2y = []

#looping regresi polynomial
n= len(df)
for i in range (n):
    x_2 = df['x'][i]**2
    x_3 = df['x'][i]**3
    x_4 = df['x'][i]**4
    xy = df['x'][i]*df['y'][i]
    x2y = x_2*df['y'][i]
    x_pow.append(x_2)
    x3_pow.append(x_3)
    x4_pow.append(x_4)
    list_xy.append(xy)
    list_x2y.append(x2y)
    i+=1

#menyimpan data hasil looping ke dalam data frame
result = pd.DataFrame({'x^2':x_pow,
                       'x^3':x3_pow,
                       'x^4':x4_pow,
                       'xy':list_xy,
                       'x^2y':list_x2y})

#menghitung nilai sigma dari x^2, x^3,x^4, xy,x^y
sum_x2 = round(sum(result['x^2']),3)
sum_x3 = round(sum(result['x^3']),3)
sum_x4 = round(sum(result['x^4']),3)
sum_xy = round(sum(result['xy']),3)
sum_x2y = round(sum(result['x^2y']),3)

#membuat matriks menggunakan array
A = np.array([[n, sum_x, sum_x2], [sum_x, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4]])
b = np.array([sum_y,sum_xy,sum_x2y])

#mencari nilai invers
A_inv = np.linalg.inv(A)

#mencari nilai (a0,a1,a2)
x = np.dot(A_inv,b)

print()
print('The value of a0, a1, and a2')
print('a0 =', (round((x[0]))), 'a1 =',(round((x[1]))), 'a2 =', (round((x[2]))))
print()
print('The function of Polynomial Regression')
print('z = %s + %s x + %s x^2'% (round((x[0])) ,round((x[1])) ,round((x[2]))))

print('-------------------------------- FINISH --------------------------------------')

'''
Algoritma Linear, Multiple, Non Linear, dan Polynomial Regression =
1. Membuat file excel (.csv) untuk menyimpan data x,y,z
2. Memasukkan file csv ke dalam python menggunakan modul pandas
3. Looping perthiungan data yang dibutuhkan untuk matriks (x2,x3,x4y2,xy,xz,yz,dst.)
4. Menyimpan hasil perhitungan ke dalam dataframe
5. Melakukan perhitungan sigma dari data yang dibutuhkan
6. Membuat matriks
7. Mencari nilai invers
8. Mencari nilai a0,a1,a2
9. Selesai

(+) Penggunaan file excel agar memudahkan penginputan data, jika data yang dibutuhkan banyak.

'''
