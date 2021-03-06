# parâmetros
MMA_INTERVAL = 40
MME_INTERVAL = periodo_considerado = 9  # período considerado
k_value_on_mme = 2 / (periodo_considerado + 1)  # valor de k na MME
N_MAIORES_BM = 10
# capital_total_inicial = 100000  # capital inicial total
# acoes_na_carteira = 10  # ações da carteira

ABREVIATURA_ACOES_CHOICES = (
    (1, 'AMAR3'),
    (2, 'ARTR3'),
    (3, 'BBAS3'),
    (4, 'BBRK3'),
    (5, 'BEEF3'),
    (6, 'BRFS3'),
    (7, 'BRML3'),
    (8, 'BTOW3'),
    (9, 'BVMF3'),
    (10, 'CARD3'),
    (11, 'CCRO3'),
    (12, 'CIEL3'),
    (13, 'CPFE3'),
    (14, 'CSAN3'),
    (15, 'CSMG3'),
    (16, 'CYRE3'),
    (17, 'DASA3'),
    (18, 'DTEX3'),
    (19, 'EMBR3'),
    (20, 'ENBR3'),
    (21, 'ENEV3'),
    (22, 'EQTL3'),
    (23, 'ESTC3'),
    (24, 'ETER3'),
    (25, 'EVEN3'),
    (26, 'EZTC3'),
    (27, 'FHER3'),
    (28, 'FIBR3'),
    (29, 'FLRY3'),
    (30, 'GFSA3'),
    (31, 'GRND3'),
    (32, 'GSHP3'),
    (33, 'HBOR3'),
    (34, 'HGTX3'),
    (35, 'HYPE3'),
    (36, 'IDNT3'),
    (37, 'IGTA3'),
    (38, 'JBSS3'),
    (39, 'JHSF3'),
    (40, 'LIGT3'),
    (41, 'LOGN3'),
    (42, 'LPSB3'),
    (43, 'LREN3'),
    (44, 'LUPA3'),
    (45, 'MAGG3'),
    (46, 'MDIA3'),
    (47, 'MMXM3'),
    (48, 'MRFG3'),
    (49, 'MRVE3'),
    (50, 'MYPK3'),
    (51, 'NATU3'),
    (52, 'ODPV3'),
    (53, 'OGXP3'),
    (54, 'PDGR3'),
    (55, 'PMAM3'),
    (56, 'POSI3'),
    (57, 'PRML3'),
    (58, 'PSSA3'),
    (59, 'RADL3'),
    (60, 'RENT3'),
    (61, 'RNAR3'),
    (62, 'RSID3'),
    (63, 'SBSP3'),
    (64, 'SLCE3'),
    (65, 'SMTO3'),
    (66, 'TBLE3'),
    (67, 'TCSA3'),
    (68, 'TGMA3'),
    (69, 'TIMP3'),
    (70, 'TOTS3'),
    (71, 'TPIS3'),
    (72, 'VAGR3'),
    (73, 'VIVR3'),
    (74, 'VLID3'),
    (75, 'WEGE3'),
)

NOME_ACOES_CHOICES = (
    (1, 'Lojas Marisa'),
    (2, 'Arteris'),
    (3, 'Brasil'),
    (4, 'BR Brokers'),
    (5, 'Minerva'),
    (6, 'BRF SA'),
    (7, 'BR Malls Par'),
    (8, 'B2W Digital'),
    (9, 'BmfBovespa'),
    (10, 'Csu Cardsyst'),
    (11, 'CCR SA'),
    (12, 'Cielo'),
    (13, 'CPFL Energia'),
    (14, 'Cosan'),
    (15, 'Copasa'),
    (16, 'Cyrela Realt'),
    (17, 'Dasa'),
    (18, 'Duratex'),
    (19, 'Embraer'),
    (20, 'Energias BR'),
    (21, 'Eneva'),
    (22, 'Equatorial'),
    (23, 'Estacio Part'),
    (24, 'Eternit'),
    (25, 'Even'),
    (26, 'Eztec'),
    (27, 'Fer Heringer'),
    (28, 'Fibria'),
    (29, 'Fleury'),
    (30, 'Gafisa'),
    (31, 'Grendene'),
    (32, 'Generalshopp'),
    (33, 'Helbor'),
    (34, 'Cia Hering'),
    (35, 'Hypermarcas'),
    (36, 'Ideiasnet'),
    (37, 'Iguatemi'),
    (38, 'JBS'),
    (39, 'JHSF Part'),
    (40, 'Light S/A'),
    (41, 'Log-In'),
    (42, 'Lopes Brasil'),
    (43, 'Lojas Renner'),
    (44, 'Lupatech'),
    (45, 'Magnesita SA'),
    (46, 'M.Diasbranco'),
    (47, 'MMX Miner'),
    (48, 'Marfrig'),
    (49, 'MRV'),
    (50, 'Iochp-Maxion'),
    (51, 'Natura'),
    (52, 'Odontoprev'),
    (53, 'OGX Petroleo'),
    (54, 'PDG Realt'),
    (55, 'Paranapanema'),
    (56, 'Positivo Inf'),
    (57, 'Prumo'),
    (58, 'Porto Seguro'),
    (59, 'RaiaDrogasil'),
    (60, 'Localiza'),
    (61, 'Renar'),
    (62, 'Rossi Resid'),
    (63, 'Sabesp'),
    (64, 'SLC Agricola'),
    (65, 'Sao Martinho'),
    (66, 'Tractebel'),
    (67, 'Tecnisa'),
    (68, 'Tegma'),
    (69, 'Tim Part S/A'),
    (70, 'Totvs'),
    (71, 'Triunfo Part'),
    (72, 'V-Agro'),
    (73, 'Viver'),
    (74, 'Valid'),
    (75, 'Weg'),
)

DECISAO_CHOICES = (
    (1, 'Comprar'),
    (2, 'Vender'),
    (3, None)
)
