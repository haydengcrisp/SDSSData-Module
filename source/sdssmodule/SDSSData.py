class SDSSData(object):
    def __init__(self, filepath=None):
        if filepath is None:
            raise SDSSFileNotSpecified("Must define a file")
        self.filepath = filepath
        self.datafile = open(self.filepath)
        self._ra = None
        self._dec = None

    def ra(self):
        '''Returns the RA of the spectrum in degrees'''
        if self._ra == None:
            # opens fits file
            # read the right HDU
            self._ra = hdu.header["ra"]
        return self._ra

'''--------- API ---------
from package import SDSSData

s = Spectrum(filename = 'somefile.fits')
print(s.ra)
print(s.dec)
'''
