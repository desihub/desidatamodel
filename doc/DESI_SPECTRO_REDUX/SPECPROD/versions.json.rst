=============
versions.json
=============

:Summary: Documents the versions of pipeline code used in this production.
:Naming Convention: ``versions.json``
:Regex: ``versions\.json``
:File Type: JSON


This file contains a JSON document of which versions of code were used for
this production, *e.g.* ::

  {
    "specex": "1.2.3",
    "specter": "0.3.1",
    "harp": "0.9.8",
    "desispec": "2.3.4"
  }
  
Note: the pipeline currently does not write this file.  The code versions
used are included in the header keywords of the data files, and the commands
to configure that environment are kept in the ``setup.sh`` file instead.
