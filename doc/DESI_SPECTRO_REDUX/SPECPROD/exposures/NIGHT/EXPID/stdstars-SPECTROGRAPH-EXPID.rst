================================
stdstars-SPECTROGRAPH-EXPID.fits
================================

:Summary: This file contains the normalized standard star models fitted to the
    frame data.
:Naming Convention: ``stdstars-{SPECTROGRAPH}-{EXPID}.fits`` where
    ``{SPECTROGRAPH}`` is the single-digit spectrograph number 0-9, and
    ``{EXPID}`` is the zero-padded 8-digit exposure number.
:Regex: ``stdstars-[0-9]-[0-9]{8}\.fits``
:File Type: FITS, 5 MB

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    stdstar flux[nstd, nwave] in erg/s/cm^2/Angstrom
HDU1_  WAVELENGTH IMAGE    wavelength grid used, Angstroms
HDU2_  FIBERS     IMAGE    1D array of which fibers these models correspond to
HDU3_  METADATA   BINTABLE metadata from input standard star templates
HDU4_  COEFF      IMAGE    *Brief Description*
====== ========== ======== ===================


FITS Header Units
=================

HDU0
----

EXTNAME = FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================== ==== ==============================================
KEY      Example Value              Type Comment
======== ========================== ==== ==============================================
NAXIS1   118466                     int
NAXIS2   10                         int
BUNIT    1e-17 erg/(s cm2 Angstrom) str  Flux units
CHECKSUM 3pia4mgV3mga3mgU           str  HDU checksum updated 2018-03-01T15:07:19
DATASUM  1249793481                 str  data unit checksum updated 2018-03-01T15:07:19
======== ========================== ==== ==============================================

Data: FITS image [float32, 118466x10]

HDU1
----

EXTNAME = WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   118466           int
BUNIT    Angstrom         str  Wavelength units
CHECKSUM LNePONbMLNbMLNbM str  HDU checksum updated 2018-03-01T15:07:19
DATASUM  439161490        str  data unit checksum updated 2018-03-01T15:07:19
======== ================ ==== ==============================================

Data: FITS image [float32, 118466]

HDU2
----

EXTNAME = FIBERS

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   10               int
CHECKSUM cg56ef23cf23cf23 str  HDU checksum updated 2018-03-01T15:07:19
DATASUM  37951            str  data unit checksum updated 2018-03-01T15:07:19
======== ================ ==== ==============================================

Data: FITS image [int32, 10]

HDU3
----

EXTNAME = METADATA

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   56               int  length of dimension 1
NAXIS2   10               int  length of dimension 2
CHECKSUM 1bNA1bN71bNA1bN7 str  HDU checksum updated 2018-03-01T15:07:19
DATASUM  1348439413       str  data unit checksum updated 2018-03-01T15:07:19
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ===== ===========
Name      Type    Units Description
========= ======= ===== ===========
LOGG      float64
TEFF      float64
FEH       float64
CHI2DOF   float64
REDSHIFT  float64
DATA_G-R  float64
MODEL_G-R float64
========= ======= ===== ===========

HDU4
----

EXTNAME = COEFF

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   931              int
NAXIS2   10               int
CHECKSUM X5d6X2c6X2c6X2c6 str  HDU checksum updated 2018-03-01T15:07:19
DATASUM  1138832925       str  data unit checksum updated 2018-03-01T15:07:19
======== ================ ==== ==============================================

Data: FITS image [float64, 931x10]


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*
