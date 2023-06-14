.. _lsscats:


=======
LSScats
=======

``$DESI_ROOT/vac/RELEASE/lss/SPECPROD/SURVEY/VERSION/LSScats`` contains the directories for ``full`` (including information on all targets) and ``clustering`` (only information needed for clustering measurements and weights/cuts to optimize those clustering measurements). Files detailing the estimated n(z) in units of (h/Mpc)^3 are also here.

Catalogs were created for the four extra-galactic DESI target types: LRG, ELG, QSO, and BGS. For all except QSO, catalogs are produced for additional sub-type definitions. In the cases where the sub-type corresponds to a bitname from `SV3 targeting`_, we use that name:

* The additional LRG selection, named LRG_main, keeps only targets that satisfy the main survey selection (see `Zhou et al. (2022)`_ for details).

* The ELG sample is cut in three additional ways. First, ELG_HIP contains only the ~75% of the ELG sample that is at higher priority (see `Raichoor et al. (2022)`_ for more details). Then, for each of ELG and ELG_HIP, we also remove QSO targets.

* QSO targets have the highest priority and one may wish to therefore treat any targets that satisfy both the QSO and ELG selections within the QSO analysis.

* Finally, there are two BGS samples: BGS_ANY and BGS_BRIGHT. BGS_ANY is the combination of both the BGS_BRIGHT and BGS_FAINT BGS selections. See `Hahn et al. (2023)`_ for more details.

.. _SV3 targeting: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv3/data/sv3_targetmask.yaml
.. _Zhou et al. (2022): https://iopscience.iop.org/article/10.3847/1538-3881/aca5fb
.. _Raichoor et al. (2022): https://iopscience.iop.org/article/10.3847/1538-3881/acb213
.. _Hahn et al. (2023): https://iopscience.iop.org/article/10.3847/1538-3881/accff8

.. toctree::
   :maxdepth: 1

   TARGET_PHOTSYS_nz.txt : Target densities as a function of redshift <nz_lss>
   clustering/index
   full/index
