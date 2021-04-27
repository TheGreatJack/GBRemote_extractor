#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:45:37 2021

@author: anderjackf
"""


from sys import argv

#Pequeño handler de datos de entrada, no se ve afectado por el orden de
#entrada de los argumentos

def arg_handler():
	query=""
	email="andrescrz48@gmail.com"
	retmax=10

	print(argv)
	for x in argv[1:]:
		if x.startswith("query="):
			query=x.split("=")[1]
		if x.startswith("email="):
	    		email=x.split("=")[1]
		if x.startswith("retmax="):
			try:
				retmax=int(x.split("=")[1])
			except: 
				print("esto esta mal puesto se pone el retmax default")

	return query,email,retmax
    
