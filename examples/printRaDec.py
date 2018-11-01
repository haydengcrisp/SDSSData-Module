'''
This is a script to print the name, RA and dec for all galaxies in /data/spectra
'''

import SDSSData as sdss
import os

#find the spectra directory over which we will iterate

directory = '../data/spectra'

for file in os.scandir(directory):
	if '.fits' in file.name:
		print(file.name)

		gal = sdss.Thing(file.name) #???

		gal.ra
		gal.dec
		gal.name