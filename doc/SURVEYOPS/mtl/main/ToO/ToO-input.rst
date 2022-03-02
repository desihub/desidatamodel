=========
ToO-input
=========

:Summary: Targets of Opportunity input ledger
:Naming Convention: ``ToO-input.ecsv``
:Regex: ``ToO-input\.ecsv``
:File Type: ecsv, about 100 MB

Contents
========

========== ======== ==========
EXTNAME    Type     Contents
========== ======== ==========
TOO        TABLE    ToO Ledger
========== ======== ==========


Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======= ============= ==== ===========================================================================
KEY     Example Value Type Comment
======= ============= ==== ===========================================================================
RELEASE 9999           int Ersatz Legacy Surveys RELEASE used for Targets of Opportunity (always 9999)
======= ============= ==== ===========================================================================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============================= ======== =========== =================================================
Name                          Type     Units       Description
============================= ======== =========== =================================================
RA                            float64  deg         Right ascension
DEC                           float64  deg         Declination
PMRA                          float32  mas/yr      Proper motion in the RA direction
PMDEC                         float32  mas/yr      Proper motion in the Dec direction
REF_EPOCH                     float32  yr          Reference epoch for Gaia/Tycho astrometry
CHECKER                       char[2]              Initials of researcher who vetted the target
TOO_TYPE                      char[4]              Either "TILE" for a special tile or "FIBER" for a fiber-override ToO
TOO_PRIO                      char[2]              Either "HI" for a very-high-priority target or "LO" for a very-low-priority target
OCLAYER                       char[6]              Either "DARK" for dark-time or "BRIGHT" to observe in either bright- or dark-time
MJD_BEGIN                     float64  d           Start of the allowed observing window for this target (Modified Julian Date)
MJD_END                       float64  d           End of the allowed observing window for this target (Modified Julian Date)
TOOID                         int32                ID for this target assigned by the CHECKER
============================= ======== =========== =================================================
