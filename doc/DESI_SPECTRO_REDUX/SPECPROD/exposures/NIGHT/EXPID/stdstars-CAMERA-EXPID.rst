========
stdstars
========

:Summary: *This section should be filled in with a high-level description of
    this file. In general, you should remove or replace the emphasized text
    (\*this text is emphasized\*) in this document.*
:Naming Convention: ``stdstars-7-00000020.fits``, where ... *Give a human readable
    description of the filename, e.g. ``blat-{EXPID}`` where ``{EXPID}``
    is the 8-digit exposure ID.*
:Regex: ``stdstars-7-00000020.fits`` *Give a regular expression for this filename.
    For example, a six-digit number would correspond to ``[0-9]{6}``.*
:File Type: FITS, 5 MB  *This section gives the type of the file
    and its approximate size.*

Contents
========

====== ========== ======== ===================
Number EXTNAME    Type     Contents
====== ========== ======== ===================
HDU0_  FLUX       IMAGE    *Brief Description*
HDU1_  WAVELENGTH IMAGE    *Brief Description*
HDU2_  FIBERS     IMAGE    *Brief Description*
HDU3_  METADATA   BINTABLE *Brief Description*
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
