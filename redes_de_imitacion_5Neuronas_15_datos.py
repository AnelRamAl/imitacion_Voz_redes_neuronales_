import random
import numpy as np

# declarando variables; pesos 
w0 = 0
w1 = 0
w2 = 0
w3 = 0

v0 = 0
v1 = 0
v2 = 0
v3 = 0

y0 = 0
y1 = 0
y2 = 0
y3 = 0

l0 = 0
l1 = 0
l2 = 0
l3 = 0

m0 = 0
m1 = 0
m2 = 0
m3 = 0

w0 = 0
w1 = 0
w2 = 0
w3 = 0

v0 = 0
v1 = 0
v2 = 0
v3 = 0

y0 = 0
y1 = 0
y2 = 0
y3 = 0

l0 = 0
l1 = 0
l2 = 0
l3 = 0

m0 = 0
m1 = 0
m2 = 0
m3 = 0

i = 0
#LA LONGITUD DE LAS CADENAS DEBE SER IGALES, igualmente en el for por pasos de 5 hasta la lungitud-5 de la cadena total
#cadena de datos de entrada ---"Xi"--- a la red neuronal -AUDIO IMITADOR-
#X_imitador = [0.2, 0.4, 0.5, 0.9, 0.7, 0.2, 0.5, 0.6, 0.8, 0.9, 0.2, 0.5, 0.7, 0.3, 0.1]
X_imitador = [-0.02896,-0.02921,-0.03030,-0.02994,-0.02698,-0.02295,-0.02020,-0.01877,-0.01669,-0.01263,-0.00793,-0.00479,-0.00336,-0.00143,0.00232];


auxiliar = 0;

for i in range(15):

    if  X_imitador[i] < 0:
        auxiliar = abs(X_imitador[i]);
        X_imitador[i] = auxiliar;

print("X_imitador POSITIVO", X_imitador)

#cadena de datos de salida deseada ---"SDi"--- a la red neuronal -AUDIO A IMITAR-
#SDi_a_imitar = [0.4, 0.5, 0.55, 0, 0, 0.4, 0.3, 0.7, 0.1, 0.9, 0.4, 0.1, 0.2, 0.1, 0.3]
SDi_a_imitar = [-0.28577,-0.27557,-0.27344,-0.26559,-0.23425,-0.18600,-0.14560,-0.12164,-0.09650,-0.05569,-0.00946,0.02612,0.05563,0.09515,0.14285];

auxiliar = 0;
array_negativos_SDi = [];

for i in range(15):

    if  SDi_a_imitar[i] < 0:
        auxiliar = abs(SDi_a_imitar[i]);
        SDi_a_imitar[i] = auxiliar;
        array_negativos_SDi.append(-1);

    else:
        array_negativos_SDi.append(1);

print("SDi_a_imitar POSITIVO", SDi_a_imitar)


# definiendo la cadena de w´s de cada dato

w_imitador = []
v_imitador = []
y_imitador = []
l_imitador = []
m_imitador = []

S_imitacion = []

# aquí inicia el recorrido del procesamieto de 5 datos

longitud_data = len(X_imitador)


