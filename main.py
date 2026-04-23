from machine import Pin
import time
import sensores, atuadores
from sensores import ler_luminosidade
from atuadores import Leds

modo = Pin(2, Pin.IN, Pin.PULL_UP)
botao1 = Pin(33, Pin.IN, Pin.PULL_UP)
botao2 = Pin(32, Pin.IN, Pin.PULL_UP)
temporizador = 0
tempoAtual = 0
tempoAnterior = 0
tempoS = 0
intervalo = 1000
intervaloBotao = 200
intervaloSerial = 200
segundosOn = 0

tempoAnterior = time.ticks_ms()


while True:
    modoValor = not modo.value()
    if modoValor == True:
        if botao1.value() == 0:
            tempoAtual = time.ticks_ms()
            if time.ticks_diff(tempoAtual, tempoAnterior) >= intervaloBotao:
                temporizador += 10
                tempoAnterior = tempoAtual
                if temporizador > 40:
                    temporizador = 40

        if botao2.value() == 0:
            tempoAtual = time.ticks_ms()
            if time.ticks_diff(tempoAtual, tempoAnterior) >= intervaloBotao:
                temporizador -= 10
                tempoAnterior = tempoAtual
                if temporizador < 0:
                    temporizador = 0

    Leds(modoValor, ler_luminosidade(), temporizador)

    tempoAtual = time.ticks_ms()
    if time.ticks_diff(tempoAtual, tempoAnterior) >= intervalo:
        tempoAnterior = tempoAtual
        print("\n\nLuminosidade:",ler_luminosidade(), "Modo:", modoValor, "Temporizador:", temporizador)
        print("T:", time.localtime())
        print("Segundos desde ligado:", segundosOn)
        segundosOn += 1

        temporizador -= 1
        if temporizador < 0:
            temporizador = 0