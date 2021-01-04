# Playstation store base link
PSSTR = 'https://store.playstation.com'
PS_PRODUCT = PSSTR + '/es-es/product/'
PSSTR_SEARCH = PSSTR + '/es-es/grid/search-game/1?gameContentType=games&query='

# Steam store base link
STMSTR = 'https://store.steampowered.com'
STM_PRODUCT = STMSTR + '/app/'
STMSTR_SEARCH = STMSTR + '/search/?term='

# Games URLs
GAMES = {'read-dead-redemption-2':{'ps':'EP1004-CUSA08519_00-REDEMPTION000002','st':'1174180/Red_Dead_Redemption_2/'},
         'spyro':{'ps':'EP0002-CUSA12085_00-SPYROTRILOGY0001','st':None},
         'sekiro':{'ps':'EP0002-CUSA13801_00-SEKIROGAME000001','st':'814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/'},
         'god-of-war':{'ps':'EP9000-CUSA07411_00-0000000GODOFWARN','st':None},
         'nier-automata':{'ps':'EP0082-CUSA04480_00-GOTYORHADIGITAL0','st':'app/524220/NieRAutomata/'},
         'doom':{'ps':'EP1003-CUSA02092_00-DOOMEUROPEROWSKU','st':'379720/DOOM/'},
         'doom-eternal':{'ps':'EP1003-CUSA13275_00-DOOMETERNALBUNDL','st':'782330/DOOM_Eternal/'},
         'shadow-of-the-colossus':{'ps':'EP9000-CUSA08809_00-SOTC0000000000EU','st':None},
         'the-last-of-us-parte-2':{'ps':'EP9000-CUSA10249_00-THELASTOFUSPART2','st':None},
         'prey':{'ps':'EP1003-CUSA06560_00-PREYPS4FULLGAME1','st':'480490/Prey/'},
         'no-mans-sky':{'ps':'EP2034-PPSA01412_00-NOMANSSKYHG00001','st':'275850/No_Mans_Sky/'},
         'yakuza-6':{'ps':'EP0177-CUSA09660_00-YAKUZA6SONGOFLEN','st':None},
         'persona-5':{'ps':'EP4062-CUSA06638_00-PERSONA512345678','st':None},
         'cuphead':{'ps':'EP8254-CUSA20469_00-CUPHEAD000000000','st':'268910/Cuphead/'},
         'death-stranding':{'ps':'EP9000-CUSA12606_00-DEATHSTRAND00001','st':None},
         'devil-may-cry-5':{'ps':'EP0102-CUSA08161_00-DMC5000000000001','st':'601150/Devil_May_Cry_5/'},
         'mafia-1':{'ps':'EP1001-CUSA18100_00-MAFIAONEREMASTER','st':'1030840/Mafia_Edicin_Definitiva/'},
         'mafia-2':{'ps':'EP1001-CUSA17761_00-MAFIATWOREMASTER','st':'1030830/Mafia_II_Edicin_Definitiva/'},
         'days-gone':{'ps':'EP9000-CUSA09175_00-DAYSGONECOMPLETE','st':None},
         'middle-earth-2':{'ps':'EP1018-CUSA04402_00-KRAKENEDIT0STAND','st':'356190/Middleearth_Shadow_of_War/'},
         'kingdom-hearts-3-re-mind':{'ps':'EP0082-CUSA12025_00-KHX30DLC00000003','st':None},
         'kingdom-hearts-1.5+2.5 remix':{'ps':'EP0082-CUSA05786_00-KINGDOMHEART1525','st':None},
         'kingdom-hearts-2.8':{'ps':'EP0082-CUSA05787_00-KINGDOMHEARTSX28','st':None},
         'assassins-creed-origins':{'ps':'EP0001-CUSA05625_00-GAMEACEMPIRE0000','st':'582160/Assassins_Creed_Origins/'},
         'yakuza:-like-a_dragon':{'ps':'EP0177-CUSA16745_00-SHINRYUGAGOTOKEN','st':'1235140/Yakuza_Like_a_Dragon/'},
         'yakuza-remastered-collection':{'ps':'EP0177-CUSA15360_00-YAKUZAREMASTERED','st':None},
         'dark-souls-1':{'ps':'EP0700-CUSA08495_00-DARKSOULSHD00000','st':'570940/DARK_SOULS_REMASTERED/'},
         'dark-souls-3':{'ps':'EP0700-CUSA03365_00-DARKSOULS3000000','st':'374320/DARK_SOULS_III/'},
         'star-wars-jedi:-fallen-order':{'ps':'EP0006-CUSA12529_00-RESPAWNSWBIRDDOG','st':'1172380/STAR_WARS_Jedi_La_Orden_cada/'},
         'final-fantasy-7-remake':{'ps':'EP0082-CUSA07187_00-FFVIIREMAKE00000','st':None},
         'kentucky-route-zero':{'ps':'EP2333-CUSA10030_00-KRZTVSIEE0000000','st':'231200/Kentucky_Route_Zero_PC_Edition/'}
        }