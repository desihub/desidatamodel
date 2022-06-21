===
ToO
===

The ``ToO`` directory hosts a monolithic ledger of Targets of Opportunity.
This is used by the DESI fiberassign pipeline to assign
special, time-critical, observations.

Note that for the DESI main survey, the Targets of Opportunity ledger that
is read by fiberassign is split into two. The ``ToO.ecsv`` file hosts
Targets of Opportunity assigned on their own special tiles. The
``ToO-fiber.ecsv`` file hosts Targets of Opportunity assigned to fibers
during the course of normal survey operations.


.. toctree::
   :maxdepth: 1

   ToO-input.ecsv : Minimal information used to derive the Targets of Opportunity ledger <ToO-input>
   ToO.ecsv : Targets of Opportunity ledger in a form that can be read by fiberassign (tile overrides) <ToO>
   ToO-fiber.ecsv : Targets of Opportunity ledger in a form that can be read by fiberassign (fiber overrides) <ToO-fiber>
