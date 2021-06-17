from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6645B4, Add, -100663296),# units:Graphics  index:191    from 43 To 37
        SetMemory(0x6606AC, Add, 536870912),# units:Unit Direction  index:191    from 0 To 32
        SetMemory(0x66486C, Add, 16777216),# units:Shield Enable  index:191    from 0 To 1
        SetMemory(0x660F7C, Add, 3276800),# units:Shield Amount  index:191    from 100 To 150
        SetMemory(0x660F98, Add, -6553600),# units:Shield Amount  index:205    from 100 To 0
        SetMemory(0x660F9C, Add, -100),# units:Shield Amount  index:206    from 100 To 0
        SetMemory(0x66264C, Add, -25548800),# units:Hit Points  index:191    from 25600000 To 51200
        SetMemory(0x662684, Add, -25600000),# units:Hit Points  index:205    from 25600000 To 0
        SetMemory(0x662688, Add, -25600000),# units:Hit Points  index:206    from 25600000 To 0
        SetMemory(0x66320C, Add, 251658240),# units:Elevation Level  index:191    from 1 To 16
        SetMemory(0x66321C, Add, 720896),# units:Elevation Level  index:206    from 4 To 15
        SetMemory(0x661084, Add, 3305111552),# units:Unknown (old Movement)  index:191    from 0 To 197
        SetMemory(0x663E8C, Add, 167772160),# units:Rank/Sublabel  index:191    from 0 To 10
        SetMemory(0x662F5C, Add, 1795162112),# units:Comp AI Idle  index:191    from 23 To 130
        SetMemory(0x662324, Add, 1795162112),# units:Human AI Idle  index:191    from 23 To 130
        SetMemory(0x664954, Add, -352321536),# units:Return to Idle  index:191    from 23 To 2
        SetMemory(0x6633DC, Add, -218103808),# units:Attack Unit  index:191    from 23 To 10
        SetMemory(0x663B0C, Add, -352321536),# units:Attack Move  index:191    from 23 To 2
        SetMemory(0x663774, Add, -889192448),# units:Ground Weapon  index:191    from 130 To 77
        SetMemory(0x66469C, Add, 16777216),# units:Max Ground Hits  index:191    from 0 To 1
        SetMemory(0x66179C, Add, -889192448),# units:Air Weapon  index:191    from 130 To 77
        SetMemory(0x65FCD4, Add, 16777216),# units:Max Air Hits  index:191    from 0 To 1
        SetMemory(0x660234, Add, -50331648),# units:AI Internal  index:191    from 3 To 0
        SetMemory(0x664174, Add, -4194304),# units:Special Ability Flags  index:61    from 406913024 To 402718720
        SetMemory(0x66437C, Add, 975175683),# units:Special Ability Flags  index:191    from 536870913 To 1512046596
        SetMemory(0x662E74, Add, 83886080),# units:Target Acquisition Range  index:191    from 0 To 5
        SetMemory(0x6632F4, Add, 16777216),# units:Sight Range  index:191    from 8 To 9
        SetMemory(0x66368C, Add, -905969664),# units:Armor Upgrade  index:191    from 60 To 6
        SetMemory(0x66223C, Add, 50331648),# units:Unit Size  index:191    from 0 To 3
        SetMemory(0x65FF84, Add, 16777216),# units:Armor  index:191    from 0 To 1
        SetMemory(0x662154, Add, 16777216),# units:Right-click Action  index:191    from 0 To 1
        SetMemory(0x66012C, Add, 35651584),# units:What Sound Start  index:191    from 15 To 559
        SetMemory(0x66014C, Add, -2),# units:What Sound Start  index:206    from 26 To 24
        SetMemory(0x662D6C, Add, 35848192),# units:What Sound End  index:191    from 15 To 562
        SetMemory(0x662D8C, Add, -2),# units:What Sound End  index:206    from 27 To 25
        SetMemory(0x662B5C, Add, -96),# units:StarEdit Placement Box Width  index:191    from 96 To 0
        SetMemory(0x662B94, Add, -135),# units:StarEdit Placement Box Width  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -135),# units:StarEdit Placement Box Width  index:206    from 136 To 1
        SetMemory(0x662B5C, Add, -4194304),# units:StarEdit Placement Box Height  index:191    from 64 To 0
        SetMemory(0x662B94, Add, -8847360),# units:StarEdit Placement Box Height  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -8847360),# units:StarEdit Placement Box Height  index:206    from 136 To 1
        SetMemory(0x661DC0, Add, -47),# units:Unit Size Left  index:191    from 48 To 1
        SetMemory(0x661E30, Add, -25),# units:Unit Size Left  index:205    from 25 To 0
        SetMemory(0x661E38, Add, -44),# units:Unit Size Left  index:206    from 44 To 0
        SetMemory(0x661DC0, Add, -2031616),# units:Unit Size Up  index:191    from 32 To 1
        SetMemory(0x661E30, Add, -1114112),# units:Unit Size Up  index:205    from 17 To 0
        SetMemory(0x661E38, Add, -1114112),# units:Unit Size Up  index:206    from 17 To 0
        SetMemory(0x661DC4, Add, -45),# units:Unit Size Right  index:191    from 47 To 2
        SetMemory(0x661E34, Add, -43),# units:Unit Size Right  index:205    from 44 To 1
        SetMemory(0x661E3C, Add, -24),# units:Unit Size Right  index:206    from 25 To 1
        SetMemory(0x661DC4, Add, -1900544),# units:Unit Size Down  index:191    from 31 To 2
        SetMemory(0x661E34, Add, -1245184),# units:Unit Size Down  index:205    from 20 To 1
        SetMemory(0x661E3C, Add, -1245184),# units:Unit Size Down  index:206    from 20 To 1
        SetMemory(0x663104, Add, 524288),# units:Portrait  index:191    from 38 To 46
        SetMemory(0x663A04, Add, -16384000),# units:Mineral Cost  index:191    from 250 To 0
        SetMemory(0x663A20, Add, -65536),# units:Mineral Cost  index:205    from 1 To 0
        SetMemory(0x663A24, Add, -1),# units:Mineral Cost  index:206    from 1 To 0
        SetMemory(0x65FE98, Add, -65536),# units:Vespene Cost  index:205    from 1 To 0
        SetMemory(0x65FE9C, Add, -1),# units:Vespene Cost  index:206    from 1 To 0
        SetMemory(0x6605C0, Add, -65536),# units:Build Time  index:205    from 1 To 0
        SetMemory(0x6605C4, Add, -1),# units:Build Time  index:206    from 1 To 0
        SetMemory(0x66385C, Add, 184549376),# units:Staredit Group Flags  index:191    from 1 To 12
        SetMemory(0x663DA4, Add, 134217728),# units:Supply Required  index:191    from 0 To 8
        SetMemory(0x663584, Add, 67174400),# units:Build Score  index:191    from 0 To 1025
        SetMemory(0x664034, Add, 134348800),# units:Destroy Score  index:191    from 0 To 2050
        SetMemory(0x661558, Add, 131072),# units:Staredit Availability Flags  index:33    from 0 To 2
        SetMemory(0x661694, Add, 30343168),# units:Staredit Availability Flags  index:191    from 0 To 463
        SetMemory(0x6616B0, Add, 131072),# units:Staredit Availability Flags  index:205    from 32 To 34
        SetMemory(0x6616B4, Add, 2),# units:Staredit Availability Flags  index:206    from 32 To 34
    ])

