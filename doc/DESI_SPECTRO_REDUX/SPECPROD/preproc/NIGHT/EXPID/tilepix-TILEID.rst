===================
tilepix-TILEID.json
===================

:Summary: This file maps the TILEID for an exposure to HEALpix pixels (nested nside=64).
:Naming Convention: ``tilepix-TILEID.json``, where ``TILEID`` is the tile id number.
:Regex: ``tilepix-[0-9]+\.json``
:File Type: JSON, 1 KB

Since each exposure observes one tile, the mapping consists of a keyword
which is the TILEID to petal number, 0 - 9, which in turn is mapped to the
HEALPix pixels that overlap the petal.

Example::

    {"51": {"0": [25596, 25598, 25599, 26965],
            "1": [25595, 25598, 25599, 26961, 26964, 26965],
            "2": [26961, 26964, 26965, 26966],
            "3": [26964, 26965, 26966, 26967],
            "4": [26965, 26967, 26973, 27650, 27656],
            "5": [26965, 27648, 27650, 27651],
            "6": [26965, 27648, 27649, 27650, 27651],
            "7": [25599, 26282, 26283, 26965, 27648, 27649],
            "8": [25597, 25599, 26280, 26282, 26965],
            "9": [25596, 25597, 25598, 25599, 26965]}}
