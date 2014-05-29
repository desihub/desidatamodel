=========================
Datamodel: DECam_00200666
=========================

General Description
===================

Summary
-------

*This section should be filled in with a high-level description of this file.
In general, you should remove or replace the emphasized text (\*this text
is emphasized\*) in this document.*

Naming Convention
-----------------

``DECam_00200666.fits.fz``, where ...  *The filename should be replaced with a regular expression
that matches the filename.  Also give a human-readable description of the
filename. For example, a six-digit number would correspond to ``[0-9]{6}``.*

File Type
---------

FITS, 536 MB  *This section gives the type of the file and its approximate size.*

Contents
========

====== ======= ======== ===================
Number EXTNAME Type     Contents           
====== ======= ======== ===================
HDU00_         IMAGE    *Brief Description*
HDU01_ S1      BINTABLE *Brief Description*
HDU02_ S2      BINTABLE *Brief Description*
HDU03_ S3      BINTABLE *Brief Description*
HDU04_ N1      BINTABLE *Brief Description*
HDU05_ N2      BINTABLE *Brief Description*
HDU06_ N3      BINTABLE *Brief Description*
HDU07_ S8      BINTABLE *Brief Description*
HDU08_ S9      BINTABLE *Brief Description*
HDU09_ S14     BINTABLE *Brief Description*
HDU10_ S15     BINTABLE *Brief Description*
HDU11_ S20     BINTABLE *Brief Description*
HDU12_ S25     BINTABLE *Brief Description*
HDU13_ N8      BINTABLE *Brief Description*
HDU14_ N9      BINTABLE *Brief Description*
HDU15_ N14     BINTABLE *Brief Description*
HDU16_ N15     BINTABLE *Brief Description*
HDU17_ N20     BINTABLE *Brief Description*
HDU18_ N25     BINTABLE *Brief Description*
HDU19_ S10     BINTABLE *Brief Description*
HDU20_ S11     BINTABLE *Brief Description*
HDU21_ S12     BINTABLE *Brief Description*
HDU22_ S13     BINTABLE *Brief Description*
HDU23_ S18     BINTABLE *Brief Description*
HDU24_ S19     BINTABLE *Brief Description*
HDU25_ S16     BINTABLE *Brief Description*
HDU26_ S17     BINTABLE *Brief Description*
HDU27_ S21     BINTABLE *Brief Description*
HDU28_ S22     BINTABLE *Brief Description*
HDU29_ S23     BINTABLE *Brief Description*
HDU30_ S24     BINTABLE *Brief Description*
HDU31_ S26     BINTABLE *Brief Description*
HDU32_ S27     BINTABLE *Brief Description*
HDU33_ S28     BINTABLE *Brief Description*
HDU34_ S29     BINTABLE *Brief Description*
HDU35_ S30     BINTABLE *Brief Description*
HDU36_ S31     BINTABLE *Brief Description*
HDU37_ N4      BINTABLE *Brief Description*
HDU38_ N5      BINTABLE *Brief Description*
HDU39_ N6      BINTABLE *Brief Description*
HDU40_ N7      BINTABLE *Brief Description*
HDU41_ S4      BINTABLE *Brief Description*
HDU42_ S5      BINTABLE *Brief Description*
HDU43_ S6      BINTABLE *Brief Description*
HDU44_ S7      BINTABLE *Brief Description*
HDU45_ N10     BINTABLE *Brief Description*
HDU46_ N11     BINTABLE *Brief Description*
HDU47_ N12     BINTABLE *Brief Description*
HDU48_ N13     BINTABLE *Brief Description*
HDU49_ N18     BINTABLE *Brief Description*
HDU50_ N19     BINTABLE *Brief Description*
HDU51_ N16     BINTABLE *Brief Description*
HDU52_ N17     BINTABLE *Brief Description*
HDU53_ N21     BINTABLE *Brief Description*
HDU54_ N22     BINTABLE *Brief Description*
HDU55_ N23     BINTABLE *Brief Description*
HDU56_ N24     BINTABLE *Brief Description*
HDU57_ N26     BINTABLE *Brief Description*
HDU58_ N27     BINTABLE *Brief Description*
HDU59_ N28     BINTABLE *Brief Description*
HDU60_ N29     BINTABLE *Brief Description*
HDU61_ N30     BINTABLE *Brief Description*
HDU62_ N31     BINTABLE *Brief Description*
HDU63_ FS1     BINTABLE *Brief Description*
HDU64_ FS2     BINTABLE *Brief Description*
HDU65_ FS3     BINTABLE *Brief Description*
HDU66_ FS4     BINTABLE *Brief Description*
HDU67_ FN1     BINTABLE *Brief Description*
HDU68_ FN2     BINTABLE *Brief Description*
HDU69_ FN3     BINTABLE *Brief Description*
====== ======= ======== ===================


FITS Header Units
=================

HDU00
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

