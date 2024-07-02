class TestCases:
    counter = 0
    def __init__(self, testCaseID):

        self.testCaseID = testCaseID

    def setTP(self, TP):
        self.TP = TP
    
    def __str__(self):
        # Mengupdate hitung
        TestCases.counter += 1
        # Menggunakan hitung untuk menampilkan nomor tes kasus
        return f"{TestCases.counter}. {self.testCaseID} | TP: {self.TP}"


class Requirements:

    def __str__(self):
        return f'{self.r_name}({self.RP})'
    
    def __init__(self, r_name, CP, DP):
        self.r_name = r_name
        self.CP = CP
        self.DP = DP
        self.RP = CP + DP
        self.parent = None
        self.childs = []
        

    def set_parent(self, req):
        #print(f'set_parent(self={self}, child={req})')
        if not (req in req.childs):
            self.parent = req # saya ngaku2 saya anaknya dia
            self.parent.childs.append(req) # orang tua saya menambahkan saya sbebagai anaknya
        else:
            print(f'Parent dari {req} sudah punya anak ini ({self})')

    def add_child(self, child):
        #print(f'add_child(self={self}, child={child})')
        if not (child in self.childs):
            child.parent = self # anak ini mengganggap saya parentnya
            self.childs.append(child) # saya anggap dia anak saya
        else:
            print(f'Parent {self} sudah punya anak {child}')

requirements_list = dict()



# List untuk menyimpan objek Requirements
class RequirementManagement:
    def __init__(self):
        pass

    def set_parent(self, parent, child):
        requirements_list[child].set_parent(requirements_list[parent])

    def add_child(self, parent, child):
        requirements_list[parent].add_child(requirements_list[child])

    def add_requirement(self, r_name, cp, dp):
        r = Requirements(r_name, cp, dp)
        requirements_list[r_name] = r
    
    def get_req(self, r_name):
        return requirements_list[r_name]

