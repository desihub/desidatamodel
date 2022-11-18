=================
Bit Masks in DESI
=================

This page linkgs to the URLs defining the bitmasks found in DESI.

Redshift fitting (Redrock) masks

=================================== ==================
BIT_MASK                            URL
=================================== ==================
ZWARN		                        `ZWARN`_
=================================== ==================

Target masks

=================================== ==================
BIT_MASK                            URL
=================================== ==================
CMX_TARGET		                    `CMX`_ 
SV1_DESI_TARGET	                    `SV1`_
SV1_BGS_TARGET	                    `SV1`_
SV1_MWS_TARGET	                    `SV1`_	
SV2_DESI_TARGET	                    `SV2`_
SV2_BGS_TARGET	                    `SV2`_
SV2_MWS_TARGET	                    `SV2`_
SV2_SCND_TARGET	                    `SV2`_
SV3_DESI_TARGET                     `SV3`_
SV3_BGS_TARGET	                    `SV3`_
SV3_MWS_TARGET	                    `SV3`_
SV3_SCND_TARGET	                    `SV3`_
DESI_TARGET		                    `TARGET`_
BGS_TARGET		                    `TARGET`_
MWS_TARGET		                    `TARGET`_
SCND_TARGET		                    `TARGET`_
OBSCONDITIONS		                `TARGET_L188`_
=================================== ==================

Fiberstatus masks

=================================== ==================
BIT_MASK                            URL
=================================== ==================
QAFIBERSTATUS	                    `MASKBITS_L55`_
FIBERSTATUS		                    `MASKBITS_L55`_
COADD_FIBERSTATUS                   `MASKBITS_L55`_
MASK		                        `MASKBITS_L84`_
=================================== ==================


Imaging masks

=================================== ==================
BIT_MASK                            URL
=================================== ==================
WISEMASK_W1		                    `BITMASKS_LEGACY`_
WISEMASK_W2		                    `BITMASKS_LEGACY`_
MASKBITS		                    `BITMASKS_LEGACY`_
=================================== ==================


.. _`CMX`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/cmx/data/cmx_targetmask.yaml
.. _`SV1`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv1/data/sv1_targetmask.yaml
.. _`SV2`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv2/data/sv2_targetmask.yaml
.. _`SV3`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/sv3/data/sv3_targetmask.yaml
.. _`TARGET`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml
.. _`MASKBITS_L55`: https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L55
.. _`TARGET_L188`: https://github.com/desihub/desitarget/blob/2.5.0/py/desitarget/data/targetmask.yaml#L188
.. _`MASKBITS_L84`: https://github.com/desihub/desispec/blob/0.55.0/py/desispec/maskbits.py#L84
.. _`ZWARN`: https://github.com/desihub/redrock/blob/0.16.0/py/redrock/zwarning.py#L14
.. _`BITMASKS_LEGACY`: https://www.legacysurvey.org/dr9/bitmasks/