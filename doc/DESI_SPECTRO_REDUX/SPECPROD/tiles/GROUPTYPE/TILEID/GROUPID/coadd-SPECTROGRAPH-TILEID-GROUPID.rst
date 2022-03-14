======================================
coadd-SPECTROGRAPH-TILEID-GROUPID.fits
======================================

:Summary: Coadded spectra.
:Naming Convention: ``coadd-SPECTROGRAPH-TILEID-GROUPID.fits``, where
    ``SPECTROGRAPH`` is the spectrograph ID, ``TILEID`` is the tile number and
    ``GROUPID`` depends on the ``GROUPTYPE`` of the tile coadd.
:Regex: ``coadd-[0-9]-[0-9]+-([14]xsubset[1-6]|lowspeedsubset[1-6]|exp[0-9]{8}|thru[0-9]{8}|[0-9]{8})\.fits``
:File Type: FITS, 213 MB


This file follows nearly the same format as the spectra files, except there is
one entry per target instead of one entry per exposure per target, and
the FIBERMAP replaces some exposure-specific columns with summary columns,
*e.g.* ``NIGHT`` becomes ``FIRST_NIGHT``, ``LAST_NIGHT``, and ``NUM_NIGHT``.

As-of software release 20.4 (desispec 0.34.4), the SCORES HDU is the last
HDU instead of HDU2.

Contents
========

====== ============ ======== ===================
Number EXTNAME      Type     Contents
====== ============ ======== ===================
HDU00_              IMAGE    Empty
HDU01_ FIBERMAP     BINTABLE fibermap table
HDU02_ EXP_FIBERMAP BINTABLE *Brief Description*
HDU03_ B_WAVELENGTH IMAGE    Wavelength array of b-channel spectra
HDU04_ B_FLUX       IMAGE    Flux of b-channel spectra
HDU05_ B_IVAR       IMAGE    Inverse variance of b-channel spectra
HDU06_ B_MASK       IMAGE    Mask of b-channel spectra
HDU07_ B_RESOLUTION IMAGE    Resolution matrices of b-channel spectra
HDU08_ R_WAVELENGTH IMAGE    Wavelength array of r-channel spectra
HDU09_ R_FLUX       IMAGE    Flux of r-channel spectra
HDU10_ R_IVAR       IMAGE    Inverse variance of r-channel spectra
HDU11_ R_MASK       IMAGE    Mask of r-channel spectra
HDU12_ R_RESOLUTION IMAGE    Resolution matrices of r-channel spectra
HDU13_ Z_WAVELENGTH IMAGE    Wavelength array of z-channel spectra
HDU14_ Z_FLUX       IMAGE    Flux of z-channel spectra
HDU15_ Z_IVAR       IMAGE    Inverse variance of z-channel spectra
HDU16_ Z_MASK       IMAGE    Mask of z-channel spectra
HDU17_ Z_RESOLUTION IMAGE    Resolution matrices of z-channel spectra
HDU18_ SCORES       BINTABLE QA scores table
====== ============ ======== ===================


FITS Header Units
=================

HDU00
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =============================== ==== ==============================================
KEY      Example Value                   Type Comment
======== =============================== ==== ==============================================
CHECKSUM AfAMBZ1KAf8KAZ8K                str  HDU checksum updated 2021-07-16T14:01:46
DATASUM  0                               str  data unit checksum updated 2021-07-16T14:01:46
FIBERMIN 1000                            int
INFIL000 spectra-2-545-thru20210510.fits str
======== =============================== ==== ==============================================

Empty HDU.

HDU01
-----

