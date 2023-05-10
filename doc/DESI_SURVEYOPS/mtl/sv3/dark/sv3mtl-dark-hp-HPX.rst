.. _mtl_ledger:

==================
sv3mtl-dark-hp-HPX
==================

:Summary: MTL ledgers for the DESI dark-time program.
:Naming Convention: ``sv3mtl-dark-hp-HPX.ecsv``, where
    HPX is the nside=32 (NESTED) HEALPixel integer.
:Regex: ``sv3mtl-dark-hp-[0-12287]\.ecsv``
:File Type: ecsv, 2-6 MB

Contents
========

========== ======== ==========
EXTNAME    Type     Contents
========== ======== ==========
MTL        TABLE    MTL Ledger
========== ======== ==========


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== =================================== ==== ============================================================================
KEY      Example Value                       Type Comment
======== =================================== ==== ============================================================================
DR       9                                   int  Legacy Surveys Data Release used to produce the targets (should always be 9)
FILEHPX  7031                                int  HEALPixel integer for the file
FILENEST True                                bool If the HEALPixel NESTED scheme was used for the file (should always be True)
FILENSID 32                                  int  HEALPixel nside used for the file (should always be 32)
INDIR    dr9/0.57.0/targets/sv3/resolve/dark str  Location of the directory of targets used to produce the file
OBSCON   DARK                                str  DESI program (DARK, BRIGHT or BACKUP)
SCND     False                               bool Whether the file is a ledger of primary or secondary targets
SURVEY   sv3                                 str  DESI survey phase (main, sv2 or sv3)
======== =================================== ==== ============================================================================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

================= ======== ====== =================================================
Name              Type     Units  Description
================= ======== ====== =================================================
RA                float64  deg    Right ascension
DEC               float64  deg    Declination
REF_EPOCH         float32  yr     Reference epoch for Gaia/Tycho astrometry
PARALLAX          float32  mas    Parallax
PMRA              float32  mas/yr Proper motion in the RA direction
PMDEC             float32  mas/yr Proper motion in the Dec direction
TARGETID          int64           Unique DESI targeting ID
SV3_DESI_TARGET   int64           DESI (dark time program) target selection bitmask
SV3_BGS_TARGET    int64           BGS (bright time program) target selection bitmask
SV3_MWS_TARGET    int64           MWS (bright time program) target selection bitmask
SUBPRIORITY       float64         Random subpriority [0-1] to break assignment ties
OBSCONDITIONS     int32           Observing conditions/program bitmask (bright/dark/backup/etc.)
PRIORITY_INIT     int64           Target's initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT       int64           Target's initial desired number of observations
SV3_SCND_TARGET   int64           Target selection bitmask for secondary programs
NUMOBS_MORE       int64           Desired number of observations given target's current state
NUMOBS            int64           Number of (good) observations of target acquired so far
Z                 float64         Redshift measured by Redrock
ZWARN             int64           Redshift warning bitmask measured by Redrock
ZTILEID           int32           ID of tile that most recently updated target's state
TARGET_STATE      char[16]        Combination of target's class and its current observational state
TIMESTAMP         char[19] s      UTC/ISO time at which the target's state was updated
VERSION           char[6]         Version of desitarget code used to update target's state
PRIORITY          int64           Target's current priority
================= ======== ====== =================================================
