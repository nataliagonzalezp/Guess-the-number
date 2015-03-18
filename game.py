#-*- coding: utf-8 -*-
#! /usr/bin/python
#importo módulo para generar aleatorios
import random

intentos = 0

#Insertar el nombre

print('Bienvenido al juego de adivinar el numero, ¿cómo te llamas?')

mellamo = raw_input()

print ('Hola, %r') % (mellamo)

#establezco desde dónde inicia la secuencia de los números

numero = random.randint(1, 100)

print('De acuerdo, ' + mellamo + ', tienes 6 intentos para adivinar un número entre 1 y 100.') 

#establezco número de intentos a 6

while intentos < 6:
	print('intenta adivinar el número.') 
	intento = input()
	intento = int(intento)
	intentos = intentos + 1
	
	print ('inténtalo de nuevo')
		
	if intento < numero:
		print('Tu apuesta es demasiado pequeña.') 
		
	if intento > numero:
		print('Tu apuesta es demasiado grande.')
		
	if intento == numero:
		break

#Adivinar el número		
if intento == numero:
	intentos = str(intentos)
	print('¡Felicitaciones, ' + mellamo + '! has adivinado mi número en ' + intentos + ' intentos!')
	Partida= raw_input("Otra Partida? Responde sí o no \n")
	if Partida == 'sí':
		print('Excelente actitud, volvamos a empezar')
		execfile("game.py")
	else:
		print("***Arrivederci***")
	
#Perder		
if intento != numero:
	numero = str(numero)
	print('Has perdido. El número que estaba pensando era el ' + numero)
	
	Partida= raw_input("Otra Partida? Responde sí o no \n")
	if Partida == 'sí':
		print('Excelente actitud, volvamos a empezar')
		execfile("game.py")	
	else:
		print '\n'
		print("***Arrivederci***")
		print '\n'
						




	


