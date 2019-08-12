
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #cspos_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_400_Beta("469.261412169+1527.47075965*@0+356071.126281*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_500_Beta("298.834628665+1912.28633079*@0+703836.737282*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_700_Beta("120.128514411+2324.67817529*@0+1203154.76041*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_1100_Beta("23.4054909821+1133.23712964*@0+964172.23109*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_3500_Beta("0.0392805442402+18.257983736*@0+69243.926803*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_400_Beta("476.728772581+4611.73494015*@0+363843.358078*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_500_Beta("299.682036785+2916.23408483*@0+686097.644149*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_700_Beta("106.699298997+3863.77728068*@0+1027835.37052*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_1100_Beta("16.866348027+930.790464593*@0+678078.696672*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_3500_Beta("0.00421423993191+1.76448233802*@0+14489.8362998*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_400_Beta("406.502013756+1609.23798825*@0+149070.57976*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_500_Beta("262.397337983+2372.29729749*@0+284205.116704*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_700_Beta("92.1727730274+3156.00353401*@0+501962.700101*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_1100_Beta("19.6021847728+1413.53674787*@0+659183.947784*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_3500_Beta("0.0344520597559+23.3599995458*@0+74060.4497052*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_400_Beta("993.696408273+5888.61390061*@0+363505.143547*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_500_Beta("625.26639726+8329.01532616*@0+637502.49054*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_700_Beta("202.103310837+6669.63847756*@0+990081.143676*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_1100_Beta("33.0838478083+2525.82999005*@0+1010893.56874*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_3500_Beta("0.0207900012323+22.6762876254*@0+50368.610044*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_400_Beta("657.705253621+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_500_Beta("418.676051707+1.11022302463e-07*@0+1602455.94657*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_700_Beta("154.09382998+1.66533453694e-07*@0+2979518.27282*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_1100_Beta("31.0814744162+2518.39461046*@0+988646.98879*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_3500_Beta("0.029904685656+36.7173637605*@0+60039.6211715*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_400_Beta("715.764460906+0.0*@0+2.22044604925e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_500_Beta("433.84530466+11044.7111326*@0+1.38222766566e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_700_Beta("149.15414119+2074.4071425*@0+2118624.39997*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_1100_Beta("23.3640768179+2019.43818384*@0+755541.056271*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_3500_Beta("0.0108186739801+3.32034322259*@0+15786.5145922*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_400_Beta("609.333497464+1986.7791754*@0+0.00123945298469*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_500_Beta("386.073651983+0.0*@0+2753175.03766*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_700_Beta("141.402063731+0.0*@0+2298271.05067*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_1100_Beta("28.4153789313+2814.85697384*@0+871436.272628*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_3500_Beta("0.0337976811443+42.932375488*@0+57573.6211786*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_400_Beta("1375.53644797+7436.54556229*@0+3077211.32147*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_500_Beta("874.770804121+20719.6927832*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_700_Beta("288.318966944+19708.0845495*@0+1.43218770177e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_1100_Beta("47.2201299608+4717.54533898*@0+1422900.33399*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_3500_Beta("0.0255889781331+35.0795925641*@0+41564.2369111*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_400_Beta("951.103063803+5.55111512313e-08*@0+31156.8117743*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_500_Beta("602.989581246+0.0*@0+2360667.97631*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_700_Beta("227.803145954+0.0*@0+4061404.27593*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_1100_Beta("44.7843443612+4972.50818726*@0+1334428.59512*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_3500_Beta("0.0443803921411+52.683251428*@0+88320.8791969*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_400_Beta("1048.67809832+1.11022302463e-07*@0+6357908.28564*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_500_Beta("626.3768923+20214.8977391*@0+1.57651669497e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_700_Beta("217.188662581+6930.60330698*@0+1999408.76354*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_1100_Beta("33.9396802968+4277.0067219*@0+0.000610234085485*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_3500_Beta("0.0157508060805+3.46663964201*@0+23638.0915009*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_400_Beta("913.081961998+2977.13378672*@0+0.00580296921626*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_500_Beta("578.528584794+4.4408920985e-07*@0+4125624.18528*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_700_Beta("211.889988504+0.0*@0+3443942.43321*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_1100_Beta("42.5802439657+4218.04319506*@0+1305841.36237*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_3500_Beta("0.0506456126556+64.3337676465*@0+86273.6748942*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_400_Beta("2061.23179423+11143.4603629*@0+4611210.44785*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_500_Beta("1310.83791924+31048.2975958*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_700_Beta("432.043918176+29532.420782*@0+2.99760216649e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_1100_Beta("70.7590253066+7069.21520266*@0+2132205.0055*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_3500_Beta("0.0383054213701+52.4482597908*@0+62360.5377272*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_400_Beta("369.17978808+1735.79582036*@0+295192.737193*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_500_Beta("221.402682855+0.0*@0+535864.848927*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_700_Beta("88.6522726731+0.0*@0+877476.120303*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_1100_Beta("16.7223362607+556.525096507*@0+638495.772522*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_3500_Beta("0.025782210573+20.756864727*@0+39734.1189368*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_400_Beta("210.753109974+1984.15617858*@0+153686.141287*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_500_Beta("121.130251377+0.0*@0+236628.55327*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_700_Beta("38.9955839703+1342.20181824*@0+312247.417109*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_1100_Beta("5.7120874187+215.791622016*@0+166108.849449*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_3500_Beta("0.00391969813054+5.72877473237*@0+3568.79601493*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_400_Beta("345.750630251+369.680508538*@0+133913.929463*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_500_Beta("208.865215413+3647.81409895*@0+226201.469379*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_700_Beta("79.1139882137+1796.9327169*@0+363463.168196*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_1100_Beta("14.6807824347+989.279572206*@0+465931.505226*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_3500_Beta("0.0176140079105+28.4856769284*@0+42170.7278975*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_400_Beta("527.95208766+6578.2767229*@0+175370.351365*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_500_Beta("311.028310826+1619.75029017*@0+306727.671566*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_700_Beta("91.9210157713+2591.20899637*@0+393894.930821*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_1100_Beta("14.132562178+802.689454238*@0+333102.376164*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_3500_Beta("0.0133580158966+9.61966883928*@0+16258.9490991*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_400_Beta("531.525139909+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_500_Beta("322.258236402+0.0*@0+1205014.09751*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_700_Beta("110.095889491+8069.36796133*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_1100_Beta("20.6253691564+1222.48163614*@0+603710.739249*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_3500_Beta("0.0171738863748+11.1115699419*@0+31760.3473735*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_400_Beta("311.469888705+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_500_Beta("180.71691454+645.826536638*@0+7.9936057773e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_700_Beta("54.575063499+1074.12365091*@0+8.881784197e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_1100_Beta("6.87172982816+688.109520863*@0+32234.6281109*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_3500_Beta("0.00249148446772+0.0*@0+5749.87044505*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_400_Beta("495.313707253+0.0*@0+1438823.16823*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_500_Beta("319.192747474+0.0*@0+1623926.06658*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_700_Beta("112.772492906+1287.69040858*@0+838089.152361*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_1100_Beta("20.8471966892+1540.5745159*@0+572918.9718*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_3500_Beta("0.0237082665004+8.39337999103*@0+38641.7456343*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_400_Beta("781.885660267+0.0*@0+0.000135336186702*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_500_Beta("433.146444676+7499.7531298*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_700_Beta("143.63648377+1075.38736188*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_1100_Beta("19.6498914003+0.0*@0+646387.481805*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_3500_Beta("0.00723700603231+0.0*@0+20031.8724045*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_400_Beta("773.462302664+0.0*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_500_Beta("469.84289267+0.0*@0+1840874.02172*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_700_Beta("159.104387103+9617.80018971*@0+682396.823356*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_1100_Beta("29.7085504762+3734.89458722*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_3500_Beta("0.0243402809376+20.9786339966*@0+44581.4575861*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_400_Beta("449.455262347+5.55111512313e-08*@0+2.22044604925e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_500_Beta("256.916343722+1596.08719341*@0+5.05151476204e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_700_Beta("80.1072764238+588.08815373*@0+0.00611360961855*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_1100_Beta("10.059549418+813.363416563*@0+105416.997366*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_3500_Beta("0.00366729406013+0.0*@0+8164.83739036*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_400_Beta("742.224096347+1.66533453694e-07*@0+2156066.05434*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_500_Beta("478.308050663+0.0*@0+2433450.45326*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_700_Beta("168.988756126+1929.61737217*@0+1255868.51495*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_1100_Beta("31.2393769261+2308.54223254*@0+858514.507513*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_3500_Beta("0.0355380729277+12.4104029275*@0+57991.5778972*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_400_Beta("1171.65012343+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_500_Beta("649.066899841+11238.3247365*@0+5.55111512313e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_700_Beta("215.238250212+1611.45756122*@0+6.66133814775e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_1100_Beta("29.4452238497+0.0*@0+968607.049173*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_3500_Beta("0.0108446038509+0.0*@0+30017.6221905*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "cspos_dielectron_2016_BB_400":
            print "cspos_dielectron_2016_BB_400 ConRR"
            return 'calccspos_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_500":
            print "cspos_dielectron_2016_BB_500 ConRR"
            return 'calccspos_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_700":
            print "cspos_dielectron_2016_BB_700 ConRR"
            return 'calccspos_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_1100":
            print "cspos_dielectron_2016_BB_1100 ConRR"
            return 'calccspos_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_3500":
            print "cspos_dielectron_2016_BB_3500 ConRR"
            return 'calccspos_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_400":
            print "cspos_dielectron_2016_BE_400 ConRR"
            return 'calccspos_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_500":
            print "cspos_dielectron_2016_BE_500 ConRR"
            return 'calccspos_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_700":
            print "cspos_dielectron_2016_BE_700 ConRR"
            return 'calccspos_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_1100":
            print "cspos_dielectron_2016_BE_1100 ConRR"
            return 'calccspos_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_3500":
            print "cspos_dielectron_2016_BE_3500 ConRR"
            return 'calccspos_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_400":
            print "cspos_dimuon_2016_BB_400 ConRR"
            return 'calccspos_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_500":
            print "cspos_dimuon_2016_BB_500 ConRR"
            return 'calccspos_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_700":
            print "cspos_dimuon_2016_BB_700 ConRR"
            return 'calccspos_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_1100":
            print "cspos_dimuon_2016_BB_1100 ConRR"
            return 'calccspos_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_3500":
            print "cspos_dimuon_2016_BB_3500 ConRR"
            return 'calccspos_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_400":
            print "cspos_dimuon_2016_BE_400 ConRR"
            return 'calccspos_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_500":
            print "cspos_dimuon_2016_BE_500 ConRR"
            return 'calccspos_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_700":
            print "cspos_dimuon_2016_BE_700 ConRR"
            return 'calccspos_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_1100":
            print "cspos_dimuon_2016_BE_1100 ConRR"
            return 'calccspos_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_3500":
            print "cspos_dimuon_2016_BE_3500 ConRR"
            return 'calccspos_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_400":
            print "cspos_dielectron_2017_BB_400 ConRR"
            return 'calccspos_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_500":
            print "cspos_dielectron_2017_BB_500 ConRR"
            return 'calccspos_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_700":
            print "cspos_dielectron_2017_BB_700 ConRR"
            return 'calccspos_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_1100":
            print "cspos_dielectron_2017_BB_1100 ConRR"
            return 'calccspos_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_3500":
            print "cspos_dielectron_2017_BB_3500 ConRR"
            return 'calccspos_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_400":
            print "cspos_dielectron_2017_BE_400 ConRR"
            return 'calccspos_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_500":
            print "cspos_dielectron_2017_BE_500 ConRR"
            return 'calccspos_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_700":
            print "cspos_dielectron_2017_BE_700 ConRR"
            return 'calccspos_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_1100":
            print "cspos_dielectron_2017_BE_1100 ConRR"
            return 'calccspos_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_3500":
            print "cspos_dielectron_2017_BE_3500 ConRR"
            return 'calccspos_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_400":
            print "cspos_dimuon_2017_BB_400 ConRR"
            return 'calccspos_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_500":
            print "cspos_dimuon_2017_BB_500 ConRR"
            return 'calccspos_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_700":
            print "cspos_dimuon_2017_BB_700 ConRR"
            return 'calccspos_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_1100":
            print "cspos_dimuon_2017_BB_1100 ConRR"
            return 'calccspos_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_3500":
            print "cspos_dimuon_2017_BB_3500 ConRR"
            return 'calccspos_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_400":
            print "cspos_dimuon_2017_BE_400 ConRR"
            return 'calccspos_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_500":
            print "cspos_dimuon_2017_BE_500 ConRR"
            return 'calccspos_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_700":
            print "cspos_dimuon_2017_BE_700 ConRR"
            return 'calccspos_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_1100":
            print "cspos_dimuon_2017_BE_1100 ConRR"
            return 'calccspos_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_3500":
            print "cspos_dimuon_2017_BE_3500 ConRR"
            return 'calccspos_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_400":
            print "cspos_dielectron_2018_BB_400 ConRR"
            return 'calccspos_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_500":
            print "cspos_dielectron_2018_BB_500 ConRR"
            return 'calccspos_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_700":
            print "cspos_dielectron_2018_BB_700 ConRR"
            return 'calccspos_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_1100":
            print "cspos_dielectron_2018_BB_1100 ConRR"
            return 'calccspos_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_3500":
            print "cspos_dielectron_2018_BB_3500 ConRR"
            return 'calccspos_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_400":
            print "cspos_dielectron_2018_BE_400 ConRR"
            return 'calccspos_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_500":
            print "cspos_dielectron_2018_BE_500 ConRR"
            return 'calccspos_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_700":
            print "cspos_dielectron_2018_BE_700 ConRR"
            return 'calccspos_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_1100":
            print "cspos_dielectron_2018_BE_1100 ConRR"
            return 'calccspos_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_3500":
            print "cspos_dielectron_2018_BE_3500 ConRR"
            return 'calccspos_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_400":
            print "cspos_dimuon_2018_BB_400 ConRR"
            return 'calccspos_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_500":
            print "cspos_dimuon_2018_BB_500 ConRR"
            return 'calccspos_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_700":
            print "cspos_dimuon_2018_BB_700 ConRR"
            return 'calccspos_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_1100":
            print "cspos_dimuon_2018_BB_1100 ConRR"
            return 'calccspos_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_3500":
            print "cspos_dimuon_2018_BB_3500 ConRR"
            return 'calccspos_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_400":
            print "cspos_dimuon_2018_BE_400 ConRR"
            return 'calccspos_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_500":
            print "cspos_dimuon_2018_BE_500 ConRR"
            return 'calccspos_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_700":
            print "cspos_dimuon_2018_BE_700 ConRR"
            return 'calccspos_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_1100":
            print "cspos_dimuon_2018_BE_1100 ConRR"
            return 'calccspos_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_3500":
            print "cspos_dimuon_2018_BE_3500 ConRR"
            return 'calccspos_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_400":
            print "csneg_dielectron_2016_BB_400 ConRR"
            return 'calccsneg_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_500":
            print "csneg_dielectron_2016_BB_500 ConRR"
            return 'calccsneg_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_700":
            print "csneg_dielectron_2016_BB_700 ConRR"
            return 'calccsneg_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_1100":
            print "csneg_dielectron_2016_BB_1100 ConRR"
            return 'calccsneg_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_3500":
            print "csneg_dielectron_2016_BB_3500 ConRR"
            return 'calccsneg_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_400":
            print "csneg_dielectron_2016_BE_400 ConRR"
            return 'calccsneg_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_500":
            print "csneg_dielectron_2016_BE_500 ConRR"
            return 'calccsneg_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_700":
            print "csneg_dielectron_2016_BE_700 ConRR"
            return 'calccsneg_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_1100":
            print "csneg_dielectron_2016_BE_1100 ConRR"
            return 'calccsneg_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_3500":
            print "csneg_dielectron_2016_BE_3500 ConRR"
            return 'calccsneg_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_400":
            print "csneg_dimuon_2016_BB_400 ConRR"
            return 'calccsneg_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_500":
            print "csneg_dimuon_2016_BB_500 ConRR"
            return 'calccsneg_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_700":
            print "csneg_dimuon_2016_BB_700 ConRR"
            return 'calccsneg_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_1100":
            print "csneg_dimuon_2016_BB_1100 ConRR"
            return 'calccsneg_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_3500":
            print "csneg_dimuon_2016_BB_3500 ConRR"
            return 'calccsneg_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_400":
            print "csneg_dimuon_2016_BE_400 ConRR"
            return 'calccsneg_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_500":
            print "csneg_dimuon_2016_BE_500 ConRR"
            return 'calccsneg_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_700":
            print "csneg_dimuon_2016_BE_700 ConRR"
            return 'calccsneg_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_1100":
            print "csneg_dimuon_2016_BE_1100 ConRR"
            return 'calccsneg_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_3500":
            print "csneg_dimuon_2016_BE_3500 ConRR"
            return 'calccsneg_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_400":
            print "csneg_dielectron_2017_BB_400 ConRR"
            return 'calccsneg_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_500":
            print "csneg_dielectron_2017_BB_500 ConRR"
            return 'calccsneg_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_700":
            print "csneg_dielectron_2017_BB_700 ConRR"
            return 'calccsneg_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_1100":
            print "csneg_dielectron_2017_BB_1100 ConRR"
            return 'calccsneg_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_3500":
            print "csneg_dielectron_2017_BB_3500 ConRR"
            return 'calccsneg_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_400":
            print "csneg_dielectron_2017_BE_400 ConRR"
            return 'calccsneg_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_500":
            print "csneg_dielectron_2017_BE_500 ConRR"
            return 'calccsneg_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_700":
            print "csneg_dielectron_2017_BE_700 ConRR"
            return 'calccsneg_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_1100":
            print "csneg_dielectron_2017_BE_1100 ConRR"
            return 'calccsneg_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_3500":
            print "csneg_dielectron_2017_BE_3500 ConRR"
            return 'calccsneg_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_400":
            print "csneg_dimuon_2017_BB_400 ConRR"
            return 'calccsneg_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_500":
            print "csneg_dimuon_2017_BB_500 ConRR"
            return 'calccsneg_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_700":
            print "csneg_dimuon_2017_BB_700 ConRR"
            return 'calccsneg_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_1100":
            print "csneg_dimuon_2017_BB_1100 ConRR"
            return 'calccsneg_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_3500":
            print "csneg_dimuon_2017_BB_3500 ConRR"
            return 'calccsneg_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_400":
            print "csneg_dimuon_2017_BE_400 ConRR"
            return 'calccsneg_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_500":
            print "csneg_dimuon_2017_BE_500 ConRR"
            return 'calccsneg_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_700":
            print "csneg_dimuon_2017_BE_700 ConRR"
            return 'calccsneg_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_1100":
            print "csneg_dimuon_2017_BE_1100 ConRR"
            return 'calccsneg_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_3500":
            print "csneg_dimuon_2017_BE_3500 ConRR"
            return 'calccsneg_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_400":
            print "csneg_dielectron_2018_BB_400 ConRR"
            return 'calccsneg_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_500":
            print "csneg_dielectron_2018_BB_500 ConRR"
            return 'calccsneg_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_700":
            print "csneg_dielectron_2018_BB_700 ConRR"
            return 'calccsneg_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_1100":
            print "csneg_dielectron_2018_BB_1100 ConRR"
            return 'calccsneg_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_3500":
            print "csneg_dielectron_2018_BB_3500 ConRR"
            return 'calccsneg_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_400":
            print "csneg_dielectron_2018_BE_400 ConRR"
            return 'calccsneg_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_500":
            print "csneg_dielectron_2018_BE_500 ConRR"
            return 'calccsneg_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_700":
            print "csneg_dielectron_2018_BE_700 ConRR"
            return 'calccsneg_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_1100":
            print "csneg_dielectron_2018_BE_1100 ConRR"
            return 'calccsneg_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_3500":
            print "csneg_dielectron_2018_BE_3500 ConRR"
            return 'calccsneg_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_400":
            print "csneg_dimuon_2018_BB_400 ConRR"
            return 'calccsneg_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_500":
            print "csneg_dimuon_2018_BB_500 ConRR"
            return 'calccsneg_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_700":
            print "csneg_dimuon_2018_BB_700 ConRR"
            return 'calccsneg_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_1100":
            print "csneg_dimuon_2018_BB_1100 ConRR"
            return 'calccsneg_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_3500":
            print "csneg_dimuon_2018_BB_3500 ConRR"
            return 'calccsneg_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_400":
            print "csneg_dimuon_2018_BE_400 ConRR"
            return 'calccsneg_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_500":
            print "csneg_dimuon_2018_BE_500 ConRR"
            return 'calccsneg_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_700":
            print "csneg_dimuon_2018_BE_700 ConRR"
            return 'calccsneg_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_1100":
            print "csneg_dimuon_2018_BE_1100 ConRR"
            return 'calccsneg_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_3500":
            print "csneg_dimuon_2018_BE_3500 ConRR"
            return 'calccsneg_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