#List untuk menyimpan objek test case
testCase_list = [
    TestCases("TC_001"),
    TestCases("TC_002"),
    TestCases("TC_003"),
    TestCases("TC_004"),
    TestCases("TC_005"),
    TestCases("TC_006"),
    TestCases("TC_007"),
    TestCases("TC_008"),
    TestCases("TC_009"),
    TestCases("TC_010"),
    TestCases("TC_011"),
    TestCases("TC_012"),
    TestCases("TC_013"),
    TestCases("TC_014"),
    TestCases("TC_015"),
    TestCases("TC_016"),
    TestCases("TC_017"),
    TestCases("TC_018"),
    TestCases("TC_019"),
    TestCases("TC_020"),
    TestCases("TC_021"),
    TestCases("TC_022"),
    TestCases("TC_023"),
    TestCases("TC_024"),
    TestCases("TC_025"),
    TestCases("TC_026"),
    TestCases("TC_027"),
    TestCases("TC_028"),
    TestCases("TC_029"),
    TestCases("TC_030"),
    TestCases("TC_031"),
    TestCases("TC_032"),
    TestCases("TC_033"),
    TestCases("TC_034"),
    TestCases("TC_035"),
    TestCases("TC_036"),
    TestCases("TC_037"),
    TestCases("TC_038"),
    TestCases("TC_039"),
    TestCases("TC_040"),
    TestCases("TC_041"),
    TestCases("TC_042"),
    TestCases("TC_043"),
    TestCases("TC_044"),
    TestCases("TC_045"),
    TestCases("TC_046"),
    TestCases("TC_047"),
    TestCases("TC_048"),
    TestCases("TC_049"),
    TestCases("TC_050"),
    TestCases("TC_051"),
    TestCases("TC_052"),
    TestCases("TC_053"),
    TestCases("TC_054"),
    TestCases("TC_055"),
    TestCases("TC_056"),
    TestCases("TC_057"),
    TestCases("TC_058"),
    TestCases("TC_059"),
    TestCases("TC_060"),
    TestCases("TC_061"),
    TestCases("TC_062"),
    TestCases("TC_063"),
    TestCases("TC_064"),
    TestCases("TC_065"),
    TestCases("TC_066"),
    TestCases("TC_067"),
    TestCases("TC_068"),
    TestCases("TC_069"),
    TestCases("TC_070"),
    TestCases("TC_071"),
    TestCases("TC_072"),
    TestCases("TC_073"),
    TestCases("TC_074"),
    TestCases("TC_075"),
    TestCases("TC_076"),
    TestCases("TC_077"),
    TestCases("TC_078"),
    TestCases("TC_079"),
    TestCases("TC_080"),
    TestCases("TC_081"),
    TestCases("TC_082"),
    TestCases("TC_083"),
    TestCases("TC_084"),
    TestCases("TC_085"),
    TestCases("TC_086"),
    TestCases("TC_087"),
    TestCases("TC_088"),
    TestCases("TC_089"),
    TestCases("TC_090"),
    TestCases("TC_091"),
    TestCases("TC_092"),
    TestCases("TC_093"),
    TestCases("TC_094"),
    TestCases("TC_095"),
    TestCases("TC_096"),
    TestCases("TC_097"),
    TestCases("TC_098"),
    TestCases("TC_099"),
    TestCases("TC_100"),
    TestCases("TC_101"),
    TestCases("TC_102"),
    TestCases("TC_103"),
    TestCases("TC_104"),
    TestCases("TC_105"),
    TestCases("TC_106"),
    TestCases("TC_107"),
    TestCases("TC_108"),
    TestCases("TC_109"),
    TestCases("TC_110"),
    TestCases("TC_111"),
    TestCases("TC_112"),
    TestCases("TC_113"),
    TestCases("TC_114"),
    TestCases("TC_115"),
    TestCases("TC_116"),
    TestCases("TC_117"),
    TestCases("TC_118"),
    TestCases("TC_119"),
    TestCases("TC_120"),
    TestCases("TC_121"),
    TestCases("TC_122"),
    TestCases("TC_123"),
    TestCases("TC_124"),
    TestCases("TC_125"),
    TestCases("TC_126"),
    TestCases("TC_127"),
    TestCases("TC_128"),
    TestCases("TC_129"),
    TestCases("TC_130"),
    TestCases("TC_131"),
    TestCases("TC_132"),
    TestCases("TC_133"),
    TestCases("TC_134"),
    TestCases("TC_135"),
    TestCases("TC_136"),
    TestCases("TC_137"),
    TestCases("TC_138"),
    TestCases("TC_139"),
    TestCases("TC_140"),
    TestCases("TC_141"),
    TestCases("TC_142"),
    TestCases("TC_143"),
    TestCases("TC_144"),
    TestCases("TC_145"),
    TestCases("TC_146"),
    TestCases("TC_147"),
    TestCases("TC_148"),
    TestCases("TC_149"),
    TestCases("TC_150"),
    TestCases("TC_151"),
    TestCases("TC_152"),
    TestCases("TC_153"),
    TestCases("TC_154"),
    TestCases("TC_155"),
    TestCases("TC_156"),
    TestCases("TC_157"),
    TestCases("TC_158")
]

