=============================
hpixexp-SURVEY-PROGRAM-PIXNUM
=============================

:Summary: Auxilliary file listing exposures that contribute to spectra in a HEALPixel.
:Naming Convention: ``hpixexp-SURVEY-PROGRAM-PIXNUM.csv``, where ``SURVEY`` is
    *e.g.* ``main`` or ``sv1``, ``PROGRAM`` is *e.g.* ``bright`` or ``dark``
    and ``PIXNUM`` is the HEALPixel number.
:Regex: ``hpixexp-(cmx|main|special|sv1|sv2|sv3)-(backup|bright|dark|other)-[0-9]+\.csv``
:File Type: CSV, 1 KB

Contents
========

The file should have these columns:

======== ======= ================================================================================
Name     Type    Description
======== ======= ================================================================================
NIGHT    int     Night of observation (YYYYMMDD) starting at local noon before observations start
EXPID    int     DESI Exposure ID number
TILEID   int     Unique DESI tile ID
SURVEY   char[*] Survey name
PROGRAM  char[*] DESI program type - BRIGHT, DARK, BACKUP, OTHER
SPECTRO  int     Spectrograph number [0-9]
HEALPIX  int     HEALPixel containing this location at NSIDE=64 in the NESTED scheme
======== ======= ================================================================================