EXTNAME = FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   387              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM H5Z5H5Z3H5Z3H5Z3 str  HDU checksum updated 2021-07-16T14:01:46
DATASUM  4214162542       str  data unit checksum updated 2021-07-16T14:01:46
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================== ======= ===== =====================================================
Name                       Type    Units Description
========================== ======= ===== =====================================================
TARGETID                   int64         Unique target ID
PETAL_LOC                  int16         Petal location [0-9]
DEVICE_LOC                 int32         Device location on focal plane [0-523]
LOCATION                   int64         FP location PETAL_LOC*1000 + DEVICE_LOC
FIBER                      int32         Fiber ID on the CCDs [0-4999]
COADD_FIBERSTATUS          int32
TARGET_RA                  float64       Target Right Ascension [degrees]
TARGET_DEC                 float64       Target declination [degrees]
PMRA                       float32       PM in +RA dir (already incl cos(dec))
PMDEC                      float32       Proper motion in +dec direction
REF_EPOCH                  float32       proper motion reference epoch
LAMBDA_REF                 float32       Wavelength at which fiber was centered
FA_TARGET                  int64
FA_TYPE                    binary        Internal fiberassign target type
OBJTYPE                    char[3]       SKY, TGT, NON
FIBERASSIGN_X              float32       Expected CS5 X on focal plane
FIBERASSIGN_Y              float32       Expected CS5 Y on focal plane
PRIORITY                   int32         Assignment priority; larger=higher priority
SUBPRIORITY                float64       Assignment subpriority [0-1)
OBSCONDITIONS              int32         bitmask of allowable observing conditions
RELEASE                    int16         imaging surveys release ID
BRICKID                    int32         Imaging Surveys brick ID
BRICK_OBJID                int32         Imaging Surveys OBJID on that brick
MORPHTYPE                  char[4]       Imaging Surveys morphological type
FLUX_G                     float32       g-band flux
FLUX_R                     float32       r-band flux
FLUX_Z                     float32       z-band flux
FLUX_IVAR_G                float32       Inverse variance of FLUX_G
FLUX_IVAR_R                float32       Inverse variance of FLUX_R
FLUX_IVAR_Z                float32       Inverse variance of FLUX_Z
MASKBITS                   int16         Photometry mask bits
REF_ID                     int64         Astrometric cat refID (Gaia SOURCE_ID)
REF_CAT                    char[2]       astrometry reference catalog
GAIA_PHOT_G_MEAN_MAG       float32       Gaia G band mag
GAIA_PHOT_BP_MEAN_MAG      float32       Gaia BP band mag
GAIA_PHOT_RP_MEAN_MAG      float32       Gaia RP band mag
PARALLAX                   float32       Parallax
BRICKNAME                  char[8]       Imaging Surveys brick name
EBV                        float32       Galactic extinction E(B-V) reddening from SFD98
FLUX_W1                    float32       WISE W1-band flux
FLUX_W2                    float32       WISE W2-band flux
FLUX_IVAR_W1               float32       Inverse variance of FLUX_W1
FLUX_IVAR_W2               float32       Inverse variance of FLUX_W2
FIBERFLUX_G                float32       g-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERFLUX_R                float32       r-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERFLUX_Z                float32       z-band model flux 1&quot; seeing, 1.5&quot; dia fiber
FIBERTOTFLUX_G             float32       fiberflux model incl. all objs at this loc
FIBERTOTFLUX_R             float32       fiberflux model incl. all objs at this loc
FIBERTOTFLUX_Z             float32       fiberflux model incl. all objs at this loc
SERSIC                     float32       Power-law index for the Sersic profile model
SHAPE_R                    float32       Half-light radius of galaxy model
SHAPE_E1                   float32       Ellipticity component 1 for galaxy model
SHAPE_E2                   float32       Ellipticity component 2 for galaxy model
PHOTSYS                    char[1]       N for BASS/MzLS, S for DECam
PRIORITY_INIT              int64         initial priority
NUMOBS_INIT                int64         initial number of requested observations
SV3_DESI_TARGET            int64
SV3_BGS_TARGET             int64
SV3_MWS_TARGET             int64
SV3_SCND_TARGET            int64
DESI_TARGET                int64         Dark survey + calibration targeting bits
BGS_TARGET                 int64         Bright Galaxy Survey targeting bits
MWS_TARGET                 int64         Milky Way Survey targeting bits
PLATE_RA                   float64       Right Ascension for Platemaker to use [degrees]
PLATE_DEC                  float64       declination for Platemaker to use [degrees]
TILEID                     int32
COADD_NUMEXP               int16
COADD_EXPTIME              float32
COADD_NUMNIGHT             int16
COADD_NUMTILE              int16
MEAN_DELTA_X               float32
RMS_DELTA_X                float32
MEAN_DELTA_Y               float32
RMS_DELTA_Y                float32
MEAN_FIBER_RA              float64
STD_FIBER_RA               float32
MEAN_FIBER_DEC             float64
STD_FIBER_DEC              float32
MEAN_PSF_TO_FIBER_SPECFLUX float32
MEAN_FIBER_X               float32
MEAN_FIBER_Y               float32
========================== ======= ===== =====================================================

