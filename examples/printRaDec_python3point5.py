'''
This is a script to print the name, RA and dec for all galaxies in /data/spectra
'''
#tell the computer where our SDSS library is!



from sdssmodule.SDSSData import SDSSData
import os

#find the spectra directory over which we will iterate

directory = 'data/spectra/'

assert os.scandir(directory) is not None, '{} has no files! Please check the directory and try again.'.format(directory) # this syntax is for python 3.6+, but am running 3.5.3

for file in os.scandir(directory):
    if '.fits' in file.name:
        gal = SDSSData('{}{}'.format(directory, file.name)) #concatenating strings to make a valid filename
        #assert gal.name is not None, f'{file.name} has no name data! Please check the file and try again.'
        assert gal.ra is not None, '{} has no RA data! Please check the file and try again.'.format(file.name) 
        assert gal.dec is not None, '{} has no dec data! Please check the file and try again.'.format(file.name) 
        print('Galaxy {} is located at RA {:.2f} and dec {:.2f}.'.format(gal.name, gal.ra, gal.dec))
