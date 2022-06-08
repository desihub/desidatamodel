=====
PHASE
=====

``PHASE`` is a specific DESI observational phase, which can include
"mainX" for iterations of the DESI Main Science Survey, "svX" for
iterations of Survey Validation and "cmx" for commissioning, where X
is an integer.

Under each phase, QA webpages are stored in directories that resemble
{``PHASE``}desitargetQA-{``DR``}-{``OBSCON``}-{``VERSION``}. Here,
``PHASE`` is a specific DESI observational phase (*e.g.* svX with X=1,2,3
for iterations of Survey Validation), ``DR`` is the Legacy Surveys Data Release
associated with the targets and randoms used to build the pixweight files on which
the QA is based, ``OBSCON`` is the observing condition
(or "layer") for the targets (*e.g.* dark), and ``VERSION`` is the version of the
desitarget code used to generate the QA. For targets that are part of the DESI Main
Science Survey ``PHASE`` is omitted from the filename.

Clicking on these QA directories (or the associated
{``PHASE``}desitargetQA-{``DR``}-{``OBSCON``}-{``VERSION``}/index.html page) will
display the QA webpages.


