#!/bin/bash
#
# Set up the environment like the minitest notebook.
#
if [[ $# < 1 ]]; then
    echo "You must specify a particular reference run, e.g. 18.2!"
    exit 1
fi
run=$1
basedir=/global/project/projectdirs/desi/datachallenge/reference_runs/${run}
export DESISURVEY_OUTPUT=${basedir}/survey
export DESI_SPECTRO_REDUX=${basedir}/spectro/redux
export DESI_SPECTRO_SIM=${basedir}/spectro/sim
export PIXPROD=mini
export SPECPROD=mini
export DESI_SPECTRO_DATA=${DESI_SPECTRO_SIM}/${PIXPROD}
#
# Run the tests.
#
for d in DESI_SPECTRO_DATA DESI_SPECTRO_REDUX DESI_SPECTRO_SIM DESISURVEY_OUTPUT; do
    [[ -f ${SCRATCH}/${d}_${run}.log ]] && /bin/rm -f ${SCRATCH}/${d}_${run}.log
    check_model ${d} ${!d} > ${SCRATCH}/${d}_${run}.log 2>&1
done
[[ -f ${SCRATCH}/DESI_TARGET_${run}.log ]] && /bin/rm -f ${SCRATCH}/DESI_TARGET_${run}.log && touch ${SCRATCH}/DESI_TARGET_${run}.log
check_model -F DESI_TARGET/mtl.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/mtl-dark.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/skies.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/sky.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
# check_model -F DESI_TARGET/stdstar.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/standards-dark.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
# check_model -F DESI_TARGET/stdstar.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/standards-bright.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/targets.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/targets-dark.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/truth.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/truth-dark.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/fiberassign/tile-TILEID-FIELDNUM.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/fiberassign/tile-011108.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
