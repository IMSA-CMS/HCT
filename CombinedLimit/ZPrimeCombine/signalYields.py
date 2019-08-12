from ROOT import gROOT, TFile
from numpy import array as ar
from array import array
import argparse
from copy import deepcopy
import pickle



def main():
	gROOT.SetBatch(True)
	
	parser = argparse.ArgumentParser(description='Process some integers.')
	
	parser.add_argument("-add", "--add", action="store_true", dest="useADD", default=False,
						  help="use ADD instead of CI.")
	parser.add_argument("--fakeGen", action="store_true", dest="fakeGen", default = False, help="generates 2017 and 2018 parametrizations for ADD")

	args = parser.parse_args()					  
	useADD = args.useADD	
	histos = ["BB","BE"]
	#og
	labels = ["dielectron_2016","dimuon_2016","dimuon_2017","dielectron_2017","dimuon_2018","dielectron_2018"]
	#labels = ["dimuon_2017","dielectron_2017"]
	suffixesMu = ["nominal","scaledown","smeared","muonid"]
	suffixesEle = ["nominal","scaledown","scaleup","pileup","piledown"]
	css = ["inc","cspos","csneg"]
	lambdas = [10,16,22,28,34,40,46]
	interferences = ["Con","Des"]
	hels = ["LL","LR","RR","RL"]
	massBins = [400,500,700,1100,1900,3500]
	
	if useADD:
		if args.fakeGen:
			labels = ["dielectron_2016", "dimuon_2016","dielectron_2017", "dimuon_2017","dielectron_2018", "dimuon_2018"]
		else:
			labels = ["dielectron_2016", "dimuon_2016"]
		Ele2016Lum = 35.9
		Ele2017Lum = 41.529
		Ele2018Lum = 59.4
		Muon2016Lum = 36.3
		Muon2017Lum = 42.135
		Muon2018Lum = 61.3
		lambdas = [3500+i*500 for i in range(12)]; lambdas.append(10000)
		interferences = [""]
		hels = [""]
		massBins = [2000, 2200, 2600, 3000, 3400]

	signalYields = {}

	if useADD:
		file = open("pickleParametersADD.txt","w")
	else:
		file = open("pickleParametersCI.txt","w")
	for label in labels:
		if "dimuon" in label:
			suffixes = suffixesMu
		else:
			suffixes = suffixesEle
		for suffix in suffixes:
			for cs in css:
				for histo in histos:
					for hel in hels:
						for interference in interferences:			
							model = interference+hel
							addci = "CI"
							if useADD: addci = "ADD"
							if "dimuon" in label:
								name = "%sto2mu"%addci
							else:			#~ print signalYields

								name = "%sto2e"	%addci
							if useADD:
								if "2016" or args.fakeGen in label:
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixinf_2016.root"%(name,suffix,histo.lower(),cs),"READ")
								elif "2018" in label:
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixinf_2018.root"%(name,suffix,histo.lower(),cs),"READ")
								else:
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixinf.root"%(name,suffix,histo.lower(),cs),"READ")
							else:	
								if "2016" in label:
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixdes_fixinf_limitp0_limitp1_limitp2_2016.root"%(name,suffix,histo.lower(),cs),"READ")
								elif "2018" in label:
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixdes_fixinf_limitp0_limitp1_limitp2_2018.root"%(name,suffix,histo.lower(),cs),"READ")
								else:	
									fitFile = TFile("/uscms/home/kgumpula/nobackup/YOURWORKINGAREA/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/ZPrimeCombine/CITest/CIAnalysis/%s_%s_%s_%s_parametrization_fixdes_fixinf_limitp0_limitp1_limitp2.root"%(name,suffix,histo.lower(),cs),"READ")
							for l in lambdas:
								if "dimuon" in label:
									name = "CITo2Mu_Lam%dTeV%s"%(l,model)
								else:	
									name = "CITo2E_Lam%dTeV%s"%(l,model)
								if useADD:
									name = "ADDGravTo2Mu_Lam%d"%l
									if "dielectron" in label: name = "ADDGravTo2E_Lam%d"%l
									l = l * 0.001
								if not cs == "inc":
									name += "_%s"%cs
								signalYields["%s_%s_%s"%(name,label,histo)] = {}

								scale = 1.0
								if args.fakeGen:
									if "2017" in label:
										if "electron" in label:
											scale = Ele2017Lum/Ele2016Lum
										else:
											scale = Muon2017Lum/Muon2016Lum
									elif "2018" in label:
										if "electron" in label:
											scale = Ele2018Lum/Ele2016Lum
										else:
											scale = Muon2018Lum/Muon2016Lum
								for index, massBin in enumerate(massBins):
									function = fitFile.Get("fn_m%d_%s"%(massBin,model))
									fitR = fitFile.Get("fitR_m%d_%s"%(massBin,model))
									pars = fitR.GetParams()
									errs = fitR.Errors()
									function.SetParameter(0,pars[0]*scale)
									function.SetParameter(1,pars[1]*scale)
									function.SetParameter(2,pars[2]*scale)
									function.SetParError(0,errs[0])
									function.SetParError(1,errs[1])
									function.SetParError(2,errs[2])
									if useADD:
										function.SetParameter(3, pars[3]*scale)
										function.SetParError(3, errs[3])
									functionUnc = fitFile.Get("fn_unc_m%d_%s"%(massBin,model))
									uncert = (abs((functionUnc.Eval(l)/function.Eval(l))**2 + (functionUnc.Eval(100000)/function.Eval(100000))))**0.5
									sigVal = (function.Eval(l)-function.Eval(100000))
									if sigVal == 0:
										sigVal = 1e-9
										uncert = 0
									print "%s_%s_%s"%(name,label,histo), massBin, suffix, sigVal, uncert
									signalYields["%s_%s_%s"%(name,label,histo)][massBin] = [sigVal,uncert]
									if useADD and l == lambdas[0]*0.001 and suffix == "nominal":
										file.write(name+" "+histo+" "+model+" "+str(massBin)+" "+suffix+" "+str(pars[0]*scale)+" "+str(pars[1]*scale)+" "+str(pars[2]*scale)+" "+str(pars[3]*scale)+"\n")
									elif l == lambdas[0] and suffix == "nominal":
                                                                                file.write(name+" "+histo+" "+model+" "+str(massBin)+" "+suffix+" "+str(pars[0])+" "+str(pars[1])+" "+str(pars[2])+"\n")

						if useADD: continue
						for l in lambdas:			
							if "dimuon" in label:
								name = "CITo2Mu_Lam%dTeV%s"%(l,hel)
								nameCon = "CITo2Mu_Lam%dTeV%s"%(l,"Con"+hel)
								nameDes = "CITo2Mu_Lam%dTeV%s"%(l,"Des"+hel)
							else:	
								name = "CITo2E_Lam%dTeV%s"%(l,hel)
								nameCon = "CITo2E_Lam%dTeV%s"%(l,"Con"+hel)
								nameDes = "CITo2E_Lam%dTeV%s"%(l,"Des"+hel)
							if not cs == "inc":
								name += "_%s"%cs
								nameCon += "_%s"%cs
								nameDes += "_%s"%cs
							signalYields["%s_%s_%s"%(name,label,histo)] = {}	
							for index, massBin in enumerate(massBins):
								signalYields["%s_%s_%s"%(name,label,histo)][massBin] = [(signalYields["%s_%s_%s"%(nameCon,label,histo)][massBin][0] + signalYields["%s_%s_%s"%(nameDes,label,histo)][massBin][0])/2,((signalYields["%s_%s_%s"%(nameCon,label,histo)][massBin][1]**2 + signalYields["%s_%s_%s"%(nameDes,label,histo)][massBin][1]**2))**0.5]
					

			addci = "CI"
			if useADD: addci = "ADD"
			if "dimuon" in label:
				fileName = "%ssignalYields"%addci
			else:
				fileName = "%ssignalYieldsEle"%addci
			
			if suffix == "nominal":
				otherSuffix = "default"
			elif suffix == "scaledown":
				otherSuffix = "scaleDown"
			elif suffix == "scaleup":
				otherSuffix = "scaleUp"
			elif suffix == "smeared":
				otherSuffix = "resolution"
			elif suffix == "muonid":
				otherSuffix = "ID"
			elif suffix == "pileup":
				otherSuffix = "pileup"
			elif suffix == "piledown":
				otherSuffix = "piledown"
			else:
				print (suffix)
			outFilePkl = open("input/inputsCI/%s_%s.pkl"%(fileName,otherSuffix),"wb")
			pickle.dump(signalYields, outFilePkl, protocol=2)
			outFilePkl.close()	
	file.close()
	
	
			
							
main()