HDU02
-----

EXTNAME = EXP_FIBERMAP

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   162              int  length of dimension 1
NAXIS2   1000             int  length of dimension 2
ENCODING ascii            str
CHECKSUM 3f5X4e3U3e3U3e3U str  HDU checksum updated 2021-07-16T14:01:46
DATASUM  360255485        str  data unit checksum updated 2021-07-16T14:01:46
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== ======= ===== ===============================================
Name                  Type    Units Description
===================== ======= ===== ===============================================
TARGETID              int64         Unique target ID
PRIORITY              int32         Assignment priority; larger=higher priority
SUBPRIORITY           float64       Assignment subpriority [0-1)
NIGHT                 int32
EXPID                 int32
MJD                   float64
TILEID                int32
EXPTIME               float64       Exposure time
PETAL_LOC             int16         Petal location [0-9]
DEVICE_LOC            int32         Device location on focal plane [0-523]
LOCATION              int64         FP location PETAL_LOC*1000 + DEVICE_LOC
FIBER                 int32         Fiber ID on the CCDs [0-4999]
FIBERSTATUS           int32         Fiber status; 0=good
FIBERASSIGN_X         float32       Expected CS5 X on focal plane
FIBERASSIGN_Y         float32       Expected CS5 Y on focal plane
LAMBDA_REF            float32       Wavelength at which fiber was centered
PLATE_RA              float64       Right Ascension for Platemaker to use [degrees]
PLATE_DEC             float64       declination for Platemaker to use [degrees]
NUM_ITER              int64         Number of positioner iterations
FIBER_X               float64       CS5 X location requested by PlateMaker
FIBER_Y               float64       CS5 Y location requested by PlateMaker
DELTA_X               float64       CS5 X diff requested and actual position
DELTA_Y               float64       CS5 Y diff requested and actual position
FIBER_RA              float64       RA of actual fiber position
FIBER_DEC             float64       DEC of actual fiber position
PSF_TO_FIBER_SPECFLUX float64
===================== ======= ===== ===============================================

HDU03
-----

EXTNAME = B_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
BUNIT    Angstrom         str
CHECKSUM 7CGAA9F99AFAA9F9 str  HDU checksum updated 2021-07-16T14:01:46
DATASUM  979185614        str  data unit checksum updated 2021-07-16T14:01:46
======== ================ ==== ==============================================

Data: FITS image [float64, 2751]

HDU04
-----

EXTNAME = B_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ==== ==============================================
KEY      Example Value                Type Comment
======== ============================ ==== ==============================================
NAXIS1   2751                         int
NAXIS2   500                          int
BUNIT    10**-17 erg/(s cm2 Angstrom) str
CHECKSUM lgKZngKZlgKZlgKZ             str  HDU checksum updated 2021-07-16T14:01:46
DATASUM  1157856797                   str  data unit checksum updated 2021-07-16T14:01:46
======== ============================ ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU05
-----

EXTNAME = B_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2751                              int
NAXIS2   500                               int
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
CHECKSUM JATXJASUJASUJASU                  str  HDU checksum updated 2021-07-16T14:01:47
DATASUM  2428790047                        str  data unit checksum updated 2021-07-16T14:01:47
======== ================================= ==== ==============================================

Data: FITS image [float32, 2751x500]

HDU06
-----

EXTNAME = B_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
NAXIS2   500              int
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM W4fLW4dLW4dLW4dL str  HDU checksum updated 2021-07-16T14:01:47
DATASUM  688030           str  data unit checksum updated 2021-07-16T14:01:47
======== ================ ==== ==============================================

Data: FITS image [int32, 2751x500]

HDU07
-----

EXTNAME = B_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2751             int
NAXIS2   11               int
NAXIS3   500              int
CHECKSUM 1l9M1i6K1i6K1i6K str  HDU checksum updated 2021-07-16T14:01:50
DATASUM  1827421509       str  data unit checksum updated 2021-07-16T14:01:50
======== ================ ==== ==============================================

Data: FITS image [float32, 2751x11x500]

HDU08
-----

EXTNAME = R_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
BUNIT    Angstrom         str
CHECKSUM 7JPAAHO78HOAAHO7 str  HDU checksum updated 2021-07-16T14:01:51
DATASUM  456732359        str  data unit checksum updated 2021-07-16T14:01:51
======== ================ ==== ==============================================

