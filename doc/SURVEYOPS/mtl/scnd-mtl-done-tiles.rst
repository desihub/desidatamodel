===================
scnd-mtl-done-tiles
===================

:Summary: Record of tiles with MTL updates for secondary targets.
:Naming Convention: ``scnd-mtl-done-tiles.ecsv``
:Regex: ``scnd-mtl-done-tiles\.ecsv``
:File Type: ecsv, 200 KB

Contents
========

========== ======== ===================
EXTNAME    Type     Contents
========== ======== ===================
MTLTILE    TABLE    Tile information
========== ======== ===================


Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ======= ===== =================================================
Name         Type    Units Description
============ ======= ===== =================================================
TILEID       int32         Unique tile ID on which MTL updates occurred
TIMESTAMP    str         s UTC/ISO time when MTL updates on tile completed
VERSION      str           Version of desitarget code used to update ledgers
PROGRAM      str           DESI program type - BRIGHT or DARK
ZDATE        int64         Final night (YYYYMMDD) when redshifts were acquired
ARCHIVEDATE  int64         Date (YYYYMMDD) on which redshifts were archived
============ ======= ===== =================================================
