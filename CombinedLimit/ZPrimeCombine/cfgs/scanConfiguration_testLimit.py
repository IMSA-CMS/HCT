leptons = "elmu"
systematics = ["lumi",'res','massScale',"zPeak","trig","jets","xSecOther","pdf","ID","stats","PU"]
#systematics = ["lumi",'res',"zPeak","trig","jets","xSecOther","ID"]
#systematics = ['massScale',"pdf","stats"]
backgrounds = ['DY','Other','Jets']

LPCUsername = "kgumpula"



correlate = True

#lambdas = [16]
lambdas = [10,16,22,28,34,40,46]
#interferences = ["ConLL","DesLL"]
#interferences = ["ConLL","ConLR","ConRR"]
#interferences = ["ConLL","DesLL"]
interferences = ["ConLL"]
#interferences = ["ConLL","DesLL"]
#interferences = ["ConLL","ConLR","ConRR"]
#interferences = ["ConLL","ConLR","ConRL","ConRR","DesLL","DesLR","DesRL","DesRR"]

#5000 CAN NOT BE USED AS A SINGLE BIN
#DO NOT USE --singlebin switch with combineSigDY
#binning = [400,500]
#used in original analysis
#binning = [400,500,700,1100,1900,3500,10000]
binning = [3500,10000]
#binning = [400,500,700,1100,1900,3500,5000]

#binning = [400]
#binning = [2200]
#binning = [2200,5000]

#all possible mass ranges that we have data for
#400,500,700,1100,1200,1400,1600,1800,1900,2000,2200,2400,3500

#binning = [2200]
#binning = [2200,5000]
libraries = ["ZPrimeMuonBkgPdf2_cxx.so","PowFunc_cxx.so"]

#channels = ["dimuon_2016_BB","dimuon_2016_BE","dielectron_2016_BB","dielectron_2016_BE","dimuon_2017_BB","dimuon_2017_BE","dielectron_2017_BB","dielectron_2017_BE","dimuon_2018_BB","dimuon_2018_BE","dielectron_2018_BB","dielectron_2018_BE"]
#channels = ["cspos_dielectron_2017_BE","csneg_dielectron_2017_BE","cspos_dielectron_2017_BB","csneg_dielectron_2017_BB"]
#channels = ["cspos_dielectron_2017_BE","csneg_dielectron_2017_BE","cspos_dimuon_2017_BE","csneg_dimuon_2017_BE","cspos_dielectron_2017_BB","csneg_dielectron_2017_BB","cspos_dimuon_2017_BB","csneg_dimuon_2017_BB"]
#channels = ["cspos_dielectron_2016_BB","cspos_dielectron_2016_BE","cspos_dimuon_2016_BB","cspos_dimuon_2016_BE","cspos_dielectron_2017_BB","cspos_dielectron_2017_BE","cspos_dimuon_2017_BB","cspos_dimuon_2017_BE","cspos_dielectron_2018_BB","cspos_dielectron_2018_BE","cspos_dimuon_2018_BB","cspos_dimuon_2018_BE","csneg_dielectron_2016_BB","csneg_dielectron_2016_BE","csneg_dimuon_2016_BB","csneg_dimuon_2016_BE","csneg_dielectron_2017_BB","csneg_dielectron_2017_BE","csneg_dimuon_2017_BB","csneg_dimuon_2017_BE","csneg_dielectron_2018_BB","csneg_dielectron_2018_BE","csneg_dimuon_2018_BB","csneg_dimuon_2018_BE"]
#channels = ["dimuon_Moriond2017_BB", "dimuon_Moriond2017_BE"]
channels = ["dimuon_2017_BB"]
#channels = ["dielectron_Moriond2017_BB", "dielectron_Moriond2017_BE", "dimuon_Moriond2017_BB", "dimuon_Moriond2017_BE"]
#channels = ["dielectron_Moriond2017_BE", "dielectron_Moriond2017_BB", "dimuon_Moriond2017_BB", "dimuon_Moriond2017_BE"]
numInt = 1000000
numToys = 6
exptToys = 500
#numToys = 1
#exptToys = 1
#exptToys = 5
submitTo = "FNAL"

		