Data: FITS image [float64, 2326]

HDU09
-----

EXTNAME = R_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ==== ==============================================
KEY      Example Value                Type Comment
======== ============================ ==== ==============================================
NAXIS1   2326                         int
NAXIS2   500                          int
BUNIT    10**-17 erg/(s cm2 Angstrom) str
CHECKSUM M3ENO3BMM3BMM3BM             str  HDU checksum updated 2021-07-16T14:01:51
DATASUM  640139918                    str  data unit checksum updated 2021-07-16T14:01:51
======== ============================ ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU10
-----

EXTNAME = R_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2326                              int
NAXIS2   500                               int
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
CHECKSUM VDCjYABhVABhVABh                  str  HDU checksum updated 2021-07-16T14:01:51
DATASUM  2650218726                        str  data unit checksum updated 2021-07-16T14:01:51
======== ================================= ==== ==============================================

Data: FITS image [float32, 2326x500]

HDU11
-----

EXTNAME = R_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   500              int
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM m7e4n4e1m4e1m4e1 str  HDU checksum updated 2021-07-16T14:01:51
DATASUM  582966           str  data unit checksum updated 2021-07-16T14:01:51
======== ================ ==== ==============================================

Data: FITS image [int32, 2326x500]

HDU12
-----

EXTNAME = R_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2326             int
NAXIS2   11               int
NAXIS3   500              int
CHECKSUM e3FYh09Xe0CXe09X str  HDU checksum updated 2021-07-16T14:01:54
DATASUM  1488519775       str  data unit checksum updated 2021-07-16T14:01:54
======== ================ ==== ==============================================

Data: FITS image [float32, 2326x11x500]

HDU13
-----

EXTNAME = Z_WAVELENGTH

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2881             int
BUNIT    Angstrom         str
CHECKSUM gaVNgYSLgaSLgWSL str  HDU checksum updated 2021-07-16T14:01:54
DATASUM  3106662670       str  data unit checksum updated 2021-07-16T14:01:54
======== ================ ==== ==============================================

Data: FITS image [float64, 2881]

HDU14
-----

EXTNAME = Z_FLUX

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ============================ ==== ==============================================
KEY      Example Value                Type Comment
======== ============================ ==== ==============================================
NAXIS1   2881                         int
NAXIS2   500                          int
BUNIT    10**-17 erg/(s cm2 Angstrom) str
CHECKSUM 9GPWGFMU9FMUGFMU             str  HDU checksum updated 2021-07-16T14:01:55
DATASUM  3338246075                   str  data unit checksum updated 2021-07-16T14:01:55
======== ============================ ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU15
-----

EXTNAME = Z_IVAR

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================================= ==== ==============================================
KEY      Example Value                     Type Comment
======== ================================= ==== ==============================================
NAXIS1   2881                              int
NAXIS2   500                               int
BUNIT    10**+34 (s2 cm4 Angstrom2) / erg2 str
CHECKSUM 4Ala47iR4AiX47iX                  str  HDU checksum updated 2021-07-16T14:01:55
DATASUM  2758170465                        str  data unit checksum updated 2021-07-16T14:01:55
======== ================================= ==== ==============================================

Data: FITS image [float32, 2881x500]

HDU16
-----

EXTNAME = Z_MASK

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2881             int
NAXIS2   500              int
BSCALE   1                int
BZERO    2147483648       int
CHECKSUM 95fkD3fk93fkC3fk str  HDU checksum updated 2021-07-16T14:01:56
DATASUM  720616           str  data unit checksum updated 2021-07-16T14:01:56
======== ================ ==== ==============================================

Data: FITS image [int32, 2881x500]

HDU17
-----

EXTNAME = Z_RESOLUTION

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   2881             int
NAXIS2   11               int
NAXIS3   500              int
CHECKSUM DFFSG99QDECQD99Q str  HDU checksum updated 2021-07-16T14:01:59
DATASUM  500309470        str  data unit checksum updated 2021-07-16T14:01:59
======== ================ ==== ==============================================

Data: FITS image [float32, 2881x11x500]

HDU18
-----