# Dictionary T ke R
# array Test:[array requirement]
T_to_R = {
    0:[1],
    1:[1],
    2:[1],
    3:[1],
    4:[1],
    5:[1],
    6:[1],
    7:[1],
    8:[1],
    9:[1],
    10:[1],
    11:[1],
    12:[1],
    13:[1],
    14:[1],
    15:[1],
    16:[1],
    17:[1],
    18:[1],
    19:[1],
    20:[2],
    21:[2],
    22:[3],
    23:[3],
    24:[3],
    25:[3],
    26:[3],
    27:[3],
    28:[3],
    29:[3],
    30:[3],
    31:[4],
    32:[4],
    33:[5,6],
    34:[6,7],
    35:[5,8,18],
    36:[5,8,18],
    37:[5,8,18],
    38:[5,8,18],
    39:[5,8,18],
    40:[5,8,18],
    41:[5],
    42:[5,6],
    43:[5,8],
    44:[5,6,8],
    45:[5,8],
    46:[5,8],
    47:[5,8],
    48:[5,8],
    49:[5,8],
    50:[5,8],
    51:[5,8],
    52:[5,8],
    53:[8],
    54:[8],
    55:[8],
    56:[8],
    57:[8],
    58:[8],
    59:[8],
    60:[8],
    61:[9,10,11,12,13,14,20],
    62:[9,10,11,12,13,14],
    63:[9,10],
    64:[9,10,11,12],
    65:[9,10,11,12],
    66:[9,10,13,14],
    67:[9,10,13,14],
    68:[9,10,13,14],
    69:[9,10,15],
    70:[9,10,11,15],
    71:[9,10,11,12,15],
    72:[9,10,11,12,13,15],
    73:[9,10],
    74:[9,10,11,12],
    75:[9,16],
    76:[9,16],
    77:[9,16],
    78:[9,16],
    79:[10,11,12,13,14,17,19],
    80:[10,11,12,13,15,17,19],
    81:[10,11,12,13,14,17,19],
    82:[10,11,12,13,15,17,19],
    83:[19],
    84:[19],
    85:[19],
    86:[19],
    87:[19],
    88:[19],
    89:[19],
    90:[19],
    91:[19],
    92:[8,19],
    93:[19],
    94:[19],
    95:[8,19],
    96:[8,19],
    97:[8,19],
    98:[8,19],
    99:[8,19],
    100:[8,19],
    101:[8,19],
    102:[8,19],
    103:[20,21,22],
    104:[20,21,22],
    105:[20,21,22],
    106:[20,21,22],
    107:[20],
    108:[20,21,23],
    109:[20,21],
    110:[20,28],
    111:[20,27,28],
    112:[20,27,28],
    113:[20,27,28],
    114:[20,27,28],
    115:[20,27,28],
    116:[20,27,28],
    117:[20,27,28],
    118:[20,27,28],
    119:[20,27,28],
    120:[20,27,28],
    121:[25,28],
    122:[25,28],
    123:[25,28],
    124:[25,28],
    125:[25,28],
    126:[25,28],
    127:[25,28],
    128:[25,28],
    129:[25,28],
    130:[25,28],
    131:[25,28],
    132:[25,28],
    133:[25,28],
    134:[25,28],
    135:[25,28],
    136:[25,28],
    137:[25,28,29,30],
    138:[25,28,29,30],
    139:[25,28,29,30],
    140:[25,28,29,30],
    141:[25,28,29,30],
    142:[25,28,29,30],
    143:[25,28,29,30],
    144:[20,26],
    145:[20,26],
    146:[20,26],
    147:[20,26],
    148:[20,26],
    149:[20,26],
    150:[20,26],
    151:[20,26],
    152:[20,26],
    153:[20,26],
    154:[20,26],
    155:[20,26],
    156:[20,26],
    157:[20,26],

}

# Dictionary R ke T
# array requirement:[array test]
# R_to_T = {
#     0:[1,2],
#     1:[0,2]
# }

#misal t1 itu satisfy r1 dan r2:
    #maka, TP dari t1 --> nilai RP r1 + RP r3 = 17,5 + 14
    # r1 = create event, r3 = edit event, t1 ini dia mengetes fungsionalitas dari form inputan 
def calculateTP(testCaseToReqID):
    # sum([requirements_list[f'r{req_id}'].RP for req_id in T_to_R[testCaseToReqID] ])
    total_tp = 0
    for req_id in T_to_R[testCaseToReqID]:
        total_tp += requirements_list[f'r{req_id}'].RP
    testCase_list[testCaseToReqID].setTP(total_tp)     

