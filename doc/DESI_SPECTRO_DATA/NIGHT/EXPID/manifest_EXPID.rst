==============
manifest_EXPID
==============

:Summary: JSON file containing centroid data associated with the guide cameras.
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
``expid``        Exposure number
``frames``       *Description needed*
================ ============================================

