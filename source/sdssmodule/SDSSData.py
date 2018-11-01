from astropy.io import fits

class SDSSData(object):
    def __init__(self, filepath=None):
        if filepath is None:
            raise SDSSFileNotSpecified("Must define a file")
        self.filepath = filepath
        #self.datafile = open(self.filepath)
        self._ra = None
        self._dec = None
        self._name = None

    @property
    def ra(self):
        '''Returns the Right Assention of the spectrum in degrees'''
        if self._ra == None:
            # opens fits file
            hdu_list = fits.open(self.filepath)
            hdu = hdu_list[0]
            # read the right HDU
            self._ra = hdu.header["ra"]
        return self._ra

    @property
    def dec(self):
        '''Returns the Declination of the spectrum'''
        if self._dec == None:
            # open fits file
            hdu_list = fits.open(self.filepath) # Not sure if this is right...
            hdu = hdu_list[0]
            # read the right HDU
            self._dec = hdu.header["dec"]
        return self._dec


    @property
    def name(self):
        '''Returns the name header'''
        if self._name == None:
            # open fits file
            hdu_list = fits.open(self.filepath) # Not sure if this is right...
            hdu = hdu_list[0]
            # read the right HDU
            self._name = hdu.header["name"]
        return self._name


'''--------- API ---------
from package import SDSSData

s = Spectrum(filename = 'somefile.fits')
print(s.ra)
print(s.dec)
'''
