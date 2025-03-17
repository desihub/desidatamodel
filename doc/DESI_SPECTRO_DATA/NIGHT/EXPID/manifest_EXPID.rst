==============
manifest_EXPID
==============

:Summary: JSON file containing descriptive data about an exposure. These files
    were used in early commissioning, but are now obsolete.
:Naming Convention: ``manifest_EXPID.json``, where EXPID is the zero-padded 8-digit
    exposure ID.
:Regex: ``manifest_[0-9]{8}\.json``
:File Type: JSON, 250 B

Contents
========

Each file contains a dictionary with the following top-level keys:

================ ============================================
Key              Description
================ ============================================
``MANIFEST``     TODO: *Description needed.*
``PURPOSE``      TODO: *Description needed.*
``PROGRAM``      TODO: *Description needed.*
``EXPID``        Exposure ID.
``NIGHT``        Observation night.
``DATE-OBS``     Timestamp of observation.
``MJD-OBS``      MJD of observation.
``LAST``         TODO: *Description needed.*
================ ============================================
