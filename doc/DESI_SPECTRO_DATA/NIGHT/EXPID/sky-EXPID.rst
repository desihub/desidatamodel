=========
sky-EXPID
=========

:Summary: Placeholder datamodel for the sky monitor raw data
:Naming Convention: ``sky-EXPID.fits.fz``, where EXPID is the zero-padded
    8-digit exposure ID.
:Regex: ``sky-[0-9]{8}\.fits.fz``
:File Type: FITS, 350 MB

Contents
========

Details are TBD, but the nominal format is:

====== ========== ================= =========================
Number EXTNAME    Type              Contents
====== ========== ================= =========================
HDU0   SKY        IMAGE             Header keywords only
HDU1   SKYCAMERA  Compressed IMAGE  Sky camera frames
HDU2   SKYCAMERAT BINTABLE          Metadata about each frame
====== ========== ================= =========================

The SKYCAMERA data will be 3D[nframes, ny, nx] such that
`data[i]` is the 2D sky camera frame number `i`.  Row `i` of the
SKYCAMERAT table will contain the metadata about that frame, e.g. the
DATE-OBS and EXPTIME.
