===
ToO
===

:Summary: Targets of Opportunity ledger
:Naming Convention: ``ToO.ecsv``
:Regex: ``ToO\.ecsv``
:File Type: ecsv, 112 KB

Contents
========

========== ======== ==========
EXTNAME    Type     Contents
========== ======== ==========
TOO        TABLE    ToO Ledger
========== ======== ==========


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===========================================================================
KEY     Example Value Type Comment
======= ============= ==== ===========================================================================
RELEASE 9999           int Ersatz Legacy Surveys RELEASE used for Targets of Opportunity (always 9999)
======= ============= ==== ===========================================================================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~

============================= ======== =========== =================================================
Name                          Type     Units       Description
============================= ======== =========== =================================================
RA                            float64  deg         Right ascension
DEC                           float64  deg         Declination
PMRA                          float64  mas/yr      Proper motion in the RA direction
PMDEC                         float64  mas/yr      Proper motion in the Dec direction
REF_EPOCH                     float64  yr          Reference epoch for Gaia/Tycho astrometry
FLUX_G                        float32  nanomaggies Flux in the Legacy Survey g-band (placeholder; needed by fiberassign)
FLUX_R                        float32  nanomaggies Flux	in the Legacy Survey r-band (placeholder; needed by fiberassign)
FLUX_Z                        float32  nanomaggies Flux	in the Legacy Survey z-band (placeholder; needed by fiberassign)
PARALLAX                      float32  mas         Parallax (placeholder; needed by fiberassign)
GAIA_PHOT_G_MEAN_MAG          float32  mag         Magnitude in the Gaia G-band (placeholder; needed by fiberassign)
GAIA_PHOT_BP_MEAN_MAG         float32  mag         Magnitude in	the Gaia BP-band (placeholder; needed by fiberassign)
GAIA_PHOT_RP_MEAN_MAG         float32  mag         Magnitude in	the Gaia RP-band (placeholder; needed by fiberassign)
GAIA_ASTROMETRIC_EXCESS_NOISE float32              Gaia astrometric excess noise (placeholder; needed by fiberassign)
TARGETID                      int64                Unique DESI targeting ID
SV3_DESI_TARGET               int64                DESI (dark time program) target selection bitmask
SV3_SCND_TARGET               int64                Target selection bitmask for DESI secondary programs
SCND_ORDER                    int32                Number of row for target entry in secondary file (placeholder; needed by fiberassign)
PRIORITY_INIT                 int64                Target's initial priority from target selection bitmasks and OBSCONDITIONS
SUBPRIORITY                   float64              Random subpriority [0-1] to break assignment ties
NUMOBS_INIT                   int64                Target's initial desired number of observations
OBSCONDITIONS                 int64                Observing conditions/program bitmask (bright/dark/backup/etc.)
CHECKER                       char[5]              Initials of researcher who vetted the target
TOO_TYPE                      char[5]              Either "TILE" for a special tile or "FIBER" for a fiber-override ToO
TOO_PRIO                      char[2]              Either "HI" for a very-high-priority target or "LO" for a very-low-priority target
OCLAYER                       char[6]              Either "DARK" for dark-time or "BRIGHT" to observe in either bright- or dark-time
MJD_BEGIN                     float64  d           Start of the allowed observing window for this target (Modified Julian Date)
MJD_END                       float64  d           End of the allowed observing window for this target (Modified Julian Date)
TOOID                         int64                ID for this target assigned by the CHECKER
============================= ======== =========== =================================================
