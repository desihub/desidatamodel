=========================
frame-CAMERA-EXPID.fits
=========================

General Description
===================

Summary
-------

spframe files contain the raw extracted electrons from DESI data, without
any further calibration.

Naming Convention
-----------------

``frame-AS-EXPID.fits``, where
A is the camera arm b, r, or z;
S is the spectrograph number 0-9,
and EXPID is the zero-padded 8-digit exposure ID.

regex: ``frame-[brz][0-9]-[0-9]{8}.fits``

File Type
---------

FITS, *TBD* MB

Contents
========

====== ========== ===== ===================
Number EXTNAME    Type  Contents           
====== ========== ===== ===================
HDU0_             IMAGE Extracted electrons (photons)
HDU1_  IVAR       IMAGE Inverse variance of extracted electrons
HDU2_  WAVELENGTH IMAGE Wavelength grid of the extraction
HDU3_  RESOLUTION IMAGE Resolution matrix
====== ========== ===== ===================

FITS Header Units
=================

HDU0
----

Extracted electrons[nspec, nwave]

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =========================================== ===== ==================================
KEY      Example Value                               Type  Comment                           
======== =========================================== ===== ==================================
NAXIS1   6001                                        int   Number of wavelength samples             
NAXIS2   500                                         int   Number of extracted spectra             
EXTNAME  FLUX                                        str                                     
CRVAL1   7089.0                                      float Starting wavelength [Angstroms]   
CDELT1   0.2                                         float Wavelength step [Angstroms]       
AIRORVAC vac                                         str   Vacuum wavelengths                
LOGLAM   0                                           int   linear wavelength steps, not log10
SIMFILE  alpha-3/20150107/simspec-00000003.fits      str   Input simulation file             
CAMERA   r0                                          str   Spectograph Camera                
VSPECTER 0.0.0                                       str   TODO: Specter version             
EXPTIME  1000.0                                      float Exposure time [sec]               
RDNOISE  2.9                                         float Read noise [electrons]            
FLAVOR   science                                     str   Exposure type (arc, flat, science)
SPECMIN  0                                           int   First spectrum                    
SPECMAX  1                                           int   Last spectrum                     
NSPEC    2                                           int   Number of spectra                 
WAVEMIN  7089.0                                      float First wavelength [Angstroms]      
WAVEMAX  7110.5                                      float Last wavelength [Angstroms]       
WAVESTEP 0.5                                         float Wavelength step size [Angstroms]  
SPECTER  0.1.dev1                                    str   https://github.com/sbailey/specter
IN_PSF   .../desimodel/trunk/data/specpsf/psf-r.fits str   Input spectral PSF                
IN_IMG   ...im/alpha-3/20150107/pix-r0-00000003.fits str   Input image                       
======== =========================================== ===== ==================================

HDU1
----

EXTNAME = IVAR

Inverse variance of the electrons in HDU0.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment              
======= ============= ==== =====================
NAXIS1  6001          int  Number of wavlengths
NAXIS2  500           int  Number of spectra
EXTNAME IVAR          str                       
======= ============= ==== =====================

Data: FITS image [float64]

HDU2
----

EXTNAME = WAVELENGTH

1D array of wavelengths.  NAXIS1 here is the same length as NAXIS2 of
the first 2 HDUs.

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment              
======= ============= ==== =====================
NAXIS1  6001          int  Number of wavelengths
EXTNAME WAVELENGTH    str                       
======= ============= ==== =====================

Data: FITS image [float64]

HDU3
----

EXTNAME = RESOLUTION

Resolution matrix stored as a 3D sparse matrix:

Rdata[nspec, ndiag, nwave]

To convert this into sparse matrices for convolving a model that is sampled
at the same wavelengths as the extractions (HDU EXTNAME='WAVELENGTH'):

.. code::

    from scipy.sparse import spdiags
    from astropy.io import fits
    import numpy as np

    #- read a model and its wavelength vector from somewhere
    #- IMPORTANT: cast them to .astype(np.float64) to get native endian

    #- read the resolution data
    resdata = fits.getdata(framefile, 'RESOLUTION').astype(np.float64)

    nspec, nwave = model.shape
    convolvedmodel = np.zeros((nspec, nwave))
    diags = np.arange(10, -11, -1)

    for i in range(nspec):
        R = spdiags(resdata[i], diags, nwave, nwave)
        convolvedmodel[i] = R.dot(model)

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== =====================
KEY     Example Value Type Comment              
======= ============= ==== =====================
NAXIS1  6001          int  length of data axis 1
NAXIS2  21            int  length of data axis 2
NAXIS3  500           int  length of data axis 3
EXTNAME RESOLUTION    str                       
======= ============= ==== =====================

Data: FITS image [float64]

Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

