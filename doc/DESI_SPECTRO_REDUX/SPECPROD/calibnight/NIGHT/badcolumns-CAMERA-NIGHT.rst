=======================
badcolumns-CAMERA-NIGHT
=======================

:Summary: Auxilliary file listing bad columns.
:Naming Convention: ``badcolumns-CAMERA-NIGHT.csv``, where ``CAMERA`` is
    *e.g.*, "b0", "r5", etc. and ``NIGHT`` is the observation night in
    YYYYMMDD format.
:Regex: ``badcolumns-[brz][0-9]-[0-9]{8}\.csv``
:File Type: CSV, 1 KB

Contents
========

Note: in some cases the file may contain no data.

The file should have these columns:

============ ======= ================================================================================
Name         Type    Description
============ ======= ================================================================================
CAMERA       char[*] Camera identifier. Passband and SPECGRPH ([brz][0-9]).
COLUMN       int     TODO: description needed
ELEC_PER_SEC float   TODO: description needed
SIGMA        float   TODO: description needed
============ ======= ================================================================================
