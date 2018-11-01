from astropy.io import fits

class SDSSData(object):
    def __init__(self, filepath=None):
        if filepath is None:
            raise SDSSFileNotSpecified("Must define a file")
        self.filepath = filepath
        self.datafile = open(self.filepath)
        self._ra = None
        self._dec = None

    @property
    def ra(self):
        '''Returns the Right Assention of the spectrum in degrees'''
        if self._ra == None:
            # opens fits file
            hdu_list = fits.open(self.datafile) # Not sure if this is right...
            # read the right HDU
            self._ra = hdu_list.header["ra"]
        return self._ra

    @property
    def dec(self):
        '''Returns the Declination of the spectrum'''
        if self._dec == None:
            # open fits file
            hdu_list = fits.open(self.datafile) # Not sure if this is right...
            # read the right HDU
            self._dec = hdu_list.header["dec"]
        return self._ra

'''--------- API ---------
from package import SDSSData

s = Spectrum(filename = 'somefile.fits')
print(s.ra)
print(s.dec)
'''