for i in [0,5,10]:


    # TABLA DE DATOS DE ENTRADA A LA RED NEURONAL
    x1 = X_imitador[i]
    x2 = X_imitador[i+1]
    x3 = X_imitador[i+2]
    x4 = X_imitador[i+3]
    x5 = X_imitador[i+4]

    # TABLA DE DATOS DE "SALIDA DESEADA" DE LA RED NEURONAL
    SD1 = SDi_a_imitar[i]
    SD2 = SDi_a_imitar[i+1]
    SD3 = SDi_a_imitar[i+2]
    SD4 = SDi_a_imitar[i+3]
    SD5 = SDi_a_imitar[i+4]

    delta1 = 0
    delta2 = 0
    delta3 = 0
    delta4 = 0
    delta5 = 0


    NumDeIteracion = 0
    bandera_deltaDeError = 0
    bandera_NumDeIteracion = 0

    # PASO 0: Asignación de valores aleatorios
    pasos = 0.1
    start = -5   # tomar en cuenta que toma el intervalo como: [start,end)
    end = 5.1

    x = 1/pasos
    inicio = start*x
    fin = end*x

    w0 = random.randrange(inicio, fin, 1) #calculara para [-10, 11) en pasos de 1
    w1 = random.randrange(inicio, fin, 1)
    w2 = random.randrange(inicio, fin, 1)
    w3 = random.randrange(inicio, fin, 1)

    v0 = random.randrange(inicio, fin, 1) #calculara para [-10, 11) en pasos de 1
    v1 = random.randrange(inicio, fin, 1)
    v2 = random.randrange(inicio, fin, 1)
    v3 = random.randrange(inicio, fin, 1)

    y0 = random.randrange(inicio, fin, 1) #calculara para [-10, 11) en pasos de 1
    y1 = random.randrange(inicio, fin, 1)
    y2 = random.randrange(inicio, fin, 1)
    y3 = random.randrange(inicio, fin, 1)

    l0 = random.randrange(inicio, fin, 1) #calculara para [-10, 11) en pasos de 1
    l1 = random.randrange(inicio, fin, 1)
    l2 = random.randrange(inicio, fin, 1)
    l3 = random.randrange(inicio, fin, 1)

    m0 = random.randrange(inicio, fin, 1) #calculara para [-10, 11) en pasos de 1
    m1 = random.randrange(inicio, fin, 1)
    m2 = random.randrange(inicio, fin, 1)
    m3 = random.randrange(inicio, fin, 1)

    bandera_deltaDeError = 0

    ParoTotal = 1  # en función de que cumpla las condiciones de Paro 

    def sumaPonderada(f1,f2,f3,w1,w2,w3,w0):
        fE= f1*w1 + f2*w2 + f3*w3 + w0
        return fE

    xs1 = sumaPonderada(x1,x2,x5,w1,w2,w3,w0)  # x de f(x)
    print("xs1")
    print(xs1)

    def funcionDeActivacion(s1):
        S = 1 / (1+(2.7182818284590452353602874713527)**(-s1))
        return S

    while ParoTotal == 1 :

        if NumDeIteracion >= 1:
            # Paso 3: Actualizando valores de los pesos 
            w0 = w0 + delta1
            w1 = w1 + delta1*x1 
            w2 = w2 + delta1*x2
            w3 = w3 + delta1*x5

            v0 = v0 + delta2
            v1 = v1 + delta2*x1
            v2 = v2 + delta2*x2
            v3 = v3 + delta2*x3

            y0 = y0 + delta3
            y1 = y1 + delta3*x2
            y2 = y2 + delta3*x3
            y3 = y3 + delta3*x4

            l0 = l0 + delta4
            l1 = l1 + delta4*x3
            l2 = l2 + delta4*x4
            l3 = l3 + delta4*x5

            m0 = m0 + delta5
            m1 = m1 + delta5*x1
            m2 = m2 + delta5*x4
            m3 = m3 + delta5*x5


        #PASO 1 calculo de función  
        xs1 = sumaPonderada(x1,x2,x5,w1,w2,w3,w0)  # x de f(x)
        xs2 = sumaPonderada(x1,x2,x3,v1,v2,v3,v0)
        xs3 = sumaPonderada(x2,x3,x4,y1,y2,y3,y0)
        xs4 = sumaPonderada(x3,x4,x5,l1,l2,l3,l0)
        xs5 = sumaPonderada(x1,x4,x5,m1,m2,m3,m0)

            
        # evaluacion de la funcion de activación (sigmoide) f(x) = 1 / 1+ e^(-x)

        S1 = funcionDeActivacion(xs1)
        S2 = funcionDeActivacion(xs2)
        S3 = funcionDeActivacion(xs3)
        S4 = funcionDeActivacion(xs4)
        S5 = funcionDeActivacion(xs5)

        # Paso 2: delta de error
        delta1 = SD1 - S1
        delta2 = SD2 - S2
        delta3 = SD3 - S3
        delta4 = SD4 - S4
        delta5 = SD5 - S5

        # Paso 4: Condición de paro
        deltaDeError = abs(delta1) + abs(delta2) + abs(delta3) + abs(delta4) + abs(delta5)

        if deltaDeError <= 0.00005:
            ParoTotal = 0
            bandera_deltaDeError = 1

        if NumDeIteracion == 200:
            ParoTotal = 0
            bandera_NumDeIteracion = 1
    

        NumDeIteracion = NumDeIteracion + 1

    # RESULTADOS

    # redondeando a cinco decimales

    w0 = round(w0, 5) 
    w1 = round(w1, 5) 
    w2 = round(w2, 5) 
    w3 = round(w3, 5) 

    v0 = round(v0, 5) 
    v1 = round(v1, 5) 
    v2 = round(v2, 5) 
    v3 = round(v3, 5) 

    y0 = round(y0, 5) 
    y1 = round(y1, 5) 
    y2 = round(y2, 5) 
    y3 = round(y3, 5) 

    l0 = round(l0, 5) 
    l1 = round(l1, 5) 
    l2 = round(l2, 5) 
    l3 = round(l3, 5) 

    m0 = round(m0, 5) 
    m1 = round(m1, 5) 
    m2 = round(m2, 5) 
    m3 = round(m3, 5) 

    # redondeando los valores de S calculados de la red

    S1 = round(S1, 5) 
    S2 = round(S2, 5) 
    S3 = round(S3, 5) 
    S4 = round(S4, 5) 
    S5 = round(S5, 5) 

    cadena_Ws = [w0,w1,w2,w3]
    cadena_Vs = [v0,v1,v2,v3]
    cadena_Ys = [y0,y1,y2,y3]
    cadena_Ls = [l0,l1,l2,l3]
    cadena_Ms = [m0,m1,m2,m3]

    cadena_Ss = [S1,S2,S3,S4,S5]

    w_imitador.extend(cadena_Ws)
    v_imitador.extend(cadena_Vs)
    y_imitador.extend(cadena_Ys)
    l_imitador.extend(cadena_Ls)
    m_imitador.extend(cadena_Ms)

    S_imitacion.extend(cadena_Ss)


# pesos

print("Pesos")

print("")
print("w_imitador = ", w_imitador)

print("")
print("v_imitador = ", v_imitador)

print("")
print("y_imitador = ", y_imitador)

print("")
print("l_imitador = ", l_imitador)

print("")
print("m_imitador = ", m_imitador)


# resultados que calculo la red

print("")
print("S_imitacion = ", S_imitacion)


# condición de paro activada

#if bandera_deltaDeError == 1 :
#    print("Condición de paro: Error menor a 0.01")

#if bandera_NumDeIteracion == 1:
#    print("Condición de paro: Iteración num 200")



#cadena de datos de salida RESULTADO DE LA RED NEURONAL ---"Si"---  -AUDIO IMITADO- sonido/data sintética creado por la Red
# creado por los pesos de las conexiones de la red 


SDi_a_imitar_original = [];

for i in range(15):
    SDi_a_imitar_original.append(S_imitacion[i]*array_negativos_SDi[i]);


print("array negativos", array_negativos_SDi)
print("x_ imitar ORIGINAL", SDi_a_imitar_original)