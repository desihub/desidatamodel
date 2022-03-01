========
override
========

The ``override`` directory hosts ledgers used to override MTL
information for secondary targets in the DESI dark-time program.
Each entry is copied over the entry for the corresponding TARGETID
in the standard ledgers, each time the MTL code is run. Targets are
stored in ledgers that are split by HEALPixel (in the NESTED scheme) at
a resolution of nside=32.

The filename for each ledger resembles mtl-override-dark-hp-HPX.ecsv, where
HPX is the healpixel number.

.. toctree::
   :maxdepth: 1

   mtl-override-dark-hp-HPX.rst : MTL ledgers used to override DESI dark-time program secondary targets.
