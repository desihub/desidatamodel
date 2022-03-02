===============
mtl-dark-hp-HPX
===============

:Summary: MTL ledgers used to override information for DESI dark-time secondary targets.
:Naming Convention: ``mtl-override-dark-hp-HPX.ecsv``, where
    HPX is the nside=32 (NESTED) HEALPixel integer.
:Regex: ``mtl-override-dark-hp-[0-12287]\.ecsv``
:File Type: ecsv, 0-10 KB

Contents
========

========== ======== ==========
EXTNAME    Type     Contents
========== ======== ==========
MTL        TABLE    MTL Ledger
========== ======== ==========


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~

======== ===================================== ==== ============================================================================
KEY      Example Value                         Type Comment
======== ===================================== ==== ============================================================================
DR       0                                     int  Legacy Surveys Data Release (meaningless for secondary targets)
FILEHPX  4447                                  int  HEALPixel integer for the file
FILENEST True                                  bool If the HEALPixel NESTED scheme was used for the file (should always be True)
FILENSID 32                                    int  HEALPixel nside used for the file (should always be 32)
INDIR    dr9/1.1.1/targets/main/secondary/dark str  Location of the directory of targets used to produce the file
OBSCON   DARK                                  str  DESI program (DARK, BRIGHT or BACKUP)
OVERRIDE True                                  bool Whether this ledger is a regular, standard ledger or used for overrides
SCND     True                                  bool Whether the file is a ledger of primary or secondary targets
SURVEY   main                                  str  DESI survey phase (main, sv2 or sv3)
======== ===================================== ==== ============================================================================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~

============= ======== ====== =================================================
Name          Type     Units  Description
============= ======== ====== =================================================
RA            float64  deg    Right ascension
DEC           float64  deg    Declination
PMRA          float32  mas/yr Proper motion in the RA direction
PMDEC         float32  mas/yr Proper motion in the Dec direction
REF_EPOCH     float32  yr     Reference epoch for Gaia/Tycho astrometry
PARALLAX      float32  mas    Parallax
TARGETID      int64           Unique DESI targeting ID
DESI_TARGET   int64           DESI (dark time program) target selection bitmask
SCND_TARGET   int64           Target selection bitmask for secondary programs
SUBPRIORITY   float64         Random subpriority [0-1] to break assignment ties
OBSCONDITIONS int32           Observing conditions/program bitmask (bright/dark/backup/etc.)
PRIORITY_INIT int64           Target's initial priority from target selection bitmasks and OBSCONDITIONS
NUMOBS_INIT   int64           Target's initial desired number of observations
BGS_TARGET    int64           BGS (bright time program) target selection bitmask
MWS_TARGET    int64           MWS (bright time program) target selection bitmask
NUMOBS_MORE   int64           Desired number of observations given target's current state
NUMOBS        int64           Number of (good) observations of target acquired so far
Z             float64         Redshift measured by Redrock
ZWARN         int64           Redshift warning bitmask measured by Redrock
ZTILEID       int32           ID of tile that most recently updated target's state
Z_QN          float64         Redshift measured by QuasarNET
IS_QSO_QN     int16           Classification determined by QuasarNET (1=QSO)
DELTACHI2     float64         Delta-chi-squared for template fit from Redrock
TARGET_STATE  char[18]        Combination of target's class and its current observational state
TIMESTAMP     char[25] s      UTC/ISO time at which the target's state was updated
VERSION       char[5]         Version of desitarget code used to update target's state
PRIORITY      int64           Target's current priority
NUMOVERRIDE   int64           Number of times to override a target's state (typically a large number)
============= ======== ====== =================================================
