import matplotlib.pyplot as plt
import os

import numpy as np

# Create a list of values from 0 to 100
y = [
10762,
6736,
7178,
1041082,
9991,
479475,
332602,
40176,
56492,
22432,
32928,
40384,
26937,
13648,
16742,
28148,
12428,
16394,
13116,
18108,
11308,
15421,
21760,
9610,
32010,
16960,
14202,
12029,
30480,
10595,
16019,
14343,
9603,
13364,
19872,
10279,
14339,
8665,
74585,
10684,
10057,
12506,
11094,
7709,
8288,
11420,
6211,
13991,
10285,
12736,
18409,
13165,
17763,
9033,
515353,
24435,
27849,
107508,
172688,
14880,
24163,
139674,
174842,
164899,
131530,
61033,
91959,
93754,
80567,
88839,
129053,
74362,
102925,
102807,
99174,
29645,
22355,
49028,
24022,
29386,
26695,
23888,
13338,
22775,
12294,
11769,
17804,
21299,
15017,
11869,
22553,
25721,
24262,
15763,
15341,
10438,
32566,
16198,
18205,
15331,
12490,
9405,
14851,
13063,
21772,
16051,
28416,
14989,
18659,
19574,
22682,
14237,
16788,
13581,
12083,
20947,
12263,
19159,
23193,
9095,
10624,
18886,
12521,
10291,
9065,
10867,
13187,
13847,
21274,
15587,
13783,
14052,
13229,
11968,
11772,
18288,
9075,
21120,
22963,
12269,
17548,
8883,
18137,
10439,
11052,
10214,
10244,
15268,
19962,
11901,
12988,
22608,
23148,
15780,
10151,
15197,
15648,
13184,
24147,
19034,
18720,
12013,
8723,
11008,
9616,
15095,
14375,
11703,
38435,
18406,
10259,
17587,
26931,
27671,
17539,
16388,
15769,
11805,
11482,
13677,
18464,
8349,
11754,
12131,
15116,
7754,
18880,
18964,
10973,
18780,
7289,
11532,
11475,
12701,
15891,
9655,
6221,
8499,
7559,
7501,
12294,
7728,
7972,
7510,
7005,
6746,
8202,
6873,
8374,
6441,
10461,
6765,
10950,
6563,
7517,
8736,
34359,
14343,
19248,
20035,
25149,
17299,
21139,
22198,
11143,
14823,
13066,
22291,
26233,
11126,
26467,
14336,
20125,
14022,
24413,
21850,
11405,
15484,
14464,
21357,
24964,
12320,
21126,
15645,
16678,
16224,
20762,
12740,
19958,
22435,
18970,
24390,
15101,
15206,
14118,
13433,
10455,
12404,
29798,
7696,
13245,
15123,
12586,
14214,
19693,
12784,
18652,
11581,
8340,
11580,
13209,
16653,
17196,
10931,
18784,
12867,
14288,
17123,
20429,
11680,
15916,
15338,
12662,
9773,
11062,
19968,
11428,
12265,
9536,
13488,
9772,
10938,
16601,
12564,
12972,
10096,
7200,
13267,
11831,
15171,
8320,
10080,
17664,
7904,
13024,
12742,
10468,
10851,
15459,
13856,
9619,
9811,
17942,
12973,
7088,
6906,
10169,
14228,
21581,
9078,
13504,
8569,
13891,
9383,
7174,
12825,
10573,
10762,
16035,
14439,
25001,
8186,
15241,
6602,
19334,
11130,
20183,
11786,
9034,
12602,
13149,
16845,
29014,
21392,
20615,
11786,
10932,
17709,
13469,
22202,
13702,
9430,
13152,
19254,
12426,
17709,
7101,
9465,
11814,
13367,
10803,
12620,
8230,
11082,
6790,
16435,
11776,
17366,
8598,
8842,
10342,
11671,
6454,
9952,
10227,
10886,
9911,
9884,
8842,
10688,
16131,
8963,
8048,
17194,
12630,
7718,
6893,
8873,
14122,
9139,
8455,
10311,
14061,
11165,
9209,
11533,
11187,
11165,
14192,
12563,
19824,
10669,
16237,
21168,
14724,
14647,
10668,
11834,
11584,
19049,
27594,
11110,
15581,
11197,
13248,
18531,
23580,
14682,
16278,
16710,
12150,
13203,
10605,
18710,
12592,
26054,
13143,
12224,
13364,
20563,
9831,
11856,
11789,
11907,
15508,
18893,
15382,
13561,
24253,
12771,
11923,
70784,
9700,
8630,
43882,
16221,
31120,
12041,
18426,
10400,
11865,
10598,
16714,
9044,
18058,
11830,
12614,
140329,
10656,
13632,
29523,
11469,
9178,
10266,
17226,
10025,
21191,
73437,
35303,
42349,
67542,
23302,
17120,
30201,
18204,
75916,
15017,
9364,
8052,
6317,
6310,
8836,
9392,
13949,
11533,
12186,
7920,
14352,
8640,
9876,
8589,
9936,
9020,
7680,
9344,
8339,
39158,
15478,
44092,
21376,
62857,
12166,
29593,
33754,
22246,
44352,
17456,
20330,
11930,
16893,
18906,
19939,
13241,
16589,
18992,
11724,
36893,
20410,
11760,
10973,
18374,
19149,
15066,
10675,
11993,
14803,
13466,
13459,
13401,
19788,
13452,
11258,
18189,
21424,
14208,
15958,
10451,
13284,
14464,
14166,
9030,
10701,
12416,
10490,
10569,
13837,
15011,
9290,
22758,
14134,
10169,
8537,
17900,
11657,
18688,
13034,
21108,
12320,
33325,
14368,
17290,
24371,
14090,
19907,
19171,
11680,
14758,
18515,
14051,
16787,
17831,
13341,
15741,
17321,
22554,
21881,
15587,
16810,
10701,
20055,
14851,
19491,
16724,
17507,
20042,
15923,
24445,
12215,
26211,
18214,
14582,
15674,
17312,
17696,
15430,
17398,
15543,
10852,
13616,
13111,
13680,
22483,
16906,
13366,
19923,
10394,
12468,
16272,
15331,
10371,
16941,
11396,
12909,
12803,
15815,
16185,
18400,
9920,
13565,
10285,
14071,
19859,
10576,
18211,
14211,
10781,
10493,
12512,
16890,
11469,
19955,
14000,
14576,
11799,
22823,
11994,
28467,
18198,
13146,
19757,
24000,
15162,
12793,
11277,
14054,
10346,
12829,
10954,
19235,
13059,
10733,
17523,
12147,
15936,
12557,
14039,
12371,
16599,
20659,
12365,
13597,
19363,
11975,
12454,
18528,
19728,
13107,
13693,
14656,
13667,
23856,
19635,
17997,
13728,
15766,
21952,
9002,
11232,
10544,
7590,
13616,
3454998,
22336,
15421,
6688,
7299,
11965,
12688,
9731,
7245,
11376,
12396,
15606,
17110,
7319,
6580,
14861,
13482,
8522,
11360,
11943,
12272,
12022,
18512,
17494,
10764,
17542,
20227,
11444,
19405,
10979,
14569,
14896,
13763,
26253,
21296,
9686,
10500,
11834,
8662,
10710,
13232,
8634,
13750,
15177,
8749,
10285,
17779,
8506,
9824,
10343,
13158,
9309,
20455,
9050,
11402,
13033,
19593,
12368,
10848,
11625,
20231,
15478,
12796,
22243,
13190,
10989,
10636,
15555,
24960,
15354,
16563,
18060,
16925,
18567,
13110,
17277,
15779,
28496,
13498,
18873,
29252,
22182,
14179,
19277,
15347,
14365,
14102,
15814,
12803,
14976,
20637,
23629,
11754,
16327,
13258,
13686,
16182,
12650,
15683,
19068,
13667,
18067,
17555,
12333,
20733,
13712,
13335,
21606,
20916,
15532,
19606,
15968,
12547,
22336,
21833,
12090,
8838,
10947,
11261,
13293,
10109,
12848,
19514,
16887,
14685,
10349,
13191,
12358,
15779,
12403,
11616,
10467,
12199,
14816,
12858,
19174,
14387,
13609,
12247,
18944,
11702,
14925,
11252,
11312,
13776,
12080,
13684,
13123,
17580,
15465,
17683,
27911,
19629,
12323,
12346,
14755,
12889,
11018,
13593,
15088,
11687,
14441,
12400,
16118,
12758,
22477,
12211,
19494,
17962,
12890,
17101,
16016,
12198,
13699,
20192,
16499,
19872,
12221,
17642,
19712,
13383,
11654,
17047,
19613,
12115,
13081,
21732,
14048,
13047,
12215,
14410,
12125,
12307,
11709,
15689,
43001,
207213,
15561,
11731,
12848,
16586,
13779,
11882,
15846,
18653,
10455,
20976,
15795,
13543,
23507,
11021,
11837,
26928,
17046,
16201,
18919,
20832,
38457,
10343,
12096,
13437,
11670,
10854,
11575,
15376,
13120,
11037,
106336,
21484,
11936,
12348,
13770,
13108,
12106,
10589,
6893,
8224,
7894,
6855,
7802,
8672,
9641,
9171,
7501,
9450,
6237,
9152,
7674,
14061,
9796,
6666,
8739,
8112,
8877,
6509,
12730,
11143,
14746,
30407,
23923,
12505,
10960,
14761,
10099,
12384,
12525,
9751,
14256,
21079,
17098,
13914,
12230,
8733,
10694,
12323,
18019,
12167,
13036,
12016,
10103,
14377,
11449,
19161,
8819,
19072,
10819,
12332,
11776,
10759,
14931,
13210,
11517,
10701,
13852,
11859,
15763,
17447,
10400,
10646,
20678,
10188,
8781,
8854,
8640,
9075,
9722,
8848,
17994,
13114,
11517,
21225,
10365,
9879,
8397,
11760,
12339,
11059,
9264,
14989,
10147,
44480,
15609,
10067,
10714,
15212,
16150,
8857,
16358,
9268,
13136,
9590,
13187,
15206,
9421,
10419,
13207,
10224,
21763,
10701,
18182,
17030,
11123,
14272,
12160,
13466,
8637,
17462,
10560,
11168,
11203,
11188,
13434,
14285,
10400,
12058,
11130,
13347,
14679,
14931,
12912,
11533,
37981,
15392,
10531,
13804,
19126,
8352,
18861,
11341,
19917,
10692,
12253,
11446,
10841,
10938,
10778,
12212,
14310,
9312,
6125,
11997,
15924,
12163,
13222,
11587,
9491,
13667,
10170,
9251,
7917,
12025,
8471,
14086,
11356,
8281,
15037,
12944,
10224,
13443,
16938,
14756,
13715,
38089,
20244,
11225,
11127,
12185,
17162,
14944,
18467,
23600,
17024,
15802,
18154,
11978,
12118,
12612,
14448,
12582,
20602,
11120,
17485,
18265,
12480,
11028,
12029,
10419,
16896,
12230,
16477,
13075,
12205,
12003,
1622953,
19220,
12029,
13760,
16554,
12297,
15421,
15386,
12800,
14973,
12742,
25539,
18800,
14358,
13433,
17443,
14633,
12858,
19514,
14954,
19354,
21206,
15418,
12112,
8483,
9460,
13161,
7232,
9916,
11533,
13414,
12621,
14074,
10739,
16371,
9748,
13044,
11171,
8179,
10864,
10340,
14480,
11312,
13705,
22637,
11696,
11587,
10566,
13609,
13120,
11290,
12903,
23494,
15066,
12871,
8423,
9335,
13081,
13239,
18272,
8928,
11204,
11309,
7402,
8023,
9158,
7430,
9385,
10723,
10979,
10204,
7952,
9418,
10314,
6134,
9068,
10592,
7859,
9245,
9955,
10870,
11414,
16515,
25558,
13632,
12375,
19856,
18422,
12940,
15712,
15136,
24669,
19258,
1503433,
13849,
19236,
17779,
29840,
13356,
14938,
16275,
12045,
16467,
13657,
18902,
28118,
17680,
11719,
12089,
12781,
24220,
13110,
13632,
17248,
20471,
13232,
24298,
15853,
18477,
11677,
14263,
15901,
7527,
8029,
18378,
15568,
11849,
10042,
15719,
9414,
12246,
12230,
14362,
8218,
43130,
16983,
9731,
14311,
11097,
9766,
11260,
13540,
12061,
13443,
18566,
12282,
16205,
13082,
18304,
14234,
13683,
11520,
11987,
20013,
24212,
21405,
13699,
11181,
303280,
15155,
11283,
22265,
52307,
18480,
22025,
660083,
19993,
22349,
24509,
20653,
10266,
14000,
12957,
14259,
16806,
18755,
16954,
16701,
15959,
18160,
24176,
23306,
16403,
12000,
9926,
10810,
15001,
27161,
14691,
9549,
15604,
17216,
9952,
11466,
17011,
12924,
12547,
14009,
13942,
9517,
21283,
16480,
12797,
14237,
20455,
15603,
19593,
11168,
16285,
14630,
16762,
14775,
17164,
11203,
16128,
20432,
10135,
17849,
21562,
11696,
12496,
21447,
18473,
10323,
15456,
16452,
15706,
21856,
21072,
13932,
16672,
14243,
10899,
10442,
15366,
12748,
9987,
20457,
13594,
15805,
14480,
15980,
14861,
6291,
12918,
6793,
7353,
12972,
8515,
7504,
8397,
8803,
9101,
11059,
6787,
10157,
8330,
11092,
9837,
15126,
12749,
6534,
15996,
11146,
8551,
11411,
20282,
15616,
11696,
10000,
9040,
8291,
13149,
20192,
17539,
9504,
13789,
10394,
24377,
14093,
17367,
14336,
10381,
7680,
10761,
8249,
7373,
7683,
8346,
10426,
7571,
6416,
7376,
7142,
7904,
8160,
6544,
7376,
9869,
9405,
6796,
9728,
6400,
7254,
11574,
9437,
8410,
14694,
14067,
2699779,
9683,
8486,
9677,
11539,
6534,
8883,
6948,
9191,
6528,
9363,
6823,
10404,
19466,
15033,
16592,
11875,
18551,
11910,
11783,
21178,
15245,
13680,
12643,
11738,
15437,
11366,
13206,
8739,
18800,
18580,
17687,
23684,
18348,
12096,
11668,
28396,
11098,
11780,
11872,
15309,
18467,
23350,
15162,
12985,
10122,
15673,
12390,
12804,
12269,
13356,
12761,
17514,
22877,
12166,
10253,
13536,
11097,
16362,
15417,
13370,
11257,
12761,
10742,
11796,
14477,
]

x = np.array(range(len(y))) / len(y) * 100
y = sorted(y)
y = np.array(y)
y = y / 1000

# figsize 8x6
fig, ax1 = plt.subplots(figsize=(4, 3))

color = 'tab:red'
ax1.set_xlabel("Percentage of data")
ax1.set_ylabel("Latency (us)", color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 50)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel("Latency (us)", color=color)
ax2.plot(x, y, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1000)

if os.path.exists("figure") == False:
    os.mkdir("figure")

filename = "figure/exp-7-latency-distribution.pdf"

if os.path.exists(filename):
    os.remove(filename)

plt.savefig(filename, format="pdf", bbox_inches="tight")

plt.show()