# -*- coding: utf-8 -*-


#GPGGA,145223.556,3930.0422,N,00232.0727,E,1,03,50.0,0.0,M,,,,0000*30
#GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

#GGA          Datos GPS
    #123519       Hora del dato en horario UTC
    #4807.038,N   Latitud
    #01131.000,E  Longitud
    #1            Validez:     0 = invalido
                              #1 = GPS valido
                              #2 = DGPS valido
                              #6 = estimatedo
          #8 = modo simulación
    #08           Número de satelites utilizados
    #0.9          Desviación horizontal
    #545.4,M      Altitud en metros
    #46.9,M       Geoid
    #(vacío)      Tiempo desde última actualización
    #(vacío)      ID estación DGPS
    #*47          checksum

import serial
import re
ser=serial.Serial('/dev/rfcomm1')
horaPat='.+?GPGGA,(\d+\.\d+)'
latPat='.+?,(\d+\.\d+),N'
lonPat='.+?,(\d+\.\d+),E'
hightPat='.+?,(\d+\.\d+),M'
validPat='.+?E,(\d)'

def llegirDades():
    linia = ser.readline()
    begin=linia[1:6]
    v='0'
    while v=='0':
        linia=ser.readline()
        begin=linia[1:6]
        if begin=='GPGGA':
            v=re.match(validPat,linia).group(1)
            print linia
            print v
    hora=re.match(horaPat,linia).group(1)
    lat=re.match(latPat,linia).group(1)
    lon=re.match(lonPat,linia).group(1)
    h=re.match(hightPat,linia).group(1)
    print "v",v,"hora",hora,"lat",lat,"lon",lon,"h",h
    print "BONA",linia
    
llegirDades()
ser.close()


