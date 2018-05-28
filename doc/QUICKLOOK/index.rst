=========
QUICKLOOK
=========

.. toctree::
   :maxdepth: 1

   ql-checkHDUs-{camera}-{expid}.json : QA output providing the result of matching camera and expid between the argument and the raw header 
   
   ql-getbias-{camera}-{expid}.json : QA output concerning bias in oversan 
   
   ql-getrms-{camera}-{expid}.json : QA output concerning RMS in preprocessed image 
   
   ql-countpix-{camera}-{expid}.json : QA output counting pixels above threshold in preprocessed image 
   
   ql-xwsigma-{camera}-{expid}.json : QA output fitting X and W sigmas to preprocessed spectra
   
   ql-countbins-{camera}-{expid}.json : QA output counting bins in spectrum above thresholds 
   
   ql-skycont-{camera}-{expid}.json : QA output from sky continuum calculation 
   
   ql-skypeak-{camera}-{expid}.json : QA output calculating statistics at peak sky wavelengths   
   
   ql-skyresid-{camera}-{expid}.json : QA output providing residuals for sky fibers after subtraction 
   
   ql-integ-{camera}-{expid}.json : QA output calculating total counts for standard stars 
   
   ql-snr-{camera}-{expid}.json : QA output for the signal to noise calculation after sky subtraction 
   
   ql-mergedQA-{camera}-{expid}.json : contains the content of all the individual QA dictionaries listed above grouped based on the tasks that they accomplish: CHECK_HDUs, CHECK_CCDs, CHECK_FIBERS, CHECK_SPECTRA 
