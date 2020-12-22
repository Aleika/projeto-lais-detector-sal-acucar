# Programa que deve ser utilizado para gerar gráficos com dados enviados pelo Arduino utilizando comunicação serial.
# Observação: Este programa não foi efetivamente testado com o Arduino, logo, serve apenas como base para a implementação real

from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.backends
import threading
import serial
import csv

matplotlib.use ("TkAgg")

def tela(window):
    plotarGraficoTensao = Button(window, text="Plotar Gráfico Tensão", command=lambda: gerarGraficoTensaoThread())
    plotarGraficoTensao.place(x = 20, y = 20)

    plotarGraficoCorrente = Button(window, text="Plotar Gráfico Corrente", command=lambda: gerarGraficoCorrenteThread())
    plotarGraficoCorrente.place(x = 200, y = 20)


def gerarGraficoTensaoThread():
    global graficoTensaoThread
    graficoTensaoThread.start()
    graficoTensaoThread.join()

def gerarGraficoCorrenteThread():
    global graficoTensaoThread
    graficoCorrenteThread.start()
    graficoCorrenteThread.join()

def gerarGraficoTensaoTempo():
    plt.ylabel('Tensão (V)')
    plt.xlabel('Tempo (s)')
    # i=0
    # while True: 
    #   linha = ser.readline() 
    #   if(linha.split('/')[0]== 'V'):
    #       plt.plot((i, float(linha.decode()))
    #   i+= 1 
    # plt.show() 
    # plt.pause(0.0001)
    plt.plot([1, 2, 3, 4], [3.2, 2.8, 4.1, 3.3])
    plt.show()

def gerarGraficoCorrenteTempo():  
    plt.ylabel('Corrente (mA)')
    plt.xlabel('Tempo (s)')  
    # i=0
    # while True: 
    #   linha = ser.readline() 
    #   if(linha.split('/')[0] == 'C'):
    #       plt.plot(i, float(linha.decode()))
    #   i+= 1 
    #   plt.show() 
    #   plt.pause(0.0001)
    plt.plot([1, 2, 3, 4], [1, 1.5, 1.2, 1.3])
    plt.show()


# ser = serial.Serial('/dev/ttyACM0', 9600)
# ser.open()

window = Tk()
window.title("Interface para plotagem dos gráficos")
window.geometry('400x100')

graficoTensaoThread = threading.Thread(target=gerarGraficoTensaoTempo, args=[] )
graficoCorrenteThread = threading.Thread(target=gerarGraficoCorrenteTempo, args=[] )
tela = threading.Thread(target=tela, args=[window] )

# ser.close()

tela.start()

window.mainloop()

tela.join()

