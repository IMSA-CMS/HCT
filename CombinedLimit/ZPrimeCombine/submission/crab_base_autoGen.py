import os
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'limits_backgroundFix_5500_20190703_202143'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True


config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'dummyPSet.py'
config.JobType.scriptExe= 'runLimits'
config.JobType.scriptArgs= ['dummy=dummy.py','tarFile=gridPack.tar','outputTag=backgroundFix','mass=5500','nIter=500000','nToys=20','expected=1','config=DimuonRun2','inject=0']
config.JobType.inputFiles= ['gridPack.tar',os.environ['CMSSW_BASE']+'/bin/'+os.environ['SCRAM_ARCH']+'/combine','FrameworkJobReport.xml']
config.JobType.outputFiles= ['expectedLimit_DimuonRun2_backgroundFix_5500.root']
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 100
config.Data.outputPrimaryDataset = 'backgroundFix'
config.Data.outputDatasetTag = 'test'
config.Data.outLFNDirBase = '/store/user/jschulte/limits/DimuonRun2'
 
config.section_("Site")
config.Site.storageSite = "T2_US_Purdue"
config.Site.blacklist = ["T3_US_UCR","T3_MX_Cinvestav","T3_TW_NTU_HEP"]
config.section_("User")
