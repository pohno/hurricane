#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:11:26 2018

@author: geiger
"""

import numpy as np

class RefrIndexData:
    
    def __init__(self):
        #initialize dictionary to hold all data
        self.data = dict()
        
        #air, ciddor
        wavelengths = np.array([230,244.6,259.2,273.8,288.4,303,317.6,332.2,346.8,361.4,376,390.6,405.2,419.8,434.4,449,463.6,478.2,492.8,507.4,522,536.6,551.2,565.8,580.4,595,609.6,624.2,638.8,653.4,668,682.6,697.2,711.8,726.4,741,755.6,770.2,784.8,799.4,814,828.6,843.2,857.8,872.4,887,901.6,916.2,930.8,945.4,960,974.6,989.2,1004,1018,1033,1048,1062,1077,1091,1106,1121,1135,1150,1164,1179,1194,1208,1223,1237,1252,1267,1281,1296,1310,1325,1340,1354,1369,1383,1398,1413,1427,1442,1456,1471,1486,1500,1515,1529,1544,1559,1573,1588,1602,1617,1632,1646,1661,1675,1690])
        refr = np.array([1.000308003,1.000303036,1.00029911,1.000295938,1.000293329,1.000291152,1.000289313,1.000287743,1.000286391,1.000285217,1.000284191,1.000283287,1.000282488,1.000281777,1.000281141,1.00028057,1.000280056,1.00027959,1.000279168,1.000278783,1.000278432,1.00027811,1.000277814,1.000277542,1.000277291,1.000277059,1.000276844,1.000276644,1.000276458,1.000276285,1.000276123,1.000275972,1.000275831,1.000275698,1.000275573,1.000275456,1.000275346,1.000275242,1.000275144,1.000275051,1.000274964,1.000274881,1.000274802,1.000274728,1.000274657,1.00027459,1.000274526,1.000274465,1.000274407,1.000274352,1.000274299,1.000274249,1.0002742,1.000274154,1.000274111,1.000274068,1.000274027,1.00027399,1.000273951,1.000273917,1.000273882,1.000273848,1.000273818,1.000273787,1.000273759,1.00027373,1.000273702,1.000273677,1.000273651,1.000273627,1.000273603,1.00027358,1.000273559,1.000273537,1.000273518,1.000273497,1.000273478,1.00027346,1.000273442,1.000273425,1.000273408,1.000273391,1.000273376,1.00027336,1.000273346,1.000273331,1.000273317,1.000273304,1.00027329,1.000273278,1.000273265,1.000273253,1.000273242,1.00027323,1.000273219,1.000273208,1.000273197,1.000273188,1.000273177,1.000273168,1.000273158])
        self.data['air'] = [wavelengths,refr]
        
        #Water, discontinuity near 6000
        wavelengths = np.array([182., 191.5, 200.9, 210.4, 219.9, 229.4, 238.8,248.3, 257.8, 267.2, 276.7, 286.2, 295.6, 305.1, 314.6, 324.1, 333.5,343., 352.5, 361.9, 371.4, 380.9, 390.3, 399.8, 409.3, 418.8, 428.2,437.7, 447.2, 456.6, 466.1, 475.6, 485., 494.5, 504., 513.5, 522.9,532.4, 541.9, 551.3, 560.8, 570.3, 579.7, 589.2, 598.7, 608.2, 617.6,627.1, 636.6, 646., 655.5, 665., 674.4, 683.9, 693.4, 702.9, 712.3,721.8, 731.3, 740.7, 750.2, 759.7, 769.1, 778.6, 788.1, 797.6, 807.,816.5, 826., 835.4, 844.9, 854.4, 863.8, 873.3, 882.8, 892.3, 901.7,911.2, 920.7, 930.1, 939.6, 949.1, 958.5, 968., 977.5, 987., 996.4,1006., 1015.0, 1025., 1034., 1044., 1053., 1063., 1072., 1082.,1091., 1101., 1110., 1120., 1129., 1200., 1400., 1600., 1800., 2000.,2020., 2041., 2062., 2083., 2105., 2128., 2151., 2174., 2198., 2222.,2247., 2273., 2299., 2326., 2353., 2381., 2410., 2439., 2469., 2500.,2506., 2513., 2519., 2525., 2532., 2538., 2545., 2551., 2558., 2564.,2571., 2577., 2584., 2591., 2597., 2604., 2611., 2618., 2625., 2632.,2639., 2646., 2653., 2660., 2667., 2674., 2681., 2688., 2695., 2703.,2710., 2717., 2725., 2732., 2740., 2747., 2755., 2762., 2770., 2778.,2786., 2793., 2801., 2809., 2817., 2825., 2833., 2841., 2849., 2857.,2865., 2874., 2882., 2890., 2899., 2907., 2915., 2924., 2933., 2941.,2950., 2959., 2967., 2976., 2985., 2994., 3003., 3012., 3021., 3030.,3040., 3049., 3058., 3067., 3077., 3086., 3096., 3106., 3115., 3125.,3135., 3145., 3155., 3165., 3175., 3185., 3195., 3205., 3215., 3226.,3236., 3247., 3257., 3268., 3279., 3289., 3300., 3311., 3322., 3333.,3344., 3356., 3367., 3378., 3390., 3401., 3413., 3425., 3436., 3448.,3460., 3472., 3484., 3497., 3509., 3521., 3534., 3546., 3559., 3571.,3584., 3597., 3610., 3623., 3636., 3650., 3663., 3676., 3690., 3704.,3717., 3731., 3745., 3759., 3774., 3788., 3802., 3817., 3831., 3846.,3861., 3876., 3891., 3906., 3922., 3937., 3953., 3968., 3984., 4000.,4016., 4032., 4049., 4065., 4082., 4098., 4115., 4132., 4149., 4167.,4184., 4202., 4219., 4237., 4255., 4274., 4292., 4310., 4329., 4348.,4367., 4386., 4405., 4425., 4444., 4464., 4484., 4505., 4525., 4545.,4566., 4587., 4608., 4630., 4651., 4673., 4695., 4717., 4739., 4762.,4785., 4808., 4831., 4854., 4878., 4902., 4926., 4950., 4975., 5000.,5025., 5051., 5076., 5102., 5128., 5155., 5181., 5208., 5236., 5263.,5291., 5319., 5348., 5376., 5405., 5435., 5464., 5495., 5525., 5556.,5587., 5618., 5650., 5682., 5714., 5747., 5780., 5814., 5848., 5882.,5917., 5952., 5988., 6024., 6061., 6098., 6135., 6173., 6211., 6250.,6289., 6329., 6369., 6410., 6452., 6494., 6536., 6579., 6623., 6667.,6700., 6800., 6900., 7000., 7100., 7200., 7300., 7400., 7500., 7600.,7700., 7800., 7900., 8000., 8200., 8400., 8600., 8800., 9000., 9200.,9400., 9600., 9800., 10000., 10500., 11000., 11500., 12000., 12500.,13000., 13500., 14000., 14500., 15000., 15500., 16000., 16500., 17000.,17500., 18000., 18500., 19000., 19500., 20000., 21000., 22000., 23000.,24000., 25000., 26000., 27000., 28000., 29000., 30000., 32000., 34000.,36000., 38000., 40000., 42000., 44000., 46000., 48000., 50000., 60000.,70000., 80000., 90000., 100000., 110000., 120000., 130000., 140000.,150000., 160000., 170000., 180000., 190000., 200000.])
        refr = np.array([1.4677,1.4404,1.4224,1.409,1.3986,1.3904,1.3837,1.3781,1.3733,1.3693,1.3657,1.3626,1.3599,1.3575,1.3554,1.3534,1.3517,1.3501,1.3487,1.3474,1.3462,1.3451,1.3441,1.3432,1.3423,1.3415,1.3408,1.3401,1.3394,1.3388,1.3382,1.3377,1.3372,1.3367,1.3362,1.3358,1.3354,1.335,1.3346,1.3342,1.3339,1.3336,1.3333,1.333,1.3327,1.3324,1.3321,1.3319,1.3316,1.3314,1.3311,1.3309,1.3307,1.3305,1.3303,1.3301,1.3299,1.3297,1.3295,1.3293,1.3291,1.329,1.3288,1.3286,1.3284,1.3283,1.3281,1.328,1.3278,1.3276,1.3275,1.3273,1.3272,1.327,1.3269,1.3267,1.3266,1.3265,1.3263,1.3262,1.326,1.3259,1.3257,1.3256,1.3255,1.3253,1.3252,1.325,1.3249,1.3248,1.3246,1.3245,1.3243,1.3242,1.3241,1.3239,1.3238,1.3236,1.3235,1.3234,1.3232, 1.324, 1.321, 1.317,1.312, 1.303, 1.301,1.301, 1.3, 1.298, 1.298, 1.296, 1.295, 1.294, 1.293, 1.291, 1.289, 1.287,1.285, 1.282, 1.28, 1.277, 1.274, 1.27, 1.265, 1.261, 1.26, 1.259, 1.257,1.256, 1.255, 1.254, 1.252, 1.25, 1.249, 1.247, 1.246, 1.243, 1.241, 1.24,1.238, 1.235, 1.232, 1.23, 1.227, 1.224, 1.221, 1.218, 1.214, 1.21, 1.205,1.2, 1.195, 1.191, 1.185, 1.179, 1.172, 1.166, 1.157, 1.149, 1.144, 1.139,1.138, 1.138, 1.139, 1.141, 1.144, 1.149, 1.154, 1.158, 1.161, 1.165,1.171, 1.177, 1.183, 1.191, 1.199, 1.212, 1.22, 1.233, 1.246, 1.258, 1.271,1.282, 1.293, 1.305, 1.317, 1.329, 1.342, 1.353, 1.364, 1.376, 1.386,1.398, 1.407, 1.417, 1.426, 1.434, 1.442, 1.45, 1.457, 1.465, 1.471, 1.476,1.48, 1.483, 1.486, 1.487, 1.487, 1.487, 1.486, 1.485, 1.482, 1.479, 1.477,1.474, 1.472, 1.467, 1.464, 1.461, 1.457, 1.454, 1.451, 1.448, 1.444,1.441, 1.437, 1.434, 1.431, 1.427, 1.425, 1.421, 1.418, 1.415, 1.413, 1.41,1.407, 1.405, 1.403, 1.4, 1.398, 1.396, 1.394, 1.392, 1.39, 1.388, 1.387,1.385, 1.383, 1.382, 1.379, 1.378, 1.377, 1.375, 1.374, 1.372, 1.371, 1.37,1.369, 1.367, 1.366, 1.365, 1.363, 1.361, 1.361, 1.36, 1.358, 1.358, 1.357,1.355, 1.354, 1.353, 1.352, 1.351, 1.35, 1.349, 1.348, 1.348, 1.347, 1.346,1.345, 1.344, 1.344, 1.343, 1.342, 1.341, 1.34, 1.34, 1.338, 1.337, 1.337,1.335, 1.334, 1.334, 1.333, 1.332, 1.332, 1.331, 1.33, 1.33, 1.33, 1.329,1.329, 1.329, 1.328, 1.328, 1.327, 1.327, 1.327, 1.327, 1.327, 1.326,1.326, 1.326, 1.325, 1.325, 1.325, 1.325, 1.325, 1.325, 1.324, 1.324,1.323, 1.322, 1.322, 1.321, 1.32, 1.319, 1.318, 1.318, 1.317, 1.316, 1.314,1.313, 1.311, 1.31, 1.308, 1.306, 1.304, 1.302, 1.299, 1.297, 1.294, 1.291,1.288, 1.285, 1.282, 1.278, 1.275, 1.271, 1.267, 1.262, 1.256, 1.251,1.247, 1.242, 1.241, 1.241, 1.247, 1.265, 1.289, 1.311, 1.332, 1.349,1.354, 1.356, 1.354, 1.35, 1.345, 1.341, 1.337, 1.333, 1.33, 1.326, 1.324,1.322, 1.329, 1.324, 1.321, 1.317, 1.314, 1.312, 1.309, 1.307, 1.304,1.302, 1.299, 1.297, 1.294, 1.291, 1.286, 1.281, 1.275, 1.269, 1.262,1.255, 1.247, 1.239, 1.229, 1.218, 1.185, 1.153, 1.126, 1.111, 1.123,1.146, 1.177, 1.21, 1.241, 1.27, 1.297, 1.325, 1.351, 1.376, 1.401, 1.423,1.443, 1.461, 1.476, 1.48, 1.487, 1.5, 1.511, 1.521, 1.531, 1.539, 1.545,1.549, 1.551, 1.551, 1.546, 1.536, 1.527, 1.522, 1.519, 1.522, 1.53, 1.541,1.555, 1.587, 1.703, 1.821, 1.886, 1.924, 1.957, 1.966, 2.004, 2.036,2.056, 2.069, 2.081, 2.094, 2.107, 2.119, 2.13])
        self.data['water'] = [wavelengths,refr]
        
        #Fused Silica
        wavelengths = np.array([210,217.4,225.1,233,241.2,249.7,258.5,267.6,277,286.8,296.9,307.4,318.2,329.4,341,353,365.5,378.3,391.7,405.5,419.7,434.5,449.8,465.7,482.1,499.1,516.7,534.9,553.7,573.2,593.4,614.3,636,658.4,681.6,705.6,730.5,756.2,782.9,810.4,839,868.6,899.2,930.8,963.6,997.6,1033,1069,1107,1146,1186,1228,1271,1316,1362,1410,1460,1512,1565,1620,1677,1736,1797,1861,1926,1994,2064,2137,2212,2290,2371,2454,2541,2630,2723,2819,2918,3021,3128,3238,3352,3470,3592,3719,3850,3986,4126,4271,4422,4578,4739,4906,5079,5258,5443,5635,5833,6039,6252,6472,6700])
        refr = np.array([1.53835762,1.530846431,1.524078907,1.518041768,1.512572116,1.507609587,1.503100963,1.498999219,1.495262719,1.491821503,1.488683281,1.485791437,1.483150433,1.480714442,1.478467652,1.47639513,1.474468282,1.47270468,1.471052512,1.46952865,1.468121822,1.46680482,1.46558083,1.464436031,1.463371935,1.462376439,1.461444991,1.460573079,1.459756285,1.458986561,1.458260788,1.457575807,1.456925601,1.456310408,1.455724699,1.45516603,1.454629875,1.454116165,1.453618854,1.45313961,1.452671274,1.452213821,1.451765383,1.451324079,1.450885397,1.450447736,1.450006962,1.44957109,1.449121462,1.448668311,1.448209659,1.447732246,1.447245577,1.446736352,1.446213852,1.445664578,1.445086147,1.444475988,1.443843402,1.443173929,1.442464576,1.441712173,1.440913367,1.440050939,1.439148066,1.438172943,1.43713496,1.436013962,1.434819618,1.433529881,1.432137211,1.430651699,1.429028728,1.427296094,1.425404433,1.423361368,1.421154416,1.418745952,1.416117293,1.413274157,1.410169683,1.406778215,1.403070896,1.398982,1.394503572,1.389555342,1.384120806,1.378099774,1.371370131,1.363881434,1.355526219,1.346117123,1.335482357,1.323410544,1.3096384,1.293746028,1.275372396,1.253728956,1.228088835,1.197325672,1.159649414])
        self.data['fusedsilica'] = [wavelengths,refr]
        
        #CaF2
        wavelengths = np.array([230,238.8,247.9,257.3,267.1,277.3,287.9,298.9,310.3,322.1,334.4,347.1,360.4,374.1,388.4,403.2,418.5,434.5,451.1,468.3,486.1,504.6,523.9,543.9,564.6,586.1,608.5,631.7,655.8,680.8,706.7,733.7,761.6,790.7,820.8,852.1,884.6,918.3,953.3,989.7,1027,1067,1107,1149,1193,1239,1286,1335,1386,1439,1494,1551,1610,1671,1735,1801,1870,1941,2015,2092,2171,2254,2340,2429,2522,2618,2718,2822,2929,3041,3157,3277,3402,3532,3667,3806,3951,4102,4259,4421,4589,4764,4946,5135,5330,5534,5745,5964,6191,6427,6672,6927,7191,7465,7749,8045,8352,8670,9001,9344,9700])
        refr = np.array([1.475754569,1.47171345,1.468070333,1.464780247,1.461775236,1.459031407,1.456526303,1.454238984,1.452150053,1.450241635,1.448483879,1.446878285,1.445389492,1.444030361,1.442771679,1.44161498,1.440551803,1.439562575,1.438648949,1.437805349,1.437026402,1.436303283,1.435628998,1.435003868,1.434424176,1.433883957,1.433378364,1.432907271,1.432466222,1.432053089,1.431665742,1.431299488,1.430955322,1.43062795,1.430318179,1.430022459,1.42973953,1.429468092,1.429206109,1.428951736,1.428707083,1.428459692,1.428225113,1.427990107,1.427753995,1.427515968,1.427280067,1.427040126,1.426795173,1.426544171,1.426286039,1.426019657,1.425743875,1.425457519,1.425154636,1.424838648,1.424503384,1.424152275,1.423778891,1.423381533,1.422963775,1.42251319,1.422033059,1.42152137,1.420970012,1.420382453,1.419749994,1.419069627,1.418345084,1.417559529,1.416716159,1.415811359,1.414833391,1.413777402,1.412638284,1.411419601,1.410098179,1.408667011,1.407118676,1.405455793,1.403660447,1.401712552,1.399601433,1.397315727,1.394856211,1.392171345,1.389271982,1.386128686,1.38272369,1.379021864,1.37500043,1.370617152,1.365861216,1.360684113,1.355051211,1.348881869,1.342150253,1.334806461,1.326745172,1.317922827,1.308237467])
        self.data['caf2'] = [wavelengths,refr]
        
        #Calcite, Extraordinary Ray
        wavelengths = np.array([204,208,211,214,219,226,231,242,257,263,267,274,291,303,312,330,340,346,361,394,410,434,441,508,533,560,589,643,656,670,700,768,795,801,833,867,905,946,991,1042,1097,1159,1229,1307,1396,1497,1615,1749,1909,2100,3324])
        refr = np.array([1.57081,1.5664,1.56327,1.55976,1.55496,1.54921,1.54541,1.53782,1.53005,1.52736,1.52547,1.52261,1.51705,1.51365,1.5114,1.50746,1.50562,1.5045,1.50224,1.4981,1.4964,1.4943,1.49373,1.48956,1.48841,1.48736,1.4864,1.4849,1.48459,1.48426,1.48353,1.48259,1.48216,1.48216,1.48176,1.48137,1.48098,1.4806,1.48022,1.47985,1.47948,1.4791,1.4787,1.47831,1.47789,1.47744,1.47695,1.47638,1.47573,1.47492,1.47392])
        self.data['calciteE'] = [wavelengths,refr]
        
        #Calcite, Ordinary Ray
        wavelengths = np.array([204,208,211,214,219,226,231,242,257,263,267,274,291,303,312,330,340,346,361,394,410,434,441,508,533,560,589,643,656,670,700,768,795,801,833,867,905,946,991,1042,1097,1159,1229,1273,1307,1320,1369,1396,1422,1479,1497,1541,1609,1682,1761,1849,1946,2053,2172])     
        refr = np.array([1.88224,1.86733,1.85692,1.84558,1.83075,1.81309,1.80233,1.78211,1.76038,1.75343,1.74864,1.74139,1.72774,1.71959,1.71425,1.70515,1.70078,1.69833,1.69316,1.68374,1.68014,1.67552,1.67423,1.66527,1.66277,1.66046,1.65835,1.65504,1.65437,1.65367,1.65207,1.64974,1.64886,1.64869,1.64772,1.64676,1.64578,1.6448,1.6438,1.64276,1.64167,1.64051,1.63926,1.63849,1.63789,1.63767,1.63681,1.63637,1.6359,1.6349,1.63457,1.63381,1.63261,1.63127,1.62974,1.628,1.62602,1.62372,1.62099])
        self.data['calciteO'] = [wavelengths,refr]
