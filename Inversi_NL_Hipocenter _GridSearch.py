import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy import interpolate

# Mendefinisikan parameter yang diketahui
to=0         
v=4                
x=np.array((20, 50, 40, 10))            
y=np.array((10, 25, 50, 40))
z=np.array((1,2,2,1))             
n=len(x)


# Mendefinisikan grid untuk nilai error
grid_x = []
grid_y = []
grid_z = []

for i in range (0,61,2):
    grid_x.append(i)
    grid_y.append(i)
    grid_z.append(i)

grid_x=np.array(grid_x)
grid_y=np.array(grid_y)
grid_z=np.array(grid_z)
g=len(grid_x)

t_cal = np.ones((n))


# PLOT BIDANG YZ (X=40)        
E = np.zeros((g,g))
        
# menghitung waktu tempuh t sebagai fungsi yz dengan hiposenter (40,30,20)
t_dat= np.ones((n))
for i in range (0,n):
    t_dat[i] = to+(1/v)*np.sqrt(((y[i]-30)**2+(z[i]-20)**2))

# Menambahkan noise random dengan mean 0, standar deviasi 2, dan x=0.01 
noise = np.random.normal(0,2,t_dat.shape)

for i in range (0,n):
    t_dat[i] = t_dat[i]+noise[i]*0.01
        
# Menghitung nilai error untuk setiap grid
for i in range (0,g):
    for j in range (0,g):
        for k in range (0,n):
            t_cal[k] = (np.sqrt(+(y[k]-grid_y[i])**2+(z[k]-grid_z[j])**2))/v
            E[(i,j)] = E[(i,j)] + np.sqrt(((t_cal[k]-t_dat[k])**2)/n)
                
    
# Melakukan plot grafis 
X, Y = np.mgrid[0:60:31j, 0:60:31j]        
pl.subplots(figsize=(8, 4))
rbf = interpolate.Rbf(X.ravel(), Y.ravel(), E.ravel(), smooth=0.000001)

X2, Y2 = np.mgrid[0:60:60j, 0:60:60j]
c3 = pl.contourf(X2, Y2, rbf(X2, Y2),35, cmap='coolwarm')
    
cbar = pl.colorbar(c3)       
cbar.set_label('Error (s)', rotation=270, labelpad=15, y=0.5)
                
plt.plot(y,z,'vk', markersize=10, label='Stasiun')
for i in range (n):
            plt.text(y[i]-1.5,z[i]+5,'St'+ str(i+1))
        
plt.plot(30,20,'*r', markersize=10, label='Error Minimum Global \n(Hipocenter)')

plt.xlabel('Northing (Y)')       
plt.ylabel('Depth (Z)')
plt.title('Plot Slice X=40 (Y-Z)', fontsize=20)
        
plt.legend(bbox_to_anchor=(1.2, 0.35), loc='upper left')
plt.tight_layout()
        
plt.axis([0,60,60,0])
        
        
# PLOT BIDANG XZ (Y=30)
       
E = np.zeros((g,g)) 

# menghitung waktu tempuh t sebagai fungsi xz dengan hiposenter (40,30,20)
t_dat= np.ones((n))
for i in range (0,n):
    t_dat[i] = to+(1/v)*np.sqrt(((x[i]-40)**2+(z[i]-20)**2))

# Menambahkan noise random dengan mean 0, standar deviasi 2, dan x=0.01 
noise = np.random.normal(0,2,t_dat.shape)

for i in range (0,n):
    t_dat[i] = t_dat[i]+noise[i]*0.01

# Menghitung nilai error untuk setiap grid
for i in range (0,g):
    for j in range (0,g):
        for k in range (0,n):
            t_cal[k] = (np.sqrt((x[k]-grid_x[i])**2+(z[k]-grid_z[j])**2))/v
            E[(i,j)] = E[(i,j)] + np.sqrt(((t_cal[k]-t_dat[k])**2)/n)
                
                
# Melakukan plot grafis 
X, Y = np.mgrid[0:60:31j, 0:60:31j]
fig = pl.subplots(figsize=(8, 4))
rbf = interpolate.Rbf(X.ravel(), Y.ravel(), E.ravel(), smooth=0.000001)

X2, Y2 = np.mgrid[0:60:60j, 0:60:60j]
c3 = pl.contourf(X2, Y2, rbf(X2, Y2),35, cmap='coolwarm')

cbar = pl.colorbar(c3)       
cbar.set_label('Error (s)', rotation=270, labelpad=15, y=0.5)

plt.plot(x,z,'vk', markersize=10, label='Stasiun')
for i in range (n):
    plt.text(x[i]-1.5,z[i]+5,'St'+ str(i+1))
                    
plt.xlabel('Easting (X)')       
plt.ylabel('Depth (Z)')
plt.title('Plot Slice Y=30 (X-Z)', fontsize=20)
                    
plt.plot(40,20,'*r', markersize=10, label='Error Minimum Global \n(Hipocenter)')
                
plt.legend(bbox_to_anchor=(1.2, 0.15), loc='upper left')
plt.tight_layout()

plt.axis([0,60,60,0])
    

# PLOT BIDANG XY (Z=20)
E = np.zeros((g,g))

# menghitung waktu tempuh t sebagai fungsi yz dengan hiposenter (40,30,-20)
t_dat= np.ones((n))
for i in range (0,n):
    t_dat[i] = to+(1/v)*np.sqrt(((x[i]-40)**2+(y[i]-30)**2))

# Menambahkan noise random dengan mean 0, standar deviasi 2, dan x=0.01 
noise = np.random.normal(0,2,t_dat.shape)

for i in range (0,n):
    t_dat[i] = t_dat[i]+noise[i]*0.01
   
# Menghitung nilai error untuk setiap grid
for i in range (0,g):
    for j in range (0,g):
        for k in range (0,n):
            t_cal[k] = (np.sqrt((x[k]-grid_x[i])**2+(y[k]-grid_y[j])**2))/v
            E[(i,j)] = E[(i,j)] + np.sqrt(((t_cal[k]-t_dat[k])**2)/n)
        

# Melakukan plot grafis 
X, Y = np.mgrid[0:60:31j, 0:60:31j]
fig = pl.subplots(figsize=(8, 4))
rbf = interpolate.Rbf(X.ravel(), Y.ravel(), E.ravel(), smooth=0.000001)

X2, Y2 = np.mgrid[0:60:60j, 0:60:60j]
c3 = pl.contourf(X2, Y2, rbf(X2, Y2),30, cmap='coolwarm')

cbar = pl.colorbar(c3)       
cbar.set_label('Error (s)', rotation=270, labelpad=15, y=0.5)

plt.plot(x,y,'vk', markersize=10, label='Stasiun')
for i in range (n):
    plt.text(x[i]-1.5,y[i]+4,'St'+ str(i+1))

plt.xlabel('Easting (X)')       
plt.ylabel('Northing (Y)')
plt.title('Plot Slice Z=20 (X-Y)', fontsize=20)

# Lakukan input secara manual
plt.plot(40,30,'*r', markersize=10, label='Error Minimum Global \n(Hipocenter)')

plt.legend(bbox_to_anchor=(1.2, 0.15), loc='upper left')
plt.tight_layout()

plt.show()
    
    
        
