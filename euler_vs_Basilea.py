import math
import matplotlib.pyplot as plt


n= 100
def cal_aprox_pi(n):

    pi= 0

    for i in range(n):
        numerador = (2**i)*(math.factorial(i)**2)
        denomidador = math.factorial(2*i+1)
        fraction = numerador/denomidador

        pi += fraction
    pi = 2*pi

    return pi


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
list_euler = []
Err_list_euler = []

for i in range(1, n+1):

    aprox_piB = cal_aprox_piB(i)
    list_Basi.append(aprox_piB)

    aprox_pi = cal_aprox_pi(i)
    list_euler.append(aprox_pi)


    Err_realB = math.pi - aprox_piB
    Err_absB = abs(Err_realB)
    Err_relativB = abs(Err_realB/math.pi)


    Err_real = math.pi - aprox_pi
    Err_abs = abs(Err_real)
    Err_relativ = abs(Err_real/math.pi)


    Err_list_euler.append(Err_relativ)
    list_Err_Basi.append(Err_relativB)


    print("%d \t %f \t %f \t %f \t %f \t %.4f \t %.4f " % (i, aprox_pi, aprox_piB,  Err_real, Err_abs,Err_relativ*100, Err_relativB*100 ))










plt.figure("Serie de Euler vs Basilea")
plt.plot([0, n], [math.pi, math.pi], "g-")
plt.plot(list_euler , "bo-", label="Serie de Euler")
plt.plot(list_Basi, "ro-", label = "Serie de Basilea")
plt.xlabel("n")
plt.ylabel(u"$\pi$")
plt.grid(ls="dashed")
plt.legend()

plt.figure("Gráfica del Error Serie de Euler vs Basilea")
plt.plot(Err_list_euler, "bo-", label=" Serie de Euler")
plt.plot(list_Err_Basi, "ro-", label = "Serie de Basilea")
plt.xlabel("n")
plt.ylabel(u"$\% error$")
plt.grid(ls="dashed")
plt.legend()

plt.show()
