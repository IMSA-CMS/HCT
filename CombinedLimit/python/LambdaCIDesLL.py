
from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class CIlambda(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)

    def doParametersOfInterest(self):
        self.modelBuilder.doVar('Beta[0,0,1]')
        self.modelBuilder.doSet('POI','Beta')
        
        #cspos_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_400_Beta("463.748960779+-4211.32204625*@0+341547.172603*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_500_Beta("282.775758176+-63.3359313099*@0+703322.768695*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_700_Beta("111.625932091+-2014.5690355*@0+1131520.98141*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_1100_Beta("21.7726528153+-1335.75466742*@0+834694.235506*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BB_3500_Beta("0.0313944999485+-44.2433959489*@0+69993.9588777*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_400_Beta("465.717264893+-2501.50498707*@0+350364.483604*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_500_Beta("285.146961697+-11.3541531642*@0+623108.1121*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_700_Beta("102.272564709+-3591.58039521*@0+1023569.06593*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_1100_Beta("15.7916875659+-1647.99499582*@0+568171.17737*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2016_BE_3500_Beta("0.00448731062788+-7.59703036845*@0+14183.2794951*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_400_Beta("405.535553939+-2564.20556009*@0+139608.523579*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_500_Beta("244.957262906+-49.1753229031*@0+281253.98342*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_700_Beta("91.4217027886+-657.762448851*@0+488064.801762*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_1100_Beta("18.9334104662+-1087.56627071*@0+620210.651684*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BB_3500_Beta("0.041867132291+-41.5569897442*@0+72427.965299*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_400_Beta("995.952598375+-9954.88232084*@0+334920.042239*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_500_Beta("569.793546345+-33.899174756*@0+637062.197403*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_700_Beta("201.817723577+-8397.47601704*@0+994363.28729*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_1100_Beta("31.6501707271+-2993.2251024*@0+962434.81519*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2016_BE_3500_Beta("0.0281913833034+-31.2061954763*@0+46581.2971179*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_400_Beta("648.876315681+-10182.5269314*@0+994767.57771*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_500_Beta("400.248084784+-42.67841283*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_700_Beta("157.501653097+-5295.890937*@0+640720.42901*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_1100_Beta("30.3086268306+-1812.14490301*@0+775964.79078*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BB_3500_Beta("0.031064261809+-26.6741797801*@0+57850.4523247*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_400_Beta("692.683313157+-22421.3221271*@0+6685090.18394*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_500_Beta("413.523256354+-18.4980761763*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_700_Beta("145.941343668+-8963.26180879*@0+1986247.7314*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_1100_Beta("23.0934894845+-2568.48267796*@0+605623.707008*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2017_BE_3500_Beta("0.0101477486389+-12.2087860398*@0+15744.3503925*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_400_Beta("588.632945524+7006.78145146*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_500_Beta("381.538402362+-40.7397505738*@0+1.49880108324e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_700_Beta("156.302938879+-7792.55970712*@0+965336.96292*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_1100_Beta("28.9295177908+-1714.86868069*@0+797938.561976*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BB_3500_Beta("0.0336203910455+-31.140372236*@0+62337.0177051*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_400_Beta("1386.81121734+-3799.51880812*@0+1.12132525487e-05*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_500_Beta("851.156267965+-17.9506417526*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_700_Beta("285.731581596+-3534.03036174*@0+554722.719064*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_1100_Beta("46.7833073935+-3804.32207682*@0+1007201.05033*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2017_BE_3500_Beta("0.0233458478885+-22.0753738309*@0+40776.3288809*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_400_Beta("936.245721693+-1.67590916636e-07*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_500_Beta("586.864185877+-59.6488007517*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_700_Beta("229.899695112+-8498.40181557*@0+1195111.51589*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_1100_Beta("45.0691586696+-4985.41770217*@0+1718532.40859*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BB_3500_Beta("0.0443405365628+-37.2797941514*@0+82620.1373598*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_400_Beta("1013.40264102+-38476.781922*@0+12082136.931*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_500_Beta("600.214757143+-29.5821812092*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_700_Beta("390.207650115+-15226.8125555*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_1100_Beta("33.904597528+-4112.84737757*@0+977398.835321*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dielectron_2018_BE_3500_Beta("0.0143406169638+-19.1306754768*@0+24093.8646679*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_400_Beta("882.062295374+10499.6669883*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_500_Beta("571.732608249+-61.0488892402*@0+2.77555756156e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_700_Beta("234.218847707+-11677.0978006*@0+1446548.74456*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_1100_Beta("43.3506835154+-2569.72817372*@0+1195707.54222*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BB_3500_Beta("0.0503799192226+-46.6636247184*@0+93411.5798202*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_400_Beta("2078.12676481+-5693.55868827*@0+1.11022302463e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_500_Beta("1275.45165879+-26.8965901961*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_700_Beta("428.166791917+-5295.73005503*@0+831247.493728*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_1100_Beta("70.1044518893+-5700.74642558*@0+1509282.89367*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #cspos_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccspos_dimuon_2018_BE_3500_Beta("0.0349835838557+-33.0797791743*@0+61103.0361444*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_400_Beta("356.738722025+-387.830754194*@0+281811.760251*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_500_Beta("219.61450815+-48.1338217744*@0+536076.11065*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_700_Beta("86.7490513432+-2687.63862896*@0+840269.698008*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_1100_Beta("15.4965574178+-633.726000646*@0+556147.42717*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BB_3500_Beta("0.0216295888344+-35.8982234439*@0+45188.4623487*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_400_Beta("212.142908002+-1535.4853038*@0+176097.347419*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_500_Beta("117.104901599+-5.36084346327*@0+234123.915291*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_700_Beta("39.2972780626+-924.208242416*@0+319547.153262*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_1100_Beta("5.57913747098+-252.883656592*@0+156084.401837*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2016_BE_3500_Beta("3.4367984758e-06+-3.64445931702*@0+4770.39690755*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_400_Beta("350.580240437+-1922.81845245*@0+131597.852242*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_500_Beta("201.985968888+-31.388871841*@0+217845.916674*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_700_Beta("75.2299946316+-593.365029872*@0+379291.076851*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_1100_Beta("14.5185913168+-686.902707724*@0+453603.931473*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BB_3500_Beta("0.031358222519+-24.2166792101*@0+43323.6715927*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_400_Beta("533.686458086+-2533.4476804*@0+160367.18775*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_500_Beta("299.128000753+-11.1843508354*@0+299155.357067*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_700_Beta("95.8708596777+-2124.35080667*@0+373313.105289*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_1100_Beta("14.1762920213+-721.109273984*@0+332576.332386*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2016_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2016_BE_3500_Beta("0.0127694084704+-7.97135539129*@0+16093.4235832*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_400_Beta("509.960068719+-4.53307011451e-07*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_500_Beta("316.309290513+-1397.12749683*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_700_Beta("118.091099206+-13960.1378222*@0+3600718.20413*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_1100_Beta("21.0515207787+-1823.96765541*@0+693175.99889*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BB_3500_Beta("0.0142777213305+3.00514361714*@0+34320.2526646*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_400_Beta("320.446175332+-3228.64107301*@0+1002178.66433*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_500_Beta("188.351030003+-19874.4358543*@0+4099311.14149*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_700_Beta("52.1152689005+-5.58922136449e-08*@0+27369.3448662*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_1100_Beta("7.05323733019+-237.741294701*@0+104706.119179*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2017_BE_3500_Beta("0.00279810023745+4.63475003419*@0+6683.30292969*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_400_Beta("506.292744119+-8545.30400071*@0+2152204.21103*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_500_Beta("304.388187749+5346.51123927*@0+165582.768898*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_700_Beta("112.00942432+-4051.93316349*@0+1302250.05914*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_1100_Beta("20.1912171736+-6.04577917991e-08*@0+374206.089104*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BB_3500_Beta("0.0206286593457+-1.2514969909*@0+38234.4503092*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_400_Beta("765.537991532+-7051.15040015*@0+3220908.28796*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_500_Beta("444.727109443+-6843.13370984*@0+5.55111512313e-08*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_700_Beta("136.236432508+-5.57459632984e-08*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_1100_Beta("18.072913484+-206.762341917*@0+219856.188841*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2017_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2017_BE_3500_Beta("0.0108839465105+5.21398945044*@0+20297.7619418*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_400_Beta("744.615145449+-1.07600682828e-06*@0+0.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_500_Beta("464.681684279+-6755.81154832*@0+3.21964677141e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_700_Beta("160.171451341+-2.20858722725e-07*@0+636931.351339*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_1100_Beta("29.1026180343+-1924.87329046*@0+1592921.68169*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BB_3500_Beta("0.0200917704009+3.23620179198*@0+50706.6638071*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_400_Beta("475.228931946+-12907.670522*@0+2487977.76627*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_500_Beta("12883.8621934+-7944344.14327*@0+1000000000.0*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_700_Beta("75.2568606441+-5.66745325702e-08*@0+0.00133626443244*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_1100_Beta("10.2521813998+-429.401047762*@0+229311.13462*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dielectron_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dielectron_2018_BE_3500_Beta("0.00393768982884+7.25778049754*@0+9714.14419282*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_400_Beta("758.676152144+-12805.0963348*@0+3225065.72953*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_500_Beta("456.123541894+8011.70194973*@0+248123.583244*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_700_Beta("167.845335514+-6071.80789639*@0+1951415.31773*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_1100_Beta("31.9953510968+-3013.92295648*@0+1243797.76449*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BB_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BB_3500_Beta("0.0309119030656+-1.87535845878*@0+57294.0538781*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_400
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_400_Beta("1147.15319962+-10566.0980638*@0+4826505.16965*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_500_Beta("666.420471887+-10254.3989929*@0+4.16333634234e-06*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_700
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_700_Beta("204.149334389+-5.57104763163e-08*@0+3.33066907388e-07*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_1100
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_1100_Beta("27.0821314862+-309.828660047*@0+329452.226072*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        #csneg_dimuon_2018_BE_3500
        self.modelBuilder.factory_('expr::calccsneg_dimuon_2018_BE_3500_Beta("0.0163095168054+7.81312612707*@0+30416.0532175*@0*@0+0.0*@0*@0*@0*@0",Beta)')
      
        self.modelBuilder.out.Print()

    def getYieldScale(self,bin,process):
        print bin, process
        
        if bin == "cspos_dielectron_2016_BB_400":
            print "cspos_dielectron_2016_BB_400 DesLL"
            return 'calccspos_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_500":
            print "cspos_dielectron_2016_BB_500 DesLL"
            return 'calccspos_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_700":
            print "cspos_dielectron_2016_BB_700 DesLL"
            return 'calccspos_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_1100":
            print "cspos_dielectron_2016_BB_1100 DesLL"
            return 'calccspos_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BB_3500":
            print "cspos_dielectron_2016_BB_3500 DesLL"
            return 'calccspos_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_400":
            print "cspos_dielectron_2016_BE_400 DesLL"
            return 'calccspos_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_500":
            print "cspos_dielectron_2016_BE_500 DesLL"
            return 'calccspos_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_700":
            print "cspos_dielectron_2016_BE_700 DesLL"
            return 'calccspos_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_1100":
            print "cspos_dielectron_2016_BE_1100 DesLL"
            return 'calccspos_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2016_BE_3500":
            print "cspos_dielectron_2016_BE_3500 DesLL"
            return 'calccspos_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_400":
            print "cspos_dimuon_2016_BB_400 DesLL"
            return 'calccspos_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_500":
            print "cspos_dimuon_2016_BB_500 DesLL"
            return 'calccspos_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_700":
            print "cspos_dimuon_2016_BB_700 DesLL"
            return 'calccspos_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_1100":
            print "cspos_dimuon_2016_BB_1100 DesLL"
            return 'calccspos_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BB_3500":
            print "cspos_dimuon_2016_BB_3500 DesLL"
            return 'calccspos_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_400":
            print "cspos_dimuon_2016_BE_400 DesLL"
            return 'calccspos_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_500":
            print "cspos_dimuon_2016_BE_500 DesLL"
            return 'calccspos_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_700":
            print "cspos_dimuon_2016_BE_700 DesLL"
            return 'calccspos_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_1100":
            print "cspos_dimuon_2016_BE_1100 DesLL"
            return 'calccspos_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2016_BE_3500":
            print "cspos_dimuon_2016_BE_3500 DesLL"
            return 'calccspos_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_400":
            print "cspos_dielectron_2017_BB_400 DesLL"
            return 'calccspos_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_500":
            print "cspos_dielectron_2017_BB_500 DesLL"
            return 'calccspos_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_700":
            print "cspos_dielectron_2017_BB_700 DesLL"
            return 'calccspos_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_1100":
            print "cspos_dielectron_2017_BB_1100 DesLL"
            return 'calccspos_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BB_3500":
            print "cspos_dielectron_2017_BB_3500 DesLL"
            return 'calccspos_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_400":
            print "cspos_dielectron_2017_BE_400 DesLL"
            return 'calccspos_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_500":
            print "cspos_dielectron_2017_BE_500 DesLL"
            return 'calccspos_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_700":
            print "cspos_dielectron_2017_BE_700 DesLL"
            return 'calccspos_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_1100":
            print "cspos_dielectron_2017_BE_1100 DesLL"
            return 'calccspos_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2017_BE_3500":
            print "cspos_dielectron_2017_BE_3500 DesLL"
            return 'calccspos_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_400":
            print "cspos_dimuon_2017_BB_400 DesLL"
            return 'calccspos_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_500":
            print "cspos_dimuon_2017_BB_500 DesLL"
            return 'calccspos_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_700":
            print "cspos_dimuon_2017_BB_700 DesLL"
            return 'calccspos_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_1100":
            print "cspos_dimuon_2017_BB_1100 DesLL"
            return 'calccspos_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BB_3500":
            print "cspos_dimuon_2017_BB_3500 DesLL"
            return 'calccspos_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_400":
            print "cspos_dimuon_2017_BE_400 DesLL"
            return 'calccspos_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_500":
            print "cspos_dimuon_2017_BE_500 DesLL"
            return 'calccspos_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_700":
            print "cspos_dimuon_2017_BE_700 DesLL"
            return 'calccspos_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_1100":
            print "cspos_dimuon_2017_BE_1100 DesLL"
            return 'calccspos_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2017_BE_3500":
            print "cspos_dimuon_2017_BE_3500 DesLL"
            return 'calccspos_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_400":
            print "cspos_dielectron_2018_BB_400 DesLL"
            return 'calccspos_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_500":
            print "cspos_dielectron_2018_BB_500 DesLL"
            return 'calccspos_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_700":
            print "cspos_dielectron_2018_BB_700 DesLL"
            return 'calccspos_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_1100":
            print "cspos_dielectron_2018_BB_1100 DesLL"
            return 'calccspos_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BB_3500":
            print "cspos_dielectron_2018_BB_3500 DesLL"
            return 'calccspos_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_400":
            print "cspos_dielectron_2018_BE_400 DesLL"
            return 'calccspos_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_500":
            print "cspos_dielectron_2018_BE_500 DesLL"
            return 'calccspos_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_700":
            print "cspos_dielectron_2018_BE_700 DesLL"
            return 'calccspos_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_1100":
            print "cspos_dielectron_2018_BE_1100 DesLL"
            return 'calccspos_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dielectron_2018_BE_3500":
            print "cspos_dielectron_2018_BE_3500 DesLL"
            return 'calccspos_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_400":
            print "cspos_dimuon_2018_BB_400 DesLL"
            return 'calccspos_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_500":
            print "cspos_dimuon_2018_BB_500 DesLL"
            return 'calccspos_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_700":
            print "cspos_dimuon_2018_BB_700 DesLL"
            return 'calccspos_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_1100":
            print "cspos_dimuon_2018_BB_1100 DesLL"
            return 'calccspos_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BB_3500":
            print "cspos_dimuon_2018_BB_3500 DesLL"
            return 'calccspos_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_400":
            print "cspos_dimuon_2018_BE_400 DesLL"
            return 'calccspos_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_500":
            print "cspos_dimuon_2018_BE_500 DesLL"
            return 'calccspos_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_700":
            print "cspos_dimuon_2018_BE_700 DesLL"
            return 'calccspos_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_1100":
            print "cspos_dimuon_2018_BE_1100 DesLL"
            return 'calccspos_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "cspos_dimuon_2018_BE_3500":
            print "cspos_dimuon_2018_BE_3500 DesLL"
            return 'calccspos_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_400":
            print "csneg_dielectron_2016_BB_400 DesLL"
            return 'calccsneg_dielectron_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_500":
            print "csneg_dielectron_2016_BB_500 DesLL"
            return 'calccsneg_dielectron_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_700":
            print "csneg_dielectron_2016_BB_700 DesLL"
            return 'calccsneg_dielectron_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_1100":
            print "csneg_dielectron_2016_BB_1100 DesLL"
            return 'calccsneg_dielectron_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BB_3500":
            print "csneg_dielectron_2016_BB_3500 DesLL"
            return 'calccsneg_dielectron_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_400":
            print "csneg_dielectron_2016_BE_400 DesLL"
            return 'calccsneg_dielectron_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_500":
            print "csneg_dielectron_2016_BE_500 DesLL"
            return 'calccsneg_dielectron_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_700":
            print "csneg_dielectron_2016_BE_700 DesLL"
            return 'calccsneg_dielectron_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_1100":
            print "csneg_dielectron_2016_BE_1100 DesLL"
            return 'calccsneg_dielectron_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2016_BE_3500":
            print "csneg_dielectron_2016_BE_3500 DesLL"
            return 'calccsneg_dielectron_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_400":
            print "csneg_dimuon_2016_BB_400 DesLL"
            return 'calccsneg_dimuon_2016_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_500":
            print "csneg_dimuon_2016_BB_500 DesLL"
            return 'calccsneg_dimuon_2016_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_700":
            print "csneg_dimuon_2016_BB_700 DesLL"
            return 'calccsneg_dimuon_2016_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_1100":
            print "csneg_dimuon_2016_BB_1100 DesLL"
            return 'calccsneg_dimuon_2016_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BB_3500":
            print "csneg_dimuon_2016_BB_3500 DesLL"
            return 'calccsneg_dimuon_2016_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_400":
            print "csneg_dimuon_2016_BE_400 DesLL"
            return 'calccsneg_dimuon_2016_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_500":
            print "csneg_dimuon_2016_BE_500 DesLL"
            return 'calccsneg_dimuon_2016_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_700":
            print "csneg_dimuon_2016_BE_700 DesLL"
            return 'calccsneg_dimuon_2016_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_1100":
            print "csneg_dimuon_2016_BE_1100 DesLL"
            return 'calccsneg_dimuon_2016_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2016_BE_3500":
            print "csneg_dimuon_2016_BE_3500 DesLL"
            return 'calccsneg_dimuon_2016_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_400":
            print "csneg_dielectron_2017_BB_400 DesLL"
            return 'calccsneg_dielectron_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_500":
            print "csneg_dielectron_2017_BB_500 DesLL"
            return 'calccsneg_dielectron_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_700":
            print "csneg_dielectron_2017_BB_700 DesLL"
            return 'calccsneg_dielectron_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_1100":
            print "csneg_dielectron_2017_BB_1100 DesLL"
            return 'calccsneg_dielectron_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BB_3500":
            print "csneg_dielectron_2017_BB_3500 DesLL"
            return 'calccsneg_dielectron_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_400":
            print "csneg_dielectron_2017_BE_400 DesLL"
            return 'calccsneg_dielectron_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_500":
            print "csneg_dielectron_2017_BE_500 DesLL"
            return 'calccsneg_dielectron_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_700":
            print "csneg_dielectron_2017_BE_700 DesLL"
            return 'calccsneg_dielectron_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_1100":
            print "csneg_dielectron_2017_BE_1100 DesLL"
            return 'calccsneg_dielectron_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2017_BE_3500":
            print "csneg_dielectron_2017_BE_3500 DesLL"
            return 'calccsneg_dielectron_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_400":
            print "csneg_dimuon_2017_BB_400 DesLL"
            return 'calccsneg_dimuon_2017_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_500":
            print "csneg_dimuon_2017_BB_500 DesLL"
            return 'calccsneg_dimuon_2017_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_700":
            print "csneg_dimuon_2017_BB_700 DesLL"
            return 'calccsneg_dimuon_2017_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_1100":
            print "csneg_dimuon_2017_BB_1100 DesLL"
            return 'calccsneg_dimuon_2017_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BB_3500":
            print "csneg_dimuon_2017_BB_3500 DesLL"
            return 'calccsneg_dimuon_2017_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_400":
            print "csneg_dimuon_2017_BE_400 DesLL"
            return 'calccsneg_dimuon_2017_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_500":
            print "csneg_dimuon_2017_BE_500 DesLL"
            return 'calccsneg_dimuon_2017_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_700":
            print "csneg_dimuon_2017_BE_700 DesLL"
            return 'calccsneg_dimuon_2017_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_1100":
            print "csneg_dimuon_2017_BE_1100 DesLL"
            return 'calccsneg_dimuon_2017_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2017_BE_3500":
            print "csneg_dimuon_2017_BE_3500 DesLL"
            return 'calccsneg_dimuon_2017_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_400":
            print "csneg_dielectron_2018_BB_400 DesLL"
            return 'calccsneg_dielectron_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_500":
            print "csneg_dielectron_2018_BB_500 DesLL"
            return 'calccsneg_dielectron_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_700":
            print "csneg_dielectron_2018_BB_700 DesLL"
            return 'calccsneg_dielectron_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_1100":
            print "csneg_dielectron_2018_BB_1100 DesLL"
            return 'calccsneg_dielectron_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BB_3500":
            print "csneg_dielectron_2018_BB_3500 DesLL"
            return 'calccsneg_dielectron_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_400":
            print "csneg_dielectron_2018_BE_400 DesLL"
            return 'calccsneg_dielectron_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_500":
            print "csneg_dielectron_2018_BE_500 DesLL"
            return 'calccsneg_dielectron_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_700":
            print "csneg_dielectron_2018_BE_700 DesLL"
            return 'calccsneg_dielectron_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_1100":
            print "csneg_dielectron_2018_BE_1100 DesLL"
            return 'calccsneg_dielectron_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dielectron_2018_BE_3500":
            print "csneg_dielectron_2018_BE_3500 DesLL"
            return 'calccsneg_dielectron_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_400":
            print "csneg_dimuon_2018_BB_400 DesLL"
            return 'calccsneg_dimuon_2018_BB_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_500":
            print "csneg_dimuon_2018_BB_500 DesLL"
            return 'calccsneg_dimuon_2018_BB_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_700":
            print "csneg_dimuon_2018_BB_700 DesLL"
            return 'calccsneg_dimuon_2018_BB_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_1100":
            print "csneg_dimuon_2018_BB_1100 DesLL"
            return 'calccsneg_dimuon_2018_BB_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BB_3500":
            print "csneg_dimuon_2018_BB_3500 DesLL"
            return 'calccsneg_dimuon_2018_BB_3500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_400":
            print "csneg_dimuon_2018_BE_400 DesLL"
            return 'calccsneg_dimuon_2018_BE_400_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_500":
            print "csneg_dimuon_2018_BE_500 DesLL"
            return 'calccsneg_dimuon_2018_BE_500_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_700":
            print "csneg_dimuon_2018_BE_700 DesLL"
            return 'calccsneg_dimuon_2018_BE_700_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_1100":
            print "csneg_dimuon_2018_BE_1100 DesLL"
            return 'calccsneg_dimuon_2018_BE_1100_Beta' if self.DC.isSignal[process] else 1
      
        elif bin == "csneg_dimuon_2018_BE_3500":
            print "csneg_dimuon_2018_BE_3500 DesLL"
            return 'calccsneg_dimuon_2018_BE_3500_Beta' if self.DC.isSignal[process] else 1
      
CIlambda = CIlambda()
