import math
import numpy as np
import statistics 
from statistics import mean

#the input DOS may have energy values past the Fermi energy so this sets the Fermi energy as the upper bound
F_text = input ("Fermi energy (units are defined by input file):")                          
F = float(F_text)

#input DOS to be read
file = input ("File of DOS:")
a, b = np.genfromtxt(file, delimiter=None, unpack=True, usecols=[0, 1]) 

M = len(a)
under = []

#select energy values under Fermi energy
for j in range(0,M-1):
    if a[j] < F:  
        under.append(a[j])  

#integrate DOS under Fermi energy through trapezoid method
N = len(under)                                                                 
area_under = []
area = []
Earea_u = []
width = []
for i in range(0,N):
    trap_u = ((b[i] + b[i+1])/2)*(0.01)
    area_under.append(trap_u)     
A_u = sum(area_under)                                                               

#integrate DOS through trapezoid method
for n in range(0,M-1):
    trap = ((b[n] + b[n+1])/2)*(0.01)
    area.append(trap)
A = sum(area)

#integrate DOS * E under Fermi energy through trapezoid method
for k in range(0,N):
    trapE = (( (a[k]*b[k]) + (a[k+1]*b[k+1])) /2)*(0.01)
    Earea_u.append(trapE)
EA_u = sum(Earea_u)

#calculate d-band centrioid
E_d = EA_u / A_u
print("e_f:", round(F,2))
print("E_d:", round(E_d,2))

#calculate d-band center
e_d = E_d - F
print("e_d:", round(e_d,2))

#calculate d-band width
for m in range(0,M-1):
    trapW = (((((a[m] - E_d)**2)*b[m]) + (((a[m+1] - E_d)**2)*b[m+1]))/2)*(0.01)
    width.append(trapW)
W = sum(width)
dbw = math.sqrt((W / A))
print("e_w:", round(dbw,2))


