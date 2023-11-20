5# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:46:31 2023

@author: amaru
"""
import math
import matplotlib.pyplot as plt


# Cantidad de iteraciones definidas por el usuario 


n = int(input("Ingrese un número de iteraciones para calcular Pi \n  con la fórmula de Nilakantha y Ramanujan " ))



# Serie de Nilakantha

def calcular_pi_aproximacion(n):
    pi = 3.0  # Comenzamos con el valor inicial de 3 
    
    for i in range(1, n + 1):
        denominador_nk = (2 * i) * (2 * i + 1) * (2 * i + 2)
        termino = 4 / denominador_nk
        
        if i % 2 == 0:
            pi -= termino
        else:
            pi += termino
    
    return pi



 #Serie de Ramanujan

k = (2 * math.sqrt(2)) / 9801
 
def calcular_pi_ramanujan(n):
    pi = 0.0
    
    for i in range(n):
        
        numerador = math.factorial(4*i) * (26390*i + 1103)
        denominador_r = (math.factorial(i) ** 4) * (396 ** (4*i))
        termino = numerador / denominador_r
        
        pi += termino

    pi = 1/(k*pi)
    
    return pi




#Calculo del error 

list_aprox_pi_r= []
list_aprox_pi_nk = []

Err_list_nk= []
Err_list_r = []

for i in range(1,n+1):
    
    
    aprox_pi_nk = calcular_pi_aproximacion(i)
    aprox_pi_r = calcular_pi_ramanujan(i)
    
    list_aprox_pi_nk.append(aprox_pi_nk)
    list_aprox_pi_r.append(aprox_pi_r)
   
    Err_real_nk = math.pi - aprox_pi_nk
    Err_abs_nk = abs(Err_real_nk)
    Err_relativ_nk = abs(Err_real_nk/math.pi)

    Err_real_r = math.pi - aprox_pi_r
    Err_abs_r = abs(Err_real_r)
    Err_relativ_r = abs(Err_real_r/math.pi)
    
    Err_list_nk.append(Err_relativ_nk)
    Err_list_r.append(Err_relativ_r)
    
    print("%d \t %f \t %.12f \t %f \t %f \t %f \t %f \t %f \t %f\t %.4f \t %.12f" % (i, aprox_pi_nk, aprox_pi_r, Err_real_nk, Err_real_r, Err_abs_nk, Err_abs_r, Err_relativ_nk, Err_relativ_r, Err_relativ_nk*100, Err_relativ_r*100))




#Graficas 

plt.figure("Gráfica de las Series")
plt.plot([0, n], [math.pi, math.pi], "g-")
plt.plot(list_aprox_pi_nk , "bo-", label="Serie Nilakantha")
plt.plot(list_aprox_pi_r , "ro-",  label="Serie Ramanujan")
plt.xlabel("n")
plt.ylabel(u"$\pi$")
plt.grid(ls="dashed")
plt.legend()

plt.figure("Gráfica del Error")
plt.plot(Err_list_nk, "bo-", label=" Serie Nilakantha")
plt.plot( Err_list_r, "ro-",  label="Serie Ramanujan")
plt.xlabel("n")
plt.ylabel(u"$\% error$")
plt.grid(ls="dashed")
plt.legend()

plt.show()









