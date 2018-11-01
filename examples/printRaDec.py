'''
This is a script to print the name, RA and dec for all galaxies in /data/spectra
'''

#import SDSSData
import os

#find the spectra directory over which we will iterate

directory = '../data/spectra/'

for file in os.scandir(directory):
	if '.fits' in file.name:
		print(file.name)
		print(f'{directory}{file.name}')
		assert gal.name != None f'{file.name} has no name data! Please check the file and try again.'
		assert gal.ra != None f'{file.name} has no RA data! Please check the file and try again.' 
		assert gal.dec != None f'{file.name} has no dec data! Please check the file and try again.' 
 
#		gal = SDSSData(f'{directory}{file.name}') 
#
#		print(f'Galaxy {gal.name} is located at RA {gal.ra}%.2f and dec {gal.dec}%.2f.')