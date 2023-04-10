=============
request-EXPID
=============

:Summary: JSON file containing commands to be executed during the current exposure. 
:Naming Convention: ``request-EXPID.json``, where EXPID is the zero-padded 8-digit
    exposure ID.
:Regex: ``request-[0-9]{8}\.json``
:File Type: JSON, 100 bB

Contents
========

Each file contains a dictionary with the following top-level keys:

================ ============================================
Key              Description
================ ============================================
``SEQUENCE``     Overall exposure type.
================ ============================================

