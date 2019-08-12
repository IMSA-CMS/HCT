
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #cspos_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_400_Beta("456.610041804+12006.9642801*@0+249119.156315*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_500_Beta("304.792023226+4834.36302401*@0+538405.885981*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_700_Beta("116.310362627+5744.45149432*@0+855581.401068*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_1100_Beta("24.5565177626+844.872115713*@0+619041.015813*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_3500_Beta("0.0274876062138+17.2683820021*@0+41418.3607603*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_400_Beta("469.291060956+6389.79780893*@0+158757.378644*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_500_Beta("290.943896966+3692.21182528*@0+236171.715751*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_700_Beta("100.424833184+4632.27100833*@0+293442.361545*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_1100_Beta("16.2562949407+512.453830481*@0+159447.061771*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_3500_Beta("0.00354775682905+7.82971371072*@0+2458.01173226*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_400_Beta("410.17990286+3390.12782158*@0+126705.45177*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_500_Beta("245.889099815+9184.75206979*@0+225209.786926*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_700_Beta("100.189239503+5181.33882915*@0+379477.885418*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_1100_Beta("18.3271367141+5312.54604497*@0+467415.135976*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_3500_Beta("0.0420412677418+24.107184915*@0+47085.0084689*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_400_Beta("988.745896432+2580.9604195*@0+182211.481625*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_500_Beta("595.984512289+11141.2479244*@0+278431.754638*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_700_Beta("197.310625676+12493.0507951*@0+371502.913072*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_1100_Beta("29.9000983879+7551.39526387*@0+316236.317585*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_3500_Beta("0.0423568437563+13.9877838201*@0+13417.3668847*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_400_Beta("642.789699977+3058.10048096*@0+4.99600361081e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_500_Beta("419.688982458+0.0*@0+72657.2424098*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_700_Beta("148.733202529+9562.06900998*@0+153492.913495*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_1100_Beta("30.2698626401+3707.45903383*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_3500_Beta("0.026071019618+13.5201102536*@0+34025.6461421*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_400_Beta("689.180306486+5485.03785691*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_500_Beta("436.348778278+1701.49765982*@0+2482454.89259*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_700_Beta("147.892307438+4417.08977844*@0+141219.974639*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_1100_Beta("23.1003960167+697.491348567*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_3500_Beta("0.00921327636576+0.0*@0+7046.77307506*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_400_Beta("612.54214984+0.0*@0+0.000302313729605*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_500_Beta("364.608908092+15034.5195308*@0+1105071.81942*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_700_Beta("141.65924415+0.0*@0+3371636.03889*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_1100_Beta("28.7342932104+1534.76579973*@0+2994767.99045*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_3500_Beta("0.0400503860628+24.8346647136*@0+30866.7162365*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_400_Beta("1400.22953605+2.22044604925e-07*@0+922225.155415*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_500_Beta("880.881078797+3770.56816947*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_700_Beta("294.832581382+0.0*@0+5219599.82289*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_1100_Beta("46.7718582368+0.0*@0+5081298.944*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_3500_Beta("0.033365304582+2.05438882572*@0+17457.7559607*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_400_Beta("931.765726617+740.264474719*@0+7.73270336651e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_500_Beta("607.591097441+0.0*@0+2424155.52499*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_700_Beta("221.413019864+0.0*@0+15130635.5692*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_1100_Beta("44.2789795277+5225.31399827*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_3500_Beta("0.0382249247098+18.0019899543*@0+49143.4266716*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_400_Beta("994.746881454+13414.6004657*@0+1.2490009027e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_500_Beta("633.177145985+120.523066471*@0+3833211.22888*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_700_Beta("212.313467969+0.0*@0+8969219.2012*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_1100_Beta("33.7379088733+1058.82337453*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_3500_Beta("0.0129310029987+0.0*@0+10330.6851711*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_400_Beta("917.89007956+5.55111512313e-08*@0+2.20379270388e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_500_Beta("546.36383448+22529.1981186*@0+1655925.85445*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_700_Beta("212.275380978+0.0*@0+5052374.42239*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_1100_Beta("43.0581365728+2299.83724015*@0+4487637.38457*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_3500_Beta("0.060015232968+37.2139994376*@0+46253.7444869*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_400_Beta("2098.23411108+1.66533453694e-07*@0+1381946.91225*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_500_Beta("1319.99401855+5650.19104515*@0+0.000134670052887*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_700_Beta("441.804567902+3.33066907388e-07*@0+7821530.75435*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_1100_Beta("70.0872990505+0.0*@0+7614289.80659*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_3500_Beta("0.0499977202382+3.07820369194*@0+26160.4380928*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_400_Beta("370.258933442+11174.7823562*@0+358516.205698*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_500_Beta("212.301470539+9581.93463063*@0+681207.423215*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_700_Beta("90.3082241613+5976.09780101*@0+1171928.45839*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_1100_Beta("17.7198220291+1502.71333832*@0+943410.687303*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_3500_Beta("0.0188657513963+15.5407711699*@0+67377.4931055*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_400_Beta("197.147654807+11594.3361795*@0+344304.216038*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_500_Beta("123.640679312+8550.95550489*@0+682658.135713*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_700_Beta("45.1940225932+3339.69720739*@0+1050151.33239*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_1100_Beta("6.31387440224+1462.94215153*@0+625061.906285*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_3500_Beta("0.00412536680936+1.60293661677*@0+14373.9732402*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_400_Beta("335.838194258+7052.76442647*@0+133522.102129*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_500_Beta("212.518343202+6917.15428563*@0+286056.107104*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_700_Beta("71.4212965785+10012.9066443*@0+499406.063164*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_1100_Beta("13.5281103457+7883.30779167*@0+658036.427519*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_3500_Beta("0.0320120529957+40.5493169042*@0+71660.5245294*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_400_Beta("555.333545469+3520.3727789*@0+332915.249808*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_500_Beta("286.879741118+26716.5267712*@0+614921.854129*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_700_Beta("89.3137820312+28610.5949057*@0+944766.967345*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_1100_Beta("12.9819455599+13736.2484697*@0+1021157.15181*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_3500_Beta("0.0515953685904+0.0*@0+50532.5767809*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_400_Beta("510.307979035+6477.71483592*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_500_Beta("325.789945827+0.0*@0+5358956.42302*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_700_Beta("114.796366164+7620.23616052*@0+928715.059119*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_1100_Beta("20.7539192937+5577.96097339*@0+217879.355306*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_3500_Beta("0.0126950980776+30.3514624544*@0+57215.7100088*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_400_Beta("316.360017737+12425.3144976*@0+5.66213742559e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_500_Beta("181.114589365+5.55111512313e-08*@0+3477841.86168*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_700_Beta("49.6303221995+6874.43152481*@0+1987865.17576*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_1100_Beta("6.67854044649+4575.22024877*@0+146959.109765*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_3500_Beta("0.00152346597336+8.17362261207*@0+14933.0396518*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_400_Beta("502.722043927+11073.8387153*@0+2130918.30219*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_500_Beta("313.439964118+11759.7276597*@0+8.62088178621e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_700_Beta("106.935833201+8546.37675102*@0+2346560.30847*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_1100_Beta("20.768063887+3302.11160227*@0+4706095.13456*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_3500_Beta("0.0452600428113+53.0356140116*@0+51626.8771577*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_400_Beta("737.409882742+17875.5902961*@0+2.22044604925e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_500_Beta("427.7199963+17425.9167757*@0+3866175.54327*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_700_Beta("141.340056616+0.0*@0+12771158.4394*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_1100_Beta("17.3078640231+0.0*@0+19371918.7171*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_3500_Beta("0.0608994206338+12.2994558427*@0+46358.7019907*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_400_Beta("9543.38208595+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_500_Beta("482.776435176+0.0*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_700_Beta("166.75305846+17368.6559704*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_1100_Beta("29.7741071671+8202.45268912*@0+341105.317604*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_3500_Beta("0.0186199334869+46.1518837591*@0+82371.4375162*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_400_Beta("461.908165699+16739.5172536*@0+0.000841660074968*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_500_Beta("259.448795249+1.11022302463e-07*@0+5266473.64165*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_700_Beta("72.1392780674+8660.35987024*@0+3358562.03071*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_1100_Beta("9.50511807688+7265.64385051*@0+69980.9724353*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_3500_Beta("0.00222482008713+11.5481983975*@0+21544.4444086*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_400_Beta("753.325417956+16594.0909343*@0+3193164.27008*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_500_Beta("469.687554998+17621.8888564*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_700_Beta("160.242595701+12806.6914329*@0+3516302.7903*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_1100_Beta("31.1207991283+4948.18613611*@0+7052051.05082*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_3500_Beta("0.0678218542757+79.4733022724*@0+77362.4849428*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_400_Beta("1105.00349017+26786.4538761*@0+3.99680288865e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_500_Beta("640.935386453+26112.5588228*@0+5793450.4056*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_700_Beta("211.7970845+0.0*@0+19137490.8974*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_1100_Beta("25.935711867+0.0*@0+29028683.8004*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_3500_Beta("0.0912573516294+18.4304347339*@0+69468.3343557*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "cspos_dielectron_2016_BB_400":
            print "cspos_dielectron_2016_BB_400 ConLR"
            return 'calccspos_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_500":
            print "cspos_dielectron_2016_BB_500 ConLR"
            return 'calccspos_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_700":
            print "cspos_dielectron_2016_BB_700 ConLR"
            return 'calccspos_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_1100":
            print "cspos_dielectron_2016_BB_1100 ConLR"
            return 'calccspos_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_3500":
            print "cspos_dielectron_2016_BB_3500 ConLR"
            return 'calccspos_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_400":
            print "cspos_dielectron_2016_BE_400 ConLR"
            return 'calccspos_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_500":
            print "cspos_dielectron_2016_BE_500 ConLR"
            return 'calccspos_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_700":
            print "cspos_dielectron_2016_BE_700 ConLR"
            return 'calccspos_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_1100":
            print "cspos_dielectron_2016_BE_1100 ConLR"
            return 'calccspos_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_3500":
            print "cspos_dielectron_2016_BE_3500 ConLR"
            return 'calccspos_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_400":
            print "cspos_dimuon_2016_BB_400 ConLR"
            return 'calccspos_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_500":
            print "cspos_dimuon_2016_BB_500 ConLR"
            return 'calccspos_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_700":
            print "cspos_dimuon_2016_BB_700 ConLR"
            return 'calccspos_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_1100":
            print "cspos_dimuon_2016_BB_1100 ConLR"
            return 'calccspos_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_3500":
            print "cspos_dimuon_2016_BB_3500 ConLR"
            return 'calccspos_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_400":
            print "cspos_dimuon_2016_BE_400 ConLR"
            return 'calccspos_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_500":
            print "cspos_dimuon_2016_BE_500 ConLR"
            return 'calccspos_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_700":
            print "cspos_dimuon_2016_BE_700 ConLR"
            return 'calccspos_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_1100":
            print "cspos_dimuon_2016_BE_1100 ConLR"
            return 'calccspos_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_3500":
            print "cspos_dimuon_2016_BE_3500 ConLR"
            return 'calccspos_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_400":
            print "cspos_dielectron_2017_BB_400 ConLR"
            return 'calccspos_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_500":
            print "cspos_dielectron_2017_BB_500 ConLR"
            return 'calccspos_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_700":
            print "cspos_dielectron_2017_BB_700 ConLR"
            return 'calccspos_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_1100":
            print "cspos_dielectron_2017_BB_1100 ConLR"
            return 'calccspos_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_3500":
            print "cspos_dielectron_2017_BB_3500 ConLR"
            return 'calccspos_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_400":
            print "cspos_dielectron_2017_BE_400 ConLR"
            return 'calccspos_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_500":
            print "cspos_dielectron_2017_BE_500 ConLR"
            return 'calccspos_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_700":
            print "cspos_dielectron_2017_BE_700 ConLR"
            return 'calccspos_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_1100":
            print "cspos_dielectron_2017_BE_1100 ConLR"
            return 'calccspos_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_3500":
            print "cspos_dielectron_2017_BE_3500 ConLR"
            return 'calccspos_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_400":
            print "cspos_dimuon_2017_BB_400 ConLR"
            return 'calccspos_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_500":
            print "cspos_dimuon_2017_BB_500 ConLR"
            return 'calccspos_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_700":
            print "cspos_dimuon_2017_BB_700 ConLR"
            return 'calccspos_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_1100":
            print "cspos_dimuon_2017_BB_1100 ConLR"
            return 'calccspos_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_3500":
            print "cspos_dimuon_2017_BB_3500 ConLR"
            return 'calccspos_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_400":
            print "cspos_dimuon_2017_BE_400 ConLR"
            return 'calccspos_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_500":
            print "cspos_dimuon_2017_BE_500 ConLR"
            return 'calccspos_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_700":
            print "cspos_dimuon_2017_BE_700 ConLR"
            return 'calccspos_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_1100":
            print "cspos_dimuon_2017_BE_1100 ConLR"
            return 'calccspos_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_3500":
            print "cspos_dimuon_2017_BE_3500 ConLR"
            return 'calccspos_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_400":
            print "cspos_dielectron_2018_BB_400 ConLR"
            return 'calccspos_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_500":
            print "cspos_dielectron_2018_BB_500 ConLR"
            return 'calccspos_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_700":
            print "cspos_dielectron_2018_BB_700 ConLR"
            return 'calccspos_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_1100":
            print "cspos_dielectron_2018_BB_1100 ConLR"
            return 'calccspos_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_3500":
            print "cspos_dielectron_2018_BB_3500 ConLR"
            return 'calccspos_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_400":
            print "cspos_dielectron_2018_BE_400 ConLR"
            return 'calccspos_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_500":
            print "cspos_dielectron_2018_BE_500 ConLR"
            return 'calccspos_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_700":
            print "cspos_dielectron_2018_BE_700 ConLR"
            return 'calccspos_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_1100":
            print "cspos_dielectron_2018_BE_1100 ConLR"
            return 'calccspos_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_3500":
            print "cspos_dielectron_2018_BE_3500 ConLR"
            return 'calccspos_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_400":
            print "cspos_dimuon_2018_BB_400 ConLR"
            return 'calccspos_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_500":
            print "cspos_dimuon_2018_BB_500 ConLR"
            return 'calccspos_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_700":
            print "cspos_dimuon_2018_BB_700 ConLR"
            return 'calccspos_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_1100":
            print "cspos_dimuon_2018_BB_1100 ConLR"
            return 'calccspos_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_3500":
            print "cspos_dimuon_2018_BB_3500 ConLR"
            return 'calccspos_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_400":
            print "cspos_dimuon_2018_BE_400 ConLR"
            return 'calccspos_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_500":
            print "cspos_dimuon_2018_BE_500 ConLR"
            return 'calccspos_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_700":
            print "cspos_dimuon_2018_BE_700 ConLR"
            return 'calccspos_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_1100":
            print "cspos_dimuon_2018_BE_1100 ConLR"
            return 'calccspos_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_3500":
            print "cspos_dimuon_2018_BE_3500 ConLR"
            return 'calccspos_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_400":
            print "csneg_dielectron_2016_BB_400 ConLR"
            return 'calccsneg_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_500":
            print "csneg_dielectron_2016_BB_500 ConLR"
            return 'calccsneg_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_700":
            print "csneg_dielectron_2016_BB_700 ConLR"
            return 'calccsneg_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_1100":
            print "csneg_dielectron_2016_BB_1100 ConLR"
            return 'calccsneg_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_3500":
            print "csneg_dielectron_2016_BB_3500 ConLR"
            return 'calccsneg_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_400":
            print "csneg_dielectron_2016_BE_400 ConLR"
            return 'calccsneg_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_500":
            print "csneg_dielectron_2016_BE_500 ConLR"
            return 'calccsneg_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_700":
            print "csneg_dielectron_2016_BE_700 ConLR"
            return 'calccsneg_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_1100":
            print "csneg_dielectron_2016_BE_1100 ConLR"
            return 'calccsneg_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_3500":
            print "csneg_dielectron_2016_BE_3500 ConLR"
            return 'calccsneg_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_400":
            print "csneg_dimuon_2016_BB_400 ConLR"
            return 'calccsneg_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_500":
            print "csneg_dimuon_2016_BB_500 ConLR"
            return 'calccsneg_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_700":
            print "csneg_dimuon_2016_BB_700 ConLR"
            return 'calccsneg_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_1100":
            print "csneg_dimuon_2016_BB_1100 ConLR"
            return 'calccsneg_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_3500":
            print "csneg_dimuon_2016_BB_3500 ConLR"
            return 'calccsneg_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_400":
            print "csneg_dimuon_2016_BE_400 ConLR"
            return 'calccsneg_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_500":
            print "csneg_dimuon_2016_BE_500 ConLR"
            return 'calccsneg_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_700":
            print "csneg_dimuon_2016_BE_700 ConLR"
            return 'calccsneg_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_1100":
            print "csneg_dimuon_2016_BE_1100 ConLR"
            return 'calccsneg_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_3500":
            print "csneg_dimuon_2016_BE_3500 ConLR"
            return 'calccsneg_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_400":
            print "csneg_dielectron_2017_BB_400 ConLR"
            return 'calccsneg_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_500":
            print "csneg_dielectron_2017_BB_500 ConLR"
            return 'calccsneg_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_700":
            print "csneg_dielectron_2017_BB_700 ConLR"
            return 'calccsneg_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_1100":
            print "csneg_dielectron_2017_BB_1100 ConLR"
            return 'calccsneg_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_3500":
            print "csneg_dielectron_2017_BB_3500 ConLR"
            return 'calccsneg_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_400":
            print "csneg_dielectron_2017_BE_400 ConLR"
            return 'calccsneg_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_500":
            print "csneg_dielectron_2017_BE_500 ConLR"
            return 'calccsneg_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_700":
            print "csneg_dielectron_2017_BE_700 ConLR"
            return 'calccsneg_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_1100":
            print "csneg_dielectron_2017_BE_1100 ConLR"
            return 'calccsneg_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_3500":
            print "csneg_dielectron_2017_BE_3500 ConLR"
            return 'calccsneg_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_400":
            print "csneg_dimuon_2017_BB_400 ConLR"
            return 'calccsneg_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_500":
            print "csneg_dimuon_2017_BB_500 ConLR"
            return 'calccsneg_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_700":
            print "csneg_dimuon_2017_BB_700 ConLR"
            return 'calccsneg_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_1100":
            print "csneg_dimuon_2017_BB_1100 ConLR"
            return 'calccsneg_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_3500":
            print "csneg_dimuon_2017_BB_3500 ConLR"
            return 'calccsneg_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_400":
            print "csneg_dimuon_2017_BE_400 ConLR"
            return 'calccsneg_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_500":
            print "csneg_dimuon_2017_BE_500 ConLR"
            return 'calccsneg_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_700":
            print "csneg_dimuon_2017_BE_700 ConLR"
            return 'calccsneg_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_1100":
            print "csneg_dimuon_2017_BE_1100 ConLR"
            return 'calccsneg_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_3500":
            print "csneg_dimuon_2017_BE_3500 ConLR"
            return 'calccsneg_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_400":
            print "csneg_dielectron_2018_BB_400 ConLR"
            return 'calccsneg_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_500":
            print "csneg_dielectron_2018_BB_500 ConLR"
            return 'calccsneg_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_700":
            print "csneg_dielectron_2018_BB_700 ConLR"
            return 'calccsneg_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_1100":
            print "csneg_dielectron_2018_BB_1100 ConLR"
            return 'calccsneg_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_3500":
            print "csneg_dielectron_2018_BB_3500 ConLR"
            return 'calccsneg_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_400":
            print "csneg_dielectron_2018_BE_400 ConLR"
            return 'calccsneg_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_500":
            print "csneg_dielectron_2018_BE_500 ConLR"
            return 'calccsneg_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_700":
            print "csneg_dielectron_2018_BE_700 ConLR"
            return 'calccsneg_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_1100":
            print "csneg_dielectron_2018_BE_1100 ConLR"
            return 'calccsneg_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_3500":
            print "csneg_dielectron_2018_BE_3500 ConLR"
            return 'calccsneg_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_400":
            print "csneg_dimuon_2018_BB_400 ConLR"
            return 'calccsneg_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_500":
            print "csneg_dimuon_2018_BB_500 ConLR"
            return 'calccsneg_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_700":
            print "csneg_dimuon_2018_BB_700 ConLR"
            return 'calccsneg_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_1100":
            print "csneg_dimuon_2018_BB_1100 ConLR"
            return 'calccsneg_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_3500":
            print "csneg_dimuon_2018_BB_3500 ConLR"
            return 'calccsneg_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_400":
            print "csneg_dimuon_2018_BE_400 ConLR"
            return 'calccsneg_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_500":
            print "csneg_dimuon_2018_BE_500 ConLR"
            return 'calccsneg_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_700":
            print "csneg_dimuon_2018_BE_700 ConLR"
            return 'calccsneg_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_1100":
            print "csneg_dimuon_2018_BE_1100 ConLR"
            return 'calccsneg_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_3500":
            print "csneg_dimuon_2018_BE_3500 ConLR"
            return 'calccsneg_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
