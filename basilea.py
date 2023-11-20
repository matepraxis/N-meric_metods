import math
import matplotlib.pyplot as plt


n=100

def cal_aprox_piB(n):
    
    pi= 0

    for i in range(1,n+1):
        termino = 1/(i**2)
        pi += termino
    pi = 6*pi
    pi = math.sqrt(pi)

    return pi

list_Basi = []
list_Err_Basi = []

for i in range(1,n+1):
    
    aprox_piB = cal_aprox_piB(i)
    list_Basi.append(aprox_piB)

    Err_realB = math.pi - aprox_piB
    Err_absB = abs(Err_realB)
    Err_relativB = abs(Err_realB/math.pi)

    list_Err_Basi.append(Err_relativB)
    
    print("%d \t %f \t %f \t %f \t %.4f" % (i, aprox_piB, Err_realB, Err_absB, Err_relativB*100))

plt.figure("Grafica de la serie de Basilea")
plt.plot( [0,n], [math.pi, math.pi], "g-")
plt.plot(list_Basi, "bo-", label = "Serie de Basilea")
plt.xlabel("n")
plt.ylabel(u"$\pi$")
plt.grid(ls="dashed")
plt.legend()

plt.figure("Grafica del error")
plt.plot(list_Err_Basi, "ro-", label= "Serie de Basilea")
plt.xlabel("n")
plt.ylabel(u"$\pi$")
plt.grid(ls="dashed")
plt.legend()

plt.show()