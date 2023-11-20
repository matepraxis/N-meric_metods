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
list_euler = []
Err_list_euler = []

for i in range(1, n):
    aprox_pi = cal_aprox_pi(i)
    list_euler.append(aprox_pi)

    Err_real = math.pi - aprox_pi
    Err_abs = abs(Err_real)
    Err_relativ = abs(Err_real/math.pi)

    Err_list_euler.append(Err_relativ)
    print("%d \t %f \t %f \t %f \t %.4f " % (i, aprox_pi, Err_real, Err_abs,Err_relativ*100 ))

plt.figure("Serie de Euler")
plt.plot([0, n], [math.pi, math.pi], "g-")
plt.plot(list_euler , "bo-", label="Serie de Euler")
plt.xlabel("n")
plt.ylabel(u"$\pi$")
plt.grid(ls="dashed")
plt.legend()

plt.figure("Gráfica del Error")
plt.plot(Err_list_euler, "bo-", label=" Serie de Euler")
plt.xlabel("n")
plt.ylabel(u"$\% error$")
plt.grid(ls="dashed")
plt.legend()

plt.show()









