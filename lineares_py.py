import math
import numpy as np
import matplotlib.pyplot as plt


t = [0.167, 0.2, 0.234, 0.267, 0.3, 0.334, 0.367, 0.4, 0.434]
x = [21.8, 20.7, 19.4, 18.3, 17.2, 16.0, 14.7, 13.6, 12.4 ]
theta = [151, 144, 138, 131, 124, 118, 112, 105, 99]


fig, ax = plt.subplots()
ax.scatter(t, x, color="red", label=u"Posição" )
ax.set_xlabel('tempo [s]')
ax.set_ylabel(u'posição [cm]')
plt.title(u'Posição da fita vermelha')
plt.legend()


fig, ax2 = plt.subplots()
ax2.scatter(t, theta, color="gray", label=u"Ângulo" )
ax2.set_xlabel('tempo [s]')
ax2.set_ylabel(u'Angulo [⁰]')
plt.title(u'Ângulo do marcador amarelo')
plt.legend()

plt.show()

ti = 1
v = []
omega = []
t_med = []
C = []
soma_C = 0
print ("t[ti-1]         v[ti-1]        omega[ti-1]        C[ti-1]" )
while (ti < len(t)-1):
    v_inst = (x[ti+1]-x[ti-1])/(t[ti+1]-t[ti-1])
    v.append(v_inst)
    omega_inst = (theta[ti+1]-theta[ti-1])/(t[ti+1]-t[ti-1])*math.pi/180.
    omega.append(omega_inst)
    t_med.append((t[ti+1]+t[ti-1])/2)
    C_inst = v_inst/omega_inst
    C.append(C_inst)
    soma_C+=C_inst
    print (t_med[ti-1], v[ti-1], omega[ti-1], C[ti-1])
    ti+=1
print ("C_médio = " + str(soma_C/len(C)))