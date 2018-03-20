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
# Clean up log files.
#
[[ -f ${SCRATCH}/DESI_SPECTRO_DATA_${run}.log ]] && /bin/rm -f ${SCRATCH}/DESI_SPECTRO_DATA_${run}.log
[[ -f ${SCRATCH}/DESI_SPECTRO_REDUX_${run}.log ]] && /bin/rm -f ${SCRATCH}/DESI_SPECTRO_REDUX_${run}.log
[[ -f ${SCRATCH}/DESI_SPECTRO_SIM_${run}.log ]] && /bin/rm -f ${SCRATCH}/DESI_SPECTRO_SIM_${run}.log
[[ -f ${SCRATCH}/DESI_TARGET_${run}.log ]] && /bin/rm -f ${SCRATCH}/DESI_TARGET_${run}.log && touch ${SCRATCH}/DESI_TARGET_${run}.log
#
# Run the tests.
#
check_model DESI_SPECTRO_DATA ${DESI_SPECTRO_DATA} > ${SCRATCH}/DESI_SPECTRO_DATA_${run}.log 2>&1
check_model DESI_SPECTRO_REDUX ${DESI_SPECTRO_REDUX} > ${SCRATCH}/DESI_SPECTRO_REDUX_${run}.log 2>&1
check_model DESI_SPECTRO_SIM ${DESI_SPECTRO_SIM} > ${SCRATCH}/DESI_SPECTRO_SIM_${run}.log 2>&1
check_model -F DESI_TARGET/mtl.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/mtl.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/sky.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/sky.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/stdstar.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/standards-dark.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/stdstar.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/standards-bright.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/targets.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/targets.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/truth.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/targets/truth.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
check_model -F DESI_TARGET/fiberassign/tile.rst /global/projecta/projectdirs/desi/datachallenge/reference_runs/${run}/fiberassign/tile_11108.fits >> ${SCRATCH}/DESI_TARGET_${run}.log 2>&1
