
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calcdimuon_2017_BB_3500_Beta("0.0768074032233+7.05399705314*@0+107519.153165*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "dimuon_2017_BB_3500":
            print "dimuon_2017_BB_3500 ConLL"
            return 'calcdimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
