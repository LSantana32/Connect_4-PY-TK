import numpy as np
from colorama import init, Fore, Style

def crear_tablero(nFilas,nCols):
    tablero= np.zeros((nFilas,nCols),str)
    
    for nfila in range(nFilas):
        for ncol in range(nCols):
            tablero[nfila][ncol]=''
    return (tablero)

def imprimir_tablero(tablero):
    print('|', end='')
    for element in range(1,len(tablero[0])+1):
        print(element,end='|')
    print("")
    for fila in tablero:
        print("|",end='|')
        
        for valor in fila:
             
        

































        \

          
        
tab=crear_tablero(7,6)
imprimir_tablero(tab)