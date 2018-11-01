'''
This is a script to print the name, RA and dec for all galaxies in /data/spectra
'''
#tell the computer where our SDSS library is!



from sdssmodule.SDSSData import SDSSData
import os

#find the spectra directory over which we will iterate

directory = '../data/spectra/'

assert os.scandir(directory) is not None, f'{directory} has no files! Please check the directory and try again.'

for file in os.scandir(directory):
	if '.fits' in file.name:
		print(file.name)
		print(f'{directory}{file.name}')
		gal = SDSSData(f'{directory}{file.name}') 
		#assert gal.name is not None, f'{file.name} has no name data! Please check the file and try again.'
		assert gal.ra is not None, f'file.name has no RA data! Please check the file and try again.' 
		assert gal.dec is not None, f'file.name has no dec data! Please check the file and try again.' 
 
		print(f'Galaxy gal.name is located at RA {gal.ra}%.2f and dec {gal.dec}%.2f.')