from machine import Pin
import time

tempoAnterior = time.ticks_ms()

intervalo = 1000

ledR1 = Pin(13, Pin.OUT)
ledR2 = Pin(12, Pin.OUT)

ledM1 = Pin(14, Pin.OUT)
ledM2 = Pin(27, Pin.OUT)
ledM3 = Pin(26, Pin.OUT)
ledM4 = Pin(25, Pin.OUT)

def Leds(modo, luminosidade, temporizador):
    global tempoAnterior
    tempoAtual = time.ticks_ms()
    ledM4.off()
    ledM3.off()
    ledM2.off()
    ledM1.off()
    if modo == False:
        if time.ticks_diff(tempoAtual, tempoAnterior) >= intervalo:
            tempoAnterior = tempoAtual
            ledM1.value(not ledM1.value())
            if luminosidade < 500: ledM2.value(not ledM2.value())
        
        if luminosidade < 500:
            ledR1.on()
            ledR2.on()
        else:
            ledR1.off()
            ledR2.off()
    else:
        if temporizador > 0:

            ledM1.on()
            ledM2.off()
            ledM3.off()
            ledM4.off()
            if temporizador >= 11:
                ledM2.on()
            else:
                ledM2.off()
            if temporizador >= 21:
                ledM3.on()
            else:
                ledM3.off()
            if temporizador >= 31:
                ledM4.on()
            else:
                ledM4.off()
            
            ledR1.on()
            ledR2.on()
                  
        else:
            ledM1.off()
            ledR1.off()
            ledR2.off() 



    



