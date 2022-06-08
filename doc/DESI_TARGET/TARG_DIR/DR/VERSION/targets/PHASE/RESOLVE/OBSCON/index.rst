======
OBSCON
======

``OBSCON`` designates the observational conditions (or "layer") in which targets
will be observed. Possible values include "dark" and "bright" for dark-time and
bright-time targets, respectively. Under each observing condition, targets are
stored in files that are grouped by (nested) HEALPixel number in filenames that
resemble {``PHASE``}targets-{``OBSCON``}-{``RESOLVE``}-hp-{``HP``}.fits . For
targets that are *not* resolved ``RESOLVE`` is omitted from the filename. For
targets that are part of the DESI Main Science Survey ``PHASE`` is omitted from
the filename.

There is a special case of secondary targets that were not merged
with primary targets --- these secondary targets have no concept of a "resolve". Such
"standalone" secondary targets are written to monolithic files with names resembling
targets-{``OBSCON``}-secondary.fits .


.. toctree::
   :maxdepth: 1

   {phase}targets-{obscon}-{resolve}-hp-{hp}.fits: target selection catalog <PHASEtargets-OBSCON-RESOLVE-hp-HP>
   targets-{obscon}-secondary.fits: catalog of "standalone" secondary targets <targets-OBSCON-secondary>
   deprecated: DR3 target catalog format <targets-dr3>
   deprecated: DR6 target catalog format <targets-dr6>
   deprecated: DR7 target catalog format <targets-dr7>
   deprecated: DR8 target catalog format <targets-dr8>
