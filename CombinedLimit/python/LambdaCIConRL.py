
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #cspos_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_400_Beta("461.478599964+6357.23358205*@0+253187.394349*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_500_Beta("306.957115427+5.55111512313e-08*@0+540866.606762*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_700_Beta("116.417999122+2722.60008094*@0+857871.329875*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_1100_Beta("23.9303340288+0.0*@0+625084.876337*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_3500_Beta("0.0266191799378+16.2219908062*@0+41510.4908177*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_400_Beta("471.876375524+3528.45888918*@0+160554.284187*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_500_Beta("291.926668336+1823.3769401*@0+236897.944026*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_700_Beta("100.72157638+3359.20429151*@0+294478.448085*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_1100_Beta("15.9843661985+306.044048659*@0+161116.503*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_3500_Beta("0.00355054875583+7.36099714516*@0+2481.78287937*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_400_Beta("410.718090389+4550.21174739*@0+126031.803201*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_500_Beta("246.585271343+9886.63502804*@0+225079.095681*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_700_Beta("100.947117576+5051.25188982*@0+380057.679198*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_1100_Beta("18.7511288505+4691.97767666*@0+467845.139361*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_3500_Beta("0.0386504795176+19.2585180026*@0+47348.2127498*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_400_Beta("989.057018657+4598.69563146*@0+178748.922036*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_500_Beta("595.889890752+10496.2946332*@0+278963.856275*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_700_Beta("197.357243461+11969.0361923*@0+373984.336897*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_1100_Beta("30.0438436542+7061.45740603*@0+316726.865799*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_3500_Beta("0.0325658030509+18.1068769978*@0+13061.0634773*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_400_Beta("642.659224368+96.6729253871*@0+3.53606033343e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_500_Beta("414.492301925+0.0*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_700_Beta("150.054866957+4773.92025078*@0+7.77156117238e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_1100_Beta("30.0776062219+1896.39450754*@0+147964.749099*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_3500_Beta("0.0276456196015+22.7647670159*@0+28644.0643675*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_400_Beta("689.47752663+3878.59664253*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_500_Beta("436.248719618+1249.52482394*@0+2013184.01001*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_700_Beta("149.016109944+2214.30802178*@0+1.03805852802e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_1100_Beta("22.9673269082+386.639005756*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_3500_Beta("0.0108958498307+0.0*@0+6352.68103727*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_400_Beta("614.239658712+0.0*@0+389743.979652*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_500_Beta("365.661672122+15828.7414194*@0+1252516.42822*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_700_Beta("142.748674909+0.0*@0+3277003.0713*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_1100_Beta("28.8738101075+2363.43694499*@0+2197761.06061*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_3500_Beta("0.039282267173+25.8326831037*@0+30623.5351697*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_400_Beta("1401.26659975+4.99600361081e-07*@0+1111688.1813*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_500_Beta("880.897450213+5174.7642989*@0+119843.892478*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_700_Beta("295.580097312+0.0*@0+4578251.84827*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_1100_Beta("47.4597177828+0.0*@0+4002206.3267*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_3500_Beta("0.0344800201753+14.8011306544*@0+13896.2687836*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_400_Beta("926.643881645+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_500_Beta("605.033884423+6.10622663544e-07*@0+973265.136204*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_700_Beta("220.325677225+0.0*@0+13260781.7132*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_1100_Beta("43.5500228775+3525.45527366*@0+26224.7929795*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_3500_Beta("0.039052305513+67.156541772*@0+12804.7865011*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_400_Beta("995.25661994+10973.9157903*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_500_Beta("632.651696132+2.05391259556e-06*@0+3101788.7507*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_700_Beta("212.268654467+0.0*@0+8062750.59193*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_1100_Beta("33.5857623039+618.110443773*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_3500_Beta("0.0155971654558+0.0*@0+9204.58115011*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_400_Beta("920.433745093+2.77555756156e-07*@0+584035.839716*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_500_Beta("547.941397062+23719.2740274*@0+1876879.52893*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_700_Beta("213.907881155+0.0*@0+4910564.88134*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_1100_Beta("43.2672001695+3541.5941852*@0+3293329.20367*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_3500_Beta("0.0588642012609+38.7100888566*@0+45889.1528532*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_400_Beta("2099.78813076+9.99200722163e-07*@0+1665853.45096*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_500_Beta("1320.01871946+7754.30176769*@0+179598.467422*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_700_Beta("442.924682755+0.0*@0+6860478.69091*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_1100_Beta("71.1180472714+0.0*@0+5997279.52514*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_3500_Beta("0.0516680665402+22.1789042132*@0+20823.6385558*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_400_Beta("375.242069709+4765.93563692*@0+362551.139873*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_500_Beta("218.358588363+2220.43218595*@0+685541.549119*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_700_Beta("91.6321444652+1191.62974993*@0+1174736.37461*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_1100_Beta("16.9991992672+295.046271359*@0+959315.688066*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_3500_Beta("0.0174616172558+14.5417302089*@0+67542.4155436*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_400_Beta("203.443413129+5322.9122437*@0+349035.989053*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_500_Beta("129.831394583+1460.99290738*@0+687913.807938*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_700_Beta("46.0232927612+285.393050969*@0+1053940.20102*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_1100_Beta("6.08982575985+554.242561623*@0+643385.589067*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_3500_Beta("0.00405233735354+1.28776334041*@0+14409.8351778*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_400_Beta("336.455721338+8087.97327384*@0+133235.88296*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_500_Beta("213.330772356+7535.60543643*@0+285833.02812*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_700_Beta("72.6101623083+9375.33780432*@0+500431.54714*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_1100_Beta("13.6658587878+7214.27021738*@0+658154.348698*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_3500_Beta("0.0294467900818+30.5233519016*@0+72072.6432961*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_400_Beta("554.80001824+4718.57337397*@0+332147.240404*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_500_Beta("286.467643959+27752.686269*@0+618679.069888*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_700_Beta("89.5809715307+26741.3530086*@0+943277.171359*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_1100_Beta("13.0224519592+13224.7363273*@0+1022751.88509*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_3500_Beta("0.0405528325468+0.0*@0+50586.5957623*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_400_Beta("510.012517999+3522.84956151*@0+1.89293025699e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_500_Beta("323.925954786+5.55111512313e-08*@0+4302930.6874*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_700_Beta("114.944663386+4677.28808096*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_1100_Beta("20.6238531101+2581.10609441*@0+555062.069938*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_3500_Beta("0.0108934752876+2.84823642449*@0+67803.8299294*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_400_Beta("316.667053594+9877.23623908*@0+9.85878045867e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_500_Beta("180.552113053+0.0*@0+2293649.72569*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_700_Beta("49.4458089878+7608.10872708*@0+6.58362253603e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_1100_Beta("6.73810672708+2427.77815151*@0+400608.166591*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_3500_Beta("0.00142531810696+0.0*@0+16518.7456695*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_400_Beta("503.611265617+12498.8687147*@0+2231816.99025*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_500_Beta("314.766720639+12861.0137782*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_700_Beta("107.476818486+9802.32638359*@0+1761141.89728*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_1100_Beta("20.8654932763+4572.90436684*@0+3268464.68621*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_3500_Beta("0.031213310856+0.0*@0+70073.209434*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_400_Beta("748.532973893+9780.50074063*@0+1616272.17494*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_500_Beta("428.404319865+24478.9904792*@0+2114278.25146*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_700_Beta("141.932141038+1462.05138513*@0+10556102.8254*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_1100_Beta("18.0201731227+0.0*@0+15826995.2729*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_3500_Beta("0.0344048822559+0.0*@0+42642.7546902*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_400_Beta("9544.1529201+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_500_Beta("478.280674008+0.0*@0+5.66213742559e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_700_Beta("168.859568568+7283.33607941*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_1100_Beta("29.5378803151+4019.36797978*@0+796719.669153*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_3500_Beta("0.0159651298689+5.47239531468*@0+97971.3014323*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_400_Beta("462.478227973+12933.5315647*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_500_Beta("258.547205059+0.0*@0+3632002.53848*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_700_Beta("71.6274405371+10072.4171347*@0+249353.821953*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_1100_Beta("9.54264817903+4037.85973568*@0+459950.336302*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_3500_Beta("0.00208334272076+0.0*@0+23997.6161041*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_400_Beta("754.657867795+18729.4536867*@0+3344375.18952*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_500_Beta("471.675700999+19272.1419879*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_700_Beta("161.053251359+14688.7164266*@0+2639058.77919*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_1100_Beta("31.2667939875+6852.46529519*@0+4897771.27376*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_3500_Beta("0.0467729261395+0.0*@0+105004.206602*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_400_Beta("1121.67134311+14656.0693619*@0+2421958.13599*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_500_Beta("641.960847359+36681.5001597*@0+3168261.30693*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_700_Beta("212.684297225+2190.92245091*@0+15818235.3851*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_1100_Beta("27.0031036549+0.0*@0+23716640.8488*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_3500_Beta("0.0515554725096+0.0*@0+63899.8659135*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "cspos_dielectron_2016_BB_400":
            print "cspos_dielectron_2016_BB_400 ConRL"
            return 'calccspos_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_500":
            print "cspos_dielectron_2016_BB_500 ConRL"
            return 'calccspos_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_700":
            print "cspos_dielectron_2016_BB_700 ConRL"
            return 'calccspos_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_1100":
            print "cspos_dielectron_2016_BB_1100 ConRL"
            return 'calccspos_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_3500":
            print "cspos_dielectron_2016_BB_3500 ConRL"
            return 'calccspos_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_400":
            print "cspos_dielectron_2016_BE_400 ConRL"
            return 'calccspos_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_500":
            print "cspos_dielectron_2016_BE_500 ConRL"
            return 'calccspos_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_700":
            print "cspos_dielectron_2016_BE_700 ConRL"
            return 'calccspos_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_1100":
            print "cspos_dielectron_2016_BE_1100 ConRL"
            return 'calccspos_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_3500":
            print "cspos_dielectron_2016_BE_3500 ConRL"
            return 'calccspos_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_400":
            print "cspos_dimuon_2016_BB_400 ConRL"
            return 'calccspos_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_500":
            print "cspos_dimuon_2016_BB_500 ConRL"
            return 'calccspos_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_700":
            print "cspos_dimuon_2016_BB_700 ConRL"
            return 'calccspos_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_1100":
            print "cspos_dimuon_2016_BB_1100 ConRL"
            return 'calccspos_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_3500":
            print "cspos_dimuon_2016_BB_3500 ConRL"
            return 'calccspos_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_400":
            print "cspos_dimuon_2016_BE_400 ConRL"
            return 'calccspos_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_500":
            print "cspos_dimuon_2016_BE_500 ConRL"
            return 'calccspos_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_700":
            print "cspos_dimuon_2016_BE_700 ConRL"
            return 'calccspos_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_1100":
            print "cspos_dimuon_2016_BE_1100 ConRL"
            return 'calccspos_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_3500":
            print "cspos_dimuon_2016_BE_3500 ConRL"
            return 'calccspos_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_400":
            print "cspos_dielectron_2017_BB_400 ConRL"
            return 'calccspos_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_500":
            print "cspos_dielectron_2017_BB_500 ConRL"
            return 'calccspos_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_700":
            print "cspos_dielectron_2017_BB_700 ConRL"
            return 'calccspos_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_1100":
            print "cspos_dielectron_2017_BB_1100 ConRL"
            return 'calccspos_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_3500":
            print "cspos_dielectron_2017_BB_3500 ConRL"
            return 'calccspos_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_400":
            print "cspos_dielectron_2017_BE_400 ConRL"
            return 'calccspos_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_500":
            print "cspos_dielectron_2017_BE_500 ConRL"
            return 'calccspos_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_700":
            print "cspos_dielectron_2017_BE_700 ConRL"
            return 'calccspos_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_1100":
            print "cspos_dielectron_2017_BE_1100 ConRL"
            return 'calccspos_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_3500":
            print "cspos_dielectron_2017_BE_3500 ConRL"
            return 'calccspos_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_400":
            print "cspos_dimuon_2017_BB_400 ConRL"
            return 'calccspos_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_500":
            print "cspos_dimuon_2017_BB_500 ConRL"
            return 'calccspos_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_700":
            print "cspos_dimuon_2017_BB_700 ConRL"
            return 'calccspos_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_1100":
            print "cspos_dimuon_2017_BB_1100 ConRL"
            return 'calccspos_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_3500":
            print "cspos_dimuon_2017_BB_3500 ConRL"
            return 'calccspos_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_400":
            print "cspos_dimuon_2017_BE_400 ConRL"
            return 'calccspos_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_500":
            print "cspos_dimuon_2017_BE_500 ConRL"
            return 'calccspos_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_700":
            print "cspos_dimuon_2017_BE_700 ConRL"
            return 'calccspos_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_1100":
            print "cspos_dimuon_2017_BE_1100 ConRL"
            return 'calccspos_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_3500":
            print "cspos_dimuon_2017_BE_3500 ConRL"
            return 'calccspos_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_400":
            print "cspos_dielectron_2018_BB_400 ConRL"
            return 'calccspos_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_500":
            print "cspos_dielectron_2018_BB_500 ConRL"
            return 'calccspos_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_700":
            print "cspos_dielectron_2018_BB_700 ConRL"
            return 'calccspos_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_1100":
            print "cspos_dielectron_2018_BB_1100 ConRL"
            return 'calccspos_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_3500":
            print "cspos_dielectron_2018_BB_3500 ConRL"
            return 'calccspos_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_400":
            print "cspos_dielectron_2018_BE_400 ConRL"
            return 'calccspos_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_500":
            print "cspos_dielectron_2018_BE_500 ConRL"
            return 'calccspos_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_700":
            print "cspos_dielectron_2018_BE_700 ConRL"
            return 'calccspos_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_1100":
            print "cspos_dielectron_2018_BE_1100 ConRL"
            return 'calccspos_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_3500":
            print "cspos_dielectron_2018_BE_3500 ConRL"
            return 'calccspos_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_400":
            print "cspos_dimuon_2018_BB_400 ConRL"
            return 'calccspos_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_500":
            print "cspos_dimuon_2018_BB_500 ConRL"
            return 'calccspos_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_700":
            print "cspos_dimuon_2018_BB_700 ConRL"
            return 'calccspos_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_1100":
            print "cspos_dimuon_2018_BB_1100 ConRL"
            return 'calccspos_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_3500":
            print "cspos_dimuon_2018_BB_3500 ConRL"
            return 'calccspos_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_400":
            print "cspos_dimuon_2018_BE_400 ConRL"
            return 'calccspos_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_500":
            print "cspos_dimuon_2018_BE_500 ConRL"
            return 'calccspos_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_700":
            print "cspos_dimuon_2018_BE_700 ConRL"
            return 'calccspos_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_1100":
            print "cspos_dimuon_2018_BE_1100 ConRL"
            return 'calccspos_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_3500":
            print "cspos_dimuon_2018_BE_3500 ConRL"
            return 'calccspos_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_400":
            print "csneg_dielectron_2016_BB_400 ConRL"
            return 'calccsneg_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_500":
            print "csneg_dielectron_2016_BB_500 ConRL"
            return 'calccsneg_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_700":
            print "csneg_dielectron_2016_BB_700 ConRL"
            return 'calccsneg_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_1100":
            print "csneg_dielectron_2016_BB_1100 ConRL"
            return 'calccsneg_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_3500":
            print "csneg_dielectron_2016_BB_3500 ConRL"
            return 'calccsneg_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_400":
            print "csneg_dielectron_2016_BE_400 ConRL"
            return 'calccsneg_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_500":
            print "csneg_dielectron_2016_BE_500 ConRL"
            return 'calccsneg_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_700":
            print "csneg_dielectron_2016_BE_700 ConRL"
            return 'calccsneg_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_1100":
            print "csneg_dielectron_2016_BE_1100 ConRL"
            return 'calccsneg_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_3500":
            print "csneg_dielectron_2016_BE_3500 ConRL"
            return 'calccsneg_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_400":
            print "csneg_dimuon_2016_BB_400 ConRL"
            return 'calccsneg_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_500":
            print "csneg_dimuon_2016_BB_500 ConRL"
            return 'calccsneg_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_700":
            print "csneg_dimuon_2016_BB_700 ConRL"
            return 'calccsneg_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_1100":
            print "csneg_dimuon_2016_BB_1100 ConRL"
            return 'calccsneg_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_3500":
            print "csneg_dimuon_2016_BB_3500 ConRL"
            return 'calccsneg_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_400":
            print "csneg_dimuon_2016_BE_400 ConRL"
            return 'calccsneg_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_500":
            print "csneg_dimuon_2016_BE_500 ConRL"
            return 'calccsneg_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_700":
            print "csneg_dimuon_2016_BE_700 ConRL"
            return 'calccsneg_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_1100":
            print "csneg_dimuon_2016_BE_1100 ConRL"
            return 'calccsneg_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_3500":
            print "csneg_dimuon_2016_BE_3500 ConRL"
            return 'calccsneg_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_400":
            print "csneg_dielectron_2017_BB_400 ConRL"
            return 'calccsneg_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_500":
            print "csneg_dielectron_2017_BB_500 ConRL"
            return 'calccsneg_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_700":
            print "csneg_dielectron_2017_BB_700 ConRL"
            return 'calccsneg_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_1100":
            print "csneg_dielectron_2017_BB_1100 ConRL"
            return 'calccsneg_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_3500":
            print "csneg_dielectron_2017_BB_3500 ConRL"
            return 'calccsneg_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_400":
            print "csneg_dielectron_2017_BE_400 ConRL"
            return 'calccsneg_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_500":
            print "csneg_dielectron_2017_BE_500 ConRL"
            return 'calccsneg_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_700":
            print "csneg_dielectron_2017_BE_700 ConRL"
            return 'calccsneg_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_1100":
            print "csneg_dielectron_2017_BE_1100 ConRL"
            return 'calccsneg_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_3500":
            print "csneg_dielectron_2017_BE_3500 ConRL"
            return 'calccsneg_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_400":
            print "csneg_dimuon_2017_BB_400 ConRL"
            return 'calccsneg_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_500":
            print "csneg_dimuon_2017_BB_500 ConRL"
            return 'calccsneg_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_700":
            print "csneg_dimuon_2017_BB_700 ConRL"
            return 'calccsneg_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_1100":
            print "csneg_dimuon_2017_BB_1100 ConRL"
            return 'calccsneg_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_3500":
            print "csneg_dimuon_2017_BB_3500 ConRL"
            return 'calccsneg_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_400":
            print "csneg_dimuon_2017_BE_400 ConRL"
            return 'calccsneg_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_500":
            print "csneg_dimuon_2017_BE_500 ConRL"
            return 'calccsneg_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_700":
            print "csneg_dimuon_2017_BE_700 ConRL"
            return 'calccsneg_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_1100":
            print "csneg_dimuon_2017_BE_1100 ConRL"
            return 'calccsneg_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_3500":
            print "csneg_dimuon_2017_BE_3500 ConRL"
            return 'calccsneg_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_400":
            print "csneg_dielectron_2018_BB_400 ConRL"
            return 'calccsneg_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_500":
            print "csneg_dielectron_2018_BB_500 ConRL"
            return 'calccsneg_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_700":
            print "csneg_dielectron_2018_BB_700 ConRL"
            return 'calccsneg_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_1100":
            print "csneg_dielectron_2018_BB_1100 ConRL"
            return 'calccsneg_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_3500":
            print "csneg_dielectron_2018_BB_3500 ConRL"
            return 'calccsneg_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_400":
            print "csneg_dielectron_2018_BE_400 ConRL"
            return 'calccsneg_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_500":
            print "csneg_dielectron_2018_BE_500 ConRL"
            return 'calccsneg_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_700":
            print "csneg_dielectron_2018_BE_700 ConRL"
            return 'calccsneg_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_1100":
            print "csneg_dielectron_2018_BE_1100 ConRL"
            return 'calccsneg_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_3500":
            print "csneg_dielectron_2018_BE_3500 ConRL"
            return 'calccsneg_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_400":
            print "csneg_dimuon_2018_BB_400 ConRL"
            return 'calccsneg_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_500":
            print "csneg_dimuon_2018_BB_500 ConRL"
            return 'calccsneg_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_700":
            print "csneg_dimuon_2018_BB_700 ConRL"
            return 'calccsneg_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_1100":
            print "csneg_dimuon_2018_BB_1100 ConRL"
            return 'calccsneg_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_3500":
            print "csneg_dimuon_2018_BB_3500 ConRL"
            return 'calccsneg_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_400":
            print "csneg_dimuon_2018_BE_400 ConRL"
            return 'calccsneg_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_500":
            print "csneg_dimuon_2018_BE_500 ConRL"
            return 'calccsneg_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_700":
            print "csneg_dimuon_2018_BE_700 ConRL"
            return 'calccsneg_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_1100":
            print "csneg_dimuon_2018_BE_1100 ConRL"
            return 'calccsneg_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_3500":
            print "csneg_dimuon_2018_BE_3500 ConRL"
            return 'calccsneg_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
