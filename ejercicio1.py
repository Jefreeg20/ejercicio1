from datetime import datetime, date, time, timedelta
import calendar

ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora Hoy= ",ahora.utcnow())  # Muestra fecha/hora
print('***************Lista de Pais************')
print('*Numero Lista 1 Honduras               *')
print('*Numero Lista 2 Panama                 *')
print('*Numero Lista 3 Guatemala              *') 
print('*Numero Lista 4 Nicaragua              *')
print('*Numero Lista 5 Salvador               *')
print('****************************************')
Pais = {'Honduras':9.746, 'Panama':4.246, 'Guatemala':16.6, 'Nicaragua':6.44,'Salvador':6.454}
Poblacion = input('¿Qué Pais va Selecionar? ').title()

if Poblacion in Pais:
    print( 'La Poblacion de', Poblacion, 'es', Pais[Poblacion], 'Millones')
else: 
    print("Lo siento, el Pais", Poblacion, "no está disponible Favor Ingresar Pais Correcto de la lista.")
    print("help", "copyright", "Jefree Satiel Gomez" or "Clase de Rpbotica" )