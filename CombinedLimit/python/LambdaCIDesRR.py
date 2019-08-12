
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #cspos_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_400_Beta("462.704662596+-1665.12954751*@0+347677.847886*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_500_Beta("280.011353084+-24.7780934933*@0+677117.233045*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_700_Beta("111.518073456+-2534.18292537*@0+1183903.15608*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_1100_Beta("21.2399806401+-1235.36677672*@0+829278.79601*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_3500_Beta("0.0256484800828+-19.9034305597*@0+67531.3356112*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_400_Beta("471.006466839+-4196.11595841*@0+388583.12*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_500_Beta("277.141344743+-6.01504460969*@0+671683.508242*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_700_Beta("104.165940199+-4211.98878891*@0+1022736.71753*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_1100_Beta("14.6220383901+-1014.67520431*@0+539644.931775*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_3500_Beta("0.00374275914385+-1.9235010939*@0+13652.0064217*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_400_Beta("405.533033361+-1754.26580593*@0+143316.801316*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_500_Beta("240.351654138+-26.5108409442*@0+292586.87671*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_700_Beta("95.6409285629+-3233.80050851*@0+494268.569789*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_1100_Beta("19.4582655998+-1540.92756964*@0+637625.273304*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_3500_Beta("0.0278157992047+-25.4652504656*@0+72228.776724*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_400_Beta("972.917605481+-6419.30782491*@0+351149.414276*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_500_Beta("575.991367892+-24.3450023787*@0+647607.133094*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_700_Beta("200.463409018+-6068.55702155*@0+957463.935899*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_1100_Beta("31.3567042752+-2753.46295295*@0+953587.559399*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_3500_Beta("0.0242347562157+-24.7199210289*@0+48744.5320937*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_400_Beta("651.270849834+-13239.5818622*@0+1925226.3008*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_500_Beta("416.109826899+-46.4163692797*@0+1564984.15396*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_700_Beta("147.599034953+-1.69098230394e-07*@0+6.10622663544e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_1100_Beta("31.0138445666+-2745.35748173*@0+940285.379869*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_3500_Beta("0.0345389282012+-33.4083198682*@0+63422.43834*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_400_Beta("697.428977297+-26473.5811014*@0+5036489.47656*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_500_Beta("430.393867574+-8.14420005494*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_700_Beta("146.465852349+-2261.35695536*@0+627608.242687*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_1100_Beta("22.9046281996+-2201.43408182*@0+611287.432429*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_3500_Beta("0.00917664580229+-3.61957934242*@0+13134.1618045*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_400_Beta("605.083603191+-2165.83177676*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_500_Beta("374.211149902+-58.0735732385*@0+646359.107599*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_700_Beta("153.733958873+-13741.7070295*@0+2823260.52863*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_1100_Beta("29.1521519575+-2742.4453546*@0+1049075.30032*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_3500_Beta("0.0375104574151+-39.0632220317*@0+66235.9637328*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_400_Beta("1385.27135505+-8106.74225277*@0+1727282.71549*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_500_Beta("850.120345444+-41.8545127322*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_700_Beta("298.194991611+-17931.9516758*@0+3462338.23899*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_1100_Beta("46.8161893728+-5142.7001702*@0+1607040.86671*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_3500_Beta("0.0286594862122+-31.9181479602*@0+47533.9152676*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_400_Beta("927.81031541+-5.56378479956e-08*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_500_Beta("603.833567479+-68.5144886387*@0+3499754.93878*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_700_Beta("229.602963534+-34243.3745974*@0+7732008.84276*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_1100_Beta("45.2626912238+-4524.37558287*@0+1507725.06977*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_3500_Beta("0.0490361787483+-47.9353290958*@0+92746.3174992*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_400_Beta("992.38583879+-1.1143103271e-07*@0+1.05471187339e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_500_Beta("625.930227168+-9.69857259229*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_700_Beta("390.324202097+-7555.20344698*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_1100_Beta("33.7948811094+-3891.55413157*@0+1062717.99999*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_3500_Beta("0.0125570108119+-3.77906029428*@0+18924.2154531*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_400_Beta("906.713454589+-3245.43917048*@0+1.49880108324e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_500_Beta("560.75268476+-86.8703100241*@0+968529.709233*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_700_Beta("230.369259276+-20591.8667907*@0+4230639.2987*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_1100_Beta("43.6842937302+-4109.53346382*@0+1572031.73456*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_3500_Beta("0.0562091226819+-58.5358769724*@0+99254.0960768*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_400_Beta("2075.81912826+-12147.7317941*@0+2588296.27853*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_500_Beta("1273.89835673+-62.0536983258*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_700_Beta("446.843070501+-26870.8986406*@0+5188288.67746*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_1100_Beta("70.1537317915+-7706.3073301*@0+2408141.0332*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_3500_Beta("0.0429088641718+-47.7215153852*@0+71188.9458612*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_400_Beta("363.702603633+-1892.22928861*@0+272885.759862*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_500_Beta("212.326737201+-23.3057060145*@0+521113.317668*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_700_Beta("86.4510374419+-3608.3125888*@0+833571.331206*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_1100_Beta("15.1524278057+-606.680276048*@0+550428.908449*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_3500_Beta("0.0182261182203+-18.8862136394*@0+42410.0257738*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_400_Beta("211.212661577+-1805.33996706*@0+155873.12291*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_500_Beta("114.465868974+-6.2574250465*@0+234764.975428*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_700_Beta("40.7445592916+-1221.23984618*@0+322262.058832*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_1100_Beta("5.45464201595+-235.239204189*@0+153095.463099*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_3500_Beta("0.00710984480765+-6.05641267655*@0+3896.7516538*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_400_Beta("330.252172737+-402.996871795*@0+127120.048069*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_500_Beta("208.576996113+-34.1589609957*@0+232980.825188*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_700_Beta("75.1271679226+-1831.79498717*@0+353684.902275*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_1100_Beta("14.731892094+-1078.43546989*@0+452166.284373*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_3500_Beta("0.0258232031929+-25.9184894832*@0+42723.7282739*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_400_Beta("528.930857674+-5985.42897509*@0+174736.019515*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_500_Beta("295.57383439+-13.353845713*@0+287836.081033*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_700_Beta("94.0872420219+-2824.73404899*@0+389292.425226*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_1100_Beta("13.9793424882+-834.422123671*@0+327238.846836*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_3500_Beta("0.00470224139758+-8.75272461557*@0+18148.3774168*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_400_Beta("519.502502975+-17719.7716396*@0+3268004.69852*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_500_Beta("305.727272645+-12.6280850825*@0+259738.030729*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_700_Beta("120.397307162+-8796.59590023*@0+1926501.75462*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_1100_Beta("20.2840273184+-1332.65418062*@0+600994.851292*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_3500_Beta("0.0152474435854+-10.1101725406*@0+37958.6584844*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_400_Beta("322.833122867+-4093.82529655*@0+7.82707232361e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_500_Beta("181.412462984+-8410.30621947*@0+1982653.24915*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_700_Beta("48.8460839396+-1170.92587013*@0+548554.013905*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_1100_Beta("7.30250509987+-626.095683967*@0+195373.246233*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_3500_Beta("0.00282349047606+0.292114983806*@0+6531.71066939*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_400_Beta("525.01989615+-21230.5464801*@0+4007413.63241*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_500_Beta("310.998134877+-16.0347844757*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_700_Beta("113.853957629+-1403.73970093*@0+405535.243577*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_1100_Beta("20.7629505289+-1401.73479074*@0+724655.814081*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_3500_Beta("0.0190292517585+-8.31701837048*@0+39035.6448111*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_400_Beta("775.05489392+-14827.5785962*@0+1518498.05805*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_500_Beta("442.3840381+-5433.29499666*@0+1771196.88445*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_700_Beta("133.198017059+-978.47125415*@0+1073921.57717*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_1100_Beta("18.8932337141+-1671.22985051*@0+615867.64371*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_3500_Beta("0.00853582364094+1.12335618904*@0+21356.5318342*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_400_Beta("756.31731239+-14393.2853569*@0+1809411.39517*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_500_Beta("449.751135808+-27.6267636769*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_700_Beta("171.442473518+-10484.5760069*@0+3197140.63206*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_1100_Beta("30.0353188635+-3398.29825083*@0+1235821.17305*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_3500_Beta("0.0222150642414+-19.087996609*@0+58177.032063*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_400_Beta("459.445104284+-5.56828434584e-08*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_500_Beta("12884.0175434+-7773436.335*@0+1000000000.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_700_Beta("71.8256332661+-641.087860475*@0+532606.460343*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_1100_Beta("10.5189329728+-740.061442507*@0+256946.301066*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_3500_Beta("0.0040404009255+0.635594941347*@0+9418.67277021*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_400_Beta("763.880682894+-1.67516490851e-07*@0+2.77555756156e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_500_Beta("466.028520774+-24.0277139877*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_700_Beta("170.609368563+-2103.5184349*@0+607696.498545*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_1100_Beta("31.1131379792+-2100.49168661*@0+1085892.03875*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_3500_Beta("0.0285151935548+-12.4629962865*@0+58494.6417234*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_400_Beta("1161.41404614+-22218.8925015*@0+2275446.55752*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_500_Beta("662.909409418+-8141.73872083*@0+2654121.66105*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_700_Beta("199.596316512+-1466.22971119*@0+1609262.80419*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_1100_Beta("28.3113772199+-2504.3263266*@0+922873.365131*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_3500_Beta("0.0127908713157+1.68334791365*@0+32002.6024792*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "cspos_dielectron_2016_BB_400":
            print "cspos_dielectron_2016_BB_400 DesRR"
            return 'calccspos_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_500":
            print "cspos_dielectron_2016_BB_500 DesRR"
            return 'calccspos_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_700":
            print "cspos_dielectron_2016_BB_700 DesRR"
            return 'calccspos_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_1100":
            print "cspos_dielectron_2016_BB_1100 DesRR"
            return 'calccspos_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_3500":
            print "cspos_dielectron_2016_BB_3500 DesRR"
            return 'calccspos_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_400":
            print "cspos_dielectron_2016_BE_400 DesRR"
            return 'calccspos_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_500":
            print "cspos_dielectron_2016_BE_500 DesRR"
            return 'calccspos_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_700":
            print "cspos_dielectron_2016_BE_700 DesRR"
            return 'calccspos_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_1100":
            print "cspos_dielectron_2016_BE_1100 DesRR"
            return 'calccspos_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_3500":
            print "cspos_dielectron_2016_BE_3500 DesRR"
            return 'calccspos_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_400":
            print "cspos_dimuon_2016_BB_400 DesRR"
            return 'calccspos_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_500":
            print "cspos_dimuon_2016_BB_500 DesRR"
            return 'calccspos_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_700":
            print "cspos_dimuon_2016_BB_700 DesRR"
            return 'calccspos_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_1100":
            print "cspos_dimuon_2016_BB_1100 DesRR"
            return 'calccspos_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_3500":
            print "cspos_dimuon_2016_BB_3500 DesRR"
            return 'calccspos_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_400":
            print "cspos_dimuon_2016_BE_400 DesRR"
            return 'calccspos_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_500":
            print "cspos_dimuon_2016_BE_500 DesRR"
            return 'calccspos_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_700":
            print "cspos_dimuon_2016_BE_700 DesRR"
            return 'calccspos_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_1100":
            print "cspos_dimuon_2016_BE_1100 DesRR"
            return 'calccspos_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_3500":
            print "cspos_dimuon_2016_BE_3500 DesRR"
            return 'calccspos_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_400":
            print "cspos_dielectron_2017_BB_400 DesRR"
            return 'calccspos_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_500":
            print "cspos_dielectron_2017_BB_500 DesRR"
            return 'calccspos_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_700":
            print "cspos_dielectron_2017_BB_700 DesRR"
            return 'calccspos_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_1100":
            print "cspos_dielectron_2017_BB_1100 DesRR"
            return 'calccspos_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_3500":
            print "cspos_dielectron_2017_BB_3500 DesRR"
            return 'calccspos_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_400":
            print "cspos_dielectron_2017_BE_400 DesRR"
            return 'calccspos_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_500":
            print "cspos_dielectron_2017_BE_500 DesRR"
            return 'calccspos_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_700":
            print "cspos_dielectron_2017_BE_700 DesRR"
            return 'calccspos_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_1100":
            print "cspos_dielectron_2017_BE_1100 DesRR"
            return 'calccspos_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_3500":
            print "cspos_dielectron_2017_BE_3500 DesRR"
            return 'calccspos_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_400":
            print "cspos_dimuon_2017_BB_400 DesRR"
            return 'calccspos_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_500":
            print "cspos_dimuon_2017_BB_500 DesRR"
            return 'calccspos_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_700":
            print "cspos_dimuon_2017_BB_700 DesRR"
            return 'calccspos_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_1100":
            print "cspos_dimuon_2017_BB_1100 DesRR"
            return 'calccspos_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_3500":
            print "cspos_dimuon_2017_BB_3500 DesRR"
            return 'calccspos_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_400":
            print "cspos_dimuon_2017_BE_400 DesRR"
            return 'calccspos_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_500":
            print "cspos_dimuon_2017_BE_500 DesRR"
            return 'calccspos_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_700":
            print "cspos_dimuon_2017_BE_700 DesRR"
            return 'calccspos_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_1100":
            print "cspos_dimuon_2017_BE_1100 DesRR"
            return 'calccspos_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_3500":
            print "cspos_dimuon_2017_BE_3500 DesRR"
            return 'calccspos_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_400":
            print "cspos_dielectron_2018_BB_400 DesRR"
            return 'calccspos_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_500":
            print "cspos_dielectron_2018_BB_500 DesRR"
            return 'calccspos_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_700":
            print "cspos_dielectron_2018_BB_700 DesRR"
            return 'calccspos_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_1100":
            print "cspos_dielectron_2018_BB_1100 DesRR"
            return 'calccspos_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_3500":
            print "cspos_dielectron_2018_BB_3500 DesRR"
            return 'calccspos_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_400":
            print "cspos_dielectron_2018_BE_400 DesRR"
            return 'calccspos_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_500":
            print "cspos_dielectron_2018_BE_500 DesRR"
            return 'calccspos_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_700":
            print "cspos_dielectron_2018_BE_700 DesRR"
            return 'calccspos_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_1100":
            print "cspos_dielectron_2018_BE_1100 DesRR"
            return 'calccspos_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_3500":
            print "cspos_dielectron_2018_BE_3500 DesRR"
            return 'calccspos_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_400":
            print "cspos_dimuon_2018_BB_400 DesRR"
            return 'calccspos_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_500":
            print "cspos_dimuon_2018_BB_500 DesRR"
            return 'calccspos_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_700":
            print "cspos_dimuon_2018_BB_700 DesRR"
            return 'calccspos_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_1100":
            print "cspos_dimuon_2018_BB_1100 DesRR"
            return 'calccspos_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_3500":
            print "cspos_dimuon_2018_BB_3500 DesRR"
            return 'calccspos_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_400":
            print "cspos_dimuon_2018_BE_400 DesRR"
            return 'calccspos_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_500":
            print "cspos_dimuon_2018_BE_500 DesRR"
            return 'calccspos_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_700":
            print "cspos_dimuon_2018_BE_700 DesRR"
            return 'calccspos_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_1100":
            print "cspos_dimuon_2018_BE_1100 DesRR"
            return 'calccspos_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_3500":
            print "cspos_dimuon_2018_BE_3500 DesRR"
            return 'calccspos_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_400":
            print "csneg_dielectron_2016_BB_400 DesRR"
            return 'calccsneg_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_500":
            print "csneg_dielectron_2016_BB_500 DesRR"
            return 'calccsneg_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_700":
            print "csneg_dielectron_2016_BB_700 DesRR"
            return 'calccsneg_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_1100":
            print "csneg_dielectron_2016_BB_1100 DesRR"
            return 'calccsneg_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_3500":
            print "csneg_dielectron_2016_BB_3500 DesRR"
            return 'calccsneg_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_400":
            print "csneg_dielectron_2016_BE_400 DesRR"
            return 'calccsneg_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_500":
            print "csneg_dielectron_2016_BE_500 DesRR"
            return 'calccsneg_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_700":
            print "csneg_dielectron_2016_BE_700 DesRR"
            return 'calccsneg_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_1100":
            print "csneg_dielectron_2016_BE_1100 DesRR"
            return 'calccsneg_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_3500":
            print "csneg_dielectron_2016_BE_3500 DesRR"
            return 'calccsneg_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_400":
            print "csneg_dimuon_2016_BB_400 DesRR"
            return 'calccsneg_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_500":
            print "csneg_dimuon_2016_BB_500 DesRR"
            return 'calccsneg_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_700":
            print "csneg_dimuon_2016_BB_700 DesRR"
            return 'calccsneg_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_1100":
            print "csneg_dimuon_2016_BB_1100 DesRR"
            return 'calccsneg_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_3500":
            print "csneg_dimuon_2016_BB_3500 DesRR"
            return 'calccsneg_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_400":
            print "csneg_dimuon_2016_BE_400 DesRR"
            return 'calccsneg_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_500":
            print "csneg_dimuon_2016_BE_500 DesRR"
            return 'calccsneg_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_700":
            print "csneg_dimuon_2016_BE_700 DesRR"
            return 'calccsneg_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_1100":
            print "csneg_dimuon_2016_BE_1100 DesRR"
            return 'calccsneg_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_3500":
            print "csneg_dimuon_2016_BE_3500 DesRR"
            return 'calccsneg_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_400":
            print "csneg_dielectron_2017_BB_400 DesRR"
            return 'calccsneg_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_500":
            print "csneg_dielectron_2017_BB_500 DesRR"
            return 'calccsneg_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_700":
            print "csneg_dielectron_2017_BB_700 DesRR"
            return 'calccsneg_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_1100":
            print "csneg_dielectron_2017_BB_1100 DesRR"
            return 'calccsneg_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_3500":
            print "csneg_dielectron_2017_BB_3500 DesRR"
            return 'calccsneg_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_400":
            print "csneg_dielectron_2017_BE_400 DesRR"
            return 'calccsneg_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_500":
            print "csneg_dielectron_2017_BE_500 DesRR"
            return 'calccsneg_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_700":
            print "csneg_dielectron_2017_BE_700 DesRR"
            return 'calccsneg_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_1100":
            print "csneg_dielectron_2017_BE_1100 DesRR"
            return 'calccsneg_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_3500":
            print "csneg_dielectron_2017_BE_3500 DesRR"
            return 'calccsneg_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_400":
            print "csneg_dimuon_2017_BB_400 DesRR"
            return 'calccsneg_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_500":
            print "csneg_dimuon_2017_BB_500 DesRR"
            return 'calccsneg_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_700":
            print "csneg_dimuon_2017_BB_700 DesRR"
            return 'calccsneg_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_1100":
            print "csneg_dimuon_2017_BB_1100 DesRR"
            return 'calccsneg_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_3500":
            print "csneg_dimuon_2017_BB_3500 DesRR"
            return 'calccsneg_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_400":
            print "csneg_dimuon_2017_BE_400 DesRR"
            return 'calccsneg_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_500":
            print "csneg_dimuon_2017_BE_500 DesRR"
            return 'calccsneg_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_700":
            print "csneg_dimuon_2017_BE_700 DesRR"
            return 'calccsneg_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_1100":
            print "csneg_dimuon_2017_BE_1100 DesRR"
            return 'calccsneg_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_3500":
            print "csneg_dimuon_2017_BE_3500 DesRR"
            return 'calccsneg_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_400":
            print "csneg_dielectron_2018_BB_400 DesRR"
            return 'calccsneg_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_500":
            print "csneg_dielectron_2018_BB_500 DesRR"
            return 'calccsneg_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_700":
            print "csneg_dielectron_2018_BB_700 DesRR"
            return 'calccsneg_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_1100":
            print "csneg_dielectron_2018_BB_1100 DesRR"
            return 'calccsneg_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_3500":
            print "csneg_dielectron_2018_BB_3500 DesRR"
            return 'calccsneg_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_400":
            print "csneg_dielectron_2018_BE_400 DesRR"
            return 'calccsneg_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_500":
            print "csneg_dielectron_2018_BE_500 DesRR"
            return 'calccsneg_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_700":
            print "csneg_dielectron_2018_BE_700 DesRR"
            return 'calccsneg_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_1100":
            print "csneg_dielectron_2018_BE_1100 DesRR"
            return 'calccsneg_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_3500":
            print "csneg_dielectron_2018_BE_3500 DesRR"
            return 'calccsneg_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_400":
            print "csneg_dimuon_2018_BB_400 DesRR"
            return 'calccsneg_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_500":
            print "csneg_dimuon_2018_BB_500 DesRR"
            return 'calccsneg_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_700":
            print "csneg_dimuon_2018_BB_700 DesRR"
            return 'calccsneg_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_1100":
            print "csneg_dimuon_2018_BB_1100 DesRR"
            return 'calccsneg_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_3500":
            print "csneg_dimuon_2018_BB_3500 DesRR"
            return 'calccsneg_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_400":
            print "csneg_dimuon_2018_BE_400 DesRR"
            return 'calccsneg_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_500":
            print "csneg_dimuon_2018_BE_500 DesRR"
            return 'calccsneg_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_700":
            print "csneg_dimuon_2018_BE_700 DesRR"
            return 'calccsneg_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_1100":
            print "csneg_dimuon_2018_BE_1100 DesRR"
            return 'calccsneg_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_3500":
            print "csneg_dimuon_2018_BE_3500 DesRR"
            return 'calccsneg_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
