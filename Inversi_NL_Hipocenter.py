import numpy as np
from numpy.linalg import inv
from matplotlib import cm
import matplotlib.pyplot as plt

# Mendefinisikan parameter yang diketahui
to=0         
v=4                 
x=np.array((20, 50, 40, 10))            
y=np.array((10, 25, 50, 40))
z=np.array((-1,-1,-1,-1))            
n=len(x)

# menghitung waktu tempuh t sebagai fungsi xyz dengan hiposenter (40,30,-20)
t_dat= np.ones((n))
for i in range (0,n):
    t_dat[i] = to+(1/v)*np.sqrt(((x[i]-40)**2+(y[i]-30)**2+(z[i]+20)**2))

# Menambahkan noise random dengan mean 0 dan standar deviasi 2 dan k=0.01
noise_tdat = np.random.normal(0,2,t_dat.shape)

for i in range (0,n):
    t_dat[i] = t_dat[i]+noise_tdat[i]*0.01


M0=np.array((10,20,-30))      # Initial Model


t_cal= np.ones((n))
J = np.ones((n,3))    
M=M0
l=1

while True:
    print('\n----------------------------------------------------')
    print('\nMelakukan iterasi',l,'\n')
    
    for j in range (0,n):
        
        # Melakukan perhitungan matriks jacobian dan t kalkulasi
        t = to+(1/v)*(np.sqrt((M0[0]-x[j])**2+(M0[1]-y[j])**2+(M0[2]-z[j])**2))
        dt_dx = ((M0[0]-x[j]))/(v*np.sqrt((M0[0]-x[j])**2+(M0[1]-y[j])**2+(M0[2]-z[j])**2))
        dt_dy = ((M0[1]-y[j]))/(v*np.sqrt((M0[0]-x[j])**2+(M0[1]-y[j])**2+(M0[2]-z[j])**2))
        dt_dz = ((M0[2]-z[j]))/(v*np.sqrt((M0[0]-x[j])**2+(M0[1]-y[j])**2+(M0[2]-z[j])**2))
    
        J[(j,0)] = dt_dx
        J[(j,1)] = dt_dy
        J[(j,2)] = dt_dz
        t_cal[j] = t
        
    print('Matriks jacobian:')
    print(J)

    # Estimasi lokasi epicenter baru
    dM = (inv((J.T).dot(J))).dot(J.T).dot(t_dat-t_cal)    
    M_new = M0 + dM
    print('\nPrediksi lokasi epicenter (Xo, Yo, Zo):')
    print(M_new)    
    
    # Mencegah nilai z baru bernilai positif / diatas msl
    if M_new[2] > 0:
        M_new = 0
    
    M=np.append(M,M_new, axis=0)
    
    # Membuat Kriteria pemberhentian estimasi berdasarkan error
    err_0 = abs(M0[0]-M_new[0])
    err_1 = abs(M0[1]-M_new[1])
    err_2 = abs(M0[2]-M_new[2])
    print('\nError yang didapatkan untuk masing-masing estimasi Xo, Yo dan Zo adalah',err_0,',',err_1, 'dan',err_2)

    if err_0< 0.05:     
        if err_1< 0.05:
            if err_2< 0.05:
                print('\n\nEstimasi telah memenuhi kriteria untuk pemberhentian iterasi!')
                break
    
    M0=M_new
    l=l+1
    
# Mengumpulkan hasil estimasi untuk setiap iterasi
m=int(len(M)/3)
M_plot=M.reshape(m,3)
print('\nBerikut adalah tabel estimasi lokasi hipocenter untuk tiap iterasi')
print(M_plot)

# Melakukan plot grafis
xplot=[]
yplot=[]
zplot=[]
for i in range (0,m):
    xplot.append(M_plot[(i,0)])
    yplot.append(M_plot[(i,1)])
    zplot.append(M_plot[(i,2)])    
    
fig = plt.figure(figsize = (10, 7))    
ax = plt.axes(projection='3d')

ax.scatter3D(xplot,yplot,zplot, s=30, c=xplot, cmap = cm.jet, label='Prediksi Hipocenter')

m=m-1
ax.scatter3D(xplot[m],yplot[m],zplot[m], s=125, marker='*', color='red', label='Lokasi Hipocenter')

ax.set_xlabel('X', fontweight ='bold')
ax.set_ylabel('Y', fontweight ='bold')
ax.set_zlabel('Z', fontweight ='bold')

print(" ")
plt.title('Plot Hipocenter', fontsize=20)

plt.legend(bbox_to_anchor=(1, 0.5), loc='upper left')
plt.tight_layout()

plt.show()


