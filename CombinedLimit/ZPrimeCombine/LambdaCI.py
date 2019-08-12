
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #dielectron_2016_BB_2000
        self.modelBuilder.factory_('expr::calcdielectron_2016_BB_2000_Beta("1.00727799079+-0.955714036378*@0+-131.238988807*@0*@0+527954.866462*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BB_2200
        self.modelBuilder.factory_('expr::calcdielectron_2016_BB_2200_Beta("0.851834649035+-1.48890944228*@0+239.444652451*@0*@0+985249.247153*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BB_2600
        self.modelBuilder.factory_('expr::calcdielectron_2016_BB_2600_Beta("0.469043108704+-27.1280499682*@0+1160.12239088*@0*@0+848762.118042*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BB_3000
        self.modelBuilder.factory_('expr::calcdielectron_2016_BB_3000_Beta("0.324772052576+-35.1001331956*@0+1440.94707343*@0*@0+729807.86459*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BB_3400
        self.modelBuilder.factory_('expr::calcdielectron_2016_BB_3400_Beta("0.687470582869+-100.836296247*@0+4118.69006399*@0*@0+2271517.51941*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BE_2000
        self.modelBuilder.factory_('expr::calcdielectron_2016_BE_2000_Beta("0.328603731195+4.30939682987*@0+-248.127699205*@0*@0+112960.026967*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BE_2200
        self.modelBuilder.factory_('expr::calcdielectron_2016_BE_2200_Beta("0.328441010478+-4.58239810703*@0+-5.65670503729*@0*@0+171375.807011*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BE_2600
        self.modelBuilder.factory_('expr::calcdielectron_2016_BE_2600_Beta("0.106128306275+-3.65930662622*@0+89.518943998*@0*@0+119472.839466*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BE_3000
        self.modelBuilder.factory_('expr::calcdielectron_2016_BE_3000_Beta("0.0509022304795+-3.71046144721*@0+125.643615966*@0*@0+87532.0524677*@0*@0*@0*@0",Beta)')
      
        #dielectron_2016_BE_3400
        self.modelBuilder.factory_('expr::calcdielectron_2016_BE_3400_Beta("0.0767061704892+-10.5968887654*@0+407.461771837*@0*@0+246797.149761*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BE_2000
        self.modelBuilder.factory_('expr::calcdimuon_2016_BE_2000_Beta("0.888134677603+5.28653476865*@0+-423.052545797*@0*@0+312705.775868*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BE_2200
        self.modelBuilder.factory_('expr::calcdimuon_2016_BE_2200_Beta("0.814318908262+-5.20669941271*@0+-40.0766620136*@0*@0+486981.10977*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BE_2600
        self.modelBuilder.factory_('expr::calcdimuon_2016_BE_2600_Beta("0.285218761533+-7.44357534633*@0+245.01812702*@0*@0+405035.893905*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BE_3000
        self.modelBuilder.factory_('expr::calcdimuon_2016_BE_3000_Beta("0.104951116135+-5.37661944909*@0+240.747317724*@0*@0+329483.334856*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BE_3400
        self.modelBuilder.factory_('expr::calcdimuon_2016_BE_3400_Beta("0.344973408173+-46.8450333394*@0+1772.90736239*@0*@0+862181.745076*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BB_2000
        self.modelBuilder.factory_('expr::calcdimuon_2016_BB_2000_Beta("0.982577053232+-0.884708364285*@0+-45.7301319066*@0*@0+571410.78734*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BB_2200
        self.modelBuilder.factory_('expr::calcdimuon_2016_BB_2200_Beta("0.976167052188+-16.8344360443*@0+682.862573414*@0*@0+1090073.6258*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BB_2600
        self.modelBuilder.factory_('expr::calcdimuon_2016_BB_2600_Beta("0.357747861161+-16.8850872236*@0+991.464242207*@0*@0+1009465.75922*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BB_3000
        self.modelBuilder.factory_('expr::calcdimuon_2016_BB_3000_Beta("0.355052160125+-38.1588531932*@0+1574.58729137*@0*@0+818155.840449*@0*@0*@0*@0",Beta)')
      
        #dimuon_2016_BB_3400
        self.modelBuilder.factory_('expr::calcdimuon_2016_BB_3400_Beta("0.885403233413+-128.851334689*@0+5169.9612856*@0*@0+2517097.06624*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "dielectron_2016_BB_2000":
            print "dielectron_2016_BB_2000 "
            return 'calcdielectron_2016_BB_2000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BB_2200":
            print "dielectron_2016_BB_2200 "
            return 'calcdielectron_2016_BB_2200_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BB_2600":
            print "dielectron_2016_BB_2600 "
            return 'calcdielectron_2016_BB_2600_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BB_3000":
            print "dielectron_2016_BB_3000 "
            return 'calcdielectron_2016_BB_3000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BB_3400":
            print "dielectron_2016_BB_3400 "
            return 'calcdielectron_2016_BB_3400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BE_2000":
            print "dielectron_2016_BE_2000 "
            return 'calcdielectron_2016_BE_2000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BE_2200":
            print "dielectron_2016_BE_2200 "
            return 'calcdielectron_2016_BE_2200_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BE_2600":
            print "dielectron_2016_BE_2600 "
            return 'calcdielectron_2016_BE_2600_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BE_3000":
            print "dielectron_2016_BE_3000 "
            return 'calcdielectron_2016_BE_3000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dielectron_2016_BE_3400":
            print "dielectron_2016_BE_3400 "
            return 'calcdielectron_2016_BE_3400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BE_2000":
            print "dimuon_2016_BE_2000 "
            return 'calcdimuon_2016_BE_2000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BE_2200":
            print "dimuon_2016_BE_2200 "
            return 'calcdimuon_2016_BE_2200_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BE_2600":
            print "dimuon_2016_BE_2600 "
            return 'calcdimuon_2016_BE_2600_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BE_3000":
            print "dimuon_2016_BE_3000 "
            return 'calcdimuon_2016_BE_3000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BE_3400":
            print "dimuon_2016_BE_3400 "
            return 'calcdimuon_2016_BE_3400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BB_2000":
            print "dimuon_2016_BB_2000 "
            return 'calcdimuon_2016_BB_2000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BB_2200":
            print "dimuon_2016_BB_2200 "
            return 'calcdimuon_2016_BB_2200_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BB_2600":
            print "dimuon_2016_BB_2600 "
            return 'calcdimuon_2016_BB_2600_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BB_3000":
            print "dimuon_2016_BB_3000 "
            return 'calcdimuon_2016_BB_3000_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "dimuon_2016_BB_3400":
            print "dimuon_2016_BB_3400 "
            return 'calcdimuon_2016_BB_3400_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