def main():
    req_mgr = RequirementManagement()

    req_mgr.add_requirement('r1', 0, 0),
    req_mgr.add_requirement('r2', 0, 0),
    req_mgr.add_requirement('r3', 0, 0),
    req_mgr.add_requirement('r4', 0, 0),
    req_mgr.add_requirement('r5', 0, 0),
    req_mgr.add_requirement('r6', 0, 0),
    req_mgr.add_requirement('r7', 0, 0),
    req_mgr.add_requirement('r8', 0, 0),
    req_mgr.add_requirement('r9', 0, 0),
    req_mgr.add_requirement('r10', 10, 8),
    req_mgr.add_requirement('r11', 0, 0),
    req_mgr.add_requirement('r12', 0, 0),
    req_mgr.add_requirement('r13', 8, 8),
    req_mgr.add_requirement('r14', 0, 0),
    req_mgr.add_requirement('r15', 7, 7),
    req_mgr.add_requirement('r16', 0, 0),
    req_mgr.add_requirement('r17', 9, 8),
    req_mgr.add_requirement('r18', 8, 7),
    req_mgr.add_requirement('r19', 8, 7),
    req_mgr.add_requirement('r20', 0, 0),
    req_mgr.add_requirement('r21', 0, 0),
    req_mgr.add_requirement('r22', 8, 7),
    req_mgr.add_requirement('r23', 0, 0),
    req_mgr.add_requirement('r24', 8, 7),
    req_mgr.add_requirement('r25', 0, 0),
    req_mgr.add_requirement('r26', 0, 0),
    req_mgr.add_requirement('r27', 8, 7),
    req_mgr.add_requirement('r28', 0, 0),
    req_mgr.add_requirement('r29', 0, 0),
    req_mgr.add_requirement('r30', 8, 8)


    # Untuk setiap index pada test Case di range testCase_list, print test case index
    for testCase_index in range(len(testCase_list)):
        calculateTP(testCase_index)
        # print(testCase_list[testCase_index])

    # Mengurutkan Test case
    sorted_TestCase = sorted(testCase_list, key=lambda x: x.TP, reverse=True)
    # print(sorted_TestCase)
    # print(testCase_list)

    for testcase in sorted_TestCase:
        print(str(testcase))

    # requirements_list['r1'].add_child(requirements_list['r2'])
    
    # Add Child dari Requirement
    #child R1
    req_mgr.add_child('r1', 'r2')
    req_mgr.add_child('r1', 'r3')

    #child R3
    req_mgr.add_child('r3', 'r4')
    req_mgr.add_child('r3', 'r5')
    req_mgr.add_child('r3', 'r6')
    req_mgr.add_child('r3', 'r7')
    req_mgr.add_child('r3', 'r8')
    req_mgr.add_child('r3', 'r9')
    req_mgr.add_child('r3', 'r19')
    req_mgr.add_child('r3', 'r20')
    req_mgr.add_child('r3', 'r24')

    #child R8
    req_mgr.add_child('r8', 'r18')

    #child R9
    req_mgr.add_child('r9', 'r10')

    #child R10
    req_mgr.add_child('r10', 'r11')

     #child R11
    req_mgr.add_child('r11', 'r12')

     #child R12
    req_mgr.add_child('r12', 'r13')

    #child R13
    req_mgr.add_child('r13', 'r14')
    req_mgr.add_child('r13', 'r15')
    req_mgr.add_child('r13', 'r16')

    #child R19
    req_mgr.add_child('r19', 'r17')

    #child R20
    req_mgr.add_child('r20', 'r21')

    #child R21
    req_mgr.add_child('r21', 'r22')
    req_mgr.add_child('r21', 'r23')    

    #child R24
    req_mgr.add_child('r24', 'r25')
    req_mgr.add_child('r24', 'r26')  
    req_mgr.add_child('r24', 'r27')
    req_mgr.add_child('r24', 'r28')

    #child R28
    req_mgr.add_child('r28', 'r29')
    req_mgr.add_child('r28', 'r30')      

    # print(req_mgr.get_req('r5'))
    # print(req_mgr.get_req('r3'))
    # print(req_mgr.get_req('r6'))    
    # print([str(i) for i in requirements_list['r5'].childs])

    # req = req_mgr.get_req('r5')
    # print(req)
    # req.RP += 5
    # print(req_mgr.get_req('r5'))

    # Masukkan Req yang terdeteksi fault
    print('AFTER')
    failed_reqs = ['r10', 'r12','r13','r14','r15']
    for f_req in failed_reqs:
        req = req_mgr.get_req(f_req)
        req.parent.RP += 4
        req.RP += 5

        for sibling in req.parent.childs:
            if sibling.r_name==req.r_name:
                continue
            sibling.RP += 3

        for child in req.childs:
            child.RP += 2

    # print(req_mgr.get_req('r5'))
    # print(req_mgr.get_req('r3'))
    # print(req_mgr.get_req('r6'))    
    # print([str(i) for i in requirements_list['r5'].childs])

    for testCase_index in range(len(testCase_list)):
        calculateTP(testCase_index)

    sorted_TestCase = sorted(testCase_list, key=lambda x: x.TP, reverse=True)
    # print(sorted_TestCase)
    # print(testCase_list)

    for testcase in sorted_TestCase:
        print(str(testcase))
# Setelah testing pertama, ditemukan fault pada r5 dan r7, 
#         - maka tambahkan poin 5 pada r5 dan r7. 
#         - tambahkan poin 4 ke parent node, 
#         - tambahkan poin 3 ke sibling node, 
#         - tambahkan poin 2 ke child node
    
main()
