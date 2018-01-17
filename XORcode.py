import numpy as np
import random
def Sigmoid(x):
    return 1 / (1 + np.exp(-x))
def Calculator():
    matris_1[0][1]=matris_1[0][0]
    matris_1[1][1] = matris_1[1][0]
    matris_1[2][1] = matris_1[2][0]
    net=0.0
    for sayac in liste_2:
        net+=matris_1[sayac][0]*matris_1[sayac][1]
    matris_2[0][0]=net

    net = 0.0
    for sayac in liste_2:
        net += matris_1[sayac][0] * matris_1[sayac][2]
    matris_2[1][0] = net

    matris_2[0][1]=Sigmoid(matris_2[0][0])
    matris_2[1][1] = Sigmoid(matris_2[1][0])
    matris_2[2][1]=matris_2[2][0]

    net = 0.0
    for sayac in liste_2:
        net += matris_1[sayac][0] * matris_1[sayac][2]
    matris_3[0][0]= net
    matris_3[0][1] = Sigmoid(matris_3[0][0])
def AgirlikDegis():
    error = 0.0
    sm = 0.0
    sj = 0.0
    alfa = 0.5
    momentum = 0.8
    delta=0.0
    son_delta = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    error=0-matris_3[0][0]
    sm=matris_3[0][0]*(1-matris_3[0][0])*error
    for sayac in liste_2:
        delta=alfa*sm*matris_2[sayac][1]+(momentum*son_delta[sayac])
        son_delta[sayac]=delta
        matris_2[sayac][2]+=delta
    sj=matris_2[0][1]*(1-matris_2[0][1])*sm*matris_2[0][2]
    for sayac in liste_2:
        delta=alfa*sj*matris_1[sayac][1]+(momentum*son_delta[sayac+3])
        son_delta[sayac+3] = delta
        matris_1[sayac][2]+=delta
    sj = matris_2[1][1] * (1 - matris_2[1][1]) * sm * matris_2[1][2]
    for sayac in liste_2:
        delta = alfa * sj * matris_1[sayac][1] + (momentum * son_delta[sayac + 6])
        son_delta[sayac + 6] = delta
        matris_1[sayac][3] += delta
matris_1=np.array([[0.0,0.0,0.129952,0.570345],
                   [0.0,0.0,-0.923123,-0.328932],
                   [1.0,0.0,0.341232,-0.115223]])
matris_2=np.array([[0.0,0.0,0.164732],
                   [0.0,0.0,0.752621],
                   [1.0,0.0,-0.993423]])
matris_3=np.array([[0.0,0.0]])
sayac=0
sayac_2=0
sonuc=0.0
liste=range(4)
liste_2=range(3)
for sayac in liste_2:
    for sayac_2 in liste:
        matris_1[sayac][sayac_2]=random.random()
matris_1[0][0]=0.0
matris_1[1][0]=0.0
matris_1[2][0]=1.0
for sayac in liste:
    for sayac_2 in liste:
        matris_2[sayac][sayac_2]=random.random()
matris_2[0][0]=0.0
matris_2[1][0]=0.0
matris_2[2][0]=1.0
Calculator()
AgirlikDegis()
print matris_2[2][2]
