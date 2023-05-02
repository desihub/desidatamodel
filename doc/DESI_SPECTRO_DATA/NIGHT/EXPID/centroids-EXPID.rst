===============
centroids-EXPID
===============

:Summary: JSON file containing centroid data associated with the guide cameras. 
:Naming Convention: ``centroids-EXPID.json``, where EXPID is the zero-padded 8-digit
    exposure ID.
:Regex: ``centroids-[0-9]{8}\.json``
:File Type: JSON, 100 kB

Contents
========

Each file contains a dictionary with the following top-level keys:

================ ============================================
Key              Description
================ ============================================
``expid``        Exposure number
``frames``       *Description needed*
================ ============================================

