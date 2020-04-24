import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

def limiarizarParafusos(imgEntrada):
    #inicio do seu codigo
    limiar = 172
    (limiar, imgBin) =cv.threshold(imgEntrada, limiar, 255, cv.THRESH_BINARY)
    #fim do codigo
    return imgBin

def limiarizarPorcas(imgEntrada):
    #inicio do seu codigo
    
    limiar = 172
    (limiar, imgBin) = cv.threshold(imgEntrada, limiar, 255, cv.THRESH_BINARY)

    #fim do seu codigo
    return imgBin

def contarParafusos(imgBin):
    #inicio do seu codigo
    (numCC, imgLabel, stats, centros) = cv.connectedComponentsWithStats(imgBin)

    MIN = 865
    MAX = 4000
    quantParafusos = 0

    for cod in range(1, numCC):
      if (MIN <= stats[cod, cv.CC_STAT_AREA] and stats[cod, cv.CC_STAT_AREA] <= MAX ):
        quantParafusos += 1
          
        #fim do seu codigo
        
    return quantParafusos

def contarPorcas(imgBin):
    #inicio do seu codigo
    (numCC, imgLabel, stats, centros) = cv.connectedComponentsWithStats(imgBin)

    MIN = 200
    MAX = 855
    quantPorcas = 0

    for cod in range(1, numCC):
      if (MIN <= stats[cod, cv.CC_STAT_AREA] and stats[cod, cv.CC_STAT_AREA] <= MAX ):
        quantPorcas += 1
          
        #fim do seu codigo
        
    return quantPorcas

import math
from matplotlib import pyplot
arquivos = ["img01.jpg", "img02.jpg", "img03.jpg", "img04.jpg", "img05.jpg", "img06.jpg", "img07.jpg", "img08.jpg", "img09.jpg", "img10.jpg"]
parafusos =[    10     ,      10    ,     10     ,       5    ,       9    ,      10    ,      7     ,      7     ,      10    ,      10    ]
porcas =   [    10     ,      10    ,     10     ,       10   ,       9    ,      10    ,      10    ,      10    ,      10    ,      9     ]

taxaDeErroPorcas = 0
taxaDeErroParafusos = 0

for i in range(len(arquivos)):
    img = cv.imread(PATH + arquivos[i], cv.IMREAD_GRAYSCALE)

    imgBinParafusos = limiarizarParafusos(img)
    contParafusos = contarParafusos(imgBinParafusos)
    
    imgBinPorcas = limiarizarPorcas(img)
    contPorcas = contarPorcas(imgBinPorcas)
    
    taxaDeErroPorcas += (abs(porcas[i] - contPorcas) / porcas[i]) * 100
    taxaDeErroParafusos += (abs(parafusos[i] - contParafusos) / parafusos[i]) * 100
    print("Resultado:", arquivos[i], "Porcas:", contPorcas, "de", porcas[i], "Parafusos:", contParafusos, "de", parafusos[i])
        
        
#Resultado da validacao        
print("\nTaxa de acerto em porcas:", round(100 - (taxaDeErroPorcas/len(arquivos)),2), "%")
print("Taxa de acerto em parafusos:", round(100 - (taxaDeErroParafusos/len(arquivos)),2), "%")