EXTNAME = SCORES

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ================ ==== ==============================================
KEY      Example Value    Type Comment
======== ================ ==== ==============================================
NAXIS1   172              int  length of dimension 1
NAXIS2   500              int  length of dimension 2
ENCODING ascii            str
CHECKSUM EpXcGmWcEmWcEmWc str  HDU checksum updated 2021-07-16T14:01:59
DATASUM  1286335698       str  data unit checksum updated 2021-07-16T14:01:59
======== ================ ==== ==============================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=================== ======= ===== ============================================
Name                Type    Units Description
=================== ======= ===== ============================================
TARGETID            int64         DESI Unique Target ID
INTEG_COADD_FLUX_B  float32       integ. flux in wave. range 4000,5800A
MEDIAN_COADD_FLUX_B float32       median flux in wave. range 4000,5800A
MEDIAN_COADD_SNR_B  float32       median SNR/sqrt(A) in wave. range 4000,5800A
INTEG_COADD_FLUX_R  float32       integ. flux in wave. range 5800,7600A
MEDIAN_COADD_FLUX_R float32       median flux in wave. range 5800,7600A
MEDIAN_COADD_SNR_R  float32       median SNR/sqrt(A) in wave. range 5800,7600A
INTEG_COADD_FLUX_Z  float32       integ. flux in wave. range 7600,9800A
MEDIAN_COADD_FLUX_Z float32       median flux in wave. range 7600,9800A
MEDIAN_COADD_SNR_Z  float32       median SNR/sqrt(A) in wave. range 7600,9800A
TSNR2_GPBDARK_B     float32       GPBDARK B template (S/N)^2
TSNR2_ELG_B         float32       ELG B template (S/N)^2
TSNR2_GPBBRIGHT_B   float32       GPBBRIGHT B template (S/N)^2
TSNR2_LYA_B         float32       LYA B template (S/N)^2
TSNR2_BGS_B         float32       BGS B template (S/N)^2
TSNR2_GPBBACKUP_B   float32       GPBBACKUP B template (S/N)^2
TSNR2_QSO_B         float32       QSO B template (S/N)^2
TSNR2_LRG_B         float32       LRG B template (S/N)^2
TSNR2_GPBDARK_R     float32       GPBDARK R template (S/N)^2
TSNR2_ELG_R         float32       ELG R template (S/N)^2
TSNR2_GPBBRIGHT_R   float32       GPBBRIGHT R template (S/N)^2
TSNR2_LYA_R         float32       LYA R template (S/N)^2
TSNR2_BGS_R         float32       BGS R template (S/N)^2
TSNR2_GPBBACKUP_R   float32       GPBBACKUP R template (S/N)^2
TSNR2_QSO_R         float32       QSO R template (S/N)^2
TSNR2_LRG_R         float32       LRG R template (S/N)^2
TSNR2_GPBDARK_Z     float32       GPBDARK Z template (S/N)^2
TSNR2_ELG_Z         float32       ELG Z template (S/N)^2
TSNR2_GPBBRIGHT_Z   float32       GPBBRIGHT Z template (S/N)^2
TSNR2_LYA_Z         float32       LYA Z template (S/N)^2
TSNR2_BGS_Z         float32       BGS Z template (S/N)^2
TSNR2_GPBBACKUP_Z   float32       GPBBACKUP Z template (S/N)^2
TSNR2_QSO_Z         float32       QSO Z template (S/N)^2
TSNR2_LRG_Z         float32       LRG Z template (S/N)^2
TSNR2_GPBDARK       float32       GPBDARK template (S/N)^2 summed over B,R,Z
TSNR2_ELG           float32       ELG template (S/N)^2 summed over B,R,Z
TSNR2_GPBBRIGHT     float32       GPBBRIGHT template (S/N)^2 summed over B,R,Z
TSNR2_LYA           float32       LYA template (S/N)^2 summed over B,R,Z
TSNR2_BGS           float32       BGS template (S/N)^2 summed over B,R,Z
TSNR2_GPBBACKUP     float32       GPBBACKUP template (S/N)^2 summed over B,R,Z
TSNR2_QSO           float32       QSO template (S/N)^2 summed over B,R,Z
TSNR2_LRG           float32       LRG template (S/N)^2 summed over B,R,Z
=================== ======= ===== ============================================


Notes and Examples
==================

The format supports arbitrary channel names as long as for each channel {X}
there is a set of HDUs named {X}_WAVELENGTH, {X}_FLUX, {X}_IVAR, {X}_MASK,
{X}_RESOLUTION.

Upcoming changes
================

The following changes are not yet in the spectra files, but will be added in
the future:

* signal-to-noise per band
