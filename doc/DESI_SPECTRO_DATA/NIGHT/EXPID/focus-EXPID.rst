===========
focus-EXPID
===========

:Summary: Placeholder datamodel for the focus GFA raw data
:Naming Convention: ``focus-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``focus-[0-9]{8}\.fits\.fz``
:File Type: FITS, 600 MB

Contents
========

Details are TBD, but the nominal format is:

====== ========== ================= =============================
Number EXTNAME    Type              Contents
====== ========== ================= =============================
HDU0   FOCUS      IMAGE             Header keywords only
HDU1   FOCUS1     Compressed IMAGE  Focus GFA frames from petal 1
HDU2   FOCUS1T    BINTABLE          Metadata about FOCUS1 frames
HDU3   FOCUS3     Compressed IMAGE  Focus GFA frames from petal 3
HDU4   FOCUS3T    BINTABLE          Metadata about FOCUS3 frames
HDU5   FOCUS6     Compressed IMAGE  Focus GFA frames from petal 6
HDU6   FOCUS6T    BINTABLE          Metadata about FOCUS6 frames
HDU7   FOCUS8     Compressed IMAGE  Focus GFA frames from petal 8
HDU8   FOCUS8T    BINTABLE          Metadata about FOCUS8 frames
====== ========== ================= =============================

The FOCUSn data will be 3D[nframes, ny, nx] such that
`data[i]` is the 2D GFA frame number `i`.  Row `i` of the
FOCUSnT table will contain the metadata about that frame, e.g. the
DATE-OBS and EXPTIME.

Note that other than the blank data primary HDU, the order of the other
HDUs is arbitrary and some FOCUSn(T) HDUs may even be missing.  The
nominal set (1,3,6,8) is the plan for full DESI, but particularly during
commissioning other combinations will appear in the data.

Other than the name and number of the HDUs, the structure of this format
is identical to the guide GFA raw data.