============= ======================================================== ===== ==============================================
KEY           Value                                                    Type  Comment                                       
============= ======================================================== ===== ==============================================
NEXTEND       70                                                       int   Number of extensions                          
PROCTYPE      RAW                                                      str   Data processing level                         
PRODTYPE      image                                                    str   Data product type                             
DETSIZE       [1:29400,1:29050]                                        str   Detector size                                 
PIXSCAL1      0.27                                                     float [arcsec/pixel] Pixel scale, axis 1            
PIXSCAL2      0.27                                                     float [arcsec/pixel] Pixel scale, axis 2            
FILENAME      DECam_00200666.fits                                      str   Filename                                      
OBS-LONG      70.81489                                                 float [deg] Observatory east longitude              
TELESCOP      CTIO 4.0-m telescope                                     str   Telescope name                                
OBSERVAT      CTIO                                                     str   Observatory name                              
OBS-LAT       -30.16606                                                float [deg] Observatory latitude                    
OBS-ELEV      2215.0                                                   float [m] Observatory elevation                     
INSTRUME      DECam                                                    str   Instrument used to obtain these data          
EXPREQ        100.0                                                    float [s] Requested exposure duration               
EXPTIME       100.0                                                    float [s] Exposure duration                         
DARKTIME      100.8952999                                              float [s] Dark time                                 
OBSID         ct4m20130422t080259                                      str   Unique Observation ID                         
DATE-OBS      2013-04-22T08:02:59.601219                               str    UTC epoch                                    
TIME-OBS      08:02:59.601219                                          str   Time of observation start (UTC)               
MJD-OBS       56404.3354121                                            float MJD of observation start                      
OPENSHUT      2013-04-22T08:02:59.426080                               str   Time when shutter opened (UTC)                
RADESYS       FK5                                                      str   Telescope coordinate system                   
TIMESYS       UTC                                                      str   Time system                                   
EXPNUM        200666                                                   int   DECam exposure number                         
OBJECT        23740571.0                                               str   Object name                                   
OBSTYPE       object                                                   str   Observation type                              
CAMSHUT       Open                                                     str   Camera shutter at exposure start              
PROGRAM       An i-band Survey of the Equatorial Sky for MS-DESI       str   Current observi                               
OBSERVER      Abbott                                                   str   Observer name(s)                              
PROPOSER      Schlegel                                                 str   Proposal Principle Investigator               
DTPI          Schlegel                                                 str    Principal Investigator                       
PROPID        2013A-0741                                               str   Proposal ID                                   
EXCLUDED                                                               str   DECam components not used for this frame      
SEQID         23900321_                                                str   Sequence name                                 
SEQNUM        16                                                       int   Number of image in sequence                   
SEQTOT        16                                                       int   Total number of images in sequence            
AOS           T                                                        bool  AOS information availability                  
BCAM          T                                                        bool  BCAM data available if true                   
GUIDER        1                                                        int   Guider (0-absent,1-ok,2-lost star,3-los       
SKYSTAT       T                                                        bool  Cloud camera (RASICAM) available if true      
FILTER        z DECam SDSS c0004 9260.0 1520.0                         str   Unique filter identifier                      
FILTPOS       cassette_3                                               str   Filter position in FCM                        
INSTANCE      DECam_20130421                                           str   SISPI instance name                           
ERRORS        None                                                     str   SISPI readout errors                          
TELEQUIN      2000.0                                                   float Equinox of telescope coordinates              
RA            15:49:47.297                                             str   [HH:MM:SS] Target RA                          
DEC           05:43:04.141                                             str   [DD:MM:SS] Target DEC                         
TELRA         15:49:47.348                                             str   [HH:MM:SS] Telescope RA                       
TELDEC        05:43:03.400                                             str   [DD:MM:SS] Telescope DEC                      
TELFOCUS      1451.31,-2890.19,2063.31,130.99,-35.55,-0.00             str   DECam hexapod setting                         
DOMEFLOR      16.1                                                     float [deg C] Dome floor temperature                
G-MEANX       -0.0024                                                  float [arcsec] Guider x-axis mean offset            
G-MEANY       0.0578                                                   float [arcsec] Guider y-axis mean offset            
MAIRTEMP      16.1                                                     float [deg C] Mirror temperature above surface      
DONUTFS4      [0.11,0.90,-8.95,-0.37,0.10,0.14,0.42,-0.05,-0.51,]      str   Mean Wavefront                                
DONUTFS3      [-0.54,1.47,8.74,-0.34,0.14,0.15,0.36,0.11,-0.56,]       str   Mean Wavefront                                
DONUTFS2      [0.40,-0.10,-8.73,-0.18,0.23,0.01,0.46,0.37,-0.09,]      str   Mean Wavefront                                
DONUTFS1      [-0.09,1.48,9.00,-0.25,0.19,0.13,0.26,0.26,0.03,]        str   Mean Wavefront f                              
UTE-TEMP      15.95                                                    float [deg C] Upper truss temperature east          
G-FLXVAR      85735560.972                                             float [arcsec] Guider mean guide star flux variances
G-MEANXY      0.00176                                                  float [arcsec2] Guider (xy) 2nd moment mean offset  
PMW-TEMP      15.9                                                     float [deg C] Mirror west edge temperature          
LSKYPOW       0.03                                                     float RASICAM local sky normalized power            
WINDDIR       30.0                                                     float [deg] Wind direction (from North)             
UPTRTEMP      16.058                                                   float [deg C] Upper truss average temperature       
DONUTFN1      [0.39,0.19,-8.89,-0.58,-0.36,0.02,0.02,0.33,-0.35,]      str   Mean Wavefront                                
DONUTFN2      [1.40,1.24,9.77,-0.21,-0.17,-0.10,-0.06,0.58,-0.22,]     str   Mean Wavefron                                 
DONUTFN3      [0.73,0.80,-8.82,-0.20,-0.40,0.14,-0.12,0.09,0.26,]      str   Mean Wavefront                                
DONUTFN4      [0.98,0.61,8.53,-0.19,-0.89,0.20,-0.09,-0.10,0.03,]      str   Mean Wavefront                                
LSKYPHOT      T                                                        bool  RASICAM local sky clear flag                  
time_recorded 2013-04-22T08:05:02.510670                               str                                                 
G-FEEDBK      10                                                       int   [%] Guider feedback                           
G-CCDNUM      4                                                        int   Number of guide CCDs that remained active     
DOXT          0.15                                                     float [arcsec] X-theta from donut analysis          
MSURTEMP      15.775                                                   float [deg C] Mirror surface average temperature    
OUTTEMP       15.3                                                     float [deg C] Outside temperature                   
G-MAXX        0.2578                                                   float [arcsec] Guider x-axis maximum offset         
FADZ          -14.19                                                   float [um] FA Delta focus.                          
FADY          -29.9                                                    float [um] FA Delta Y.                              
FADX          93.48                                                    float [um] FA Delta X.                              
G-MODE        auto                                                     str   Guider operation mode                         
FAYT          3.46                                                     float [arcsec] FA Delta Y-theta.                    
LSKYVAR       0.0                                                      float RASICAM local sky standard deviation          
LST           17:21:46.1                                               str   LST at observation start (HH:MM:SS)           
PMN-TEMP      15.4                                                     float [deg C] Mirror edge surface temperature       
DODZ          -14.19                                                   float [um] Delta-Z from donut analysis              
DODY          -0.42                                                    float [um] Y-decenter from donut analysis           
DODX          -0.82                                                    float [um] X-decenter from donut analysis           
DIMMSEE       0.362                                                    float [arcsec] DIMM Seeing                          
GSKYPHOT      T                                                        bool  RASICAM global sky clear flag                 
BCAMAZ        0.0                                                      float [arcsec] BCAM hexapod rot. about z-axis       
MULTIEXP      F                                                        bool  Frame contains multiple exposures if true     
BCAMAX        -93.767                                                  float [arcsec] BCAM hexapod rot. about x-axis       
BCAMAY        83.77                                                    float [arcsec] BCAM hexapod rot. about y-axis       
DOMEHIGH      -999                                                     int   [deg C] High dome temperature                 
LSKYHOT       0.0                                                      float RASICAM local sky fraction above threshold    
ZD            41.99                                                    float [deg] Telescope zenith distance               
BCAMDY        2538.279                                                 float [micron] BCAM hexapod y-offset                
TELSTAT       Track                                                    str   Telescope tracking status                     
GSKYHOT       0.03                                                     float RASICAM global sky fraction above threshold   
DOMELOW       16.58                                                    float [deg C] Low dome temperature                  
BCAMDX        -950.966                                                 float [micron] BCAM hexapod x-offset                
PRESSURE      780.0                                                    float [Torr] Barometric pressure (outside)          
SKYUPDAT      2013-04-22T08:00:02                                      str   Time of last RASICAM exposure (UTC)           
G-SEEING      1.621                                                    float [arcsec] Guider average seeing                
G-TRANSP      1.256                                                    float Guider average sky transparency               
AZ            324.79                                                   float [deg] Telescope azimuth angle                 
G-MEANY2      0.011417                                                 float [arcsec2] Guider (y) 2nd moment mean offset   
PME-TEMP      16.1                                                     float [deg C] Mirror east edge temperature          
DOYT          0.29                                                     float [arcsec] Y-theta from donut analysis          
UTS-TEMP      16.08                                                    float [deg C] Upper truss temperature south         
AIRMASS       1.34                                                     float Airmass                                       
HA            01:31:25.29                                              str   [HH:MM:SS] Telescope hour angle               
G-LATENC      1.227                                                    float [s] Guider avg. latency between exposures     
PMOSTEMP      16.1                                                     float [deg C] Primary mirror top surface temperature
UTW-TEMP      16.28                                                    float [deg C] Upper truss temperature west          
HUMIDITY      15.0                                                     float [%] Ambient relative humidity (outside)       
LUTVER        working-trunk                                            str   Hexapod Lookup Table version                  
WINDSPD       16.254                                                   float [m/s] Wind speed                              
FAXT          -6.73                                                    float [arcsec] FA Delta X-theta.                    
VSUB          T                                                        bool  True if CCD substrate voltage is on           
GSKYVAR       0.03                                                     float RASICAM global sky standard deviation         
G-MAXY        0.2873                                                   float [arcsec] Guider y-axis maximum offset         
G-MEANX2      0.011449                                                 float [arcsec2] Guider (x) 2nd moment mean offset   
LWTRTEMP      -999                                                     int   [deg C] Lower truss temperature               
UTN-TEMP      15.92                                                    float [deg C] Upper truss temperature north         
PMS-TEMP      15.7                                                     float [deg C] Mirror south edge temperature         
SISPIVER      trunk                                                    str   SISPI software version                        
CONSTVER      DECAM:19                                                 str   SISPI constants version                       
HDRVER        13                                                       str   DECam fits header version                     
CHECKVER      COMPLEMENT                                               str    FITS checksum version                        
CHECKSUM      33BM409M30AM309M                                         str    ASCII 1's complement checksum                
DATASUM       0                                                        str    checksum of data records                     
DTSITE        ct                                                       str    observatory location                         
DTTELESC      ct4m                                                     str    telescope identifier                         
DTINSTRU      decam                                                    str    instrument identifier                        
DTCALDAT      2013-04-21                                               str    calendar date from observing schedule        
ODATEOBS                                                               str    previous DATE-OBS                            
DTUTC         2013-04-22T08:05:30                                      str    post exposure UTC epoch from DTS             
DTOBSERV      NOAO                                                     str    scheduling institution                       
DTPROPID      2013A-0741                                               str    observing proposal ID                        
DTPIAFFL                                                               str    PI affiliation                               
DTTITLE                                                                str    title of observing proposal                  
DTCOPYRI      AURA                                                     str    copyright holder of data                     
DTACQUIS      pipeline3.ctio.noao.edu                                  str    host name of data acquisition computer       
DTACCOUN      sispi                                                    str    observing account name                       
DTACQNAM      /data_local/images/DTS/2013A-0741/DECam_00200666.fits.fz str    file na                                      
DTNSANAM      dec073130.fits                                           str    file name in NOAO Science Archive            
DTQUEUE       des                                                      str    DTS queue (40704)                            
DTSTATUS      done                                                     str    data transport status                        
SB_HOST       pipeline3.ctio.noao.edu                                  str    iSTB client host                             
SB_ACCOU      sispi                                                    str    iSTB client user account                     
SB_SITE       ct                                                       str    iSTB host site                               
SB_LOCAL      dec                                                      str    locale of iSTB daemon                        
SB_DIR1       20130421                                                 str    level 1 directory in NSA DS                  
SB_DIR2       ct4m                                                     str    level 2 directory in NSA DS                  
SB_DIR3       2013A-0741                                               str    level 3 directory in NSA DS                  
SB_RECNO      73130                                                    int    iSTB sequence number                         
SB_ID         dec073130                                                str    unique iSTB identifier                       
SB_NAME       dec073130.fits                                           str    name assigned by iSTB                        
RMCOUNT       0                                                        int    remediation counter                          
RECNO         73130                                                    int    NOAO Science Archive sequence number         
============= ======================================================== ===== ==============================================

HDU01
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ==================== ===== ===========================================
KEY      Value                Type  Comment                                    
======== ==================== ===== ===========================================
ZIMAGE   T                    bool  extension contains compressed image        
ZTILE1   2160                 int   size of tiles to be compressed             
ZTILE2   1                    int   size of tiles to be compressed             
ZCMPTYPE RICE_1               str   compression algorithm                      
ZNAME1   BLOCKSIZE            str   compression block size                     
ZVAL1    32                   int   pixels per block                           
ZNAME2   BYTEPIX              str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                    int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                str   IMAGE extension                            
ZBITPIX  16                   int   number of bits per data pixel              
ZNAXIS   2                    int   number of data axes                        
ZNAXIS1  2160                 int   length of data axis 1                      
ZNAXIS2  4146                 int   length of data axis 2                      
ZPCOUNT  0                    int   required keyword; must = 0                 
ZGCOUNT  1                    int   required keyword; must = 1                 
BZERO    32768                int   offset data range to that of unsigned short
BSCALE   1                    int   default scaling factor                     
BUNIT    adu                  str   Brightness units for pixel array           
WCSAXES  2                    int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]    str   Detector size                              
TRIMSEC  [57:2104,51:4146]    str   Good section                               
DATASEC  [57:2104,51:4146]    str   Data section to display                    
DETSEC   [12289:14336,1:4096] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]      str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]  str   Good section from amp A                    
DETSECA  [13313:14336,1:4096] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]   str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]   str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]  str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]  str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]  str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]     str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]    str   Good section from amp B                    
DETSECB  [12289:13312,1:4096] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]      str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]      str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]    str   Data section from amp B                    
BIASSECB [7:56,51:4146]       str   Overscan from amp B                        
PRESECB  [1:6,51:4146]        str   Prescan from amp B                         
POSTSECB [57:1080,1:50]       str   Postscan from amp B                        
DETECTOR S3-111_107419-8-3    str   Detector Identifier                        
CCDNUM   25                   int   CCD number                                 
DETPOS   S1                   str   detector position ID                       
EXTNAME  S1                   str   extension name                             
GAINA    4.59347726229        float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096        float [electrons] Read noise for amp A           
SATURATA 43266.0              float [adu] Saturation for amp A                 
GAINB    4.4014084507         float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127        float [electrons] Read noise for amp B           
SATURATB 44935.0              float [adu] Saturation for amp B                 
CRPIX1   2151.2               float Coordinate Reference axis 1                
CRPIX2   14826.0              float Coordinate Reference axis 2                
FPA      DECAM_BKP1           str   DECam focal plane name                     
INHERIT  T                    bool  Inherits PHDU header                       
CCDBIN1  1                    int   Pixel binning, axis 1                      
CCDBIN2  1                    int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware  str   DHE Hardware                               
DHEFIRM  demo30               str   DHE Firmware                               
SLOT00   MCB 15 5.210000      str   Monsoon module                             
SLOT01   DESCB 22 4.010000    str   Monsoon module                             
SLOT02   DESCB 3 4.010000     str   Monsoon module                             
SLOT03   CCD12 16 4.080000    str   Monsoon module                             
SLOT04   CCD12 11 4.080000    str   Monsoon module                             
SLOT05   CCD12 14 4.080000    str   Monsoon module                             
RADESYS  FK5                  str   World coordinate reference frame           
EQUINOX  2000.0               float [yr] Equinox of WCS                        
PV1_7    0.01641672826        float PV distortion coefficient                  
CUNIT1   deg                  str                                              
PV2_8    -0.00246200658752    float PV distortion coefficient                  
PV2_9    0.00641298947322     float PV distortion coefficient                  
CD1_1    -1.8249413473e-07    float World coordinate transformation matrix     
LTM2_2   1.0                  float Detector to image transformation           
LTM2_1   0.0                  float Detector to image transformation           
PV2_0    -0.000677378816994   float PV distortion coefficient                  
PV2_1    1.01170064187        float PV distortion coefficient                  
PV2_2    -0.00154844123095    float PV distortion coefficient                  
PV2_3    0.0                  float PV distortion coefficient                  
PV2_4    -0.000974573910792   float PV distortion coefficient                  
PV2_5    0.015516347937       float PV distortion coefficient                  
PV2_6    -0.00176930825331    float PV distortion coefficient                  
PV2_7    -0.00664988058298    float PV distortion coefficient                  
LTM1_1   1.0                  float Detector to image transformation           
PV1_6    0.00735227852542     float PV distortion coefficient                  
PV2_10   -0.000605534691727   float PV distortion coefficient                  
PV1_4    0.0440579429998      float PV distortion coefficient                  
PV1_3    0.0                  float PV distortion coefficient                  
PV1_2    -0.00253295758814    float PV distortion coefficient                  
PV1_1    1.03899426784        float PV distortion coefficient                  
PV1_0    0.0107262491558      float PV distortion coefficient                  
LTM1_2   0.0                  float Detector to image transformation           
PV1_9    0.00562233785525     float PV distortion coefficient                  
PV1_8    -0.00253592468977    float PV distortion coefficient                  
CD1_2    7.28535892432e-05    float World coordinate transformation matrix     
PV1_5    -0.00480948264558    float PV distortion coefficient                  
CUNIT2   deg                  str                                              
CD2_1    -7.28499004539e-05   float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07   float World coordinate transformation matrix     
LTV2     50.0                 float Detector to image transformation           
LTV1     56.0                 float Detector to image transformation           
PV1_10   -0.00235436587955    float PV distortion coefficient                  
CTYPE2   DEC--TPV             str   Coordinate type                            
CTYPE1   RA---TPV             str   Coordinate type                            
CRVAL1   237.447283           float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611             float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                    bool  Data from amp A is valid                   
VALIDB   T                    bool  Data from amp B is valid                   
NDONUTS  0                    int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT           str    FITS checksum version                     
CHECKSUM IG6GIE5EIE5EIE5E     str    ASCII 1's complement checksum             
DATASUM  1647561873           str    checksum of data records                  
======== ==================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU02
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [12289:14336,4097:8192] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [13313:14336,4097:8192] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [12289:13312,4097:8192] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-318_135959-18-1      str   Detector Identifier                        
CCDNUM   26                      int   CCD number                                 
DETPOS   S2                      str   detector position ID                       
EXTNAME  S2                      str   extension name                             
GAINA    4.15454923141           float [electrons/adu] Gain for amp A             
RDNOISEA 6.70627336934           float [electrons] Read noise for amp A           
SATURATA 51115.0                 float [adu] Saturation for amp A                 
GAINB    4.36490615452           float [electrons/adu] Gain for amp B             
RDNOISEB 6.66564818856           float [electrons] Read noise for amp B           
SATURATB 48203.0                 float [adu] Saturation for amp B                 
CRPIX1   2151.2                  float Coordinate Reference axis 1                
CRPIX2   10566.67                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.000932904429272       float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    -0.000532086316333      float PV distortion coefficient                  
PV2_9    -0.000951469811349      float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.000241371415359      float PV distortion coefficient                  
PV2_1    1.00634640803           float PV distortion coefficient                  
PV2_2    -0.000678920484082      float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00108612482548        float PV distortion coefficient                  
PV2_5    0.00298838134435        float PV distortion coefficient                  
PV2_6    -0.000994737099299      float PV distortion coefficient                  
PV2_7    -0.0084255171603        float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.000743722380747       float PV distortion coefficient                  
PV2_10   -0.000524222785678      float PV distortion coefficient                  
PV1_4    0.00706672131479        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    -0.000494202178797      float PV distortion coefficient                  
PV1_1    1.00926265422           float PV distortion coefficient                  
PV1_0    0.00198866770483        float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    -0.00232172367327       float PV distortion coefficient                  
PV1_8    -0.00157523378801       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.0018113198119        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   -0.000849228922475      float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM OnE8Rk97OkE7Ok97        str    ASCII 1's complement checksum             
DATASUM  1928406351              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU03
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [12289:14336,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [13313:14336,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [12289:13312,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-106_123194-8-1        str   Detector Identifier                        
CCDNUM   27                       int   CCD number                                 
DETPOS   S3                       str   detector position ID                       
EXTNAME  S3                       str   extension name                             
GAINA    4.40722785368            float [electrons/adu] Gain for amp A             
RDNOISEA 7.08065226972            float [electrons] Read noise for amp A           
SATURATA 37551.0                  float [adu] Saturation for amp A                 
GAINB    4.66417910448            float [electrons/adu] Gain for amp B             
RDNOISEB 7.01166044776            float [electrons] Read noise for amp B           
SATURATB 30170.0                  float [adu] Saturation for amp B                 
CRPIX1   2151.2                   float Coordinate Reference axis 1                
CRPIX2   6307.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00440484672136        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    -0.000307854154318       float PV distortion coefficient                  
PV2_9    -0.00352520228697        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.000325615027275       float PV distortion coefficient                  
PV2_1    1.00564823323            float PV distortion coefficient                  
PV2_2    -0.000225899079434       float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.000788257093916        float PV distortion coefficient                  
PV2_5    0.000212733050612        float PV distortion coefficient                  
PV2_6    -3.48704288742e-05       float PV distortion coefficient                  
PV2_7    -0.00766248036918        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.000216149836895       float PV distortion coefficient                  
PV2_10   -3.34749389109e-05       float PV distortion coefficient                  
PV1_4    -0.000525017549007       float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00019526375756         float PV distortion coefficient                  
PV1_1    1.00548328858            float PV distortion coefficient                  
PV1_0    0.000680586273106        float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00394529797132        float PV distortion coefficient                  
PV1_8    -0.000359828630108       float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.000158582949783       float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000212500920195        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM WA4ia11ZY81fa81Z         str    ASCII 1's complement checksum             
DATASUM  76073449                 str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU04
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================== ===== ===========================================
KEY      Value                 Type  Comment                                    
======== ===================== ===== ===========================================
ZIMAGE   T                     bool  extension contains compressed image        
ZTILE1   2160                  int   size of tiles to be compressed             
ZTILE2   1                     int   size of tiles to be compressed             
ZCMPTYPE RICE_1                str   compression algorithm                      
ZNAME1   BLOCKSIZE             str   compression block size                     
ZVAL1    32                    int   pixels per block                           
ZNAME2   BYTEPIX               str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                     int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                 str   IMAGE extension                            
ZBITPIX  16                    int   number of bits per data pixel              
ZNAXIS   2                     int   number of data axes                        
ZNAXIS1  2160                  int   length of data axis 1                      
ZNAXIS2  4146                  int   length of data axis 2                      
ZPCOUNT  0                     int   required keyword; must = 0                 
ZGCOUNT  1                     int   required keyword; must = 1                 
BZERO    32768                 int   offset data range to that of unsigned short
BSCALE   1                     int   default scaling factor                     
BUNIT    adu                   str   Brightness units for pixel array           
WCSAXES  2                     int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]     str   Detector size                              
TRIMSEC  [57:2104,1:4096]      str   Good section                               
DATASEC  [57:2104,1:4096]      str   Data section to display                    
DETSEC   [14337:16384,1:4096]  str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]       str   CCD section to display                     
TRIMSECA [57:1080,1:4096]      str   Good section from amp A                    
DETSECA  [14337:15360,1:4096]  str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]       str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]       str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]      str   Data section from amp A                    
BIASSECA [7:56,1:4096]         str   Overscan from amp A                        
PRESECA  [1:6,1:4096]          str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]   str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]    str   Good section from amp B                    
DETSECB  [15361:16384,1:4096]  str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]    str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]    str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]    str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]    str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]    str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146] str   Postscan from amp B                        
DETECTOR S3-113_107419-19-2    str   Detector Identifier                        
CCDNUM   32                    int   CCD number                                 
DETPOS   N1                    str   detector position ID                       
EXTNAME  N1                    str   extension name                             
GAINA    4.33463372345         float [electrons/adu] Gain for amp A             
RDNOISEA 6.82661465106         float [electrons] Read noise for amp A           
SATURATA 50246.0               float [adu] Saturation for amp A                 
GAINB    4.35729847495         float [electrons/adu] Gain for amp B             
RDNOISEB 6.90893246187         float [electrons] Read noise for amp B           
SATURATB 48895.0               float [adu] Saturation for amp B                 
CRPIX1   -103.2001             float Coordinate Reference axis 1                
CRPIX2   14826.0               float Coordinate Reference axis 2                
FPA      DECAM_BKP1            str   DECam focal plane name                     
INHERIT  T                     bool  Inherits PHDU header                       
CCDBIN1  1                     int   Pixel binning, axis 1                      
CCDBIN2  1                     int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware   str   DHE Hardware                               
DHEFIRM  demo30                str   DHE Firmware                               
SLOT00   MCB 15 5.210000       str   Monsoon module                             
SLOT01   DESCB 22 4.010000     str   Monsoon module                             
SLOT02   DESCB 3 4.010000      str   Monsoon module                             
SLOT03   CCD12 16 4.080000     str   Monsoon module                             
SLOT04   CCD12 11 4.080000     str   Monsoon module                             
SLOT05   CCD12 14 4.080000     str   Monsoon module                             
RADESYS  FK5                   str   World coordinate reference frame           
EQUINOX  2000.0                float [yr] Equinox of WCS                        
PV1_7    0.0145310391448       float PV distortion coefficient                  
CUNIT1   deg                   str                                              
PV2_8    0.000254828190901     float PV distortion coefficient                  
PV2_9    0.00508855883805      float PV distortion coefficient                  
CD1_1    -1.8249413473e-07     float World coordinate transformation matrix     
LTM2_2   1.0                   float Detector to image transformation           
LTM2_1   0.0                   float Detector to image transformation           
PV2_0    0.000291154885356     float PV distortion coefficient                  
PV2_1    1.01017404727         float PV distortion coefficient                  
PV2_2    0.00171033952156      float PV distortion coefficient                  
PV2_3    0.0                   float PV distortion coefficient                  
PV2_4    -0.000777216617545    float PV distortion coefficient                  
PV2_5    0.0125587062442       float PV distortion coefficient                  
PV2_6    0.00246375252673      float PV distortion coefficient                  
PV2_7    -0.00673726785625     float PV distortion coefficient                  
LTM1_1   1.0                   float Detector to image transformation           
PV1_6    0.00523444472221      float PV distortion coefficient                  
PV2_10   0.000906957907489     float PV distortion coefficient                  
PV1_4    0.038781665797        float PV distortion coefficient                  
PV1_3    0.0                   float PV distortion coefficient                  
PV1_2    0.00189371725018      float PV distortion coefficient                  
PV1_1    1.03410682881         float PV distortion coefficient                  
PV1_0    0.00911572168589      float PV distortion coefficient                  
LTM1_2   0.0                   float Detector to image transformation           
PV1_9    0.00408989396628      float PV distortion coefficient                  
PV1_8    0.00205182171408      float PV distortion coefficient                  
CD1_2    7.28535892432e-05     float World coordinate transformation matrix     
PV1_5    0.00349119985963      float PV distortion coefficient                  
CUNIT2   deg                   str                                              
CD2_1    -7.28499004539e-05    float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07    float World coordinate transformation matrix     
LTV2     0.0                   float Detector to image transformation           
LTV1     56.0                  float Detector to image transformation           
PV1_10   -0.000315732801581    float PV distortion coefficient                  
CTYPE2   DEC--TPV              str   Coordinate type                            
CTYPE1   RA---TPV              str   Coordinate type                            
CRVAL1   237.447283            float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611              float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                     bool  Data from amp A is valid                   
VALIDB   T                     bool  Data from amp B is valid                   
NDONUTS  0                     int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT            str    FITS checksum version                     
CHECKSUM 3M2L4M1L3M1L3M1L      str    ASCII 1's complement checksum             
DATASUM  2983913610            str    checksum of data records                  
======== ===================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU05
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,1:4096]        str   Good section                               
DATASEC  [57:2104,1:4096]        str   Data section to display                    
DETSEC   [14337:16384,4097:8192] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [57:1080,1:4096]        str   Good section from amp A                    
DETSECA  [14337:15360,4097:8192] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]         str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]         str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]        str   Data section from amp A                    
BIASSECA [7:56,1:4096]           str   Overscan from amp A                        
PRESECA  [1:6,1:4096]            str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]     str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]      str   Good section from amp B                    
DETSECB  [15361:16384,4097:8192] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]      str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]      str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]      str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]      str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]      str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]   str   Postscan from amp B                        
DETECTOR S3-222_135959-11-1      str   Detector Identifier                        
CCDNUM   33                      int   CCD number                                 
DETPOS   N2                      str   detector position ID                       
EXTNAME  N2                      str   extension name                             
GAINA    4.35919790759           float [electrons/adu] Gain for amp A             
RDNOISEA 6.84481255449           float [electrons] Read noise for amp A           
SATURATA 47929.0                 float [adu] Saturation for amp A                 
GAINB    4.58505272811           float [electrons/adu] Gain for amp B             
RDNOISEB 7.00320953691           float [electrons] Read noise for amp B           
SATURATB 45425.0                 float [adu] Saturation for amp B                 
CRPIX1   -103.2001               float Coordinate Reference axis 1                
CRPIX2   10566.67                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00141790892896        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00137797695237        float PV distortion coefficient                  
PV2_9    -0.000858034421944      float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.000216043873597       float PV distortion coefficient                  
PV2_1    1.00655203179           float PV distortion coefficient                  
PV2_2    0.000565898669          float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.000171493196064       float PV distortion coefficient                  
PV2_5    0.00329952868394        float PV distortion coefficient                  
PV2_6    0.0010523108246         float PV distortion coefficient                  
PV2_7    -0.00634704348783       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.000694464354568       float PV distortion coefficient                  
PV2_10   0.000501383063559       float PV distortion coefficient                  
PV1_4    0.00797613445698        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.000396228352328       float PV distortion coefficient                  
PV1_1    1.00983082198           float PV distortion coefficient                  
PV1_0    0.00205124897342        float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    -0.00177706949994       float PV distortion coefficient                  
PV1_8    0.000849610300495       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    0.00101585136108        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   -0.00108961018617       float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM OVgARSg6OSgAOSg5        str    ASCII 1's complement checksum             
DATASUM  3603603040              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU06
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [14337:16384,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [14337:15360,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [15361:16384,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-313_135959-19-1       str   Detector Identifier                        
CCDNUM   34                       int   CCD number                                 
DETPOS   N3                       str   detector position ID                       
EXTNAME  N3                       str   extension name                             
GAINA    4.3233895374             float [electrons/adu] Gain for amp A             
RDNOISEA 6.64461738003            float [electrons] Read noise for amp A           
SATURATA 50010.0                  float [adu] Saturation for amp A                 
GAINB    4.46827524576            float [electrons/adu] Gain for amp B             
RDNOISEB 6.72966934763            float [electrons] Read noise for amp B           
SATURATB 55281.0                  float [adu] Saturation for amp B                 
CRPIX1   -103.2001                float Coordinate Reference axis 1                
CRPIX2   6307.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00387490274681        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    -0.000699659375611       float PV distortion coefficient                  
PV2_9    -0.00423046117408        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.000223364811806        float PV distortion coefficient                  
PV2_1    1.00550319855            float PV distortion coefficient                  
PV2_2    0.000231848849697        float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    -0.00220463025209        float PV distortion coefficient                  
PV2_5    -0.000291580114468       float PV distortion coefficient                  
PV2_6    -0.000269960626785       float PV distortion coefficient                  
PV2_7    -0.0131172260649         float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.000160569171009        float PV distortion coefficient                  
PV2_10   -0.000441300489993       float PV distortion coefficient                  
PV1_4    -5.22214877361e-05       float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    -0.00027357290974        float PV distortion coefficient                  
PV1_1    1.00561672081            float PV distortion coefficient                  
PV1_0    0.00059247714737         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00392490347911        float PV distortion coefficient                  
PV1_8    -0.00046802686395        float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.00012794061508        float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000754648596697        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM k81ml71lk71lk71l         str    ASCII 1's complement checksum             
DATASUM  2587935816               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU07
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [10241:12288,2049:6144] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [11265:12288,2049:6144] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [10241:11264,2049:6144] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-337_135960-10-1      str   Detector Identifier                        
CCDNUM   19                      int   CCD number                                 
DETPOS   S8                      str   detector position ID                       
EXTNAME  S8                      str   extension name                             
GAINA    4.3956043956            float [electrons/adu] Gain for amp A             
RDNOISEA 6.64879120879           float [electrons] Read noise for amp A           
SATURATA 42109.0                 float [adu] Saturation for amp A                 
GAINB    4.42477876106           float [electrons/adu] Gain for amp B             
RDNOISEB 6.85                    float [electrons] Read noise for amp B           
SATURATB 42705.0                 float [adu] Saturation for amp B                 
CRPIX1   4405.6                  float Coordinate Reference axis 1                
CRPIX2   12696.33                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00668311491895        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    -0.00410364608354       float PV distortion coefficient                  
PV2_9    0.00271418927189        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.0012278070553        float PV distortion coefficient                  
PV2_1    1.00813838313           float PV distortion coefficient                  
PV2_2    -0.00356158141756       float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00159671641646        float PV distortion coefficient                  
PV2_5    0.00956650157453        float PV distortion coefficient                  
PV2_6    -0.00446026939707       float PV distortion coefficient                  
PV2_7    -0.00886273819096       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00384211568326        float PV distortion coefficient                  
PV2_10   -0.00182018666935       float PV distortion coefficient                  
PV1_4    0.019960814051          float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    -0.00386258527789       float PV distortion coefficient                  
PV1_1    1.01903317899           float PV distortion coefficient                  
PV1_0    0.0050510996264         float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00286068558954        float PV distortion coefficient                  
PV1_8    -0.00583638955978       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.0095279555371        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   -4.36414470999e-05      float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 3g3g4d2e3d2e3d2e        str    ASCII 1's complement checksum             
DATASUM  682346774               str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU08
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [10241:12288,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [11265:12288,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [10241:11264,6145:10240] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-358_135960-19-4       str   Detector Identifier                        
CCDNUM   20                       int   CCD number                                 
DETPOS   S9                       str   detector position ID                       
EXTNAME  S9                       str   extension name                             
GAINA    4.51671183379            float [electrons/adu] Gain for amp A             
RDNOISEA 6.68925022584            float [electrons] Read noise for amp A           
SATURATA 43397.0                  float [adu] Saturation for amp A                 
GAINB    4.47828034035            float [electrons/adu] Gain for amp B             
RDNOISEB 6.73667711599            float [electrons] Read noise for amp B           
SATURATB 44640.0                  float [adu] Saturation for amp B                 
CRPIX1   4405.6                   float Coordinate Reference axis 1                
CRPIX2   8437.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00168529855272        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.000599043802375        float PV distortion coefficient                  
PV2_9    -0.0025624225492         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.000660029002597       float PV distortion coefficient                  
PV2_1    1.00490140427            float PV distortion coefficient                  
PV2_2    -0.000484404020586       float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00333802603109         float PV distortion coefficient                  
PV2_5    0.000494520477344        float PV distortion coefficient                  
PV2_6    -0.000595880306316       float PV distortion coefficient                  
PV2_7    -0.00778188085071        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.000852177953956       float PV distortion coefficient                  
PV2_10   -0.0003664739242         float PV distortion coefficient                  
PV1_4    0.00259677118586         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.000352991301423        float PV distortion coefficient                  
PV1_1    1.00664530671            float PV distortion coefficient                  
PV1_0    0.00103335953654         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00373845935202        float PV distortion coefficient                  
PV1_8    -0.0010452864854         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.000571890835294       float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000951411145863        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM OHlAOEl2OEl8OEl8         str    ASCII 1's complement checksum             
DATASUM  3492193805               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU09
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================== ===== ===========================================
KEY      Value                  Type  Comment                                    
======== ====================== ===== ===========================================
ZIMAGE   T                      bool  extension contains compressed image        
ZTILE1   2160                   int   size of tiles to be compressed             
ZTILE2   1                      int   size of tiles to be compressed             
ZCMPTYPE RICE_1                 str   compression algorithm                      
ZNAME1   BLOCKSIZE              str   compression block size                     
ZVAL1    32                     int   pixels per block                           
ZNAME2   BYTEPIX                str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                      int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                  str   IMAGE extension                            
ZBITPIX  16                     int   number of bits per data pixel              
ZNAXIS   2                      int   number of data axes                        
ZNAXIS1  2160                   int   length of data axis 1                      
ZNAXIS2  4146                   int   length of data axis 2                      
ZPCOUNT  0                      int   required keyword; must = 0                 
ZGCOUNT  1                      int   required keyword; must = 1                 
BZERO    32768                  int   offset data range to that of unsigned short
BSCALE   1                      int   default scaling factor                     
BUNIT    adu                    str   Brightness units for pixel array           
WCSAXES  2                      int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]      str   Detector size                              
TRIMSEC  [57:2104,51:4146]      str   Good section                               
DATASEC  [57:2104,51:4146]      str   Data section to display                    
DETSEC   [8193:10240,2049:6144] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]        str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]    str   Good section from amp A                    
DETSECA  [9217:10240,2049:6144] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]     str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]     str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]    str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]    str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]    str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]       str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]      str   Good section from amp B                    
DETSECB  [8193:9216,2049:6144]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]        str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]        str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]      str   Data section from amp B                    
BIASSECB [7:56,51:4146]         str   Overscan from amp B                        
PRESECB  [1:6,51:4146]          str   Prescan from amp B                         
POSTSECB [57:1080,1:50]         str   Postscan from amp B                        
DETECTOR S3-128_135959-6-3      str   Detector Identifier                        
CCDNUM   13                     int   CCD number                                 
DETPOS   S14                    str   detector position ID                       
EXTNAME  S14                    str   extension name                             
GAINA    4.41696113074          float [electrons/adu] Gain for amp A             
RDNOISEA 6.82022968198          float [electrons] Read noise for amp A           
SATURATA 45051.0                float [adu] Saturation for amp A                 
GAINB    4.42282176028          float [electrons/adu] Gain for amp B             
RDNOISEB 6.71782397169          float [electrons] Read noise for amp B           
SATURATB 43930.0                float [adu] Saturation for amp B                 
CRPIX1   6660.0                 float Coordinate Reference axis 1                
CRPIX2   12696.33               float Coordinate Reference axis 2                
FPA      DECAM_BKP1             str   DECam focal plane name                     
INHERIT  T                      bool  Inherits PHDU header                       
CCDBIN1  1                      int   Pixel binning, axis 1                      
CCDBIN2  1                      int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware    str   DHE Hardware                               
DHEFIRM  demo30                 str   DHE Firmware                               
SLOT00   MCB 15 5.210000        str   Monsoon module                             
SLOT01   DESCB 22 4.010000      str   Monsoon module                             
SLOT02   DESCB 3 4.010000       str   Monsoon module                             
SLOT03   CCD12 16 4.080000      str   Monsoon module                             
SLOT04   CCD12 11 4.080000      str   Monsoon module                             
SLOT05   CCD12 14 4.080000      str   Monsoon module                             
RADESYS  FK5                    str   World coordinate reference frame           
EQUINOX  2000.0                 float [yr] Equinox of WCS                        
PV1_7    0.00833203439025       float PV distortion coefficient                  
CUNIT1   deg                    str                                              
PV2_8    -0.0070808639622       float PV distortion coefficient                  
PV2_9    0.00530032133381       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07      float World coordinate transformation matrix     
LTM2_2   1.0                    float Detector to image transformation           
LTM2_1   0.0                    float Detector to image transformation           
PV2_0    -0.00344574338354      float PV distortion coefficient                  
PV2_1    1.00987520102          float PV distortion coefficient                  
PV2_2    -0.00893740155436      float PV distortion coefficient                  
PV2_3    0.0                    float PV distortion coefficient                  
PV2_4    0.000130791220583      float PV distortion coefficient                  
PV2_5    0.0155404045273        float PV distortion coefficient                  
PV2_6    -0.00967787704135      float PV distortion coefficient                  
PV2_7    -0.00645300267616      float PV distortion coefficient                  
LTM1_1   1.0                    float Detector to image transformation           
PV1_6    0.00523453644606       float PV distortion coefficient                  
PV2_10   -0.00363807008567      float PV distortion coefficient                  
PV1_4    0.0253592750911        float PV distortion coefficient                  
PV1_3    0.0                    float PV distortion coefficient                  
PV1_2    -0.00718601970356      float PV distortion coefficient                  
PV1_1    1.02468304212          float PV distortion coefficient                  
PV1_0    0.00669793195278       float PV distortion coefficient                  
LTM1_2   0.0                    float Detector to image transformation           
PV1_9    0.00476562403583       float PV distortion coefficient                  
PV1_8    -0.0103204369754       float PV distortion coefficient                  
CD1_2    7.28535892432e-05      float World coordinate transformation matrix     
PV1_5    -0.0179538825159       float PV distortion coefficient                  
CUNIT2   deg                    str                                              
CD2_1    -7.28499004539e-05     float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07     float World coordinate transformation matrix     
LTV2     50.0                   float Detector to image transformation           
LTV1     56.0                   float Detector to image transformation           
PV1_10   -0.000641227910867     float PV distortion coefficient                  
CTYPE2   DEC--TPV               str   Coordinate type                            
CTYPE1   RA---TPV               str   Coordinate type                            
CRVAL1   237.447283             float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611               float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                      bool  Data from amp A is valid                   
VALIDB   T                      bool  Data from amp B is valid                   
NDONUTS  0                      int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT             str    FITS checksum version                     
CHECKSUM ETLAGSL7ESLAESL5       str    ASCII 1's complement checksum             
DATASUM  2348166403             str    checksum of data records                  
======== ====================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU10
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [8193:10240,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [9217:10240,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [8193:9216,6145:10240]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-181_123194-20-2      str   Detector Identifier                        
CCDNUM   14                      int   CCD number                                 
DETPOS   S15                     str   detector position ID                       
EXTNAME  S15                     str   extension name                             
GAINA    4.11861614498           float [electrons/adu] Gain for amp A             
RDNOISEA 6.52306425041           float [electrons] Read noise for amp A           
SATURATA 49308.0                 float [adu] Saturation for amp A                 
GAINB    4.48229493501           float [electrons/adu] Gain for amp B             
RDNOISEB 6.71940833707           float [electrons] Read noise for amp B           
SATURATB 46155.0                 float [adu] Saturation for amp B                 
CRPIX1   6660.0                  float Coordinate Reference axis 1                
CRPIX2   8437.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.000618739509043      float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    -0.0032297804903        float PV distortion coefficient                  
PV2_9    -0.000897746935012      float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.000975920560411      float PV distortion coefficient                  
PV2_1    1.00556889941           float PV distortion coefficient                  
PV2_2    -0.00139919193513       float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00153621939638        float PV distortion coefficient                  
PV2_5    0.00421093641845        float PV distortion coefficient                  
PV2_6    -0.0015338354651        float PV distortion coefficient                  
PV2_7    -0.00558888194655       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00247144789907        float PV distortion coefficient                  
PV2_10   -0.000644224906014      float PV distortion coefficient                  
PV1_4    0.00466007128504        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    -0.00141956938885       float PV distortion coefficient                  
PV1_1    1.00809773568           float PV distortion coefficient                  
PV1_0    0.0013809870232         float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    -0.000851145932534      float PV distortion coefficient                  
PV1_8    -0.00266126507451       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.00373465873416       float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   -0.00138650431736       float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 3pYEAoXC6oXCAoXC        str    ASCII 1's complement checksum             
DATASUM  3432615180              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU11
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================== ===== ===========================================
KEY      Value                 Type  Comment                                    
======== ===================== ===== ===========================================
ZIMAGE   T                     bool  extension contains compressed image        
ZTILE1   2160                  int   size of tiles to be compressed             
ZTILE2   1                     int   size of tiles to be compressed             
ZCMPTYPE RICE_1                str   compression algorithm                      
ZNAME1   BLOCKSIZE             str   compression block size                     
ZVAL1    32                    int   pixels per block                           
ZNAME2   BYTEPIX               str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                     int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                 str   IMAGE extension                            
ZBITPIX  16                    int   number of bits per data pixel              
ZNAXIS   2                     int   number of data axes                        
ZNAXIS1  2160                  int   length of data axis 1                      
ZNAXIS2  4146                  int   length of data axis 2                      
ZPCOUNT  0                     int   required keyword; must = 0                 
ZGCOUNT  1                     int   required keyword; must = 1                 
BZERO    32768                 int   offset data range to that of unsigned short
BSCALE   1                     int   default scaling factor                     
BUNIT    adu                   str   Brightness units for pixel array           
WCSAXES  2                     int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]     str   Detector size                              
TRIMSEC  [57:2104,51:4146]     str   Good section                               
DATASEC  [57:2104,51:4146]     str   Data section to display                    
DETSEC   [6145:8192,4097:8192] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]       str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]   str   Good section from amp A                    
DETSECA  [7169:8192,4097:8192] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]    str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]    str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]   str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]   str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]   str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]      str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]     str   Good section from amp B                    
DETSECB  [6145:7168,4097:8192] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]       str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]       str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]     str   Data section from amp B                    
BIASSECB [7:56,51:4146]        str   Overscan from amp B                        
PRESECB  [1:6,51:4146]         str   Prescan from amp B                         
POSTSECB [57:1080,1:50]        str   Postscan from amp B                        
DETECTOR S3-234_135959-22-1    str   Detector Identifier                        
CCDNUM   8                     int   CCD number                                 
DETPOS   S20                   str   detector position ID                       
EXTNAME  S20                   str   extension name                             
GAINA    4.35729847495         float [electrons/adu] Gain for amp A             
RDNOISEA 6.63834422658         float [electrons] Read noise for amp A           
SATURATA 50588.0               float [adu] Saturation for amp A                 
GAINB    4.07830342577         float [electrons/adu] Gain for amp B             
RDNOISEB 6.60399673736         float [electrons] Read noise for amp B           
SATURATB 51524.0               float [adu] Saturation for amp B                 
CRPIX1   8914.4                float Coordinate Reference axis 1                
CRPIX2   10566.67              float Coordinate Reference axis 2                
FPA      DECAM_BKP1            str   DECam focal plane name                     
INHERIT  T                     bool  Inherits PHDU header                       
CCDBIN1  1                     int   Pixel binning, axis 1                      
CCDBIN2  1                     int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware   str   DHE Hardware                               
DHEFIRM  demo30                str   DHE Firmware                               
SLOT00   MCB 15 5.210000       str   Monsoon module                             
SLOT01   DESCB 22 4.010000     str   Monsoon module                             
SLOT02   DESCB 3 4.010000      str   Monsoon module                             
SLOT03   CCD12 16 4.080000     str   Monsoon module                             
SLOT04   CCD12 11 4.080000     str   Monsoon module                             
SLOT05   CCD12 14 4.080000     str   Monsoon module                             
RADESYS  FK5                   str   World coordinate reference frame           
EQUINOX  2000.0                float [yr] Equinox of WCS                        
PV1_7    0.0035474602514       float PV distortion coefficient                  
CUNIT1   deg                   str                                              
PV2_8    -0.0108493891958      float PV distortion coefficient                  
PV2_9    0.00609959757092      float PV distortion coefficient                  
CD1_1    -1.8249413473e-07     float World coordinate transformation matrix     
LTM2_2   1.0                   float Detector to image transformation           
LTM2_1   0.0                   float Detector to image transformation           
PV2_0    -0.00443883485121     float PV distortion coefficient                  
PV2_1    1.0155124127          float PV distortion coefficient                  
PV2_2    -0.00995319928534     float PV distortion coefficient                  
PV2_3    0.0                   float PV distortion coefficient                  
PV2_4    -0.0104952102173      float PV distortion coefficient                  
PV2_5    0.0200955482764       float PV distortion coefficient                  
PV2_6    -0.0102772977583      float PV distortion coefficient                  
PV2_7    0.000535776949314     float PV distortion coefficient                  
LTM1_1   1.0                   float Detector to image transformation           
PV1_6    0.0102124657323       float PV distortion coefficient                  
PV2_10   -0.00372488771359     float PV distortion coefficient                  
PV1_4    0.0152499566026       float PV distortion coefficient                  
PV1_3    0.0                   float PV distortion coefficient                  
PV1_2    -0.0098203131346      float PV distortion coefficient                  
PV1_1    1.0173804824          float PV distortion coefficient                  
PV1_0    0.00524798792351      float PV distortion coefficient                  
LTM1_2   0.0                   float Detector to image transformation           
PV1_9    0.00457246091704      float PV distortion coefficient                  
PV1_8    -0.0104106208617      float PV distortion coefficient                  
CD1_2    7.28535892432e-05     float World coordinate transformation matrix     
PV1_5    -0.017677606972       float PV distortion coefficient                  
CUNIT2   deg                   str                                              
CD2_1    -7.28499004539e-05    float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07    float World coordinate transformation matrix     
LTV2     50.0                  float Detector to image transformation           
LTV1     56.0                  float Detector to image transformation           
PV1_10   -0.0042983390356      float PV distortion coefficient                  
CTYPE2   DEC--TPV              str   Coordinate type                            
CTYPE1   RA---TPV              str   Coordinate type                            
CRVAL1   237.447283            float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611              float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                     bool  Data from amp A is valid                   
VALIDB   T                     bool  Data from amp B is valid                   
NDONUTS  0                     int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT            str    FITS checksum version                     
CHECKSUM SH8QTG6OSG6OSG6O      str    ASCII 1's complement checksum             
DATASUM  2985320762            str    checksum of data records                  
======== ===================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU12
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================== ===== ===========================================
KEY      Value                  Type  Comment                                    
======== ====================== ===== ===========================================
ZIMAGE   T                      bool  extension contains compressed image        
ZTILE1   2160                   int   size of tiles to be compressed             
ZTILE2   1                      int   size of tiles to be compressed             
ZCMPTYPE RICE_1                 str   compression algorithm                      
ZNAME1   BLOCKSIZE              str   compression block size                     
ZVAL1    32                     int   pixels per block                           
ZNAME2   BYTEPIX                str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                      int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                  str   IMAGE extension                            
ZBITPIX  16                     int   number of bits per data pixel              
ZNAXIS   2                      int   number of data axes                        
ZNAXIS1  2160                   int   length of data axis 1                      
ZNAXIS2  4146                   int   length of data axis 2                      
ZPCOUNT  0                      int   required keyword; must = 0                 
ZGCOUNT  1                      int   required keyword; must = 1                 
BZERO    32768                  int   offset data range to that of unsigned short
BSCALE   1                      int   default scaling factor                     
BUNIT    adu                    str   Brightness units for pixel array           
WCSAXES  2                      int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]      str   Detector size                              
TRIMSEC  [57:2104,51:4146]      str   Good section                               
DATASEC  [57:2104,51:4146]      str   Data section to display                    
DETSEC   [4097:6144,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]        str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]    str   Good section from amp A                    
DETSECA  [5121:6144,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]     str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]     str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]    str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]    str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]    str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]       str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]      str   Good section from amp B                    
DETSECB  [4097:5120,6145:10240] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]        str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]        str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]      str   Data section from amp B                    
BIASSECB [7:56,51:4146]         str   Overscan from amp B                        
PRESECB  [1:6,51:4146]          str   Prescan from amp B                         
POSTSECB [57:1080,1:50]         str   Postscan from amp B                        
DETECTOR S3-40_124750-19-1      str   Detector Identifier                        
CCDNUM   4                      int   CCD number                                 
DETPOS   S25                    str   detector position ID                       
EXTNAME  S25                    str   extension name                             
GAINA    4.44642063139          float [electrons/adu] Gain for amp A             
RDNOISEA 6.77234326367          float [electrons] Read noise for amp A           
SATURATA 45165.0                float [adu] Saturation for amp A                 
GAINB    4.75511174513          float [electrons/adu] Gain for amp B             
RDNOISEB 6.89538754161          float [electrons] Read noise for amp B           
SATURATB 43941.0                float [adu] Saturation for amp B                 
CRPIX1   11168.8                float Coordinate Reference axis 1                
CRPIX2   8437.0                 float Coordinate Reference axis 2                
FPA      DECAM_BKP1             str   DECam focal plane name                     
INHERIT  T                      bool  Inherits PHDU header                       
CCDBIN1  1                      int   Pixel binning, axis 1                      
CCDBIN2  1                      int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware    str   DHE Hardware                               
DHEFIRM  demo30                 str   DHE Firmware                               
SLOT00   MCB 15 5.210000        str   Monsoon module                             
SLOT01   DESCB 22 4.010000      str   Monsoon module                             
SLOT02   DESCB 3 4.010000       str   Monsoon module                             
SLOT03   CCD12 16 4.080000      str   Monsoon module                             
SLOT04   CCD12 11 4.080000      str   Monsoon module                             
SLOT05   CCD12 14 4.080000      str   Monsoon module                             
RADESYS  FK5                    str   World coordinate reference frame           
EQUINOX  2000.0                 float [yr] Equinox of WCS                        
PV1_7    0.0025929799336        float PV distortion coefficient                  
CUNIT1   deg                    str                                              
PV2_8    -0.0111438893463       float PV distortion coefficient                  
PV2_9    0.00571758838216       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07      float World coordinate transformation matrix     
LTM2_2   1.0                    float Detector to image transformation           
LTM2_1   0.0                    float Detector to image transformation           
PV2_0    -0.00657921722149      float PV distortion coefficient                  
PV2_1    1.02362586045          float PV distortion coefficient                  
PV2_2    -0.00975736229989      float PV distortion coefficient                  
PV2_3    0.0                    float PV distortion coefficient                  
PV2_4    -0.02337496749         float PV distortion coefficient                  
PV2_5    0.0200839037657        float PV distortion coefficient                  
PV2_6    -0.00898782000882      float PV distortion coefficient                  
PV2_7    0.00733672889147       float PV distortion coefficient                  
LTM1_1   1.0                    float Detector to image transformation           
PV1_6    0.00985660611706       float PV distortion coefficient                  
PV2_10   -0.00306788097912      float PV distortion coefficient                  
PV1_4    0.0137363680081        float PV distortion coefficient                  
PV1_3    0.0                    float PV distortion coefficient                  
PV1_2    -0.00958151410649      float PV distortion coefficient                  
PV1_1    1.01706113041          float PV distortion coefficient                  
PV1_0    0.00448703770946       float PV distortion coefficient                  
LTM1_2   0.0                    float Detector to image transformation           
PV1_9    0.00604766734282       float PV distortion coefficient                  
PV1_8    -0.0103788550683       float PV distortion coefficient                  
CD1_2    7.28535892432e-05      float World coordinate transformation matrix     
PV1_5    -0.0193682620268       float PV distortion coefficient                  
CUNIT2   deg                    str                                              
CD2_1    -7.28499004539e-05     float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07     float World coordinate transformation matrix     
LTV2     50.0                   float Detector to image transformation           
LTV1     56.0                   float Detector to image transformation           
PV1_10   -0.003594679107        float PV distortion coefficient                  
CTYPE2   DEC--TPV               str   Coordinate type                            
CTYPE1   RA---TPV               str   Coordinate type                            
CRVAL1   237.447283             float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611               float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                      bool  Data from amp A is valid                   
VALIDB   T                      bool  Data from amp B is valid                   
NDONUTS  0                      int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT             str    FITS checksum version                     
CHECKSUM 3FXKA9XH4EXHA9XH       str    ASCII 1's complement checksum             
DATASUM  448583556              str    checksum of data records                  
======== ====================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU13
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,1:4096]        str   Good section                               
DATASEC  [57:2104,1:4096]        str   Data section to display                    
DETSEC   [16385:18432,2049:6144] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [57:1080,1:4096]        str   Good section from amp A                    
DETSECA  [16385:17408,2049:6144] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]         str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]         str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]        str   Data section from amp A                    
BIASSECA [7:56,1:4096]           str   Overscan from amp A                        
PRESECA  [1:6,1:4096]            str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]     str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]      str   Good section from amp B                    
DETSECB  [17409:18432,2049:6144] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]      str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]      str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]      str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]      str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]      str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]   str   Postscan from amp B                        
DETECTOR S3-156_123195-22-1      str   Detector Identifier                        
CCDNUM   39                      int   CCD number                                 
DETPOS   N8                      str   detector position ID                       
EXTNAME  N8                      str   extension name                             
GAINA    4.22832980973           float [electrons/adu] Gain for amp A             
RDNOISEA 6.71416490486           float [electrons] Read noise for amp A           
SATURATA 45546.0                 float [adu] Saturation for amp A                 
GAINB    4.57247370828           float [electrons/adu] Gain for amp B             
RDNOISEB 6.70324645633           float [electrons] Read noise for amp B           
SATURATB 41854.0                 float [adu] Saturation for amp B                 
CRPIX1   -2357.6                 float Coordinate Reference axis 1                
CRPIX2   12696.33                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00805931180967        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00339196526107        float PV distortion coefficient                  
PV2_9    0.00274604020996        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.00164474691553        float PV distortion coefficient                  
PV2_1    1.00826135528           float PV distortion coefficient                  
PV2_2    0.00396837593785        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.000557296695849      float PV distortion coefficient                  
PV2_5    0.00924632226287        float PV distortion coefficient                  
PV2_6    0.00435379777874        float PV distortion coefficient                  
PV2_7    -0.00701618746909       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00427327526756        float PV distortion coefficient                  
PV2_10   0.00173276879966        float PV distortion coefficient                  
PV1_4    0.0229823044311         float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.00277177199339        float PV distortion coefficient                  
PV1_1    1.02117820548           float PV distortion coefficient                  
PV1_0    0.00514929544936        float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00213821130177        float PV distortion coefficient                  
PV1_8    0.00486282269155        float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    0.00772832043446        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00132274914837        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 7MaOBJTL9JZLAJZL        str    ASCII 1's complement checksum             
DATASUM  4119280196              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU14
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [16385:18432,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [16385:17408,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [17409:18432,6145:10240] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-210_123194-16-1       str   Detector Identifier                        
CCDNUM   40                       int   CCD number                                 
DETPOS   N9                       str   detector position ID                       
EXTNAME  N9                       str   extension name                             
GAINA    4.19815281276            float [electrons/adu] Gain for amp A             
RDNOISEA 6.56465155332            float [electrons] Read noise for amp A           
SATURATA 58683.0                  float [adu] Saturation for amp A                 
GAINB    4.52693526483            float [electrons/adu] Gain for amp B             
RDNOISEB 6.91172476234            float [electrons] Read noise for amp B           
SATURATB 48278.0                  float [adu] Saturation for amp B                 
CRPIX1   -2357.6                  float Coordinate Reference axis 1                
CRPIX2   8437.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00185663078803        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00053052081155         float PV distortion coefficient                  
PV2_9    -0.00146314973419        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.00069782071229         float PV distortion coefficient                  
PV2_1    1.00582172671            float PV distortion coefficient                  
PV2_2    0.000937936761539        float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    -0.000697427377556       float PV distortion coefficient                  
PV2_5    0.00197602686892         float PV distortion coefficient                  
PV2_6    0.00103420509589         float PV distortion coefficient                  
PV2_7    -0.00506067520466        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.00165344738586         float PV distortion coefficient                  
PV2_10   0.000437572346382        float PV distortion coefficient                  
PV1_4    0.00238209745916         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.000330337484198        float PV distortion coefficient                  
PV1_1    1.00663921448            float PV distortion coefficient                  
PV1_0    0.00094316713582         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00228546574466        float PV distortion coefficient                  
PV1_8    0.00163824476248         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.00178442014625         float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.00166848397536         float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM Z3Vif2SZZ2Sfd2SZ         str    ASCII 1's complement checksum             
DATASUM  3224776815               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU15
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,1:4096]        str   Good section                               
DATASEC  [57:2104,1:4096]        str   Data section to display                    
DETSEC   [18433:20480,2049:6144] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [57:1080,1:4096]        str   Good section from amp A                    
DETSECA  [18433:19456,2049:6144] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]         str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]         str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]        str   Data section from amp A                    
BIASSECA [7:56,1:4096]           str   Overscan from amp A                        
PRESECA  [1:6,1:4096]            str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]     str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]      str   Good section from amp B                    
DETSECB  [19457:20480,2049:6144] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]      str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]      str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]      str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]      str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]      str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]   str   Postscan from amp B                        
DETECTOR S3-191_123194-7-1       str   Detector Identifier                        
CCDNUM   45                      int   CCD number                                 
DETPOS   N14                     str   detector position ID                       
EXTNAME  N14                     str   extension name                             
GAINA    4.28265524625           float [electrons/adu] Gain for amp A             
RDNOISEA 6.67623126338           float [electrons] Read noise for amp A           
SATURATA 50339.0                 float [adu] Saturation for amp A                 
GAINB    4.56621004566           float [electrons/adu] Gain for amp B             
RDNOISEB 6.79497716895           float [electrons] Read noise for amp B           
SATURATB 45655.0                 float [adu] Saturation for amp B                 
CRPIX1   -4612.0                 float Coordinate Reference axis 1                
CRPIX2   12696.33                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.0096876976184         float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00672066432103        float PV distortion coefficient                  
PV2_9    0.00540058946524        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.00355819059217        float PV distortion coefficient                  
PV2_1    1.00868229425           float PV distortion coefficient                  
PV2_2    0.00950252389934        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.00271700753363       float PV distortion coefficient                  
PV2_5    0.0153003377574         float PV distortion coefficient                  
PV2_6    0.00996778709506        float PV distortion coefficient                  
PV2_7    -0.00834026264869       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00734469725325        float PV distortion coefficient                  
PV2_10   0.00371452056333        float PV distortion coefficient                  
PV1_4    0.028743433689          float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0077004471607         float PV distortion coefficient                  
PV1_1    1.02730781721           float PV distortion coefficient                  
PV1_0    0.00712650181372        float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00404885939767        float PV distortion coefficient                  
PV1_8    0.0109360069195         float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    0.0182462532458         float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00282786870012        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM cdCQeZAPcbAPcZAP        str    ASCII 1's complement checksum             
DATASUM  3924387062              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU16
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [18433:20480,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [18433:19456,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [19457:20480,6145:10240] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-213_124750-22-3       str   Detector Identifier                        
CCDNUM   46                       int   CCD number                                 
DETPOS   N15                      str   detector position ID                       
EXTNAME  N15                      str   extension name                             
GAINA    4.41111601235            float [electrons/adu] Gain for amp A             
RDNOISEA 6.57829730922            float [electrons] Read noise for amp A           
SATURATA 40963.0                  float [adu] Saturation for amp A                 
GAINB    4.53720508167            float [electrons/adu] Gain for amp B             
RDNOISEB 7.21052631579            float [electrons] Read noise for amp B           
SATURATB 40530.0                  float [adu] Saturation for amp B                 
CRPIX1   -4612.0                  float Coordinate Reference axis 1                
CRPIX2   8437.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00124150405198        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00341916488037         float PV distortion coefficient                  
PV2_9    -0.000338602303247       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.00147829393152         float PV distortion coefficient                  
PV2_1    1.00683924379            float PV distortion coefficient                  
PV2_2    0.00241629553299         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00123580540733         float PV distortion coefficient                  
PV2_5    0.00493239194256         float PV distortion coefficient                  
PV2_6    0.00288719564727         float PV distortion coefficient                  
PV2_7    -0.00339663522804        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.0026846636872          float PV distortion coefficient                  
PV2_10   0.00142454829367         float PV distortion coefficient                  
PV1_4    0.00416347740979         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00175547226328         float PV distortion coefficient                  
PV1_1    1.00827273875            float PV distortion coefficient                  
PV1_0    0.00108443456189         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    0.000559647891333        float PV distortion coefficient                  
PV1_8    0.00407933553245         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.00615775194769         float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000941177077713        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM lQ6RnO6RlO6RlO6R         str    ASCII 1's complement checksum             
DATASUM  1888990078               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU17
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,1:4096]        str   Good section                               
DATASEC  [57:2104,1:4096]        str   Data section to display                    
DETSEC   [20481:22528,4097:8192] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [57:1080,1:4096]        str   Good section from amp A                    
DETSECA  [20481:21504,4097:8192] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]         str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]         str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]        str   Data section from amp A                    
BIASSECA [7:56,1:4096]           str   Overscan from amp A                        
PRESECA  [1:6,1:4096]            str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]     str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]      str   Good section from amp B                    
DETSECB  [21505:22528,4097:8192] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]      str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]      str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]      str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]      str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]      str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]   str   Postscan from amp B                        
DETECTOR S3-355_135960-19-1      str   Detector Identifier                        
CCDNUM   51                      int   CCD number                                 
DETPOS   N20                     str   detector position ID                       
EXTNAME  N20                     str   extension name                             
GAINA    4.34971726838           float [electrons/adu] Gain for amp A             
RDNOISEA 6.61765985211           float [electrons] Read noise for amp A           
SATURATA 46415.0                 float [adu] Saturation for amp A                 
GAINB    4.55996352029           float [electrons/adu] Gain for amp B             
RDNOISEB 6.70405836753           float [electrons] Read noise for amp B           
SATURATB 43248.0                 float [adu] Saturation for amp B                 
CRPIX1   -6866.4                 float Coordinate Reference axis 1                
CRPIX2   10566.67                float Coordinate Reference axis 2                
FPA      DECAM_BKP1              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 15 5.210000         str   Monsoon module                             
SLOT01   DESCB 22 4.010000       str   Monsoon module                             
SLOT02   DESCB 3 4.010000        str   Monsoon module                             
SLOT03   CCD12 16 4.080000       str   Monsoon module                             
SLOT04   CCD12 11 4.080000       str   Monsoon module                             
SLOT05   CCD12 14 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00288881769965        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00916457899857        float PV distortion coefficient                  
PV2_9    0.00484588593731        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.00314429185996        float PV distortion coefficient                  
PV2_1    1.0097230514            float PV distortion coefficient                  
PV2_2    0.00888316875246        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00210141580271        float PV distortion coefficient                  
PV2_5    0.0167420101342         float PV distortion coefficient                  
PV2_6    0.00971416315626        float PV distortion coefficient                  
PV2_7    -0.00373893755397       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00623405172991        float PV distortion coefficient                  
PV2_10   0.00372909966245        float PV distortion coefficient                  
PV1_4    0.0142873286666         float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0071217678129         float PV distortion coefficient                  
PV1_1    1.01668285911           float PV distortion coefficient                  
PV1_0    0.0044661876875         float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00370012820821        float PV distortion coefficient                  
PV1_8    0.010469657567          float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    0.0166935648707         float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00224673183088        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 4MIn6JGl4JGl4JGl        str    ASCII 1's complement checksum             
DATASUM  3870666321              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU18
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [22529:24576,6145:10240] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [22529:23552,6145:10240] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [23553:24576,6145:10240] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-208_124750-3-2        str   Detector Identifier                        
CCDNUM   56                       int   CCD number                                 
DETPOS   N25                      str   detector position ID                       
EXTNAME  N25                      str   extension name                             
GAINA    4.24989375266            float [electrons/adu] Gain for amp A             
RDNOISEA 6.46876328092            float [electrons] Read noise for amp A           
SATURATA 49415.0                  float [adu] Saturation for amp A                 
GAINB    4.502476362              float [electrons/adu] Gain for amp B             
RDNOISEB 6.59882935615            float [electrons] Read noise for amp B           
SATURATB 44433.0                  float [adu] Saturation for amp B                 
CRPIX1   -9120.8                  float Coordinate Reference axis 1                
CRPIX2   8437.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP1               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 15 5.210000          str   Monsoon module                             
SLOT01   DESCB 22 4.010000        str   Monsoon module                             
SLOT02   DESCB 3 4.010000         str   Monsoon module                             
SLOT03   CCD12 16 4.080000        str   Monsoon module                             
SLOT04   CCD12 11 4.080000        str   Monsoon module                             
SLOT05   CCD12 14 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    0.00125233745422         float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.0144794478694          float PV distortion coefficient                  
PV2_9    0.00755962860345         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.00589739999132         float PV distortion coefficient                  
PV2_1    1.01894429371            float PV distortion coefficient                  
PV2_2    0.0126941586212          float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.0148989397071          float PV distortion coefficient                  
PV2_5    0.0267289992547          float PV distortion coefficient                  
PV2_6    0.0104754408077          float PV distortion coefficient                  
PV2_7    0.00276953264506         float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.00406932634706         float PV distortion coefficient                  
PV2_10   0.00304015919695         float PV distortion coefficient                  
PV1_4    0.0104044940699          float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00515337995003         float PV distortion coefficient                  
PV1_1    1.01469597309            float PV distortion coefficient                  
PV1_0    0.00317614260505         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    0.00558776852776         float PV distortion coefficient                  
PV1_8    0.00871607275097         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.0172518283639          float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.00103929771053         float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM H9UMI6RMH6RMH6RM         str    ASCII 1's complement checksum             
DATASUM  3246256917               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU19
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [10241:12288,10241:14336] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [11265:12288,10241:14336] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [10241:11264,10241:14336] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-349_135960-15-4        str   Detector Identifier                        
CCDNUM   21                        int   CCD number                                 
DETPOS   S10                       str   detector position ID                       
EXTNAME  S10                       str   extension name                             
GAINA    4.03063280935             float [electrons/adu] Gain for amp A             
RDNOISEA 6.45626763402             float [electrons] Read noise for amp A           
SATURATA 48507.0                   float [adu] Saturation for amp A                 
GAINB    4.13907284768             float [electrons/adu] Gain for amp B             
RDNOISEB 6.55877483444             float [electrons] Read noise for amp B           
SATURATB 45743.0                   float [adu] Saturation for amp B                 
CRPIX1   4405.6                    float Coordinate Reference axis 1                
CRPIX2   4177.667                  float Coordinate Reference axis 2                
FPA      DECAM_BKP3                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 12 5.210000           str   Monsoon module                             
SLOT01   DESCB 11 4.010000         str   Monsoon module                             
SLOT02   DESCB 12 4.010000         str   Monsoon module                             
SLOT03   CCD12 29 4.080000         str   Monsoon module                             
SLOT04   CCD12 15 4.080000         str   Monsoon module                             
SLOT05   CCD12 28 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00368375953448         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000241242288785        float PV distortion coefficient                  
PV2_9    -0.00313243258055         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000310262121317        float PV distortion coefficient                  
PV2_1    1.00450381778             float PV distortion coefficient                  
PV2_2    -4.80790839108e-05        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00493322832764          float PV distortion coefficient                  
PV2_5    0.000368406226306         float PV distortion coefficient                  
PV2_6    -0.000234711194211        float PV distortion coefficient                  
PV2_7    -0.0105187653762          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000687996452573        float PV distortion coefficient                  
PV2_10   -0.000184053430404        float PV distortion coefficient                  
PV1_4    0.000305647830184         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.000139531729601         float PV distortion coefficient                  
PV1_1    1.00569838993             float PV distortion coefficient                  
PV1_0    0.000295811195761         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00427933834213         float PV distortion coefficient                  
PV1_8    -0.000758989039682        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    4.63007999517e-06         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.000675317161126         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM o47jr26io26io26i          str    ASCII 1's complement checksum             
DATASUM  2647485645                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU20
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [10241:12288,14337:18432] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [11265:12288,14337:18432] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [10241:11264,14337:18432] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-303_135960-8-4         str   Detector Identifier                        
CCDNUM   22                        int   CCD number                                 
DETPOS   S11                       str   detector position ID                       
EXTNAME  S11                       str   extension name                             
GAINA    4.48430493274             float [electrons/adu] Gain for amp A             
RDNOISEA 6.79506726457             float [electrons] Read noise for amp A           
SATURATA 46380.0                   float [adu] Saturation for amp A                 
GAINB    4.33651344319             float [electrons/adu] Gain for amp B             
RDNOISEB 6.67476149176             float [electrons] Read noise for amp B           
SATURATB 47615.0                   float [adu] Saturation for amp B                 
CRPIX1   4405.6                    float Coordinate Reference axis 1                
CRPIX2   -81.66665                 float Coordinate Reference axis 2                
FPA      DECAM_BKP3                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 12 5.210000           str   Monsoon module                             
SLOT01   DESCB 11 4.010000         str   Monsoon module                             
SLOT02   DESCB 12 4.010000         str   Monsoon module                             
SLOT03   CCD12 29 4.080000         str   Monsoon module                             
SLOT04   CCD12 15 4.080000         str   Monsoon module                             
SLOT05   CCD12 28 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00446347296714         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000454567314627        float PV distortion coefficient                  
PV2_9    -0.00312177610136         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000259572907366        float PV distortion coefficient                  
PV2_1    1.00518885323             float PV distortion coefficient                  
PV2_2    -0.000302525009353        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00202510075639          float PV distortion coefficient                  
PV2_5    -6.81877176131e-05        float PV distortion coefficient                  
PV2_6    -0.000218844763686        float PV distortion coefficient                  
PV2_7    -0.00655746240806         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00109576939445         float PV distortion coefficient                  
PV2_10   7.41673213531e-05         float PV distortion coefficient                  
PV1_4    0.000141075383574         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.000607687293418         float PV distortion coefficient                  
PV1_1    1.00564274214             float PV distortion coefficient                  
PV1_0    -0.00045571857935         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00360264115312         float PV distortion coefficient                  
PV1_8    -8.79907223991e-06        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.000117848521732        float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00128195029219          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM YHa2a9W0TGa0Y9W0          str    ASCII 1's complement checksum             
DATASUM  2249659955                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU21
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [10241:12288,18433:22528] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [11265:12288,18433:22528] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [10241:11264,18433:22528] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-121_135959-17-1        str   Detector Identifier                        
CCDNUM   23                        int   CCD number                                 
DETPOS   S12                       str   detector position ID                       
EXTNAME  S12                       str   extension name                             
GAINA    4.31406384814             float [electrons/adu] Gain for amp A             
RDNOISEA 6.66393442623             float [electrons] Read noise for amp A           
SATURATA 46994.0                   float [adu] Saturation for amp A                 
GAINB    4.43458980044             float [electrons/adu] Gain for amp B             
RDNOISEB 6.81241685144             float [electrons] Read noise for amp B           
SATURATB 47770.0                   float [adu] Saturation for amp B                 
CRPIX1   4405.6                    float Coordinate Reference axis 1                
CRPIX2   -4341.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP3                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 12 5.210000           str   Monsoon module                             
SLOT01   DESCB 11 4.010000         str   Monsoon module                             
SLOT02   DESCB 12 4.010000         str   Monsoon module                             
SLOT03   CCD12 29 4.080000         str   Monsoon module                             
SLOT04   CCD12 15 4.080000         str   Monsoon module                             
SLOT05   CCD12 28 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00247268278611         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.000394261248595         float PV distortion coefficient                  
PV2_9    -0.00297984007123         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000250397170298        float PV distortion coefficient                  
PV2_1    1.00511010313             float PV distortion coefficient                  
PV2_2    -0.000373758308041        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00214908468025          float PV distortion coefficient                  
PV2_5    -0.00046936070436         float PV distortion coefficient                  
PV2_6    0.000254664444453         float PV distortion coefficient                  
PV2_7    -0.00657363508782         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.000131483365534         float PV distortion coefficient                  
PV2_10   -0.000115601220055        float PV distortion coefficient                  
PV1_4    -0.00127827876993         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    5.85070590604e-07         float PV distortion coefficient                  
PV1_1    1.00590408001             float PV distortion coefficient                  
PV1_0    -0.000861977075407        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00383617167833         float PV distortion coefficient                  
PV1_8    0.000504729798887         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    7.62808401284e-05         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   7.10814752733e-05         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM a7TAb7R7a7RAa7R5          str    ASCII 1's complement checksum             
DATASUM  4197910294                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU22
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [10241:12288,22529:26624] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [11265:12288,22529:26624] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [10241:11264,22529:26624] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-86_123194-6-1          str   Detector Identifier                        
CCDNUM   24                        int   CCD number                                 
DETPOS   S13                       str   detector position ID                       
EXTNAME  S13                       str   extension name                             
GAINA    3.95256916996             float [electrons/adu] Gain for amp A             
RDNOISEA 6.3209486166              float [electrons] Read noise for amp A           
SATURATA 52795.0                   float [adu] Saturation for amp A                 
GAINB    4.01123144805             float [electrons/adu] Gain for amp B             
RDNOISEB 6.39350180505             float [electrons] Read noise for amp B           
SATURATB 52326.0                   float [adu] Saturation for amp B                 
CRPIX1   4405.6                    float Coordinate Reference axis 1                
CRPIX2   -8600.334                 float Coordinate Reference axis 2                
FPA      DECAM_BKP3                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 12 5.210000           str   Monsoon module                             
SLOT01   DESCB 11 4.010000         str   Monsoon module                             
SLOT02   DESCB 12 4.010000         str   Monsoon module                             
SLOT03   CCD12 29 4.080000         str   Monsoon module                             
SLOT04   CCD12 15 4.080000         str   Monsoon module                             
SLOT05   CCD12 28 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00705021730556          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.00422248071239          float PV distortion coefficient                  
PV2_9    0.0020442940927           float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.00142296337266         float PV distortion coefficient                  
PV2_1    1.00812911815             float PV distortion coefficient                  
PV2_2    0.00385281194794          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.000342460288589         float PV distortion coefficient                  
PV2_5    -0.0086048298546          float PV distortion coefficient                  
PV2_6    -0.0048645421546          float PV distortion coefficient                  
PV2_7    -0.0073983513722          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00422938559004         float PV distortion coefficient                  
PV2_10   0.00201360666419          float PV distortion coefficient                  
PV1_4    -0.0210695175128          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.00426164205454          float PV distortion coefficient                  
PV1_1    1.02006125903             float PV distortion coefficient                  
PV1_0    -0.00510418623346         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00184837997673          float PV distortion coefficient                  
PV1_8    0.00652402447373          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.010244598923           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00136391464302          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM DA4UG12SD82SD82S          str    ASCII 1's complement checksum             
DATASUM  67364263                  str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU23
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [8193:10240,18433:22528] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [9217:10240,18433:22528] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [8193:9216,18433:22528]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-331_135960-13-1       str   Detector Identifier                        
CCDNUM   17                       int   CCD number                                 
DETPOS   S18                      str   detector position ID                       
EXTNAME  S18                      str   extension name                             
GAINA    4.21585160202            float [electrons/adu] Gain for amp A             
RDNOISEA 6.38195615514            float [electrons] Read noise for amp A           
SATURATA 49820.0                  float [adu] Saturation for amp A                 
GAINB    4.41891294741            float [electrons/adu] Gain for amp B             
RDNOISEB 6.68183826779            float [electrons] Read noise for amp B           
SATURATB 46250.0                  float [adu] Saturation for amp B                 
CRPIX1   6660.0                   float Coordinate Reference axis 1                
CRPIX2   -4341.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP3               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 12 5.210000          str   Monsoon module                             
SLOT01   DESCB 11 4.010000        str   Monsoon module                             
SLOT02   DESCB 12 4.010000        str   Monsoon module                             
SLOT03   CCD12 29 4.080000        str   Monsoon module                             
SLOT04   CCD12 15 4.080000        str   Monsoon module                             
SLOT05   CCD12 28 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00104574666529        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00449618747766         float PV distortion coefficient                  
PV2_9    -0.00059187655216        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.000844948007997       float PV distortion coefficient                  
PV2_1    1.00594305475            float PV distortion coefficient                  
PV2_2    0.00149949647048         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00141353403841         float PV distortion coefficient                  
PV2_5    -0.00552499218182        float PV distortion coefficient                  
PV2_6    -0.00229307888274        float PV distortion coefficient                  
PV2_7    -0.00597066297559        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.00282149031071        float PV distortion coefficient                  
PV2_10   0.001065899098           float PV distortion coefficient                  
PV1_4    -0.00445202050067        float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00217056593794         float PV distortion coefficient                  
PV1_1    1.00805791897            float PV distortion coefficient                  
PV1_0    -0.00171209193469        float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00177739680114        float PV distortion coefficient                  
PV1_8    0.00400716906072         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.00428545510115        float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.00199380547107         float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM LGAaOF7TLFAZLF7Z         str    ASCII 1's complement checksum             
DATASUM  1002956137               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU24
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [8193:10240,22529:26624] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [9217:10240,22529:26624] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [8193:9216,22529:26624]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-195_123195-21-2       str   Detector Identifier                        
CCDNUM   18                       int   CCD number                                 
DETPOS   S19                      str   detector position ID                       
EXTNAME  S19                      str   extension name                             
GAINA    4.0733197556             float [electrons/adu] Gain for amp A             
RDNOISEA 6.37230142566            float [electrons] Read noise for amp A           
SATURATA 51319.0                  float [adu] Saturation for amp A                 
GAINB    3.87296669249            float [electrons/adu] Gain for amp B             
RDNOISEB 6.33849728892            float [electrons] Read noise for amp B           
SATURATB 51694.0                  float [adu] Saturation for amp B                 
CRPIX1   6660.0                   float Coordinate Reference axis 1                
CRPIX2   -8600.334                float Coordinate Reference axis 2                
FPA      DECAM_BKP3               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 12 5.210000          str   Monsoon module                             
SLOT01   DESCB 11 4.010000        str   Monsoon module                             
SLOT02   DESCB 12 4.010000        str   Monsoon module                             
SLOT03   CCD12 29 4.080000        str   Monsoon module                             
SLOT04   CCD12 15 4.080000        str   Monsoon module                             
SLOT05   CCD12 28 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    0.00995941439539         float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00571117741251         float PV distortion coefficient                  
PV2_9    0.00616777387606         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.00337188633747        float PV distortion coefficient                  
PV2_1    1.00950992778            float PV distortion coefficient                  
PV2_2    0.00893733006886         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00112303542469         float PV distortion coefficient                  
PV2_5    -0.0156458659611         float PV distortion coefficient                  
PV2_6    -0.00937210030955        float PV distortion coefficient                  
PV2_7    -0.00643608748742        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.00792169897733        float PV distortion coefficient                  
PV2_10   0.00334360786542         float PV distortion coefficient                  
PV1_4    -0.0289736912386         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00762054724158         float PV distortion coefficient                  
PV1_1    1.02724554317            float PV distortion coefficient                  
PV1_0    -0.00708353099579        float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    0.00441166531446         float PV distortion coefficient                  
PV1_8    0.00990959252148         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.017039432471          float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.00304401853524         float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM epdghmcfemcfemcf         str    ASCII 1's complement checksum             
DATASUM  3514661040               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU25
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [8193:10240,10241:14336] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [9217:10240,10241:14336] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [8193:9216,10241:14336]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-232_135959-21-2       str   Detector Identifier                        
CCDNUM   15                       int   CCD number                                 
DETPOS   S16                      str   detector position ID                       
EXTNAME  S16                      str   extension name                             
GAINA    4.23549343499            float [electrons/adu] Gain for amp A             
RDNOISEA 6.39644218551            float [electrons] Read noise for amp A           
SATURATA 50569.0                  float [adu] Saturation for amp A                 
GAINB    4.47427293065            float [electrons/adu] Gain for amp B             
RDNOISEB 6.64876957494            float [electrons] Read noise for amp B           
SATURATB 49061.0                  float [adu] Saturation for amp B                 
CRPIX1   6660.0                   float Coordinate Reference axis 1                
CRPIX2   4177.667                 float Coordinate Reference axis 2                
FPA      DECAM_BKP3               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 12 5.210000          str   Monsoon module                             
SLOT01   DESCB 11 4.010000        str   Monsoon module                             
SLOT02   DESCB 12 4.010000        str   Monsoon module                             
SLOT03   CCD12 29 4.080000        str   Monsoon module                             
SLOT04   CCD12 15 4.080000        str   Monsoon module                             
SLOT05   CCD12 28 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00373388062127        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    -0.000783662988115       float PV distortion coefficient                  
PV2_9    -0.00289356927039        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.00067271703994        float PV distortion coefficient                  
PV2_1    1.00543700391            float PV distortion coefficient                  
PV2_2    -0.000135501760036       float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.000550946978068        float PV distortion coefficient                  
PV2_5    0.000722923778826        float PV distortion coefficient                  
PV2_6    -0.000487707904822       float PV distortion coefficient                  
PV2_7    -0.00425094549043        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.000362070061866       float PV distortion coefficient                  
PV2_10   -0.000285393752285       float PV distortion coefficient                  
PV1_4    0.000194843562443        float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    5.38851029335e-05        float PV distortion coefficient                  
PV1_1    1.00568267979            float PV distortion coefficient                  
PV1_0    0.000351446716777        float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00385206615054        float PV distortion coefficient                  
PV1_8    -0.000671414083131       float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    -0.000146728283606       float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000237174884467        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM DP8hDP6eDP6eDP6e         str    ASCII 1's complement checksum             
DATASUM  3342958902               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU26
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,51:4146]        str   Good section                               
DATASEC  [57:2104,51:4146]        str   Data section to display                    
DETSEC   [8193:10240,14337:18432] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]      str   Good section from amp A                    
DETSECA  [9217:10240,14337:18432] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]       str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]       str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]      str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]      str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]      str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]         str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]        str   Good section from amp B                    
DETSECB  [8193:9216,14337:18432]  str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]          str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]          str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]        str   Data section from amp B                    
BIASSECB [7:56,51:4146]           str   Overscan from amp B                        
PRESECB  [1:6,51:4146]            str   Prescan from amp B                         
POSTSECB [57:1080,1:50]           str   Postscan from amp B                        
DETECTOR S3-202_123194-12-1       str   Detector Identifier                        
CCDNUM   16                       int   CCD number                                 
DETPOS   S17                      str   detector position ID                       
EXTNAME  S17                      str   extension name                             
GAINA    4.16840350146            float [electrons/adu] Gain for amp A             
RDNOISEA 6.43851604835            float [electrons] Read noise for amp A           
SATURATA 56223.0                  float [adu] Saturation for amp A                 
GAINB    4.54132606721            float [electrons/adu] Gain for amp B             
RDNOISEB 6.93596730245            float [electrons] Read noise for amp B           
SATURATB 46297.0                  float [adu] Saturation for amp B                 
CRPIX1   6660.0                   float Coordinate Reference axis 1                
CRPIX2   -81.66665                float Coordinate Reference axis 2                
FPA      DECAM_BKP3               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 12 5.210000          str   Monsoon module                             
SLOT01   DESCB 11 4.010000        str   Monsoon module                             
SLOT02   DESCB 12 4.010000        str   Monsoon module                             
SLOT03   CCD12 29 4.080000        str   Monsoon module                             
SLOT04   CCD12 15 4.080000        str   Monsoon module                             
SLOT05   CCD12 28 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.00404667857155        float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00159749460637         float PV distortion coefficient                  
PV2_9    -0.00272144921408        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    -0.00058206076615        float PV distortion coefficient                  
PV2_1    1.00290997789            float PV distortion coefficient                  
PV2_2    0.00052089502532         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00662962465251         float PV distortion coefficient                  
PV2_5    -0.00141423572776        float PV distortion coefficient                  
PV2_6    -0.000434831693848       float PV distortion coefficient                  
PV2_7    -0.00910353563838        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    -0.000753772146054       float PV distortion coefficient                  
PV2_10   0.000175832529248        float PV distortion coefficient                  
PV1_4    -0.000169901674748       float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    -2.03657679526e-05       float PV distortion coefficient                  
PV1_1    1.00551747441            float PV distortion coefficient                  
PV1_0    -0.000268260131441       float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.00439318675413        float PV distortion coefficient                  
PV1_8    0.000575881710241        float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.000537512948052        float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     50.0                     float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.000691116193257        float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM nPBEnO9BnOABnO7B         str    ASCII 1's complement checksum             
DATASUM  3897812354               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU27
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================== ===== ===========================================
KEY      Value                  Type  Comment                                    
======== ====================== ===== ===========================================
ZIMAGE   T                      bool  extension contains compressed image        
ZTILE1   2160                   int   size of tiles to be compressed             
ZTILE2   1                      int   size of tiles to be compressed             
ZCMPTYPE RICE_1                 str   compression algorithm                      
ZNAME1   BLOCKSIZE              str   compression block size                     
ZVAL1    32                     int   pixels per block                           
ZNAME2   BYTEPIX                str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                      int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                  str   IMAGE extension                            
ZBITPIX  16                     int   number of bits per data pixel              
ZNAXIS   2                      int   number of data axes                        
ZNAXIS1  2160                   int   length of data axis 1                      
ZNAXIS2  4146                   int   length of data axis 2                      
ZPCOUNT  0                      int   required keyword; must = 0                 
ZGCOUNT  1                      int   required keyword; must = 1                 
BZERO    32768                  int   offset data range to that of unsigned short
BSCALE   1                      int   default scaling factor                     
BUNIT    adu                    str   Brightness units for pixel array           
WCSAXES  2                      int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]      str   Detector size                              
TRIMSEC  [57:2104,51:4146]      str   Good section                               
DATASEC  [57:2104,51:4146]      str   Data section to display                    
DETSEC   [6145:8192,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]        str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]    str   Good section from amp A                    
DETSECA  [7169:8192,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]     str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]     str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]    str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]    str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]    str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]       str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]      str   Good section from amp B                    
DETSECB  [6145:7168,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]        str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]        str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]      str   Data section from amp B                    
BIASSECB [7:56,51:4146]         str   Overscan from amp B                        
PRESECB  [1:6,51:4146]          str   Prescan from amp B                         
POSTSECB [57:1080,1:50]         str   Postscan from amp B                        
DETECTOR S3-351_135960-4-1      str   Detector Identifier                        
CCDNUM   9                      int   CCD number                                 
DETPOS   S21                    str   detector position ID                       
EXTNAME  S21                    str   extension name                             
GAINA    4.26985482494          float [electrons/adu] Gain for amp A             
RDNOISEA 6.40520922289          float [electrons] Read noise for amp A           
SATURATA 47858.0                float [adu] Saturation for amp A                 
GAINB    4.31034482759          float [electrons/adu] Gain for amp B             
RDNOISEB 6.51896551724          float [electrons] Read noise for amp B           
SATURATB 46848.0                float [adu] Saturation for amp B                 
CRPIX1   8914.4                 float Coordinate Reference axis 1                
CRPIX2   6307.333               float Coordinate Reference axis 2                
FPA      DECAM_BKP3             str   DECam focal plane name                     
INHERIT  T                      bool  Inherits PHDU header                       
CCDBIN1  1                      int   Pixel binning, axis 1                      
CCDBIN2  1                      int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware    str   DHE Hardware                               
DHEFIRM  demo30                 str   DHE Firmware                               
SLOT00   MCB 12 5.210000        str   Monsoon module                             
SLOT01   DESCB 11 4.010000      str   Monsoon module                             
SLOT02   DESCB 12 4.010000      str   Monsoon module                             
SLOT03   CCD12 29 4.080000      str   Monsoon module                             
SLOT04   CCD12 15 4.080000      str   Monsoon module                             
SLOT05   CCD12 28 4.080000      str   Monsoon module                             
RADESYS  FK5                    str   World coordinate reference frame           
EQUINOX  2000.0                 float [yr] Equinox of WCS                        
PV1_7    -0.00300182236603      float PV distortion coefficient                  
CUNIT1   deg                    str                                              
PV2_8    -0.00261907387432      float PV distortion coefficient                  
PV2_9    -0.000950568066505     float PV distortion coefficient                  
CD1_1    -1.8249413473e-07      float World coordinate transformation matrix     
LTM2_2   1.0                    float Detector to image transformation           
LTM2_1   0.0                    float Detector to image transformation           
PV2_0    -0.00127430486957      float PV distortion coefficient                  
PV2_1    1.00563100701          float PV distortion coefficient                  
PV2_2    -0.00189019881017      float PV distortion coefficient                  
PV2_3    0.0                    float PV distortion coefficient                  
PV2_4    -0.000724774258554     float PV distortion coefficient                  
PV2_5    0.0034783363866        float PV distortion coefficient                  
PV2_6    -0.00199898342349      float PV distortion coefficient                  
PV2_7    -0.00268786137906      float PV distortion coefficient                  
LTM1_1   1.0                    float Detector to image transformation           
PV1_6    0.00184216937459       float PV distortion coefficient                  
PV2_10   -0.000963296779296     float PV distortion coefficient                  
PV1_4    0.00169726304839       float PV distortion coefficient                  
PV1_3    0.0                    float PV distortion coefficient                  
PV1_2    -0.000574591083274     float PV distortion coefficient                  
PV1_1    1.00675382291          float PV distortion coefficient                  
PV1_0    0.00063950295257       float PV distortion coefficient                  
LTM1_2   0.0                    float Detector to image transformation           
PV1_9    -0.0013630659448       float PV distortion coefficient                  
PV1_8    -0.00267730599005      float PV distortion coefficient                  
CD1_2    7.28535892432e-05      float World coordinate transformation matrix     
PV1_5    -0.00329336709949      float PV distortion coefficient                  
CUNIT2   deg                    str                                              
CD2_1    -7.28499004539e-05     float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07     float World coordinate transformation matrix     
LTV2     50.0                   float Detector to image transformation           
LTV1     56.0                   float Detector to image transformation           
PV1_10   -0.00105338066346      float PV distortion coefficient                  
CTYPE2   DEC--TPV               str   Coordinate type                            
CTYPE1   RA---TPV               str   Coordinate type                            
CRVAL1   237.447283             float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611               float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                      bool  Data from amp A is valid                   
VALIDB   T                      bool  Data from amp B is valid                   
NDONUTS  0                      int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT             str    FITS checksum version                     
CHECKSUM NiHRNiFONiFONiFO       str    ASCII 1's complement checksum             
DATASUM  1316179960             str    checksum of data records                  
======== ====================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU28
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [6145:8192,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [7169:8192,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [6145:7168,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-101_107419-17-2      str   Detector Identifier                        
CCDNUM   10                      int   CCD number                                 
DETPOS   S22                     str   detector position ID                       
EXTNAME  S22                     str   extension name                             
GAINA    4.33087916847           float [electrons/adu] Gain for amp A             
RDNOISEA 6.55825032482           float [electrons] Read noise for amp A           
SATURATA 50992.0                 float [adu] Saturation for amp A                 
GAINB    4.47427293065           float [electrons/adu] Gain for amp B             
RDNOISEB 6.63579418345           float [electrons] Read noise for amp B           
SATURATB 49049.0                 float [adu] Saturation for amp B                 
CRPIX1   8914.4                  float Coordinate Reference axis 1                
CRPIX2   2048.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.00286199116983       float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    -0.000157141676132      float PV distortion coefficient                  
PV2_9    -0.0020348621046        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.000769935669999      float PV distortion coefficient                  
PV2_1    1.00371978198           float PV distortion coefficient                  
PV2_2    -5.16340491968e-06      float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00247547366852        float PV distortion coefficient                  
PV2_5    0.000275469522361       float PV distortion coefficient                  
PV2_6    -0.000893671406281      float PV distortion coefficient                  
PV2_7    -0.00449689059133       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.00112370756084        float PV distortion coefficient                  
PV2_10   -3.93907898752e-05      float PV distortion coefficient                  
PV1_4    -9.81400069006e-05      float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    -0.000792094881672      float PV distortion coefficient                  
PV1_1    1.00566478506           float PV distortion coefficient                  
PV1_0    0.000214164399713       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    -0.00301605741382       float PV distortion coefficient                  
PV1_8    0.000237162446459       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.000496313379232      float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   -0.000655519471644      float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 3aHQAVHP3aHPAUHP        str    ASCII 1's complement checksum             
DATASUM  3517491143              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU29
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [6145:8192,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [7169:8192,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [6145:7168,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-164_107419-16-2      str   Detector Identifier                        
CCDNUM   11                      int   CCD number                                 
DETPOS   S23                     str   detector position ID                       
EXTNAME  S23                     str   extension name                             
GAINA    4.47427293065           float [electrons/adu] Gain for amp A             
RDNOISEA 6.75973154362           float [electrons] Read noise for amp A           
SATURATA 47232.0                 float [adu] Saturation for amp A                 
GAINB    4.47427293065           float [electrons/adu] Gain for amp B             
RDNOISEB 6.80223713647           float [electrons] Read noise for amp B           
SATURATB 48435.0                 float [adu] Saturation for amp B                 
CRPIX1   8914.4                  float Coordinate Reference axis 1                
CRPIX2   -2211.333               float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.00284059003651       float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00464068342869        float PV distortion coefficient                  
PV2_9    -0.00107841089601       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.000974707427131      float PV distortion coefficient                  
PV2_1    1.00486399658           float PV distortion coefficient                  
PV2_2    0.00156802994781        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00142737034018        float PV distortion coefficient                  
PV2_5    -0.00562949654732       float PV distortion coefficient                  
PV2_6    -0.00173027558443       float PV distortion coefficient                  
PV2_7    -0.00440567640912       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.00252650355168       float PV distortion coefficient                  
PV2_10   0.000751265806619       float PV distortion coefficient                  
PV1_4    -0.0021991254832        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.00182713087669        float PV distortion coefficient                  
PV1_1    1.00706779222           float PV distortion coefficient                  
PV1_0    -0.00125785178032       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    -0.00115964165119       float PV distortion coefficient                  
PV1_8    0.00311506334026        float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.00381758491826       float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.001374662452          float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM iH6Yl96XiG6Xi96X        str    ASCII 1's complement checksum             
DATASUM  4180210174              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU30
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [6145:8192,20481:24576] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [7169:8192,20481:24576] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [6145:7168,20481:24576] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-211_123194-16-2      str   Detector Identifier                        
CCDNUM   12                      int   CCD number                                 
DETPOS   S24                     str   detector position ID                       
EXTNAME  S24                     str   extension name                             
GAINA    4.33651344319           float [electrons/adu] Gain for amp A             
RDNOISEA 6.61274934952           float [electrons] Read noise for amp A           
SATURATA 57491.0                 float [adu] Saturation for amp A                 
GAINB    4.60829493088           float [electrons/adu] Gain for amp B             
RDNOISEB 6.89124423963           float [electrons] Read noise for amp B           
SATURATB 45537.0                 float [adu] Saturation for amp B                 
CRPIX1   8914.4                  float Coordinate Reference axis 1                
CRPIX2   -6470.667               float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00388046055813        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00882151531298        float PV distortion coefficient                  
PV2_9    0.00501724730666        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.00501524648387       float PV distortion coefficient                  
PV2_1    1.02007061366           float PV distortion coefficient                  
PV2_2    0.00823310990369        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.0201637575738        float PV distortion coefficient                  
PV2_5    -0.0165069679643        float PV distortion coefficient                  
PV2_6    -0.0090133178034        float PV distortion coefficient                  
PV2_7    0.00684831761154        float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.00833158276357       float PV distortion coefficient                  
PV2_10   0.00334721846989        float PV distortion coefficient                  
PV1_4    -0.0161392730248        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0085730826333         float PV distortion coefficient                  
PV1_1    1.01794006015           float PV distortion coefficient                  
PV1_0    -0.00505627618887       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00382844035602        float PV distortion coefficient                  
PV1_8    0.0105930729044         float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.017190692363         float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00341483826682        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM UhiPXZZNUffNUZZN        str    ASCII 1's complement checksum             
DATASUM  300745027               str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU31
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [4097:6144,10241:14336] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [5121:6144,10241:14336] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [4097:5120,10241:14336] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-144_124750-1-1       str   Detector Identifier                        
CCDNUM   5                       int   CCD number                                 
DETPOS   S26                     str   detector position ID                       
EXTNAME  S26                     str   extension name                             
GAINA    4.49438202247           float [electrons/adu] Gain for amp A             
RDNOISEA 7.04494382022           float [electrons] Read noise for amp A           
SATURATA 45237.0                 float [adu] Saturation for amp A                 
GAINB    4.71031559114           float [electrons/adu] Gain for amp B             
RDNOISEB 7.30381535563           float [electrons] Read noise for amp B           
SATURATB 44138.0                 float [adu] Saturation for amp B                 
CRPIX1   11168.8                 float Coordinate Reference axis 1                
CRPIX2   4177.667                float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.0034338612104        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    -0.00193637356873       float PV distortion coefficient                  
PV2_9    0.000777770848218       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.000115659032054      float PV distortion coefficient                  
PV2_1    1.00186412961           float PV distortion coefficient                  
PV2_2    -0.000920145275106      float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.00255182143444        float PV distortion coefficient                  
PV2_5    0.00312235062934        float PV distortion coefficient                  
PV2_6    -0.00291571745932       float PV distortion coefficient                  
PV2_7    -0.00313211420364       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.00111776882469       float PV distortion coefficient                  
PV2_10   -0.000617706650935      float PV distortion coefficient                  
PV1_4    0.00107835735505        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.000467259811608       float PV distortion coefficient                  
PV1_1    1.00723681951           float PV distortion coefficient                  
PV1_0    0.000452940930291       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.000440452843393       float PV distortion coefficient                  
PV1_8    -0.00174609414706       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.00512811869299       float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.000486732100005       float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM ZhcCheZ9ZeaCfeY9        str    ASCII 1's complement checksum             
DATASUM  1066821449              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU32
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [4097:6144,14337:18432] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [5121:6144,14337:18432] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [4097:5120,14337:18432] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-323_135959-13-1      str   Detector Identifier                        
CCDNUM   6                       int   CCD number                                 
DETPOS   S27                     str   detector position ID                       
EXTNAME  S27                     str   extension name                             
GAINA    4.25713069391           float [electrons/adu] Gain for amp A             
RDNOISEA 6.4367816092            float [electrons] Read noise for amp A           
SATURATA 50304.0                 float [adu] Saturation for amp A                 
GAINB    4.44839857651           float [electrons/adu] Gain for amp B             
RDNOISEB 6.67838078292           float [electrons] Read noise for amp B           
SATURATB 47106.0                 float [adu] Saturation for amp B                 
CRPIX1   11168.8                 float Coordinate Reference axis 1                
CRPIX2   -81.66665               float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.00411040494239       float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00258540122372        float PV distortion coefficient                  
PV2_9    0.000820019161924       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.00167855815866        float PV distortion coefficient                  
PV2_1    0.994481593812          float PV distortion coefficient                  
PV2_2    0.0011402601191         float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.0124992940153         float PV distortion coefficient                  
PV2_5    -0.00390597213283       float PV distortion coefficient                  
PV2_6    -0.00311853418379       float PV distortion coefficient                  
PV2_7    -0.00758473400152       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.000417476841936      float PV distortion coefficient                  
PV2_10   0.000972795417814       float PV distortion coefficient                  
PV1_4    -0.00137768239281       float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.000722872996825       float PV distortion coefficient                  
PV1_1    1.00753086766           float PV distortion coefficient                  
PV1_0    -0.000676957599795      float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.000704158726107       float PV distortion coefficient                  
PV1_8    0.0027057231441         float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.00583312434095       float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.000154600064151       float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM iAeej1ZZi8bdi8ZZ        str    ASCII 1's complement checksum             
DATASUM  3382290715              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU33
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [4097:6144,18433:22528] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [5121:6144,18433:22528] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [4097:5120,18433:22528] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-37_107419-21-4       str   Detector Identifier                        
CCDNUM   7                       int   CCD number                                 
DETPOS   S28                     str   detector position ID                       
EXTNAME  S28                     str   extension name                             
GAINA    4.57038391225           float [electrons/adu] Gain for amp A             
RDNOISEA 6.74405850091           float [electrons] Read noise for amp A           
SATURATA 44540.0                 float [adu] Saturation for amp A                 
GAINB    4.43458980044           float [electrons/adu] Gain for amp B             
RDNOISEB 6.59290465632           float [electrons] Read noise for amp B           
SATURATB 45057.0                 float [adu] Saturation for amp B                 
CRPIX1   11168.8                 float Coordinate Reference axis 1                
CRPIX2   -4341.0                 float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00204980597237        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.0116703463183         float PV distortion coefficient                  
PV2_9    0.00644820505438        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.00405014666855       float PV distortion coefficient                  
PV2_1    1.01318382885           float PV distortion coefficient                  
PV2_2    0.0103241730272         float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.00872691732156       float PV distortion coefficient                  
PV2_5    -0.021501069473         float PV distortion coefficient                  
PV2_6    -0.00926777712833       float PV distortion coefficient                  
PV2_7    0.000585380696736       float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.00943885440806       float PV distortion coefficient                  
PV2_10   0.00288244896125        float PV distortion coefficient                  
PV1_4    -0.0110987379121        float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.00871668523536        float PV distortion coefficient                  
PV1_1    1.01476855594           float PV distortion coefficient                  
PV1_0    -0.00401670976268       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00550629167679        float PV distortion coefficient                  
PV1_8    0.00789618640166        float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.0164263160173        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00348207660309        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM ZloNfjlKZjlKdjlK        str    ASCII 1's complement checksum             
DATASUM  3285390374              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU34
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ====================== ===== ===========================================
KEY      Value                  Type  Comment                                    
======== ====================== ===== ===========================================
ZIMAGE   T                      bool  extension contains compressed image        
ZTILE1   2160                   int   size of tiles to be compressed             
ZTILE2   1                      int   size of tiles to be compressed             
ZCMPTYPE RICE_1                 str   compression algorithm                      
ZNAME1   BLOCKSIZE              str   compression block size                     
ZVAL1    32                     int   pixels per block                           
ZNAME2   BYTEPIX                str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                      int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                  str   IMAGE extension                            
ZBITPIX  16                     int   number of bits per data pixel              
ZNAXIS   2                      int   number of data axes                        
ZNAXIS1  2160                   int   length of data axis 1                      
ZNAXIS2  4146                   int   length of data axis 2                      
ZPCOUNT  0                      int   required keyword; must = 0                 
ZGCOUNT  1                      int   required keyword; must = 1                 
BZERO    32768                  int   offset data range to that of unsigned short
BSCALE   1                      int   default scaling factor                     
BUNIT    adu                    str   Brightness units for pixel array           
WCSAXES  2                      int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]      str   Detector size                              
TRIMSEC  [57:2104,51:4146]      str   Good section                               
DATASEC  [57:2104,51:4146]      str   Data section to display                    
DETSEC   [2049:4096,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]        str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]    str   Good section from amp A                    
DETSECA  [3073:4096,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]     str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]     str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]    str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]    str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]    str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]       str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]      str   Good section from amp B                    
DETSECB  [2049:3072,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]        str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]        str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]      str   Data section from amp B                    
BIASSECB [7:56,51:4146]         str   Overscan from amp B                        
PRESECB  [1:6,51:4146]          str   Prescan from amp B                         
POSTSECB [57:1080,1:50]         str   Postscan from amp B                        
DETECTOR S3-06_123195-15-3      str   Detector Identifier                        
CCDNUM   1                      int   CCD number                                 
DETPOS   S29                    str   detector position ID                       
EXTNAME  S29                    str   extension name                             
GAINA    4.41501103753          float [electrons/adu] Gain for amp A             
RDNOISEA 6.67373068433          float [electrons] Read noise for amp A           
SATURATA 39748.0                float [adu] Saturation for amp A                 
GAINB    4.26439232409          float [electrons/adu] Gain for amp B             
RDNOISEB 6.52878464819          float [electrons] Read noise for amp B           
SATURATB 38895.0                float [adu] Saturation for amp B                 
CRPIX1   13423.2                float Coordinate Reference axis 1                
CRPIX2   6307.333               float Coordinate Reference axis 2                
FPA      DECAM_BKP3             str   DECam focal plane name                     
INHERIT  T                      bool  Inherits PHDU header                       
CCDBIN1  1                      int   Pixel binning, axis 1                      
CCDBIN2  1                      int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware    str   DHE Hardware                               
DHEFIRM  demo30                 str   DHE Firmware                               
SLOT00   MCB 12 5.210000        str   Monsoon module                             
SLOT01   DESCB 11 4.010000      str   Monsoon module                             
SLOT02   DESCB 12 4.010000      str   Monsoon module                             
SLOT03   CCD12 29 4.080000      str   Monsoon module                             
SLOT04   CCD12 15 4.080000      str   Monsoon module                             
SLOT05   CCD12 28 4.080000      str   Monsoon module                             
RADESYS  FK5                    str   World coordinate reference frame           
EQUINOX  2000.0                 float [yr] Equinox of WCS                        
PV1_7    0.000618368874624      float PV distortion coefficient                  
CUNIT1   deg                    str                                              
PV2_8    -0.00842887692623      float PV distortion coefficient                  
PV2_9    0.00790302236959       float PV distortion coefficient                  
CD1_1    -1.8249413473e-07      float World coordinate transformation matrix     
LTM2_2   1.0                    float Detector to image transformation           
LTM2_1   0.0                    float Detector to image transformation           
PV2_0    -0.00441101222605      float PV distortion coefficient                  
PV2_1    1.01700592995          float PV distortion coefficient                  
PV2_2    -0.00863195988986      float PV distortion coefficient                  
PV2_3    0.0                    float PV distortion coefficient                  
PV2_4    -0.0181936225912       float PV distortion coefficient                  
PV2_5    0.0168279891847        float PV distortion coefficient                  
PV2_6    -0.010365069688        float PV distortion coefficient                  
PV2_7    0.00641705596954       float PV distortion coefficient                  
LTM1_1   1.0                    float Detector to image transformation           
PV1_6    0.010153274645         float PV distortion coefficient                  
PV2_10   -0.00261077202228      float PV distortion coefficient                  
PV1_4    0.00862489761958       float PV distortion coefficient                  
PV1_3    0.0                    float PV distortion coefficient                  
PV1_2    -0.00978790747587      float PV distortion coefficient                  
PV1_1    1.01430869337          float PV distortion coefficient                  
PV1_0    0.00392185213728       float PV distortion coefficient                  
LTM1_2   0.0                    float Detector to image transformation           
PV1_9    0.00654393666949       float PV distortion coefficient                  
PV1_8    -0.00736713022181      float PV distortion coefficient                  
CD1_2    7.28535892432e-05      float World coordinate transformation matrix     
PV1_5    -0.017864081795        float PV distortion coefficient                  
CUNIT2   deg                    str                                              
CD2_1    -7.28499004539e-05     float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07     float World coordinate transformation matrix     
LTV2     50.0                   float Detector to image transformation           
LTV1     56.0                   float Detector to image transformation           
PV1_10   -0.00361076208606      float PV distortion coefficient                  
CTYPE2   DEC--TPV               str   Coordinate type                            
CTYPE1   RA---TPV               str   Coordinate type                            
CRVAL1   237.447283             float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611               float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                      bool  Data from amp A is valid                   
VALIDB   T                      bool  Data from amp B is valid                   
NDONUTS  0                      int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT             str    FITS checksum version                     
CHECKSUM ZJ2AdI08ZI0AdI05       str    ASCII 1's complement checksum             
DATASUM  3834622858             str    checksum of data records                  
======== ====================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU35
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [2049:4096,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [3073:4096,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [2049:3072,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-138_135959-17-3      str   Detector Identifier                        
CCDNUM   2                       int   CCD number                                 
DETPOS   S30                     str   detector position ID                       
EXTNAME  S30                     str   extension name                             
GAINA    4.61893764434           float [electrons/adu] Gain for amp A             
RDNOISEA 6.76720554273           float [electrons] Read noise for amp A           
SATURATA 43375.0                 float [adu] Saturation for amp A                 
GAINB    4.57875457875           float [electrons/adu] Gain for amp B             
RDNOISEB 6.82051282051           float [electrons] Read noise for amp B           
SATURATB 44078.0                 float [adu] Saturation for amp B                 
CRPIX1   13423.2                 float Coordinate Reference axis 1                
CRPIX2   2048.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    -0.00133974250828       float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    7.80666520248e-05       float PV distortion coefficient                  
PV2_9    0.00637387071068        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.0087604868062        float PV distortion coefficient                  
PV2_1    1.03214315189           float PV distortion coefficient                  
PV2_2    -0.00162729037621       float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.0365108168353        float PV distortion coefficient                  
PV2_5    -0.000263380980286      float PV distortion coefficient                  
PV2_6    -0.00763887899752       float PV distortion coefficient                  
PV2_7    0.0136456601536         float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.00128527028984       float PV distortion coefficient                  
PV2_10   0.000332932486876       float PV distortion coefficient                  
PV1_4    -0.000861806001591      float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.00299536834353        float PV distortion coefficient                  
PV1_1    1.01077653064           float PV distortion coefficient                  
PV1_0    -0.00216182330648       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00570093134103        float PV distortion coefficient                  
PV1_8    0.000826181411617       float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.0137720247464        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00043211026843        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 9iZWDhWV9hWVAhWV        str    ASCII 1's complement checksum             
DATASUM  1021437869              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU36
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  4146                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:4146]       str   Good section                               
DATASEC  [57:2104,51:4146]       str   Data section to display                    
DETSEC   [2049:4096,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]         str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]     str   Good section from amp A                    
DETSECA  [3073:4096,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]      str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]     str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]       str   Good section from amp B                    
DETSECB  [2049:3072,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]         str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]       str   Data section from amp B                    
BIASSECB [7:56,51:4146]          str   Overscan from amp B                        
PRESECB  [1:6,51:4146]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR S3-154_123195-19-4      str   Detector Identifier                        
CCDNUM   3                       int   CCD number                                 
DETPOS   S31                     str   detector position ID                       
EXTNAME  S31                     str   extension name                             
GAINA    4.29737859905           float [electrons/adu] Gain for amp A             
RDNOISEA 6.39363987967           float [electrons] Read noise for amp A           
SATURATA 44635.0                 float [adu] Saturation for amp A                 
GAINB    4.20521446594           float [electrons/adu] Gain for amp B             
RDNOISEB 6.28847771236           float [electrons] Read noise for amp B           
SATURATB 44760.0                 float [adu] Saturation for amp B                 
CRPIX1   13423.2                 float Coordinate Reference axis 1                
CRPIX2   -2211.333               float Coordinate Reference axis 2                
FPA      DECAM_BKP3              str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 12 5.210000         str   Monsoon module                             
SLOT01   DESCB 11 4.010000       str   Monsoon module                             
SLOT02   DESCB 12 4.010000       str   Monsoon module                             
SLOT03   CCD12 29 4.080000       str   Monsoon module                             
SLOT04   CCD12 15 4.080000       str   Monsoon module                             
SLOT05   CCD12 28 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.00058733743652        float PV distortion coefficient                  
CUNIT1   deg                     str                                              
PV2_8    0.00904256612128        float PV distortion coefficient                  
PV2_9    0.00710579682233        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07       float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    -0.00596328842598       float PV distortion coefficient                  
PV2_1    1.02277454071           float PV distortion coefficient                  
PV2_2    0.00861804477576        float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    -0.0247234008466        float PV distortion coefficient                  
PV2_5    -0.0174692820007        float PV distortion coefficient                  
PV2_6    -0.00995467756253       float PV distortion coefficient                  
PV2_7    0.00884423211663        float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    -0.0138800477623        float PV distortion coefficient                  
PV2_10   0.00297373965497        float PV distortion coefficient                  
PV1_4    -0.00962826300077       float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0131442678081         float PV distortion coefficient                  
PV1_1    1.01455831192           float PV distortion coefficient                  
PV1_0    -0.00493451962707       float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.00622192157611        float PV distortion coefficient                  
PV1_8    0.00852151918062        float PV distortion coefficient                  
CD1_2    7.28535892432e-05       float World coordinate transformation matrix     
PV1_5    -0.0178809744613        float PV distortion coefficient                  
CUNIT2   deg                     str                                              
CD2_1    -7.28499004539e-05      float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07      float World coordinate transformation matrix     
LTV2     50.0                    float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.00503417067849        float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM GBdAIAcAGAcAGAcA        str    ASCII 1's complement checksum             
DATASUM  3138854017              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU37
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [14337:16384,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [14337:15360,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [15361:16384,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-187_124750-6-1         str   Detector Identifier                        
CCDNUM   35                        int   CCD number                                 
DETPOS   N4                        str   detector position ID                       
EXTNAME  N4                        str   extension name                             
GAINA    4.30663221361             float [electrons/adu] Gain for amp A             
RDNOISEA 6.78854435831             float [electrons] Read noise for amp A           
SATURATA 46753.0                   float [adu] Saturation for amp A                 
GAINB    4.28816466552             float [electrons/adu] Gain for amp B             
RDNOISEB 6.70240137221             float [electrons] Read noise for amp B           
SATURATB 45007.0                   float [adu] Saturation for amp B                 
CRPIX1   -103.2001                 float Coordinate Reference axis 1                
CRPIX2   2048.0                    float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00514060942565         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000924343625343        float PV distortion coefficient                  
PV2_9    -0.00364472470902         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000163971820432         float PV distortion coefficient                  
PV2_1    1.00549074963             float PV distortion coefficient                  
PV2_2    2.08713064819e-05         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00212064802375         float PV distortion coefficient                  
PV2_5    -0.000205295388566        float PV distortion coefficient                  
PV2_6    0.000148472380419         float PV distortion coefficient                  
PV2_7    -0.011734691522           float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000466264080618        float PV distortion coefficient                  
PV2_10   0.000178193596804         float PV distortion coefficient                  
PV1_4    -0.000185764356613        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -8.524667568e-05          float PV distortion coefficient                  
PV1_1    1.00567531603             float PV distortion coefficient                  
PV1_0    -3.85182451318e-05        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00453842699985         float PV distortion coefficient                  
PV1_8    0.000338187333513         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.000136304818357        float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00185637053335         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM ToYSUnXPTnXPTnXP          str    ASCII 1's complement checksum             
DATASUM  3323888300                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU38
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [14337:16384,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [14337:15360,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [15361:16384,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-133_135959-8-1         str   Detector Identifier                        
CCDNUM   36                        int   CCD number                                 
DETPOS   N5                        str   detector position ID                       
EXTNAME  N5                        str   extension name                             
GAINA    4.28265524625             float [electrons/adu] Gain for amp A             
RDNOISEA 6.84325481799             float [electrons] Read noise for amp A           
SATURATA 47455.0                   float [adu] Saturation for amp A                 
GAINB    4.48028673835             float [electrons/adu] Gain for amp B             
RDNOISEB 7.10976702509             float [electrons] Read noise for amp B           
SATURATB 44883.0                   float [adu] Saturation for amp B                 
CRPIX1   -103.2001                 float Coordinate Reference axis 1                
CRPIX2   -2211.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00318799439724         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000924245829302        float PV distortion coefficient                  
PV2_9    -0.00351549457585         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000123890683547        float PV distortion coefficient                  
PV2_1    1.00572288701             float PV distortion coefficient                  
PV2_2    0.000606023083            float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -2.87968324244e-05        float PV distortion coefficient                  
PV2_5    -0.000460900031476        float PV distortion coefficient                  
PV2_6    0.000536747377421         float PV distortion coefficient                  
PV2_7    -0.00515852430319         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000166517702881        float PV distortion coefficient                  
PV2_10   -0.000467354397833        float PV distortion coefficient                  
PV1_4    -0.000779349819067        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000970902542536        float PV distortion coefficient                  
PV1_1    1.00588127771             float PV distortion coefficient                  
PV1_0    -0.000967493835611        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00372166611779         float PV distortion coefficient                  
PV1_8    -0.00178121336354         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00111568480162          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.000392940605043        float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 9RecAOeZ9OeaAOeY          str    ASCII 1's complement checksum             
DATASUM  28982289                  str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU39
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [14337:16384,20481:24576] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [14337:15360,20481:24576] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [15361:16384,20481:24576] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-177_107419-14-1        str   Detector Identifier                        
CCDNUM   37                        int   CCD number                                 
DETPOS   N6                        str   detector position ID                       
EXTNAME  N6                        str   extension name                             
GAINA    4.36490615452             float [electrons/adu] Gain for amp A             
RDNOISEA 6.56045395024             float [electrons] Read noise for amp A           
SATURATA 46251.0                   float [adu] Saturation for amp A                 
GAINB    4.55373406193             float [electrons/adu] Gain for amp B             
RDNOISEB 6.99954462659             float [electrons] Read noise for amp B           
SATURATB 42492.0                   float [adu] Saturation for amp B                 
CRPIX1   -103.2001                 float Coordinate Reference axis 1                
CRPIX2   -6470.667                 float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00120808632091          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -7.47453476229e-05        float PV distortion coefficient                  
PV2_9    -0.0012888008955          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000340903967547         float PV distortion coefficient                  
PV2_1    1.0062274883              float PV distortion coefficient                  
PV2_2    -0.00068019010043         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.000225120199853         float PV distortion coefficient                  
PV2_5    -0.00245037339691         float PV distortion coefficient                  
PV2_6    0.00113237302523          float PV distortion coefficient                  
PV2_7    -0.00250699248089         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00142621408213         float PV distortion coefficient                  
PV2_10   -0.000556505462091        float PV distortion coefficient                  
PV1_4    -0.0074187702998          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000621322306193        float PV distortion coefficient                  
PV1_1    1.00937393652             float PV distortion coefficient                  
PV1_0    -0.00211764626303         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00154389991973         float PV distortion coefficient                  
PV1_8    -0.00137964768513         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00174052119165          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00134487055661         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM WGmiaDmhZDmhaDmh          str    ASCII 1's complement checksum             
DATASUM  1564794476                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU40
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [14337:16384,24577:28672] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [14337:15360,24577:28672] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [15361:16384,24577:28672] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-194_123195-18-4        str   Detector Identifier                        
CCDNUM   38                        int   CCD number                                 
DETPOS   N7                        str   detector position ID                       
EXTNAME  N7                        str   extension name                             
GAINA    4.68823253633             float [electrons/adu] Gain for amp A             
RDNOISEA 7.12423816221             float [electrons] Read noise for amp A           
SATURATA 42216.0                   float [adu] Saturation for amp A                 
GAINB    4.41696113074             float [electrons/adu] Gain for amp B             
RDNOISEB 6.86395759717             float [electrons] Read noise for amp B           
SATURATB 44144.0                   float [adu] Saturation for amp B                 
CRPIX1   -103.2001                 float Coordinate Reference axis 1                
CRPIX2   -10730.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.0133665867145           float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00268307360532         float PV distortion coefficient                  
PV2_9    0.00595967064359          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000173514142013         float PV distortion coefficient                  
PV2_1    1.01143967813             float PV distortion coefficient                  
PV2_2    0.000482297943323         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00148176612886          float PV distortion coefficient                  
PV2_5    -0.0148085846576          float PV distortion coefficient                  
PV2_6    -0.000948762933042        float PV distortion coefficient                  
PV2_7    -0.00583981436707         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00846931537954         float PV distortion coefficient                  
PV2_10   0.000392809918529         float PV distortion coefficient                  
PV1_4    -0.0359150642885          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000593024829405        float PV distortion coefficient                  
PV1_1    1.03176390333             float PV distortion coefficient                  
PV1_0    -0.00854559186175         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00700620615035          float PV distortion coefficient                  
PV1_8    -0.000587267315598        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00141133319595          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00186532681837         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 9VRAITP79TPAGTP7          str    ASCII 1's complement checksum             
DATASUM  212773296                 str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU41
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [12289:14336,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [13313:14336,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [12289:13312,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-214_124750-21-3        str   Detector Identifier                        
CCDNUM   28                        int   CCD number                                 
DETPOS   S4                        str   detector position ID                       
EXTNAME  S4                        str   extension name                             
GAINA    4.38020148927             float [electrons/adu] Gain for amp A             
RDNOISEA 6.84056066579             float [electrons] Read noise for amp A           
SATURATA 47271.0                   float [adu] Saturation for amp A                 
GAINB    4.56829602558             float [electrons/adu] Gain for amp B             
RDNOISEB 6.90589310187             float [electrons] Read noise for amp B           
SATURATB 43600.0                   float [adu] Saturation for amp B                 
CRPIX1   2151.2                    float Coordinate Reference axis 1                
CRPIX2   2048.0                    float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00455890451146         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00016434787284         float PV distortion coefficient                  
PV2_9    -0.00338572119261         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000101860154118        float PV distortion coefficient                  
PV2_1    1.00562966516             float PV distortion coefficient                  
PV2_2    0.000296201087258         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.000824275492071         float PV distortion coefficient                  
PV2_5    9.62815084357e-05         float PV distortion coefficient                  
PV2_6    -9.07130093109e-05        float PV distortion coefficient                  
PV2_7    -0.00788530016525         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000248051171036        float PV distortion coefficient                  
PV2_10   0.000484269401983         float PV distortion coefficient                  
PV1_4    -0.00024329640589         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000338800300778        float PV distortion coefficient                  
PV1_1    1.00568019103             float PV distortion coefficient                  
PV1_0    0.000285674387099         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00381410563223         float PV distortion coefficient                  
PV1_8    0.00145901942624          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.000162539601835        float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00105155810998          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM ZLD5dKD2ZKD2bKD2          str    ASCII 1's complement checksum             
DATASUM  2982731262                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU42
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [12289:14336,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [13313:14336,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [12289:13312,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-150_124750-7-3         str   Detector Identifier                        
CCDNUM   29                        int   CCD number                                 
DETPOS   S5                        str   detector position ID                       
EXTNAME  S5                        str   extension name                             
GAINA    4.34027777778             float [electrons/adu] Gain for amp A             
RDNOISEA 6.82248263889             float [electrons] Read noise for amp A           
SATURATA 46671.0                   float [adu] Saturation for amp A                 
GAINB    4.39174352218             float [electrons/adu] Gain for amp B             
RDNOISEB 6.87088274045             float [electrons] Read noise for amp B           
SATURATB 45384.0                   float [adu] Saturation for amp B                 
CRPIX1   2151.2                    float Coordinate Reference axis 1                
CRPIX2   -2211.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00330789589543         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    7.21044504941e-05         float PV distortion coefficient                  
PV2_9    -0.00376743302627         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.00034086691091         float PV distortion coefficient                  
PV2_1    1.00555450201             float PV distortion coefficient                  
PV2_2    0.000406792254563         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0025025594164           float PV distortion coefficient                  
PV2_5    -0.00020415415495         float PV distortion coefficient                  
PV2_6    -0.000608007896241        float PV distortion coefficient                  
PV2_7    -0.0141187624445          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.000357764560595         float PV distortion coefficient                  
PV2_10   0.000656558169235         float PV distortion coefficient                  
PV1_4    -0.000652031979234        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000225514090865        float PV distortion coefficient                  
PV1_1    1.00582940524             float PV distortion coefficient                  
PV1_0    -0.000643316748875        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00441691184207         float PV distortion coefficient                  
PV1_8    0.000488058902011         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.000268852089406        float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00099473778186         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 0eXi3dWi0dWi0dWi          str    ASCII 1's complement checksum             
DATASUM  1302263184                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU43
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [12289:14336,20481:24576] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [13313:14336,20481:24576] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [12289:13312,20481:24576] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-186_135959-8-3         str   Detector Identifier                        
CCDNUM   30                        int   CCD number                                 
DETPOS   S6                        str   detector position ID                       
EXTNAME  S6                        str   extension name                             
GAINA    4.49438202247             float [electrons/adu] Gain for amp A             
RDNOISEA 7.21213483146             float [electrons] Read noise for amp A           
SATURATA 47461.0                   float [adu] Saturation for amp A                 
GAINB    4.43655723159             float [electrons/adu] Gain for amp B             
RDNOISEB 7.04614019521             float [electrons] Read noise for amp B           
SATURATB 46472.0                   float [adu] Saturation for amp B                 
CRPIX1   2151.2                    float Coordinate Reference axis 1                
CRPIX2   -6470.667                 float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00134158822336          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.000911051315386         float PV distortion coefficient                  
PV2_9    -0.0014683322831          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.000353070558938        float PV distortion coefficient                  
PV2_1    1.00619900444             float PV distortion coefficient                  
PV2_2    0.00033135114545          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00120224112216          float PV distortion coefficient                  
PV2_5    -0.00245789543206         float PV distortion coefficient                  
PV2_6    -0.000273157429399        float PV distortion coefficient                  
PV2_7    -0.0104379727939          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000481171704887        float PV distortion coefficient                  
PV2_10   0.000145594612537         float PV distortion coefficient                  
PV1_4    -0.00771396578946         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000220343681585        float PV distortion coefficient                  
PV1_1    1.00957291654             float PV distortion coefficient                  
PV1_0    -0.00176646212898         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00298206415369         float PV distortion coefficient                  
PV1_8    0.000188570959626         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    2.76869667786e-05         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00105497144627          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM efNaecLUecLaecLU          str    ASCII 1's complement checksum             
DATASUM  1897139615                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU44
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:4146]         str   Good section                               
DATASEC  [57:2104,51:4146]         str   Data section to display                    
DETSEC   [12289:14336,24577:28672] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [1081:2104,51:4146]       str   Good section from amp A                    
DETSECA  [13313:14336,24577:28672] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:4096]        str   CCD section from amp A                     
AMPSECA  [2048:1025,4096:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:4146]       str   Data section from amp A                    
BIASSECA [2105:2154,51:4146]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:4146]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:4146]         str   Good section from amp B                    
DETSECB  [12289:13312,24577:28672] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:4096]           str   CCD section from amp B                     
AMPSECB  [1:1024,4096:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:4146]         str   Data section from amp B                    
BIASSECB [7:56,51:4146]            str   Overscan from amp B                        
PRESECB  [1:6,51:4146]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR S3-183_123194-18-4        str   Detector Identifier                        
CCDNUM   31                        int   CCD number                                 
DETPOS   S7                        str   detector position ID                       
EXTNAME  S7                        str   extension name                             
GAINA    4.38020148927             float [electrons/adu] Gain for amp A             
RDNOISEA 7.21988611476             float [electrons] Read noise for amp A           
SATURATA 38914.0                   float [adu] Saturation for amp A                 
GAINB    4.84730974309             float [electrons/adu] Gain for amp B             
RDNOISEB 7.72176442075             float [electrons] Read noise for amp B           
SATURATB 45307.0                   float [adu] Saturation for amp B                 
CRPIX1   2151.2                    float Coordinate Reference axis 1                
CRPIX2   -10730.0                  float Coordinate Reference axis 2                
FPA      DECAM_BKP4                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 0x1B70D10 5.210000    str   Monsoon module                             
SLOT01   DESCB 1 4.010000          str   Monsoon module                             
SLOT02   CCD12 20 4.080000         str   Monsoon module                             
SLOT03   CCD12 9 4.080000          str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.0142588965069           float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.00320639731374          float PV distortion coefficient                  
PV2_9    0.00550062774691          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    -0.00115434528918         float PV distortion coefficient                  
PV2_1    1.01095414767             float PV distortion coefficient                  
PV2_2    0.0027822958895           float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00206667506425         float PV distortion coefficient                  
PV2_5    -0.0138167908187          float PV distortion coefficient                  
PV2_6    -0.00249202263633         float PV distortion coefficient                  
PV2_7    -0.00489313165176         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00538823581639         float PV distortion coefficient                  
PV2_10   0.000848082901645         float PV distortion coefficient                  
PV1_4    -0.038208269692           float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.00117190836525          float PV distortion coefficient                  
PV1_1    1.03370964999             float PV distortion coefficient                  
PV1_0    -0.00895410431714         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.0035712442694           float PV distortion coefficient                  
PV1_8    0.00176380325427          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -0.00330977785024         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     50.0                      float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00158411899744          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM ZDZAZBZ9ZBZAZBZ9          str    ASCII 1's complement checksum             
DATASUM  2838088432                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU45
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [16385:18432,10240:14335] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [16385:17408,10240:14335] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [17409:18432,10240:14335] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-301_135960-7-3         str   Detector Identifier                        
CCDNUM   41                        int   CCD number                                 
DETPOS   N10                       str   detector position ID                       
EXTNAME  N10                       str   extension name                             
GAINA    4.33087916847             float [electrons/adu] Gain for amp A             
RDNOISEA 6.50324815938             float [electrons] Read noise for amp A           
SATURATA 46390.0                   float [adu] Saturation for amp A                 
GAINB    4.64468183929             float [electrons/adu] Gain for amp B             
RDNOISEB 6.8671620994              float [electrons] Read noise for amp B           
SATURATB 43719.0                   float [adu] Saturation for amp B                 
CRPIX1   -2357.6                   float Coordinate Reference axis 1                
CRPIX2   4177.667                  float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00469363657495         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.00155357579743          float PV distortion coefficient                  
PV2_9    -0.00311822678654         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000614452168603         float PV distortion coefficient                  
PV2_1    1.0049522739              float PV distortion coefficient                  
PV2_2    0.000541363262318         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00324632670807         float PV distortion coefficient                  
PV2_5    0.00110327715877          float PV distortion coefficient                  
PV2_6    0.000233889588833         float PV distortion coefficient                  
PV2_7    -0.00865086175303         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.000746212790057         float PV distortion coefficient                  
PV2_10   -1.84243264841e-05        float PV distortion coefficient                  
PV1_4    -0.000170945921303        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000214865495568        float PV distortion coefficient                  
PV1_1    1.00567972664             float PV distortion coefficient                  
PV1_0    0.000266043019338         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00388796046015         float PV distortion coefficient                  
PV1_8    -9.09811944831e-05        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    -1.50852450998e-05        float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00106422569477          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 8FJXACJV2CJV8CJV          str    ASCII 1's complement checksum             
DATASUM  1896938940                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU46
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [16385:18432,14336:18431] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [16385:17408,14336:18431] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [17409:18432,14336:18431] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-302_135960-8-3         str   Detector Identifier                        
CCDNUM   42                        int   CCD number                                 
DETPOS   N11                       str   detector position ID                       
EXTNAME  N11                       str   extension name                             
GAINA    4.41696113074             float [electrons/adu] Gain for amp A             
RDNOISEA 6.60159010601             float [electrons] Read noise for amp A           
SATURATA 49309.0                   float [adu] Saturation for amp A                 
GAINB    4.34216239687             float [electrons/adu] Gain for amp B             
RDNOISEB 6.92401215805             float [electrons] Read noise for amp B           
SATURATB 49533.0                   float [adu] Saturation for amp B                 
CRPIX1   -2357.6                   float Coordinate Reference axis 1                
CRPIX2   -81.66665                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00332662202921         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00219356213493         float PV distortion coefficient                  
PV2_9    -0.00302183590444         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000383766208478         float PV distortion coefficient                  
PV2_1    1.00452289497             float PV distortion coefficient                  
PV2_2    -7.22482452168e-05        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.0051964900393          float PV distortion coefficient                  
PV2_5    -0.00138775831016         float PV distortion coefficient                  
PV2_6    0.000377048610748         float PV distortion coefficient                  
PV2_7    -0.0114956926799          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.000944845280327        float PV distortion coefficient                  
PV2_10   -0.00018824993729         float PV distortion coefficient                  
PV1_4    -0.000542542571635        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000408990486321        float PV distortion coefficient                  
PV1_1    1.00572370178             float PV distortion coefficient                  
PV1_0    -0.000336145286764        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00397263079725         float PV distortion coefficient                  
PV1_8    -0.000635836488334        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.000154032516918         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00120924593014         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM FINMGFNMFFNMFFNM          str    ASCII 1's complement checksum             
DATASUM  1104237921                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU47
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [16385:18432,18432:22527] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [16385:17408,18432:22527] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [17409:18432,18432:22527] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-243_135960-2-2         str   Detector Identifier                        
CCDNUM   43                        int   CCD number                                 
DETPOS   N12                       str   detector position ID                       
EXTNAME  N12                       str   extension name                             
GAINA    4.52693526483             float [electrons/adu] Gain for amp A             
RDNOISEA 6.79719330014             float [electrons] Read noise for amp A           
SATURATA 40761.0                   float [adu] Saturation for amp A                 
GAINB    4.26985482494             float [electrons/adu] Gain for amp B             
RDNOISEB 6.56276686593             float [electrons] Read noise for amp B           
SATURATB 41908.0                   float [adu] Saturation for amp B                 
CRPIX1   -2357.6                   float Coordinate Reference axis 1                
CRPIX2   -4341.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00180904861084         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000883085985139        float PV distortion coefficient                  
PV2_9    -0.00261692921212         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000422231099021         float PV distortion coefficient                  
PV2_1    1.00477080324             float PV distortion coefficient                  
PV2_2    -0.000362613017084        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00412147761169         float PV distortion coefficient                  
PV2_5    -0.00114300726895         float PV distortion coefficient                  
PV2_6    0.00102887099455          float PV distortion coefficient                  
PV2_7    -0.00943731933055         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -6.88119921957e-05        float PV distortion coefficient                  
PV2_10   -0.000711701211077        float PV distortion coefficient                  
PV1_4    -0.00273153604111         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000540998255748        float PV distortion coefficient                  
PV1_1    1.00687338047             float PV distortion coefficient                  
PV1_0    -0.0011743690979          float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00247360068559         float PV distortion coefficient                  
PV1_8    -0.0022253489897          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00215429716993          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.000568068320504         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM eA2ih72heA2he52h          str    ASCII 1's complement checksum             
DATASUM  2657865782                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU48
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [16385:18432,22528:26623] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [16385:17408,22528:26623] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [17409:18432,22528:26623] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-310_135959-5-1         str   Detector Identifier                        
CCDNUM   44                        int   CCD number                                 
DETPOS   N13                       str   detector position ID                       
EXTNAME  N13                       str   extension name                             
GAINA    4.25531914894             float [electrons/adu] Gain for amp A             
RDNOISEA 6.45574468085             float [electrons] Read noise for amp A           
SATURATA 46163.0                   float [adu] Saturation for amp A                 
GAINB    4.30848772081             float [electrons/adu] Gain for amp B             
RDNOISEB 6.7190866006              float [electrons] Read noise for amp B           
SATURATB 45708.0                   float [adu] Saturation for amp B                 
CRPIX1   -2357.6                   float Coordinate Reference axis 1                
CRPIX2   -8600.334                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00763081503543          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.0042465655745          float PV distortion coefficient                  
PV2_9    0.00166206244596          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.0015270549873           float PV distortion coefficient                  
PV2_1    1.00804406903             float PV distortion coefficient                  
PV2_2    -0.00413185525339         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    3.20358221714e-06         float PV distortion coefficient                  
PV2_5    -0.00810481614457         float PV distortion coefficient                  
PV2_6    0.00510933076065          float PV distortion coefficient                  
PV2_7    -0.00704492600986         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00524843191938         float PV distortion coefficient                  
PV2_10   -0.00212605935659         float PV distortion coefficient                  
PV1_4    -0.0223435255369          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00442330201001         float PV distortion coefficient                  
PV1_1    1.02103980367             float PV distortion coefficient                  
PV1_0    -0.00547109069507         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00209440766726          float PV distortion coefficient                  
PV1_8    -0.00633593346966         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0102047280734           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00263992497473         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM bTcgeQbZbQbfbQbZ          str    ASCII 1's complement checksum             
DATASUM  1613434672                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU49
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [18433:20480,18432:22527] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [18433:19456,18432:22527] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [19457:20480,18432:22527] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-329_135960-17-1        str   Detector Identifier                        
CCDNUM   49                        int   CCD number                                 
DETPOS   N18                       str   detector position ID                       
EXTNAME  N18                       str   extension name                             
GAINA    4.30107526882             float [electrons/adu] Gain for amp A             
RDNOISEA 6.43569892473             float [electrons] Read noise for amp A           
SATURATA 49133.0                   float [adu] Saturation for amp A                 
GAINB    4.57456541629             float [electrons/adu] Gain for amp B             
RDNOISEB 6.82250686185             float [electrons] Read noise for amp B           
SATURATB 44942.0                   float [adu] Saturation for amp B                 
CRPIX1   -4612.0                   float Coordinate Reference axis 1                
CRPIX2   -4341.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.000168749051459        float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00443557345881         float PV distortion coefficient                  
PV2_9    -0.000100546170616        float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00141524942844          float PV distortion coefficient                  
PV2_1    1.0069607361              float PV distortion coefficient                  
PV2_2    -0.00254289026187         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.000694478291505         float PV distortion coefficient                  
PV2_5    -0.00605580612847         float PV distortion coefficient                  
PV2_6    0.00331810227691          float PV distortion coefficient                  
PV2_7    -0.00433244726963         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00268844137635         float PV distortion coefficient                  
PV2_10   -0.00162804745013         float PV distortion coefficient                  
PV1_4    -0.00580192051582         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00196117180579         float PV distortion coefficient                  
PV1_1    1.00891778507             float PV distortion coefficient                  
PV1_0    -0.00162271058219         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.000502266667157        float PV distortion coefficient                  
PV1_8    -0.00432831920042         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00560421660361          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.0014467472559          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 3knC6hlA3hlA3hlA          str    ASCII 1's complement checksum             
DATASUM  262184231                 str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU50
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [18433:20480,22528:26623] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [18433:19456,22528:26623] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [19457:20480,22528:26623] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-235_135959-22-2        str   Detector Identifier                        
CCDNUM   50                        int   CCD number                                 
DETPOS   N19                       str   detector position ID                       
EXTNAME  N19                       str   extension name                             
GAINA    4.29737859905             float [electrons/adu] Gain for amp A             
RDNOISEA 6.37773957886             float [electrons] Read noise for amp A           
SATURATA 48173.0                   float [adu] Saturation for amp A                 
GAINB    4.71698113208             float [electrons/adu] Gain for amp B             
RDNOISEB 6.78066037736             float [electrons] Read noise for amp B           
SATURATB 43210.0                   float [adu] Saturation for amp B                 
CRPIX1   -4612.0                   float Coordinate Reference axis 1                
CRPIX2   -8600.334                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00986863900444          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00808009120193         float PV distortion coefficient                  
PV2_9    0.00667286127161          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00404079521162          float PV distortion coefficient                  
PV2_1    1.01270209144             float PV distortion coefficient                  
PV2_2    -0.0103608440337          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.00457651410127          float PV distortion coefficient                  
PV2_5    -0.0184084840501          float PV distortion coefficient                  
PV2_6    0.0109606670848           float PV distortion coefficient                  
PV2_7    -0.00299237838418         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00859675862354         float PV distortion coefficient                  
PV2_10   -0.00391270043102         float PV distortion coefficient                  
PV1_4    -0.0287933468596          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00907804462984         float PV distortion coefficient                  
PV1_1    1.02742674661             float PV distortion coefficient                  
PV1_0    -0.00757285429449         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00620647304602          float PV distortion coefficient                  
PV1_8    -0.0102989534053          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0190838597034           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00251814492373         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM cWEAeTB4cTBAcTB3          str    ASCII 1's complement checksum             
DATASUM  967420210                 str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU51
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [18433:20480,10240:14335] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [18433:19456,10240:14335] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [19457:20480,10240:14335] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-117_123194-23-4        str   Detector Identifier                        
CCDNUM   47                        int   CCD number                                 
DETPOS   N16                       str   detector position ID                       
EXTNAME  N16                       str   extension name                             
GAINA    4.39367311072             float [electrons/adu] Gain for amp A             
RDNOISEA 6.64191564148             float [electrons] Read noise for amp A           
SATURATA 48450.0                   float [adu] Saturation for amp A                 
GAINB    4.54545454545             float [electrons/adu] Gain for amp B             
RDNOISEB 6.77727272727             float [electrons] Read noise for amp B           
SATURATB 45650.0                   float [adu] Saturation for amp B                 
CRPIX1   -4612.0                   float Coordinate Reference axis 1                
CRPIX2   4177.667                  float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.0048733840134          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000221553306954        float PV distortion coefficient                  
PV2_9    -0.00294994834706         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00042787738646          float PV distortion coefficient                  
PV2_1    1.00281779648             float PV distortion coefficient                  
PV2_2    -0.000217726235045        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00680809472004         float PV distortion coefficient                  
PV2_5    -7.49832087241e-05        float PV distortion coefficient                  
PV2_6    0.000775904098912         float PV distortion coefficient                  
PV2_7    -0.0092824377455          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.000769729665217         float PV distortion coefficient                  
PV2_10   0.000705725499373         float PV distortion coefficient                  
PV1_4    0.000160605418801         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.000640841464668         float PV distortion coefficient                  
PV1_1    1.00578008856             float PV distortion coefficient                  
PV1_0    0.000462057631302         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00365838517517         float PV distortion coefficient                  
PV1_8    0.00118869207771          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00042882575315          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.000558416219855         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM kTcLnSbIkSbIkSbI          str    ASCII 1's complement checksum             
DATASUM  1351769609                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU52
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [18433:20480,14336:18431] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [18433:19456,14336:18431] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [19457:20480,14336:18431] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-122_135959-17-2        str   Detector Identifier                        
CCDNUM   48                        int   CCD number                                 
DETPOS   N17                       str   detector position ID                       
EXTNAME  N17                       str   extension name                             
GAINA    4.43655723159             float [electrons/adu] Gain for amp A             
RDNOISEA 6.61268855368             float [electrons] Read noise for amp A           
SATURATA 42916.0                   float [adu] Saturation for amp A                 
GAINB    4.65983224604             float [electrons/adu] Gain for amp B             
RDNOISEB 6.77912395154             float [electrons] Read noise for amp B           
SATURATB 40511.0                   float [adu] Saturation for amp B                 
CRPIX1   -4612.0                   float Coordinate Reference axis 1                
CRPIX2   -81.66665                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00285291075725         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.00140157439804          float PV distortion coefficient                  
PV2_9    -0.00187956102894         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000473092714238         float PV distortion coefficient                  
PV2_1    1.00369459725             float PV distortion coefficient                  
PV2_2    0.00049412083747          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.0043153083893          float PV distortion coefficient                  
PV2_5    0.00082576646418          float PV distortion coefficient                  
PV2_6    0.000904546716752         float PV distortion coefficient                  
PV2_7    -0.00692564388198         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.000125304917733         float PV distortion coefficient                  
PV2_10   -9.28219049104e-05        float PV distortion coefficient                  
PV1_4    -0.000665441885753        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000425307595704        float PV distortion coefficient                  
PV1_1    1.00583236476             float PV distortion coefficient                  
PV1_0    -0.000771911998619        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00291576094532         float PV distortion coefficient                  
PV1_8    -0.000484454858667        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.000768536858114         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.00017082645144          float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM UofiamfgWmfgamfg          str    ASCII 1's complement checksum             
DATASUM  3043083557                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU53
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [20481:22528,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [20481:21504,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [21505:22528,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-309_135960-17-3       str   Detector Identifier                        
CCDNUM   52                       int   CCD number                                 
DETPOS   N21                      str   detector position ID                       
EXTNAME  N21                      str   extension name                             
GAINA    4.43066016837            float [electrons/adu] Gain for amp A             
RDNOISEA 6.53522374834            float [electrons] Read noise for amp A           
SATURATA 44068.0                  float [adu] Saturation for amp A                 
GAINB    4.53514739229            float [electrons/adu] Gain for amp B             
RDNOISEB 6.71700680272            float [electrons] Read noise for amp B           
SATURATB 44230.0                  float [adu] Saturation for amp B                 
CRPIX1   -6866.4                  float Coordinate Reference axis 1                
CRPIX2   6307.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 7 5.210000           str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000 str   Monsoon module                             
SLOT02   DESCB 10 4.010000        str   Monsoon module                             
SLOT03   CCD12 3 4.080000         str   Monsoon module                             
SLOT04   CCD12 23 4.080000        str   Monsoon module                             
SLOT05   CCD12 13 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.000803821380339       float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00588638753815         float PV distortion coefficient                  
PV2_9    0.00125271961535         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.00202274520066         float PV distortion coefficient                  
PV2_1    1.00850389075            float PV distortion coefficient                  
PV2_2    0.00309758515461         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00432084148164         float PV distortion coefficient                  
PV2_5    0.00845709423591         float PV distortion coefficient                  
PV2_6    0.00313926147129         float PV distortion coefficient                  
PV2_7    -0.00128863333454        float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.00372097965751         float PV distortion coefficient                  
PV2_10   0.000830631817439        float PV distortion coefficient                  
PV1_4    0.00395100133554         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00218067311554         float PV distortion coefficient                  
PV1_1    1.00761673466            float PV distortion coefficient                  
PV1_0    0.00108944718029         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    -0.000633996256324       float PV distortion coefficient                  
PV1_8    0.00298432297939         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.00417828690025         float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.00201890989466         float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM CIBWD9AVCGAVC9AV         str    ASCII 1's complement checksum             
DATASUM  58417114                 str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU54
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [20481:22528,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [20481:21504,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [21505:22528,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-305_135959-5-3         str   Detector Identifier                        
CCDNUM   53                        int   CCD number                                 
DETPOS   N22                       str   detector position ID                       
EXTNAME  N22                       str   extension name                             
GAINA    4.49438202247             float [electrons/adu] Gain for amp A             
RDNOISEA 6.98292134831             float [electrons] Read noise for amp A           
SATURATA 44487.0                   float [adu] Saturation for amp A                 
GAINB    4.61254612546             float [electrons/adu] Gain for amp B             
RDNOISEB 6.89529520295             float [electrons] Read noise for amp B           
SATURATB 43649.0                   float [adu] Saturation for amp B                 
CRPIX1   -6866.4                   float Coordinate Reference axis 1                
CRPIX2   2048.0                    float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.0028436864699          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.000741981517004         float PV distortion coefficient                  
PV2_9    -0.00146273168782         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000254413069646         float PV distortion coefficient                  
PV2_1    1.00021380164             float PV distortion coefficient                  
PV2_2    0.000147769175838         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.0085166454902          float PV distortion coefficient                  
PV2_5    0.000893581549524         float PV distortion coefficient                  
PV2_6    0.00129074288088          float PV distortion coefficient                  
PV2_7    -0.0079951635287          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.0012163443933          float PV distortion coefficient                  
PV2_10   0.000307054161422         float PV distortion coefficient                  
PV1_4    0.000169988681716         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.000628824868534        float PV distortion coefficient                  
PV1_1    1.00577101234             float PV distortion coefficient                  
PV1_0    -6.71596593686e-06        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.0028864503507          float PV distortion coefficient                  
PV1_8    0.000434756581666         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.000757138318095         float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.000693169409336        float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM WfbIadZIXdaIadYI          str    ASCII 1's complement checksum             
DATASUM  33386797                  str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU55
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [20481:22528,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [20481:21504,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [21505:22528,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-307_135959-10-2        str   Detector Identifier                        
CCDNUM   54                        int   CCD number                                 
DETPOS   N23                       str   detector position ID                       
EXTNAME  N23                       str   extension name                             
GAINA    4.24628450106             float [electrons/adu] Gain for amp A             
RDNOISEA 6.44416135881             float [electrons] Read noise for amp A           
SATURATA 51775.0                   float [adu] Saturation for amp A                 
GAINB    4.64252553389             float [electrons/adu] Gain for amp B             
RDNOISEB 6.90064995357             float [electrons] Read noise for amp B           
SATURATB 44605.0                   float [adu] Saturation for amp B                 
CRPIX1   -6866.4                   float Coordinate Reference axis 1                
CRPIX2   -2211.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00345869147477         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00271032269762         float PV distortion coefficient                  
PV2_9    -0.00087946752855         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000230825484837         float PV distortion coefficient                  
PV2_1    1.0004937065              float PV distortion coefficient                  
PV2_2    -0.00165907854547         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00834561310814         float PV distortion coefficient                  
PV2_5    -0.00358358598392         float PV distortion coefficient                  
PV2_6    0.00229858362814          float PV distortion coefficient                  
PV2_7    -0.00803493797491         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00518544222071         float PV distortion coefficient                  
PV2_10   -0.00115784870536         float PV distortion coefficient                  
PV1_4    -0.00133441621334         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00278708126308         float PV distortion coefficient                  
PV1_1    1.00647648004             float PV distortion coefficient                  
PV1_0    -0.00115080848529         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.00186488066255         float PV distortion coefficient                  
PV1_8    -0.00284614377896         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00285023105554          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00302052353831         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM CDaQFBXNCBaNCBWN          str    ASCII 1's complement checksum             
DATASUM  2462934410                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU56
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [20481:22528,20481:24576] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [20481:21504,20481:24576] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [21505:22528,20481:24576] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-147_112094-18-4        str   Detector Identifier                        
CCDNUM   55                        int   CCD number                                 
DETPOS   N24                       str   detector position ID                       
EXTNAME  N24                       str   extension name                             
GAINA    4.30107526882             float [electrons/adu] Gain for amp A             
RDNOISEA 6.68989247312             float [electrons] Read noise for amp A           
SATURATA 48147.0                   float [adu] Saturation for amp A                 
GAINB    4.31592576608             float [electrons/adu] Gain for amp B             
RDNOISEB 6.68018990073             float [electrons] Read noise for amp B           
SATURATB 46644.0                   float [adu] Saturation for amp B                 
CRPIX1   -6866.4                   float Coordinate Reference axis 1                
CRPIX2   -6470.667                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.0029947513342           float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00914740872827         float PV distortion coefficient                  
PV2_9    0.00481002746081          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00252265889634          float PV distortion coefficient                  
PV2_1    1.00631001303             float PV distortion coefficient                  
PV2_2    -0.00822352407633         float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00380380729442         float PV distortion coefficient                  
PV2_5    -0.0165015516754          float PV distortion coefficient                  
PV2_6    0.00845249043249          float PV distortion coefficient                  
PV2_7    -0.0072664353631          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00761702326803         float PV distortion coefficient                  
PV2_10   -0.003022694484           float PV distortion coefficient                  
PV1_4    -0.0137478240362          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00764915185975         float PV distortion coefficient                  
PV1_1    1.0162507815              float PV distortion coefficient                  
PV1_0    -0.00445217375402         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00457854955569          float PV distortion coefficient                  
PV1_8    -0.00920484490884         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0163853606187           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00275845713959         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 7JqmAInl8InlAInl          str    ASCII 1's complement checksum             
DATASUM  1681054347                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU57
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [22529:24576,10240:14335] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [22529:23552,10240:14335] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [23553:24576,10240:14335] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-119_123194-11-3        str   Detector Identifier                        
CCDNUM   57                        int   CCD number                                 
DETPOS   N26                       str   detector position ID                       
EXTNAME  N26                       str   extension name                             
GAINA    4.45632798574             float [electrons/adu] Gain for amp A             
RDNOISEA 6.6889483066              float [electrons] Read noise for amp A           
SATURATA 37641.0                   float [adu] Saturation for amp A                 
GAINB    4.29737859905             float [electrons/adu] Gain for amp B             
RDNOISEB 6.53029651912             float [electrons] Read noise for amp B           
SATURATB 35736.0                   float [adu] Saturation for amp B                 
CRPIX1   -9120.8                   float Coordinate Reference axis 1                
CRPIX2   4177.667                  float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00138786929934         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    0.00329563303971          float PV distortion coefficient                  
PV2_9    0.00108793467596          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.000340404592356         float PV distortion coefficient                  
PV2_1    1.00160200956             float PV distortion coefficient                  
PV2_2    0.00194925827321          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    -0.00280234025092         float PV distortion coefficient                  
PV2_5    0.0048486617586           float PV distortion coefficient                  
PV2_6    0.00342150049886          float PV distortion coefficient                  
PV2_7    -0.00324646545889         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.005054258391           float PV distortion coefficient                  
PV2_10   0.000755005431907         float PV distortion coefficient                  
PV1_4    0.00293129285915          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00387898576845         float PV distortion coefficient                  
PV1_1    1.00736585441             float PV distortion coefficient                  
PV1_0    -0.000848827426732        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    -0.000179231945428        float PV distortion coefficient                  
PV1_8    0.00303360925869          float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.00473841624834          float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00223056553084         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM CbA6CZ55CaA5CY55          str    ASCII 1's complement checksum             
DATASUM  3638019756                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU58
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [22529:24576,14336:18431] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [22529:23552,14336:18431] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [23553:24576,14336:18431] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-04_107419-13-3         str   Detector Identifier                        
CCDNUM   58                        int   CCD number                                 
DETPOS   N27                       str   detector position ID                       
EXTNAME  N27                       str   extension name                             
GAINA    4.75963826749             float [electrons/adu] Gain for amp A             
RDNOISEA 6.91623036649             float [electrons] Read noise for amp A           
SATURATA 44693.0                   float [adu] Saturation for amp A                 
GAINB    4.500450045               float [electrons/adu] Gain for amp B             
RDNOISEB 6.91269126913             float [electrons] Read noise for amp B           
SATURATB 44091.0                   float [adu] Saturation for amp B                 
CRPIX1   -9120.8                   float Coordinate Reference axis 1                
CRPIX2   -81.66665                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.0027103013886          float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00195685274764         float PV distortion coefficient                  
PV2_9    0.000738867350118         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00158702119504          float PV distortion coefficient                  
PV2_1    1.00754284966             float PV distortion coefficient                  
PV2_2    -0.000621901123605        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0055953105246           float PV distortion coefficient                  
PV2_5    -0.00305575693816         float PV distortion coefficient                  
PV2_6    0.00316294705984          float PV distortion coefficient                  
PV2_7    0.000721276262683         float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00176568933687         float PV distortion coefficient                  
PV2_10   -0.000934525864652        float PV distortion coefficient                  
PV1_4    -0.00217766011277         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00195986318429         float PV distortion coefficient                  
PV1_1    1.00744992152             float PV distortion coefficient                  
PV1_0    -0.00118619898761         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.000260485554784         float PV distortion coefficient                  
PV1_8    -0.00285807767698         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0053090241286           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00080191802643         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 9qfBHnZB9ndBEnZB          str    ASCII 1's complement checksum             
DATASUM  2768811934                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU59
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [22529:24576,18432:22527] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [22529:23552,18432:22527] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [23553:24576,18432:22527] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-178_107419-14-3        str   Detector Identifier                        
CCDNUM   59                        int   CCD number                                 
DETPOS   N28                       str   detector position ID                       
EXTNAME  N28                       str   extension name                             
GAINA    4.49236298293             float [electrons/adu] Gain for amp A             
RDNOISEA 6.70350404313             float [electrons] Read noise for amp A           
SATURATA 43039.0                   float [adu] Saturation for amp A                 
GAINB    4.33275563258             float [electrons/adu] Gain for amp B             
RDNOISEB 6.48916811092             float [electrons] Read noise for amp B           
SATURATB 43782.0                   float [adu] Saturation for amp B                 
CRPIX1   -9120.8                   float Coordinate Reference axis 1                
CRPIX2   -4341.0                   float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.00223789157             float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.0146141575147          float PV distortion coefficient                  
PV2_9    0.00721191784441          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00727619121444          float PV distortion coefficient                  
PV2_1    1.02464996368             float PV distortion coefficient                  
PV2_2    -0.0125584239415          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0227162805209           float PV distortion coefficient                  
PV2_5    -0.026617121551           float PV distortion coefficient                  
PV2_6    0.0107281926997           float PV distortion coefficient                  
PV2_7    0.00625715346526          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.012254696737           float PV distortion coefficient                  
PV2_10   -0.00339651963271         float PV distortion coefficient                  
PV1_4    -0.0128156216482          float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.0123605186183          float PV distortion coefficient                  
PV1_1    1.01742482762             float PV distortion coefficient                  
PV1_0    -0.00558440370987         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00767551192383          float PV distortion coefficient                  
PV1_8    -0.00982702080536         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.021471517253            float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.00431097666417         float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 91A1C18091A0C170          str    ASCII 1's complement checksum             
DATASUM  3472048458                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU60
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================== ===== ===========================================
KEY      Value                    Type  Comment                                    
======== ======================== ===== ===========================================
ZIMAGE   T                        bool  extension contains compressed image        
ZTILE1   2160                     int   size of tiles to be compressed             
ZTILE2   1                        int   size of tiles to be compressed             
ZCMPTYPE RICE_1                   str   compression algorithm                      
ZNAME1   BLOCKSIZE                str   compression block size                     
ZVAL1    32                       int   pixels per block                           
ZNAME2   BYTEPIX                  str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                        int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                    str   IMAGE extension                            
ZBITPIX  16                       int   number of bits per data pixel              
ZNAXIS   2                        int   number of data axes                        
ZNAXIS1  2160                     int   length of data axis 1                      
ZNAXIS2  4146                     int   length of data axis 2                      
ZPCOUNT  0                        int   required keyword; must = 0                 
ZGCOUNT  1                        int   required keyword; must = 1                 
BZERO    32768                    int   offset data range to that of unsigned short
BSCALE   1                        int   default scaling factor                     
BUNIT    adu                      str   Brightness units for pixel array           
WCSAXES  2                        int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]        str   Detector size                              
TRIMSEC  [57:2104,1:4096]         str   Good section                               
DATASEC  [57:2104,1:4096]         str   Data section to display                    
DETSEC   [24577:26624,8193:12288] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]          str   CCD section to display                     
TRIMSECA [57:1080,1:4096]         str   Good section from amp A                    
DETSECA  [24577:25600,8193:12288] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]          str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]          str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]         str   Data section from amp A                    
BIASSECA [7:56,1:4096]            str   Overscan from amp A                        
PRESECA  [1:6,1:4096]             str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]      str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]       str   Good section from amp B                    
DETSECB  [25601:26624,8193:12288] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]       str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]       str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]       str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]       str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]       str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]    str   Postscan from amp B                        
DETECTOR S3-97_123195-13-4        str   Detector Identifier                        
CCDNUM   60                       int   CCD number                                 
DETPOS   N29                      str   detector position ID                       
EXTNAME  N29                      str   extension name                             
GAINA    4.26985482494            float [electrons/adu] Gain for amp A             
RDNOISEA 6.3706233988             float [electrons] Read noise for amp A           
SATURATA 44700.0                  float [adu] Saturation for amp A                 
GAINB    4.34971726838            float [electrons/adu] Gain for amp B             
RDNOISEB 6.4441061331             float [electrons] Read noise for amp B           
SATURATB 44380.0                  float [adu] Saturation for amp B                 
CRPIX1   -11375.2                 float Coordinate Reference axis 1                
CRPIX2   6307.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5               str   DECam focal plane name                     
INHERIT  T                        bool  Inherits PHDU header                       
CCDBIN1  1                        int   Pixel binning, axis 1                      
CCDBIN2  1                        int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware      str   DHE Hardware                               
DHEFIRM  demo30                   str   DHE Firmware                               
SLOT00   MCB 7 5.210000           str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000 str   Monsoon module                             
SLOT02   DESCB 10 4.010000        str   Monsoon module                             
SLOT03   CCD12 3 4.080000         str   Monsoon module                             
SLOT04   CCD12 23 4.080000        str   Monsoon module                             
SLOT05   CCD12 13 4.080000        str   Monsoon module                             
RADESYS  FK5                      str   World coordinate reference frame           
EQUINOX  2000.0                   float [yr] Equinox of WCS                        
PV1_7    -0.000995518124344       float PV distortion coefficient                  
CUNIT1   deg                      str                                              
PV2_8    0.00737307779342         float PV distortion coefficient                  
PV2_9    0.00613823195375         float PV distortion coefficient                  
CD1_1    -1.8249413473e-07        float World coordinate transformation matrix     
LTM2_2   1.0                      float Detector to image transformation           
LTM2_1   0.0                      float Detector to image transformation           
PV2_0    0.00144178332611         float PV distortion coefficient                  
PV2_1    1.00810467066            float PV distortion coefficient                  
PV2_2    0.00624405333508         float PV distortion coefficient                  
PV2_3    0.0                      float PV distortion coefficient                  
PV2_4    0.00882675926167         float PV distortion coefficient                  
PV2_5    0.0136587225033          float PV distortion coefficient                  
PV2_6    0.00886566541131         float PV distortion coefficient                  
PV2_7    0.00304504305393         float PV distortion coefficient                  
LTM1_1   1.0                      float Detector to image transformation           
PV1_6    0.00154043263542         float PV distortion coefficient                  
PV2_10   0.00268215595355         float PV distortion coefficient                  
PV1_4    0.00777327236046         float PV distortion coefficient                  
PV1_3    0.0                      float PV distortion coefficient                  
PV1_2    0.00173503210447         float PV distortion coefficient                  
PV1_1    1.01215836257            float PV distortion coefficient                  
PV1_0    0.00150980850058         float PV distortion coefficient                  
LTM1_2   0.0                      float Detector to image transformation           
PV1_9    0.00388978466426         float PV distortion coefficient                  
PV1_8    0.00833590316552         float PV distortion coefficient                  
CD1_2    7.28535892432e-05        float World coordinate transformation matrix     
PV1_5    0.0136942616267          float PV distortion coefficient                  
CUNIT2   deg                      str                                              
CD2_1    -7.28499004539e-05       float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07       float World coordinate transformation matrix     
LTV2     0.0                      float Detector to image transformation           
LTV1     56.0                     float Detector to image transformation           
PV1_10   0.0007225122381          float PV distortion coefficient                  
CTYPE2   DEC--TPV                 str   Coordinate type                            
CTYPE1   RA---TPV                 str   Coordinate type                            
CRVAL1   237.447283               float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                 float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                        bool  Data from amp A is valid                   
VALIDB   T                        bool  Data from amp B is valid                   
NDONUTS  0                        int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT               str    FITS checksum version                     
CHECKSUM WJV5aGS2YGS2aGS2         str    ASCII 1's complement checksum             
DATASUM  2610166057               str    checksum of data records                  
======== ======================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU61
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [24577:26624,12289:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [24577:25600,12289:16384] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [25601:26624,12289:16384] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-112_107419-10-1        str   Detector Identifier                        
CCDNUM   61                        int   CCD number                                 
DETPOS   N30                       str   detector position ID                       
EXTNAME  N30                       str   extension name                             
GAINA    4.086636698               float [electrons/adu] Gain for amp A             
RDNOISEA 6.45852063752             float [electrons] Read noise for amp A           
SATURATA 56282.0                   float [adu] Saturation for amp A                 
GAINB    4.56829602558             float [electrons/adu] Gain for amp B             
RDNOISEB 6.66834170854             float [electrons] Read noise for amp B           
SATURATB 45592.0                   float [adu] Saturation for amp B                 
CRPIX1   -11375.2                  float Coordinate Reference axis 1                
CRPIX2   2048.0                    float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    -0.00247806355991         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.000824180925675        float PV distortion coefficient                  
PV2_9    0.00449485379688          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00649974314018          float PV distortion coefficient                  
PV2_1    1.02536524699             float PV distortion coefficient                  
PV2_2    -0.000826888176312        float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0292412564947           float PV distortion coefficient                  
PV2_5    -0.00159276475329         float PV distortion coefficient                  
PV2_6    0.00616501770544          float PV distortion coefficient                  
PV2_7    0.0110432850366           float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00200307060681         float PV distortion coefficient                  
PV2_10   8.18681945251e-05         float PV distortion coefficient                  
PV1_4    -0.000532958257783        float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00177295811554         float PV distortion coefficient                  
PV1_1    1.0098589883              float PV distortion coefficient                  
PV1_0    -0.000492867263892        float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00434992520561          float PV distortion coefficient                  
PV1_8    -0.000336650718999        float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0115537217064           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.000720594287328        float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM n0NNn0MNn0MNn0MN          str    ASCII 1's complement checksum             
DATASUM  1751744247                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU62
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  4146                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:4096]          str   Good section                               
DATASEC  [57:2104,1:4096]          str   Data section to display                    
DETSEC   [24577:26624,16385:20480] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:4096]           str   CCD section to display                     
TRIMSECA [57:1080,1:4096]          str   Good section from amp A                    
DETSECA  [24577:25600,16385:20480] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:4096]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:4096]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:4096]          str   Data section from amp A                    
BIASSECA [7:56,1:4096]             str   Overscan from amp A                        
PRESECA  [1:6,1:4096]              str   Prescan from amp A                         
POSTSECA [57:1080,4097:4146]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:4096]        str   Good section from amp B                    
DETSECB  [25601:26624,16385:20480] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:4096]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:4096]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:4096]        str   Data section from amp B                    
BIASSECB [2105:2154,1:4096]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:4096]        str   Prescan from amp B                         
POSTSECB [1081:2104,4097:4146]     str   Postscan from amp B                        
DETECTOR S3-344_135960-13-4        str   Detector Identifier                        
CCDNUM   62                        int   CCD number                                 
DETPOS   N31                       str   detector position ID                       
EXTNAME  N31                       str   extension name                             
GAINA    4.28449014567             float [electrons/adu] Gain for amp A             
RDNOISEA 6.52142245073             float [electrons] Read noise for amp A           
SATURATA 47995.0                   float [adu] Saturation for amp A                 
GAINB    4.34216239687             float [electrons/adu] Gain for amp B             
RDNOISEB 6.43421623969             float [electrons] Read noise for amp B           
SATURATB 46991.0                   float [adu] Saturation for amp B                 
CRPIX1   -11375.2                  float Coordinate Reference axis 1                
CRPIX2   -2211.333                 float Coordinate Reference axis 2                
FPA      DECAM_BKP5                str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 7 5.210000            str   Monsoon module                             
SLOT01   DESCB 0x1098FCC 4.010000  str   Monsoon module                             
SLOT02   DESCB 10 4.010000         str   Monsoon module                             
SLOT03   CCD12 3 4.080000          str   Monsoon module                             
SLOT04   CCD12 23 4.080000         str   Monsoon module                             
SLOT05   CCD12 13 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.000531533395974         float PV distortion coefficient                  
CUNIT1   deg                       str                                              
PV2_8    -0.00682109317684         float PV distortion coefficient                  
PV2_9    0.00548616099158          float PV distortion coefficient                  
CD1_1    -1.8249413473e-07         float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.00366629109325          float PV distortion coefficient                  
PV2_1    1.01531730322             float PV distortion coefficient                  
PV2_2    -0.0065815888678          float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0174180487887           float PV distortion coefficient                  
PV2_5    -0.0126457105151          float PV distortion coefficient                  
PV2_6    0.0085944543006           float PV distortion coefficient                  
PV2_7    0.00644381369922          float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    -0.00174113497645         float PV distortion coefficient                  
PV2_10   -0.00293520644902         float PV distortion coefficient                  
PV1_4    -0.00853299537478         float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    -0.00158631174507         float PV distortion coefficient                  
PV1_1    1.01363481871             float PV distortion coefficient                  
PV1_0    -0.00110211032204         float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.00592643593552          float PV distortion coefficient                  
PV1_8    -0.00741991233396         float PV distortion coefficient                  
CD1_2    7.28535892432e-05         float World coordinate transformation matrix     
PV1_5    0.0166601443013           float PV distortion coefficient                  
CUNIT2   deg                       str                                              
CD2_1    -7.28499004539e-05        float World coordinate transformation matrix     
CD2_2    -1.82181666096e-07        float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   -0.000582276568815        float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 95c1F2Z092b0E2Z0          str    ASCII 1's complement checksum             
DATASUM  2666900865                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU63
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  2098                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:2098]       str   Good section                               
DATASEC  [57:2104,51:2098]       str   Data section to display                    
DETSEC   [4097:6144,22529:24576] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]         str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]     str   Good section from amp A                    
DETSECA  [5121:6144,22529:24576] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]      str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]     str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]       str   Good section from amp B                    
DETSECB  [4097:5120,22529:24576] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]         str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]       str   Data section from amp B                    
BIASSECB [7:56,51:2098]          str   Overscan from amp B                        
PRESECB  [1:6,51:2098]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR A1-05_135959-6-5        str   Detector Identifier                        
CCDNUM   72                      int   CCD number                                 
DETPOS   FS1                     str   detector position ID                       
EXTNAME  FS1                     str   extension name                             
GAINA    4.59347726229           float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096           float [electrons] Read noise for amp A           
SATURATA 43266.0                 float [adu] Saturation for amp A                 
GAINB    4.4014084507            float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127           float [electrons] Read noise for amp B           
SATURATB 44935.0                 float [adu] Saturation for amp B                 
CRPIX1   11168.8                 float Coordinate Reference axis 1                
CRPIX2   -8600.334               float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F            str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 6 5.210000          str   Monsoon module                             
SLOT01   DESCB 2 4.010000        str   Monsoon module                             
SLOT02   CCD12 6 4.080000        str   Monsoon module                             
SLOT03   CCD12 32 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.002                   float PV distortion coefficient                  
PV2_8    0.0                     float PV distortion coefficient                  
PV2_9    0.002                   float PV distortion coefficient                  
CD1_1    0.0                     float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.0                     float PV distortion coefficient                  
PV2_1    1.0                     float PV distortion coefficient                  
PV2_2    0.0                     float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.0                     float PV distortion coefficient                  
PV2_5    0.0                     float PV distortion coefficient                  
PV2_6    0.0                     float PV distortion coefficient                  
PV2_7    0.002                   float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.0                     float PV distortion coefficient                  
PV2_10   0.0                     float PV distortion coefficient                  
PV1_4    0.0                     float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0                     float PV distortion coefficient                  
PV1_1    1.0                     float PV distortion coefficient                  
PV1_0    0.0                     float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.002                   float PV distortion coefficient                  
PV1_8    0.0                     float PV distortion coefficient                  
CD1_2    -7.5e-05                float World coordinate transformation matrix     
PV1_5    0.0                     float PV distortion coefficient                  
CD2_1    7.5e-05                 float World coordinate transformation matrix     
CD2_2    0.0                     float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.0                     float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 9IYJAFW93FWG9FW9        str    ASCII 1's complement checksum             
DATASUM  3270971058              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU64
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  2098                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:2098]       str   Good section                               
DATASEC  [57:2104,51:2098]       str   Data section to display                    
DETSEC   [2049:4096,20481:22528] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]         str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]     str   Good section from amp A                    
DETSECA  [3073:4096,20481:22528] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]      str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]     str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]       str   Good section from amp B                    
DETSECB  [2049:3072,20481:22528] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]         str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]       str   Data section from amp B                    
BIASSECB [7:56,51:2098]          str   Overscan from amp B                        
PRESECB  [1:6,51:2098]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR A1-02_123194-4-5        str   Detector Identifier                        
CCDNUM   71                      int   CCD number                                 
DETPOS   FS2                     str   detector position ID                       
EXTNAME  FS2                     str   extension name                             
GAINA    4.59347726229           float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096           float [electrons] Read noise for amp A           
SATURATA 43266.0                 float [adu] Saturation for amp A                 
GAINB    4.4014084507            float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127           float [electrons] Read noise for amp B           
SATURATB 44935.0                 float [adu] Saturation for amp B                 
CRPIX1   13423.2                 float Coordinate Reference axis 1                
CRPIX2   -6470.667               float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F            str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 6 5.210000          str   Monsoon module                             
SLOT01   DESCB 2 4.010000        str   Monsoon module                             
SLOT02   CCD12 6 4.080000        str   Monsoon module                             
SLOT03   CCD12 32 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.002                   float PV distortion coefficient                  
PV2_8    0.0                     float PV distortion coefficient                  
PV2_9    0.002                   float PV distortion coefficient                  
CD1_1    0.0                     float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.0                     float PV distortion coefficient                  
PV2_1    1.0                     float PV distortion coefficient                  
PV2_2    0.0                     float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.0                     float PV distortion coefficient                  
PV2_5    0.0                     float PV distortion coefficient                  
PV2_6    0.0                     float PV distortion coefficient                  
PV2_7    0.002                   float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.0                     float PV distortion coefficient                  
PV2_10   0.0                     float PV distortion coefficient                  
PV1_4    0.0                     float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0                     float PV distortion coefficient                  
PV1_1    1.0                     float PV distortion coefficient                  
PV1_0    0.0                     float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.002                   float PV distortion coefficient                  
PV1_8    0.0                     float PV distortion coefficient                  
CD1_2    -7.5e-05                float World coordinate transformation matrix     
PV1_5    0.0                     float PV distortion coefficient                  
CD2_1    7.5e-05                 float World coordinate transformation matrix     
CD2_2    0.0                     float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.0                     float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM 325A4223322A3223        str    ASCII 1's complement checksum             
DATASUM  730223322               str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU65
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ======================= ===== ===========================================
KEY      Value                   Type  Comment                                    
======== ======================= ===== ===========================================
ZIMAGE   T                       bool  extension contains compressed image        
ZTILE1   2160                    int   size of tiles to be compressed             
ZTILE2   1                       int   size of tiles to be compressed             
ZCMPTYPE RICE_1                  str   compression algorithm                      
ZNAME1   BLOCKSIZE               str   compression block size                     
ZVAL1    32                      int   pixels per block                           
ZNAME2   BYTEPIX                 str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                       int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                   str   IMAGE extension                            
ZBITPIX  16                      int   number of bits per data pixel              
ZNAXIS   2                       int   number of data axes                        
ZNAXIS1  2160                    int   length of data axis 1                      
ZNAXIS2  2098                    int   length of data axis 2                      
ZPCOUNT  0                       int   required keyword; must = 0                 
ZGCOUNT  1                       int   required keyword; must = 1                 
BZERO    32768                   int   offset data range to that of unsigned short
BSCALE   1                       int   default scaling factor                     
BUNIT    adu                     str   Brightness units for pixel array           
WCSAXES  2                       int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]       str   Detector size                              
TRIMSEC  [57:2104,51:2098]       str   Good section                               
DATASEC  [57:2104,51:2098]       str   Data section to display                    
DETSEC   [1:2048,14337:16384]    str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]         str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]     str   Good section from amp A                    
DETSECA  [1025:2048,14337:16384] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]      str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]      str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]     str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]     str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]     str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]        str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]       str   Good section from amp B                    
DETSECB  [1:1024,14337:16384]    str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]         str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]         str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]       str   Data section from amp B                    
BIASSECB [7:56,51:2098]          str   Overscan from amp B                        
PRESECB  [1:6,51:2098]           str   Prescan from amp B                         
POSTSECB [57:1080,1:50]          str   Postscan from amp B                        
DETECTOR A1-04_123195-12-5       str   Detector Identifier                        
CCDNUM   64                      int   CCD number                                 
DETPOS   FS3                     str   detector position ID                       
EXTNAME  FS3                     str   extension name                             
GAINA    4.59347726229           float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096           float [electrons] Read noise for amp A           
SATURATA 43266.0                 float [adu] Saturation for amp A                 
GAINB    4.4014084507            float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127           float [electrons] Read noise for amp B           
SATURATB 44935.0                 float [adu] Saturation for amp B                 
CRPIX1   15677.6                 float Coordinate Reference axis 1                
CRPIX2   -81.6666                float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F            str   DECam focal plane name                     
INHERIT  T                       bool  Inherits PHDU header                       
CCDBIN1  1                       int   Pixel binning, axis 1                      
CCDBIN2  1                       int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware     str   DHE Hardware                               
DHEFIRM  demo30                  str   DHE Firmware                               
SLOT00   MCB 6 5.210000          str   Monsoon module                             
SLOT01   DESCB 2 4.010000        str   Monsoon module                             
SLOT02   CCD12 6 4.080000        str   Monsoon module                             
SLOT03   CCD12 32 4.080000       str   Monsoon module                             
RADESYS  FK5                     str   World coordinate reference frame           
EQUINOX  2000.0                  float [yr] Equinox of WCS                        
PV1_7    0.002                   float PV distortion coefficient                  
PV2_8    0.0                     float PV distortion coefficient                  
PV2_9    0.002                   float PV distortion coefficient                  
CD1_1    0.0                     float World coordinate transformation matrix     
LTM2_2   1.0                     float Detector to image transformation           
LTM2_1   0.0                     float Detector to image transformation           
PV2_0    0.0                     float PV distortion coefficient                  
PV2_1    1.0                     float PV distortion coefficient                  
PV2_2    0.0                     float PV distortion coefficient                  
PV2_3    0.0                     float PV distortion coefficient                  
PV2_4    0.0                     float PV distortion coefficient                  
PV2_5    0.0                     float PV distortion coefficient                  
PV2_6    0.0                     float PV distortion coefficient                  
PV2_7    0.002                   float PV distortion coefficient                  
LTM1_1   1.0                     float Detector to image transformation           
PV1_6    0.0                     float PV distortion coefficient                  
PV2_10   0.0                     float PV distortion coefficient                  
PV1_4    0.0                     float PV distortion coefficient                  
PV1_3    0.0                     float PV distortion coefficient                  
PV1_2    0.0                     float PV distortion coefficient                  
PV1_1    1.0                     float PV distortion coefficient                  
PV1_0    0.0                     float PV distortion coefficient                  
LTM1_2   0.0                     float Detector to image transformation           
PV1_9    0.002                   float PV distortion coefficient                  
PV1_8    0.0                     float PV distortion coefficient                  
CD1_2    -7.5e-05                float World coordinate transformation matrix     
PV1_5    0.0                     float PV distortion coefficient                  
CD2_1    7.5e-05                 float World coordinate transformation matrix     
CD2_2    0.0                     float World coordinate transformation matrix     
LTV2     0.0                     float Detector to image transformation           
LTV1     56.0                    float Detector to image transformation           
PV1_10   0.0                     float PV distortion coefficient                  
CTYPE2   DEC--TPV                str   Coordinate type                            
CTYPE1   RA---TPV                str   Coordinate type                            
CRVAL1   237.447283              float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                       bool  Data from amp A is valid                   
VALIDB   T                       bool  Data from amp B is valid                   
NDONUTS  0                       int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT              str    FITS checksum version                     
CHECKSUM lj35lg02lg02lg02        str    ASCII 1's complement checksum             
DATASUM  1074827943              str    checksum of data records                  
======== ======================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU66
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ===================================================== ===== ===========================================
KEY      Value                                                 Type  Comment                                    
======== ===================================================== ===== ===========================================
ZIMAGE   T                                                     bool  extension contains compressed image        
ZTILE1   2160                                                  int   size of tiles to be compressed             
ZTILE2   1                                                     int   size of tiles to be compressed             
ZCMPTYPE RICE_1                                                str   compression algorithm                      
ZNAME1   BLOCKSIZE                                             str   compression block size                     
ZVAL1    32                                                    int   pixels per block                           
ZNAME2   BYTEPIX                                               str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                                                     int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                                                 str   IMAGE extension                            
ZBITPIX  16                                                    int   number of bits per data pixel              
ZNAXIS   2                                                     int   number of data axes                        
ZNAXIS1  2160                                                  int   length of data axis 1                      
ZNAXIS2  2098                                                  int   length of data axis 2                      
ZPCOUNT  0                                                     int   required keyword; must = 0                 
ZGCOUNT  1                                                     int   required keyword; must = 1                 
BZERO    32768                                                 int   offset data range to that of unsigned short
BSCALE   1                                                     int   default scaling factor                     
BUNIT    adu                                                   str   Brightness units for pixel array           
WCSAXES  2                                                     int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]                                     str   Detector size                              
TRIMSEC  [57:2104,1:2048]                                      str   Good section                               
DATASEC  [57:2104,1:2048]                                      str   Data section to display                    
DETSEC   [1:2048,12289:14336]                                  str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]                                       str   CCD section to display                     
TRIMSECA [57:1080,1:2048]                                      str   Good section from amp A                    
DETSECA  [1:1024,12289:14336]                                  str   Detector display tile for amp A            
CCDSECA  [1:1024,1:2048]                                       str   CCD section from amp A                     
AMPSECA  [1:1024,1:2048]                                       str   CCD section in read order for amp A        
DATASECA [57:1080,1:2048]                                      str   Data section from amp A                    
BIASSECA [7:56,1:2048]                                         str   Overscan from amp A                        
PRESECA  [1:6,1:2048]                                          str   Prescan from amp A                         
POSTSECA [57:1080,2049:2098]                                   str   Postscan from amp A                        
TRIMSECB [1081:2104,1:2048]                                    str   Good section from amp B                    
DETSECB  [1025:2048,12289:14336]                               str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:2048]                                    str   CCD section from amp B                     
AMPSECB  [2048:1025,1:2048]                                    str   CCD section in read order for amp B        
DATASECB [1081:2104,1:2048]                                    str   Data section from amp B                    
BIASSECB [2105:2154,1:2048]                                    str   Overscan from amp B                        
PRESECB  [2155:2160,1:2048]                                    str   Prescan from amp B                         
POSTSECB [1081:2104,2049:2098]                                 str   Postscan from amp B                        
DETECTOR A1-70_123195-11-5                                     str   Detector Identifier                        
CCDNUM   63                                                    int   CCD number                                 
DETPOS   FS4                                                   str   detector position ID                       
EXTNAME  FS4                                                   str   extension name                             
GAINA    4.59347726229                                         float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096                                         float [electrons] Read noise for amp A           
SATURATA 43266.0                                               float [adu] Saturation for amp A                 
GAINB    4.4014084507                                          float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127                                         float [electrons] Read noise for amp B           
SATURATB 44935.0                                               float [adu] Saturation for amp B                 
CRPIX1   15677.6                                               float Coordinate Reference axis 1                
CRPIX2   2129.667                                              float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F                                          str   DECam focal plane name                     
INHERIT  T                                                     bool  Inherits PHDU header                       
CCDBIN1  1                                                     int   Pixel binning, axis 1                      
CCDBIN2  1                                                     int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware                                   str   DHE Hardware                               
DHEFIRM  demo30                                                str   DHE Firmware                               
SLOT00   MCB 6 5.210000                                        str   Monsoon module                             
SLOT01   DESCB 2 4.010000                                      str   Monsoon module                             
SLOT02   CCD12 6 4.080000                                      str   Monsoon module                             
SLOT03   CCD12 32 4.080000                                     str   Monsoon module                             
RADESYS  FK5                                                   str   World coordinate reference frame           
EQUINOX  2000.0                                                float [yr] Equinox of WCS                        
PV1_7    0.002                                                 float PV distortion coefficient                  
PV2_8    0.0                                                   float PV distortion coefficient                  
PV2_9    0.002                                                 float PV distortion coefficient                  
CD1_1    0.0                                                   float World coordinate transformation matrix     
LTM2_2   1.0                                                   float Detector to image transformation           
LTM2_1   0.0                                                   float Detector to image transformation           
PV2_0    0.0                                                   float PV distortion coefficient                  
PV2_1    1.0                                                   float PV distortion coefficient                  
PV2_2    0.0                                                   float PV distortion coefficient                  
PV2_3    0.0                                                   float PV distortion coefficient                  
PV2_4    0.0                                                   float PV distortion coefficient                  
PV2_5    0.0                                                   float PV distortion coefficient                  
PV2_6    0.0                                                   float PV distortion coefficient                  
PV2_7    0.002                                                 float PV distortion coefficient                  
LTM1_1   1.0                                                   float Detector to image transformation           
PV1_6    0.0                                                   float PV distortion coefficient                  
PV2_10   0.0                                                   float PV distortion coefficient                  
PV1_4    0.0                                                   float PV distortion coefficient                  
PV1_3    0.0                                                   float PV distortion coefficient                  
PV1_2    0.0                                                   float PV distortion coefficient                  
PV1_1    1.0                                                   float PV distortion coefficient                  
PV1_0    0.0                                                   float PV distortion coefficient                  
LTM1_2   0.0                                                   float Detector to image transformation           
PV1_9    0.002                                                 float PV distortion coefficient                  
PV1_8    0.0                                                   float PV distortion coefficient                  
CD1_2    -7.5e-05                                              float World coordinate transformation matrix     
PV1_5    0.0                                                   float PV distortion coefficient                  
CD2_1    7.5e-05                                               float World coordinate transformation matrix     
CD2_2    0.0                                                   float World coordinate transformation matrix     
LTV2     0.0                                                   float Detector to image transformation           
LTV1     56.0                                                  float Detector to image transformation           
PV1_10   0.0                                                   float PV distortion coefficient                  
CTYPE2   DEC--TPV                                              str   Coordinate type                            
CTYPE1   RA---TPV                                              str   Coordinate type                            
CRVAL1   237.447283                                            float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                                              float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                                                     bool  Data from amp A is valid                   
VALIDB   T                                                     bool  Data from amp B is valid                   
DONUT6Z  [-0.20,0.95,-9.84,-0.43,0.17,0.03,-0.10,-0.05,-0.77,] str   Zernike term                               
DONUT1E  [2.6e+04,1.7e+06,886,501,4.57e+03,311883.75,]         str   CHI2 NELE X Y BCKG M                       
DONUT5Z  [-0.92,0.63,-8.75,-0.21,0.15,0.09,0.38,-0.08,-0.45,]  str   Zernike terms                              
DONUT2E  [5.1e+03,4.8e+05,1730,1560,4.23e+03,439733.25,]       str   CHI2 NELE X Y BCKG                         
DONUT7Z  [-0.20,-0.22,-8.82,-0.38,0.12,0.16,0.46,-0.03,-0.53,] str   Zernike term                               
DONUT3E  [8.6e+03,8.6e+05,860,1025,4.60e+03,358084.38,]        str   CHI2 NELE X Y BCKG                         
DONUT3Z  [0.13,-0.41,-8.88,-0.45,0.08,0.17,0.63,-0.03,-0.45,]  str   Zernike terms                              
DONUT7E  [8.5e+03,7.5e+05,1210,1441,4.22e+03,662949.25,]       str   CHI2 NELE X Y BCKG                         
NDONUTS  7                                                     int   Number of donuts analyzed                  
DONUT2Z  [0.96,1.58,-8.73,-0.25,0.11,0.18,0.46,-0.05,-0.47,]   str   Zernike terms                              
DONUT5E  [3.9e+03,3.8e+05,1957,1747,4.24e+03,355926.25,]       str   CHI2 NELE X Y BCKG                         
DONUT1Z  [-0.25,1.97,-8.83,-0.44,-0.03,0.19,0.63,-0.06,-0.42,] str   Zernike term                               
DONUT6E  [4.0e+04,1.7e+06,1198,1344,4.30e+03,2000890.75,]      str   CHI2 NELE X Y BCK                          
DONUT4E  [5.3e+03,6.0e+05,1150,762,4.23e+03,547015.00,]        str   CHI2 NELE X Y BCKG                         
DONUT4Z  [1.23,1.78,-8.77,-0.42,0.11,0.17,0.51,-0.07,-0.45,]   str   Zernike terms                              
CHECKVER COMPLEMENT                                            str    FITS checksum version                     
CHECKSUM Y4aZZ4UZY4aZY4UZ                                      str    ASCII 1's complement checksum             
DATASUM  3467168534                                            str    checksum of data records                  
======== ===================================================== ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU67
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  2098                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:2098]         str   Good section                               
DATASEC  [57:2104,51:2098]         str   Data section to display                    
DETSEC   [22529:24576,22528:24575] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]           str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]       str   Good section from amp A                    
DETSECA  [23553:24576,22528:24575] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]        str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]       str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]         str   Good section from amp B                    
DETSECB  [22529:23552,22528:24575] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]           str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]         str   Data section from amp B                    
BIASSECB [7:56,51:2098]            str   Overscan from amp B                        
PRESECB  [1:6,51:2098]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR A1-12_123195-6-5          str   Detector Identifier                        
CCDNUM   73                        int   CCD number                                 
DETPOS   FN1                       str   detector position ID                       
EXTNAME  FN1                       str   extension name                             
GAINA    4.59347726229             float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096             float [electrons] Read noise for amp A           
SATURATA 43266.0                   float [adu] Saturation for amp A                 
GAINB    4.4014084507              float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127             float [electrons] Read noise for amp B           
SATURATB 44935.0                   float [adu] Saturation for amp B                 
CRPIX1   -9120.8                   float Coordinate Reference axis 1                
CRPIX2   -8600.334                 float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F              str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 6 5.210000            str   Monsoon module                             
SLOT01   DESCB 2 4.010000          str   Monsoon module                             
SLOT02   CCD12 6 4.080000          str   Monsoon module                             
SLOT03   CCD12 32 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.002                     float PV distortion coefficient                  
PV2_8    0.0                       float PV distortion coefficient                  
PV2_9    0.002                     float PV distortion coefficient                  
CD1_1    0.0                       float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.0                       float PV distortion coefficient                  
PV2_1    1.0                       float PV distortion coefficient                  
PV2_2    0.0                       float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0                       float PV distortion coefficient                  
PV2_5    0.0                       float PV distortion coefficient                  
PV2_6    0.0                       float PV distortion coefficient                  
PV2_7    0.002                     float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.0                       float PV distortion coefficient                  
PV2_10   0.0                       float PV distortion coefficient                  
PV1_4    0.0                       float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.0                       float PV distortion coefficient                  
PV1_1    1.0                       float PV distortion coefficient                  
PV1_0    0.0                       float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.002                     float PV distortion coefficient                  
PV1_8    0.0                       float PV distortion coefficient                  
CD1_2    -7.5e-05                  float World coordinate transformation matrix     
PV1_5    0.0                       float PV distortion coefficient                  
CD2_1    7.5e-05                   float World coordinate transformation matrix     
CD2_2    0.0                       float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.0                       float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 9LFLHK9I9KEIGK9I          str    ASCII 1's complement checksum             
DATASUM  2536432004                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU68
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  2098                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:2098]         str   Good section                               
DATASEC  [57:2104,51:2098]         str   Data section to display                    
DETSEC   [24577:26624,20480:22527] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]           str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]       str   Good section from amp A                    
DETSECA  [25601:26624,20480:22527] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]        str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]       str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]         str   Good section from amp B                    
DETSECB  [24577:25600,20480:22527] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]           str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]         str   Data section from amp B                    
BIASSECB [7:56,51:2098]            str   Overscan from amp B                        
PRESECB  [1:6,51:2098]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR A1-67_123195-22-5         str   Detector Identifier                        
CCDNUM   74                        int   CCD number                                 
DETPOS   FN2                       str   detector position ID                       
EXTNAME  FN2                       str   extension name                             
GAINA    4.59347726229             float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096             float [electrons] Read noise for amp A           
SATURATA 43266.0                   float [adu] Saturation for amp A                 
GAINB    4.4014084507              float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127             float [electrons] Read noise for amp B           
SATURATB 44935.0                   float [adu] Saturation for amp B                 
CRPIX1   -11375.2                  float Coordinate Reference axis 1                
CRPIX2   -6470.667                 float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F              str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 6 5.210000            str   Monsoon module                             
SLOT01   DESCB 2 4.010000          str   Monsoon module                             
SLOT02   CCD12 6 4.080000          str   Monsoon module                             
SLOT03   CCD12 32 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.002                     float PV distortion coefficient                  
PV2_8    0.0                       float PV distortion coefficient                  
PV2_9    0.002                     float PV distortion coefficient                  
CD1_1    0.0                       float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.0                       float PV distortion coefficient                  
PV2_1    1.0                       float PV distortion coefficient                  
PV2_2    0.0                       float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0                       float PV distortion coefficient                  
PV2_5    0.0                       float PV distortion coefficient                  
PV2_6    0.0                       float PV distortion coefficient                  
PV2_7    0.002                     float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.0                       float PV distortion coefficient                  
PV2_10   0.0                       float PV distortion coefficient                  
PV1_4    0.0                       float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.0                       float PV distortion coefficient                  
PV1_1    1.0                       float PV distortion coefficient                  
PV1_0    0.0                       float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.002                     float PV distortion coefficient                  
PV1_8    0.0                       float PV distortion coefficient                  
CD1_2    -7.5e-05                  float World coordinate transformation matrix     
PV1_5    0.0                       float PV distortion coefficient                  
CD2_1    7.5e-05                   float World coordinate transformation matrix     
CD2_2    0.0                       float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.0                       float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM KF93K980KE80K980          str    ASCII 1's complement checksum             
DATASUM  3630773541                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU69
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  2098                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,51:2098]         str   Good section                               
DATASEC  [57:2104,51:2098]         str   Data section to display                    
DETSEC   [26625:28672,14337:16384] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]           str   CCD section to display                     
TRIMSECA [1081:2104,51:2098]       str   Good section from amp A                    
DETSECA  [27649:28672,14337:16384] str   Detector display tile for amp A            
CCDSECA  [1025:2048,1:2048]        str   CCD section from amp A                     
AMPSECA  [2048:1025,2048:1]        str   CCD section in read order for amp A        
DATASECA [1081:2104,51:2098]       str   Data section from amp A                    
BIASSECA [2105:2154,51:2098]       str   Overscan from amp A                        
PRESECA  [2155:2160,51:2098]       str   Prescan from amp A                         
POSTSECA [1081:2104,1:50]          str   Postscan from amp A                        
TRIMSECB [57:1080,51:2098]         str   Good section from amp B                    
DETSECB  [26625:27648,14337:16384] str   Detector display tile for amp B            
CCDSECB  [1:1024,1:2048]           str   CCD section from amp B                     
AMPSECB  [1:1024,2048:1]           str   CCD section in read order for amp B        
DATASECB [57:1080,51:2098]         str   Data section from amp B                    
BIASSECB [7:56,51:2098]            str   Overscan from amp B                        
PRESECB  [1:6,51:2098]             str   Prescan from amp B                         
POSTSECB [57:1080,1:50]            str   Postscan from amp B                        
DETECTOR A1-03_135959-17-5         str   Detector Identifier                        
CCDNUM   70                        int   CCD number                                 
DETPOS   FN3                       str   detector position ID                       
EXTNAME  FN3                       str   extension name                             
GAINA    4.59347726229             float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096             float [electrons] Read noise for amp A           
SATURATA 43266.0                   float [adu] Saturation for amp A                 
GAINB    4.4014084507              float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127             float [electrons] Read noise for amp B           
SATURATB 44935.0                   float [adu] Saturation for amp B                 
CRPIX1   -13629.6                  float Coordinate Reference axis 1                
CRPIX2   -81.6666                  float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F              str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 6 5.210000            str   Monsoon module                             
SLOT01   DESCB 2 4.010000          str   Monsoon module                             
SLOT02   CCD12 6 4.080000          str   Monsoon module                             
SLOT03   CCD12 32 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.002                     float PV distortion coefficient                  
PV2_8    0.0                       float PV distortion coefficient                  
PV2_9    0.002                     float PV distortion coefficient                  
CD1_1    0.0                       float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.0                       float PV distortion coefficient                  
PV2_1    1.0                       float PV distortion coefficient                  
PV2_2    0.0                       float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0                       float PV distortion coefficient                  
PV2_5    0.0                       float PV distortion coefficient                  
PV2_6    0.0                       float PV distortion coefficient                  
PV2_7    0.002                     float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.0                       float PV distortion coefficient                  
PV2_10   0.0                       float PV distortion coefficient                  
PV1_4    0.0                       float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.0                       float PV distortion coefficient                  
PV1_1    1.0                       float PV distortion coefficient                  
PV1_0    0.0                       float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.002                     float PV distortion coefficient                  
PV1_8    0.0                       float PV distortion coefficient                  
CD1_2    -7.5e-05                  float World coordinate transformation matrix     
PV1_5    0.0                       float PV distortion coefficient                  
CD2_1    7.5e-05                   float World coordinate transformation matrix     
CD2_2    0.0                       float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.0                       float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM ZAhfg4fdZAfdd3fd          str    ASCII 1's complement checksum             
DATASUM  3799020242                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================

