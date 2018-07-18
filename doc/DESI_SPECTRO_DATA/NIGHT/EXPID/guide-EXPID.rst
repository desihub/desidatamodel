===========
guide-EXPID
===========

:Summary: Placeholder datamodel for the guider GFA raw data
:Naming Convention: ``guide-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``guide-[0-9]{8}\.fits.fz``
:File Type: FITS, 1 GB

Contents
========

Details are TBD, but the nominal format is:

====== ========== ================= =============================
Number EXTNAME    Type              Contents
====== ========== ================= =============================
HDU0   GUIDE      IMAGE             Header keywords only
HDU1   GUIDE0     Compressed IMAGE  Focus GFA frames from petal 0
HDU2   GUIDE0T    BINTABLE          Metadata about FOCUS0 frames
HDU3   GUIDE2     Compressed IMAGE  Focus GFA frames from petal 2
HDU4   GUIDE2T    BINTABLE          Metadata about FOCUS2 frames
HDU5   GUIDE4     Compressed IMAGE  Focus GFA frames from petal 4
HDU6   GUIDE4T    BINTABLE          Metadata about FOCUS4 frames
HDU7   GUIDE5     Compressed IMAGE  Focus GFA frames from petal 5
HDU8   GUIDE5T    BINTABLE          Metadata about FOCUS5 frames
HDU9   GUIDE7     Compressed IMAGE  Focus GFA frames from petal 7
HDU10  GUIDE7T    BINTABLE          Metadata about FOCUS7 frames
HDU11  GUIDE9     Compressed IMAGE  Focus GFA frames from petal 9
HDU12  GUIDE9T    BINTABLE          Metadata about FOCUS9 frames
====== ========== ================= =============================

The GUIDEn data will be 3D[nframes, ny, nx] such that
`data[i]` is the 2D GFA frame number `i`.  Row `i` of the
GUIDEnT table will contain the metadata about that frame, e.g. the
DATE-OBS and EXPTIME.

Note that other than the blank data primary HDU, the order of the other
HDUs is arbitrary and some GUIDEn(T) HDUs may even be missing.  The
nominal set (0,2,4,5,7,9) is the plan for full DESI, but particularly during
commissioning other combinations will appear in the data.

Other than the name and number of the HDUs, the structure of this format
is identical to the focus GFA raw data.