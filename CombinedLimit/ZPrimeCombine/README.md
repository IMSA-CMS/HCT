# ZPrimeCombine
Tools to perform statistical analyses for the Z' -> ll analysis using the Higgs combine toolkit

## Current combine installation recipe:
export SCRAM_ARCH=slc7_amd64_gcc700
 
cmsrel CMSSW_10_2_13 

cd CMSSW_10_2_13/src 

cmsenv 

git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit 

cd HiggsAnalysis/CombinedLimit 

git fetch origin 

git checkout v8.0.1 

scramv1 b clean; scramv1 b # always make a clean build 

## Check out ZPrimeCombine toolkit:
git clone https://USERNAME@gitlab.cern.ch/cms-zprime-dileptons/ZPrimeCombine.git
## General considerations:  
This repository consits of python scripts fulfilling two purposes:

1) Create datacards and ROOT files containing workspaces as input for combine,

2) Serve as a user-friendly interface to execute combine in the appropriate configuration for limits and p-values/significance,

For detailed instructions on usage, please see the manual in the documentation folder