HDU70
-----

*Summarize the contents of this HDU.*

Required Header Keywords
~~~~~~~~~~~~~~~~~~~~~~~~

======== ========================= ===== ===========================================
KEY      Value                     Type  Comment                                    
======== ========================= ===== ===========================================
ZIMAGE   T                         bool  extension contains compressed image        
ZTILE1   2160                      int   size of tiles to be compressed             
ZTILE2   1                         int   size of tiles to be compressed             
ZCMPTYPE RICE_1                    str   compression algorithm                      
ZNAME1   BLOCKSIZE                 str   compression block size                     
ZVAL1    32                        int   pixels per block                           
ZNAME2   BYTEPIX                   str   bytes per pixel (1, 2, 4, or 8)            
ZVAL2    2                         int   bytes per pixel (1, 2, 4, or 8)            
ZTENSION IMAGE                     str   IMAGE extension                            
ZBITPIX  16                        int   number of bits per data pixel              
ZNAXIS   2                         int   number of data axes                        
ZNAXIS1  2160                      int   length of data axis 1                      
ZNAXIS2  2098                      int   length of data axis 2                      
ZPCOUNT  0                         int   required keyword; must = 0                 
ZGCOUNT  1                         int   required keyword; must = 1                 
BZERO    32768                     int   offset data range to that of unsigned short
BSCALE   1                         int   default scaling factor                     
BUNIT    adu                       str   Brightness units for pixel array           
WCSAXES  2                         int   WCS Dimensionality                         
DETSIZE  [1:29400,1:29050]         str   Detector size                              
TRIMSEC  [57:2104,1:2048]          str   Good section                               
DATASEC  [57:2104,1:2048]          str   Data section to display                    
DETSEC   [26625:28672,12289:14336] str   Location of this CCD on Focal Plane        
CCDSEC   [1:2048,1:2048]           str   CCD section to display                     
TRIMSECA [57:1080,1:2048]          str   Good section from amp A                    
DETSECA  [26625:27648,12289:14336] str   Detector display tile for amp A            
CCDSECA  [1:1024,1:2048]           str   CCD section from amp A                     
AMPSECA  [1:1024,1:2048]           str   CCD section in read order for amp A        
DATASECA [57:1080,1:2048]          str   Data section from amp A                    
BIASSECA [7:56,1:2048]             str   Overscan from amp A                        
PRESECA  [1:6,1:2048]              str   Prescan from amp A                         
POSTSECA [57:1080,2049:2098]       str   Postscan from amp A                        
TRIMSECB [1081:2104,1:2048]        str   Good section from amp B                    
DETSECB  [27649:28672,12289:14336] str   Detector display tile for amp B            
CCDSECB  [1025:2048,1:2048]        str   CCD section from amp B                     
AMPSECB  [2048:1025,1:2048]        str   CCD section in read order for amp B        
DATASECB [1081:2104,1:2048]        str   Data section from amp B                    
BIASSECB [2105:2154,1:2048]        str   Overscan from amp B                        
PRESECB  [2155:2160,1:2048]        str   Prescan from amp B                         
POSTSECB [1081:2104,2049:2098]     str   Postscan from amp B                        
DETECTOR A1-24_124750-22-5         str   Detector Identifier                        
CCDNUM   69                        int   CCD number                                 
DETPOS   FN4                       str   detector position ID                       
EXTNAME  FN4                       str   extension name                             
GAINA    4.59347726229             float [electrons/adu] Gain for amp A             
RDNOISEA 7.17960496096             float [electrons] Read noise for amp A           
SATURATA 43266.0                   float [adu] Saturation for amp A                 
GAINB    4.4014084507              float [electrons/adu] Gain for amp B             
RDNOISEB 7.01628521127             float [electrons] Read noise for amp B           
SATURATB 44935.0                   float [adu] Saturation for amp B                 
CRPIX1   -13629.6                  float Coordinate Reference axis 1                
CRPIX2   2129.667                  float Coordinate Reference axis 2                
FPA      DECAM_BKP6_F              str   DECam focal plane name                     
INHERIT  T                         bool  Inherits PHDU header                       
CCDBIN1  1                         int   Pixel binning, axis 1                      
CCDBIN2  1                         int   Pixel binning, axis 2                      
DHEINF   MNSN fermi hardware       str   DHE Hardware                               
DHEFIRM  demo30                    str   DHE Firmware                               
SLOT00   MCB 6 5.210000            str   Monsoon module                             
SLOT01   DESCB 2 4.010000          str   Monsoon module                             
SLOT02   CCD12 6 4.080000          str   Monsoon module                             
SLOT03   CCD12 32 4.080000         str   Monsoon module                             
RADESYS  FK5                       str   World coordinate reference frame           
EQUINOX  2000.0                    float [yr] Equinox of WCS                        
PV1_7    0.002                     float PV distortion coefficient                  
PV2_8    0.0                       float PV distortion coefficient                  
PV2_9    0.002                     float PV distortion coefficient                  
CD1_1    0.0                       float World coordinate transformation matrix     
LTM2_2   1.0                       float Detector to image transformation           
LTM2_1   0.0                       float Detector to image transformation           
PV2_0    0.0                       float PV distortion coefficient                  
PV2_1    1.0                       float PV distortion coefficient                  
PV2_2    0.0                       float PV distortion coefficient                  
PV2_3    0.0                       float PV distortion coefficient                  
PV2_4    0.0                       float PV distortion coefficient                  
PV2_5    0.0                       float PV distortion coefficient                  
PV2_6    0.0                       float PV distortion coefficient                  
PV2_7    0.002                     float PV distortion coefficient                  
LTM1_1   1.0                       float Detector to image transformation           
PV1_6    0.0                       float PV distortion coefficient                  
PV2_10   0.0                       float PV distortion coefficient                  
PV1_4    0.0                       float PV distortion coefficient                  
PV1_3    0.0                       float PV distortion coefficient                  
PV1_2    0.0                       float PV distortion coefficient                  
PV1_1    1.0                       float PV distortion coefficient                  
PV1_0    0.0                       float PV distortion coefficient                  
LTM1_2   0.0                       float Detector to image transformation           
PV1_9    0.002                     float PV distortion coefficient                  
PV1_8    0.0                       float PV distortion coefficient                  
CD1_2    -7.5e-05                  float World coordinate transformation matrix     
PV1_5    0.0                       float PV distortion coefficient                  
CD2_1    7.5e-05                   float World coordinate transformation matrix     
CD2_2    0.0                       float World coordinate transformation matrix     
LTV2     0.0                       float Detector to image transformation           
LTV1     56.0                      float Detector to image transformation           
PV1_10   0.0                       float PV distortion coefficient                  
CTYPE2   DEC--TPV                  str   Coordinate type                            
CTYPE1   RA---TPV                  str   Coordinate type                            
CRVAL1   237.447283                float [deg] WCS Reference Coordinate (RA)        
CRVAL2   5.717611                  float [deg] WCS Reference Coordinate (DEC)       
VALIDA   T                         bool  Data from amp A is valid                   
VALIDB   T                         bool  Data from amp B is valid                   
NDONUTS  0                         int   AOS number of donuts analyzed for this CCD 
CHECKVER COMPLEMENT                str    FITS checksum version                     
CHECKSUM 5hap5hYm5ham5hYm          str    ASCII 1's complement checksum             
DATASUM  3392123171                str    checksum of data records                  
======== ========================= ===== ===========================================

Required Data Table Columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============ ===== ===================
Name            Type         Units Description        
=============== ============ ===== ===================
COMPRESSED_DATA 8-bit stream       label for field   1
=============== ============ ===== ===================


Notes and Examples
==================

*Add notes and examples here.  You can also create links to example files.*

