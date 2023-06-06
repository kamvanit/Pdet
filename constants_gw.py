snr_th = 8.

TobsET = 1.
TobsLISA = 4.
TobsLISA2 = 10.

#O1 from 18Sep15 to 12Jan16 (116days) with 41% time LV and HF on
#O2 from 30Nov16 to 25Aug17 (269days) with 46% time LV and HF on
TobsO1 = 0.41*116./365
TobsO2 = 0.46*269./365
TobsO3 = 0.6*1.
TobsO3a = 177.3/365
TobsO4 = 0.7*1.
TobsO5 = 0.7*1.

#LIGO Projections
TobsO1O2 = TobsO1 + TobsO2
TobsO1O3 = TobsO1O2 + TobsO3
TobsO4O5 = TobsO4 + TobsO5
TobsO1O5 = TobsO1O3 + TobsO4O5

fminLISA = 1.0e-4
fminLIGO = 1.0