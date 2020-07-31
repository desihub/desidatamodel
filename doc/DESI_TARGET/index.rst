===========
DESI_TARGET
===========

:envvar:`DESI_TARGET` contains target selection and fiber assignment data,
with the canonical location of ``$DESI_ROOT/TS/target``. Where ``TS`` is one of
`ets` for DESI early target selection, `svts` for DESI Survey Validation or
`ts` for the DESI Main Science Survey.

.. toctree::
   :maxdepth: 1

   randoms-{source}-{version}.fits : random catalog <randoms>
   pixweight-{source}-{version}.fits : HEALPixel map of target densities and quantities derived from randoms <pixweight>
   skies-{source}-{version}.fits : catalog of blank sky locations <skies>
   gfas-{source}-{version}.fits : catalog of GFA targets <gfas>
   mtl-{version}.fits : merged target list catalog <mtl>
   truth-{version}.fits : truth mock catalog <truth>
   fiberassign/index
   TARG_DIR/index
