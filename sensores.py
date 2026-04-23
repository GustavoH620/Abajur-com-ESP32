from machine import ADC, Pin

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

def ler_luminosidade():
    return  ldr.read()