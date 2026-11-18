---
title: "Online Resource 1 — Data Appendix"
---

**AI-Driven Circular Business Models for Date Palm Waste Valorization in Algeria's El Oued Region**

Rabiaa Bousbia Laiche and Rachid Belmessaoud, University of El Oued, Algeria

# Purpose and contents

This appendix reproduces the tables of the open database that accompanies the chapter (version 1.5.0) and documents how it was assembled. It serves three purposes: to let readers check every figure used in the chapter, to record the audit of the working files from which the project started, and to list the data that the study still needs.

Every value in the database carries a status flag. **Official** values come from FAOSTAT, the World Bank or Algerian public bodies, directly or as reported by named outlets. **Literature** values come from peer-reviewed studies. **Derived** values are computed by the build script from inputs stated in the same row. **Unverified** values come from the authors' working files and are not used as evidence.

# Cleaning and assembly procedure

1. *Inventory.* Fifteen files were received; checksums showed six distinct files. Two (a UN Comtrade extract and its classification table) concern exports of minerals and metals and contain no date products; they were set aside. An earlier World Bank governance extract (2000-2023) was superseded by the 2025 release.
2. *Lineage.* The ten-wilaya panel (Classeur_PIML_v2_Panel60) was found to be copied from a seven-sheet working workbook: all 60 production values are identical. Both are kept unchanged in `data/raw/`.
3. *Audit.* Seventeen claims of the workbook were checked against official figures or against the workbook itself (Table A12); fourteen were contradicted. No value from either working file is used as evidence.
4. *Replacement.* Official national series, wilaya statements, trade figures, regional structure, yields and prices were collected from public sources with links (Tables A1-A5). Governance indicators for Algeria, Egypt, Tunisia and Qatar were extracted from the WGI 2025 release (Table A6).
5. *Coefficients and derivation.* Residue coefficients, composition and conversion data were taken from peer-reviewed studies (Tables A7-A9). El Oued scenarios and their sensitivity were computed from official production, palm-stock bounds implied by official figures and literature coefficients only (Tables A10-A11).
6. *Validation.* A script checks status flags, internal sums, the ordering of scenarios and the presence of a source link for every official statement. The database is rebuilt from the raw files with one command.
7. *Gaps.* Variables required by the chapter but absent from any located source were listed with their holder and collection method (Table A14).
8. *Compilation of November 2026.* A secondary-data search against the collection plan was checked against its documents. Verified ministry statistics for 2020 by wilaya are in Table A15; the other indicators are in Table A16 with their verification status. Seven of its claims were corrected or set aside, and the boundary basis of the 2020 figures was added (database corrections log, items 16-23).


# Production, trade and structure

Table: **Table A1** National date production, Algeria, 2015-2024

| Year | Production (t) | Status | Source |
|------------|---------------|------------------------------|--------------------------------------|
| 2015 | 990,377 | observed_official | FAOSTAT, reproduced by Knoema |
| 2016 | 1,029,596 | observed_official | FAOSTAT, reproduced by Knoema |
| 2017 | 1,058,600 | observed_official | FAO-based series, reproduced by Knoema |
| 2018 | 1,094,700 | observed_official | FAOSTAT, reproduced by HelgiLibrary |
| 2019 | 1,136,025 | observed_official | FAOSTAT, reproduced by HelgiLibrary |
| 2020 | 1,151,909 | observed_official | FAOSTAT, reproduced by HelgiLibrary |
| 2021 | 1,188,803 | observed_official | FAOSTAT, reproduced by HelgiLibrary |
| 2022 | 1,242,304 | observed_official | FAOSTAT, reproduced by HelgiLibrary |
| 2023 | 1,320,000 | observed_official_rounded | FAO figure as charted by Statista (1.32 Mt, rounded) |
| 2024 | 1,337,301 | observed_secondary | FAO-based figure reported by Selina Wamucii |

*Note.* 2024 refers to the 2024-2025 campaign where the source says so.

Table: **Table A2** World production and Algeria's share, 2021-2023

| Year | World (t) | Algeria (t) | Share (%) | Source |
|------------|--------------|--------------|------------|--------------------------------------|
| 2021 | 9,656,378 | 1,188,803 | 12.3 | FAOSTAT, reproduced by HelgiLibrary |
| 2022 | 9,747,570 | 1,242,304 | 12.7 | FAOSTAT, reproduced by HelgiLibrary |
| 2023 | 9,820,000 | 1,320,000 | 13.4 | FAO figures as charted by Statista (rounded) |

Table: **Table A3** Date exports, 2023-2025, as reported by three compilers

| Year | Volume (t) | Value (M USD) | Unit value (USD/t) | Share of production (%) | Source |
|------------|------------|-------------|------------------|-----------------------|--------------------------------------|
| 2023 | 83,000 | 73.0 | 880 | 6.3 | ONS, as reported by TSA |
| 2024 | 66,948 | 108.4 | 1,619 | 5.0 | Trade Map, as reported by Agence Ecofin |
| 2024 | 26,481 | 87.1 | 3,289 | 2.0 | UN Comtrade, as reported by Selina Wamucii |
| 2025 | 185,000 | 184.0 | 995 | n.a. | Trade Map, as reported by CapMad ('near' 185,000 t, 'about' 184 M USD) |

*Note.* Compilers disagree by a factor of 2.5 on the 2024 volume. All are reported; none is preferred.

Table: **Table A4** Regional structure (2017), Deglet Nour yields and local prices (2016-2017)

| Wilaya | Indicator | Value | Source |
|------------|--------------------------------------|------------|-----------------|
| Biskra | Share of palm area (%) | 27.4 | MADRP (2017) |
| El Oued | Share of palm area (%) | 22.0 | MADRP (2017) |
| Biskra | Share of palms (%) | 23.1 | MADRP (2017) |
| El Oued | Share of palms (%) | 22.4 | MADRP (2017) |
| Biskra | Share of production (%) | 41.2 | MADRP (2017) |
| El Oued | Share of production (%) | 25.0 | MADRP (2017) |
| Biskra | Deglet Nour yield (kg/palm) | 80-85 | ITDAS (2016-2017) |
| Ouargla | Deglet Nour yield (kg/palm) | 70-76 | ITDAS (2016-2017) |
| El Oued | Deglet Nour yield (kg/palm) | 60-65 | ITDAS (2016-2017) |
| Biskra | Deglet Nour price on branch, local market (DZD/kg) | 300-450 | ITDAS (2016-2017) |
| El Oued | Deglet Nour price on branch, local market (DZD/kg) | 130-250 | ITDAS (2016-2017) |

*Note.* Pre-2021 administrative boundaries.

Table: **Table A5** Official statements on production, palm stock and area, national and by wilaya

| Area | Period | Indicator | Value | Unit | Boundary and qualifiers | Source |
|---------------------------|----------------------|----------------------|---------------|------------|--------------------------------------|--------------------------------------|
| Biskra | 2017 | production | 4,380,000 | quintal | pre-2021 boundaries (incl. Ouled Djellal) | Algerie-Eco, ministry figures |
| El Oued | 2017 | production | 2,600,000 | quintal | pre-2021 boundaries (incl. El Meghaier) | Algerie-Eco, ministry figures |
| Ouargla | 2017 | production | 1,400,000 | quintal | pre-2021 boundaries (incl. Touggourt) | Algerie-Eco, ministry figures |
| El Oued | 2019 | productive palms | 4,000,000 | palm | pre-2021 boundaries (Souf and Oued Righ) | APS, Chamber of Agriculture statement |
| El Oued | 2019 | production | 3,000,000 | quintal | pre-2021 boundaries (Souf and Oued Righ); stated as 'more than' | APS, Chamber of Agriculture statement |
| El Oued | 2019 | palm area | 40,000 | hectare | pre-2021 boundaries (Souf and Oued Righ) | APS, Chamber of Agriculture statement |
| El Oued | 2021 | palms total | 4,600,000 | palm | boundary basis not stated; consistent with pre-2021 boundaries | An-Nasr, April 2021 |
| El Oued | 2021 | production | 2,800,000 | quintal | boundary basis not stated; consistent with pre-2021 boundaries | An-Nasr, April 2021 |
| El Oued | season before May 2023 | production | 1,200,000 | quintal | current boundaries (after separation of El Meghaier) | APS dispatch reproduced by allAfrica, May 2023 |
| El Oued | season before May 2023 | production deglet nour | 728,000 | quintal | current boundaries | APS dispatch reproduced by allAfrica, May 2023 |
| El Meghaier | 2021 | productive palms | 2,500,000 | palm | current boundaries; 20,000 ha; 1.4 million Deglet Nour palms | El Maghreb El Awsat (20 March 2021) |
| El Meghaier | 2024-2025 | productive palms | 2,760,000 | palm | current boundaries; stated as 'more than' | El Ittihad, DSA El Meghaier |
| El Meghaier | 2024-2025 | production | 1,660,000 | quintal | current boundaries; forecast stated as 'at least' | El Ittihad, DSA El Meghaier |
| El Meghaier | 2025-2026 | production | 2,000,000 | quintal | current boundaries; forecast stated as 'more than' | El Ikhbaria (26 November 2025), citing APS |
| El Meghaier | 2025-2026 | production deglet nour | 1,320,000 | quintal | current boundaries; forecast | El Ikhbaria (26 November 2025), citing APS |
| El Meghaier | 2025-2026 | palms total | 3,000,000 | palm | current boundaries | El Ikhbaria (26 November 2025), citing APS |
| El Meghaier | 2025-2026 | productive palms | 2,400,000 | palm | current boundaries | El Ikhbaria (26 November 2025), citing APS |
| Touggourt | season not dated | production | 1,042,711 | quintal | current boundaries | AlgeriaInvest |
| Ouargla | 2018-2019 | production | 1,650,164 | quintal | pre-2021 boundaries (incl. Touggourt) | Journal article, University of Ouargla authors |
| Ouargla | 2024-2025 | production | 904,489 | quintal | current boundaries | Radio Algerie, DSA Ouargla |
| Ouargla | 2025-2026 | production | 920,142 | quintal | current boundaries | Radio Algerie, DSA Ouargla |
| Ouargla | 2025-2026 | palms total | 1,259,632 | palm | current boundaries | Radio Algerie, DSA Ouargla |
| Ouargla | 2025-2026 | palm area | 11,451 | hectare | current boundaries | Radio Algerie, DSA Ouargla |
| Biskra | 2023-2024 | production | 4,000,000 | quintal | current boundaries; forecast stated as 'more than' | Awras, DSA Biskra |
| Biskra | 2026 | palms total | 4,200,000 | palm | current boundaries; stated as 'more than' | El Massa |
| Ouled Djellal | 2025-2026 | production | 900,000 | quintal | current boundaries; forecast stated as 'more than' | Horizons, APS |
| Algeria | 2010 | production | 644,740 | tonne | national | FAO figures cited in a paper of the 5th International Date Palm Conference |
| Algeria | 2010 | palm area | 161,090 | hectare | national | FAO figures cited in a paper of the 5th International Date Palm Conference |
| Algeria | 2017 | palm area | 167,000 | hectare | national | MADRP (2017), as reproduced in a University of Biskra thesis |
| Algeria | 2017 | palms total | 18,600,000 | palm | national; stated as 'more than' | MADRP (2017), as reproduced in a University of Biskra thesis |
| Algeria | 2017 | production | 990,000 | tonne | national; stated as 'nearly' | MADRP (2017), as reproduced in a University of Biskra thesis |
| Algeria | about 2022 | palms total | 20,000,000 | palm | national; stated as 'nearly'; 17 producing wilayas | El Moudjahid |
| Algeria | about 2022 | palm area | 170,000 | hectare | national | El Moudjahid |
| Biskra | about 2022 | palms total | 4,500,000 | palm | current boundaries | El Moudjahid |
| Biskra | 2021 | palms total | 4,345,045 | palm | boundary basis not stated | DSA figures (2021) reproduced in a University of Ouargla doctoral thesis |
| Ouargla | 2021 | palms total | 2,568,511 | palm | boundary basis not stated | DSA Ouargla (2021) reproduced in a University of Ouargla doctoral thesis |
| Ouargla | 2021 | productive palms | 2,133,184 | palm | boundary basis not stated | DSA Ouargla (2021) reproduced in a University of Ouargla doctoral thesis |
| Biskra | 2023-2024 | production deglet nour | 2,400,000 | quintal | current boundaries; forecast; 60% of the total | Algerie-Eco, DSA Biskra |
| Algeria (five main wilayas) | 2019 | palms total | 19,063,249 | palm | Biskra, El Oued, Adrar, Ouargla, Ghardaia; pre-2021 boundaries | Journal article citing MADR (2022) |

*Note.* Source links for every row are in wilaya_official_benchmarks.csv. One quintal = 0.1 tonne.

# Institutional environment

Table: **Table A6** Worldwide Governance Indicators, estimates, 2015-2024

| Dimension | Country | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|--------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| GE | Algeria | -0.36 | -0.42 | -0.52 | -0.29 | -0.32 | -0.27 | -0.46 | -0.27 | -0.36 | -0.25 |
| GE | Egypt | -0.52 | -0.44 | -0.41 | -0.41 | -0.12 | -0.23 | -0.23 | -0.14 | -0.04 | -0.10 |
| GE | Tunisia | -0.01 | -0.06 | +0.05 | +0.10 | +0.06 | -0.03 | -0.01 | -0.15 | -0.17 | -0.24 |
| GE | Qatar | +1.03 | +1.03 | +0.97 | +0.81 | +0.94 | +0.96 | +1.13 | +1.19 | +1.15 | +1.13 |
| RQ | Algeria | -0.91 | -0.93 | -0.95 | -1.04 | -1.13 | -1.08 | -0.97 | -0.88 | -0.79 | -0.75 |
| RQ | Egypt | -0.74 | -0.77 | -0.71 | -0.74 | -0.70 | -0.64 | -0.57 | -0.67 | -0.57 | -0.50 |
| RQ | Tunisia | -0.38 | -0.43 | -0.12 | -0.12 | -0.14 | -0.11 | -0.20 | -0.33 | -0.43 | -0.39 |
| RQ | Qatar | +0.77 | +0.77 | +0.56 | +0.68 | +0.79 | +0.84 | +0.84 | +0.88 | +0.94 | +0.97 |
| RL | Algeria | -0.88 | -0.86 | -0.87 | -0.85 | -0.85 | -0.78 | -0.76 | -0.80 | -0.73 | -0.70 |
| RL | Egypt | -0.84 | -0.84 | -0.78 | -0.74 | -0.75 | -0.79 | -0.82 | -0.77 | -0.78 | -0.75 |
| RL | Tunisia | -0.11 | -0.10 | -0.09 | -0.06 | -0.03 | -0.01 | -0.01 | -0.24 | -0.32 | -0.36 |
| RL | Qatar | +0.54 | +0.58 | +0.47 | +0.46 | +0.49 | +0.48 | +0.50 | +0.60 | +0.57 | +0.59 |
| CC | Algeria | -0.63 | -0.64 | -0.54 | -0.54 | -0.62 | -0.64 | -0.65 | -0.64 | -0.64 | -0.59 |
| CC | Egypt | -0.56 | -0.45 | -0.41 | -0.47 | -0.65 | -0.79 | -0.79 | -0.78 | -0.82 | -0.83 |
| CC | Tunisia | -0.01 | -0.06 | -0.05 | +0.00 | -0.03 | -0.02 | -0.14 | -0.20 | -0.19 | -0.22 |
| CC | Qatar | +0.84 | +0.86 | +0.75 | +0.75 | +0.88 | +0.88 | +0.84 | +0.82 | +0.78 | +0.76 |

*Note.* GE: government effectiveness; RQ: regulatory quality; RL: rule of law; CC: control of corruption. Scale about -2.5 (weak) to +2.5 (strong). World Bank, WGI 2025 release. 90 % confidence intervals and 0-100 scores in governance_wgi.csv.

# Residues: coefficients, composition and technology

Table: **Table A7** Residue coefficients

| Coefficient | Description | Value | Unit | Status | Source |
|----------------------|--------------------------------------|------------|-----------------|-------------------------|--------------------------------------|
| beta_low | Dry frond and leaf residues per palm per year; dry-matter basis | 20 | kg/palm/year | literature | Faiad et al. (2022), Sustainability 14(3):1134 |
| beta_central | Palm residues per tree per year (El-Juhany 2001, as cited); moisture basis not stated | 35 | kg/palm/year | literature_secondary | Nasser (2014), BioResources 9(3) |
| beta_high | Biowaste per palm per year from annual cleaning, Adrar (Algeria); as collected; includes palms, petioles, bunches and bunch peduncles | 65 | kg/palm/year | literature | Djaafri et al. (2024), Energies 17(11):2520 |
| beta_original | Dry fronds per palm per year used in the original workbook | 50 | kg/palm/year | unverified_working | Original workbook; no primary source located; inside the 20-65 range of the literature |
| alpha_low | Low-grade dates and pits as share of production, lower bound | 0.1 | t/t fruit | literature | Shi et al. (2023), Applied Sciences 13(22):12315 |
| alpha_central | Low-grade dates and pits as share of production, upper bound | 0.15 | t/t fruit | literature | Shi et al. (2023), Applied Sciences 13(22):12315 |
| alpha_high | Share of Algerian date production lost during picking, storage and marketing; chain-wide, not only at packing units | 0.3 | t/t fruit | literature | Boulal et al. (2016), African Journal of Biotechnology |
| pits_original | Pits as share of fruit mass used in the original workbook | 0.12 | t/t fruit | unverified_working | Original workbook; no primary source located |
| pedicels_original | Pedicels as share of fruit mass used in the original workbook | 0.08 | t/t fruit | unverified_working | Original workbook; no primary source located |
| culls_original | Sorting rejects as share of fruit mass used in the original workbook | 0.05 | t/t fruit | unverified_working | Original workbook; no primary source located |

Table: **Table A8** Measured composition and conversion yields

| Material | Property | Value | Unit | Source |
|-----------------------------|--------------------------------------|------------|------------|--------------------------------------|
| Date pits | Crude fibre | 37.72 | % DM | CIHEAM Options Mediterraneennes A109 (2014) |
| Date pits | Crude protein | 8.87 | % DM | CIHEAM Options Mediterraneennes A109 (2014) |
| Date pits | Fat | 6.29 | % DM | CIHEAM Options Mediterraneennes A109 (2014) |
| Date pits | In vitro dry matter digestibility | 22.78 | % | CIHEAM Options Mediterraneennes A109 (2014) |
| Palm leaves | Neutral detergent fibre | 609 | g/kg DM | Boufennara et al. (2016) |
| Palm leaves | Acid detergent fibre | 435 | g/kg DM | Boufennara et al. (2016) |
| Palm leaves | Lignin | 84 | g/kg DM | Boufennara et al. (2016) |
| Palm leaves | Crude protein | 64 | g/kg DM | Boufennara et al. (2016) |
| Low-value dates (Degla Beida) | Total sugars in juice | 62.89 | % | Guetni et al. (2024) |
| Low-value dates (Degla Beida) | Ethanol concentration after fermentation | 86.79 | g/l | Guetni et al. (2024) |
| Low-value dates (Timjouhart) | Ethanol concentration after fermentation | 68.64 | g/l | Guetni et al. (2024) |
| Common date waste | Ethanol yield | 250 | ml/kg | Boulal et al. (2016) |
| Low-quality dates | Ethanol yield | 350 | ml/kg | Oucif Khaled and Segni (2014) |

Table: **Table A9** Reported accuracy of date-grading models

| Study | Task | Images or samples | Model | Reported performance (%) |
|------------------------|--------------------------------------|-----------------|--------------------------------------|--------------------------------------|
| ElHelew et al. (2024) | Accepted versus rejected fruit; three Egyptian varieties | 5,945 | Inception-ResNet-v2 | 98.99 (accuracy) |
| Almutairi et al. (2024) | Detection and classification of nine Saudi varieties | 1,735 | YOLOv8 | 99.1 (precision) |
| Alhamdan and Howe (2021) | Nine varieties, controlled environment | 1,658 | Convolutional neural network | 97 (accuracy) |
| Neji et al. (2024) | Variety identification on two public data sets, Saudi Arabia and Turkey | not stated | DenseNet121 + Vision Transformer + XGBoost | 99.93 (Saudi set); 99.65 (Turkish set), accuracy |
| Aiadi et al. (2022) | Variety classification; public benchmark of 20 date varieties, Algerian authors | not stated | VGG-F and PCANet features fused by discriminant correlation analysis | benchmark introduced |
| Boumaraf et al. (2026) | Eight quality grades, Deglet Nour and Mech-Degla, samples from an industrial sorting facility in Algeria | 853 | Multi-view RGB, with and without thermal image and weight | fusion outperforms RGB alone for every architecture |

# El Oued: derived estimates

Table: **Table A10** Derived residue scenarios for El Oued (tonnes per year)

| Scenario | Production (t) | Alpha | Productive palms | Beta (kg/palm) | Fruit-linked (t) | Palm-linked (t) | Total (t) |
|-------------|---------------|------------|----------------|--------------|-----------------|----------------|------------|
| low | 120,000 | 0.1 | 1,090,000 | 20 | 12,000 | 21,800 | 33,800 |
| central | 120,000 | 0.15 | 1,670,000 | 35 | 18,000 | 58,450 | 76,450 |
| high | 120,000 | 0.3 | 2,000,000 | 65 | 36,000 | 130,000 | 166,000 |

*Note.* R = alpha x P + beta x N / 1000, with R and P in tonnes, N the number of productive palms and beta in kg per palm. Derived; not measured. Totals mix a dry-matter coefficient (low), a coefficient of unstated basis (central) and an as-collected one (high). Assumptions: Low: alpha: lower bound of Shi et al. (2023); palms: 3,852,520 productive palms of the former wilaya in 2020 (MADR) minus 2.76 million productive palms reported for El Meghaier in 2024-2025; beta: Faiad et al. (2022), dry matter. Central: alpha: upper bound of Shi et al. (2023); palms: 120,000 t at 72.0 kg per productive palm (MADR 2020, former wilaya); beta: El-Juhany (2001) as cited in Nasser (2014), basis not stated. High: alpha: chain-wide loss share of Boulal et al. (2016), an upper bound that includes dispersed field and marketing losses; palms: 120,000 t at 60 kg per productive palm (lowest yield on record, ITDAS); beta: Djaafri et al. (2024), as-collected cleaning waste including bunches and peduncles.

Table: **Table A11** One-at-a-time sensitivity of the central scenario

| Parameter | Low | High | Total at low (t) | Total at high (t) | Swing (t) |
|-------------------------------------|--------------|--------------|----------------|-----------------|------------|
| alpha (fruit-linked coefficient) | 0.1 | 0.3 | 70,450 | 94,450 | 24,000 |
| N (productive palms) | 1,090,000 | 2,000,000 | 56,150 | 88,000 | 31,850 |
| beta (kg of pruning residue per palm) | 20 | 65 | 51,400 | 126,550 | 75,150 |

*Note.* Central scenario: 76,450 t.

# Audit of the working files

Table: **Table A12** Audit of the source workbook (Dataset_Residus_Dattes_Sahariennes_Algerie_2020-2025)

| Item | In file | Reference | Ratio | Reference source | Verdict |
|--------------------------------------|---------------|---------------|------------|------------------------------------|--------------------------------------|
| National production 2020 (labelled FAO) | 1,192,000 | 1,151,909 | 1.03 | FAOSTAT | Series labelled FAO is flat at 1,192,000 t for 2020-2023 and does not match FAOSTAT |
| National production 2022 (labelled FAO) | 1,192,000 | 1,242,304 | 0.96 | FAOSTAT | Does not match FAOSTAT |
| National production 2023 (labelled FAO) | 1,192,000 | 1,320,000 | 0.9 | FAO, as charted by Statista | Does not match FAO |
| Exports 2023, tonnes | 130,000 | 83,000 | 1.57 | ONS, in TSA (2025) | Overstated |
| Exports 2023, million USD | 310 | 73 | 4.25 | ONS, in TSA (2025) | Overstated by a factor of about four |
| Biskra share of national production (%) | 60 | 41.2 | 1.46 | MADRP (2017) | Overstated |
| Biskra palm stock 2021 | 5,250,000 | 4,345,045 | 1.21 | DSA (2021), in Haddou thesis | Overstated |
| Ouargla palm stock 2021 | 3,220,000 | 2,568,511 | 1.25 | DSA Ouargla (2021), in Haddou thesis | Overstated |
| Ouargla palm stock 2025 | 3,350,000 | 1,259,632 | 2.66 | DSA Ouargla, Radio Algerie (2026) | Overstated; current boundaries |
| El Oued production 2022 | 60,000 | 120,000 | 0.5 | APS (2023) | Understated by half |
| Ouargla production 2024 | 260,000 | 90,449 | 2.87 | DSA Ouargla, Radio Algerie (2026) | Overstated |
| Biskra production 2023 | 780,000 | 400,000 | 1.95 | DSA Biskra forecast, 'more than' | Nearly twice an official lower bound; not strictly testable |
| Ten-wilaya production 2021 | 1,253,400 | 1,188,803 | 1.05 | FAOSTAT (national total) | Regional sum exceeds the national total |
| National palm stock 2020 | 18,000,000 | 18,600,000 | 0.97 | MADRP (2017), 'more than' | Consistent in order of magnitude; unverified |
| National palm area 2020 (ha) | 170,000 | 167,000 | 1.02 | MADRP (2017) | Consistent in order of magnitude; unverified |
| Dry fronds 2020: sheet 3 total vs sum of sheet 4 | 270,000 | 866,000 | 0.31 | Internal check | Two sheets of the same file disagree |
| Wastewater 2020: stated rate applied to production vs stated quantity | 298,000 | 50,000 | 5.96 | Internal check | Stated rate (25%) and stated quantity are inconsistent |

Table: **Table A13** Ten-wilaya working panel against official statements

| Wilaya | Panel year | Panel (t) | Official (t) | Official period | Ratio | Comparable |
|--------------|------------|------------|-------------|---------------------------------|------------|---------------|
| El Oued | 2022 | 60,000 | 120,000 | season before May 2023 | 0.5 | yes |
| Ouargla | 2024 | 260,000 | 90,449 | 2024-2025 | 2.87 | yes |
| Ouargla | 2025 | 280,000 | 92,014 | 2025-2026 | 3.04 | yes |
| Biskra | 2023 | 780,000 | 400,000 | 2023-2024 (forecast, 'more than') | 1.95 | approx |
| Touggourt | 2023 | 55,000 | 104,271 | season not dated | 0.53 | approx |

# Data still missing

Table: **Table A14** Data not yet available to the study, and how to obtain them

| ID | Variable | Section | Best available now | How to collect | Holder | Unit | Priority |
|------------|--------------------------------------|--------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|-------------|
| G01 | Pruning residue per palm in the Souf (kg/palm/year) by variety and age class | 4.6, 4.7 (Table 6, Fig. 2) | Literature range 20-65 kg; no local measurement | Field measurement at annual pruning on 30-60 palms in 3 age classes and 2 varieties; weigh fronds, petioles, fibre; oven moisture | Authors (Faculty of Natural and Life Sciences); grower cooperatives | kg dry matter per palm | 1 |
| G02 | Palm stock of El Oued within current boundaries: total, productive, by variety and commune | 4.4, 4.6 | Former wilaya, 2020: 4,017,770 planted, 3,852,520 productive (MADR 2020); current boundaries bounded at 1.09-2.0 million productive palms | Official request | DSA El Oued | palms, by commune | 1 |
| G03 | Date production by season and variety, El Oued current boundaries, 2015-2025 | 4.4 | Former wilaya, 2020: 277,550 t by variety (MADR 2020); current boundaries: one season (about 120,000 t, reported May 2023) | Official request | DSA El Oued; Chamber of Agriculture | tonnes per season and variety | 1 |
| G04 | Share of fruit rejected at sorting and conditioning, by defect class | 4.6, 5.2 | Literature 10-15% (grade losses), 30% (all losses), h'chef up to 30% (Djerbi 1994) | Weighing of reject streams at 3-5 packing units over one season | Packing and conditioning units | % of intake, by class and week | 1 |
| G05 | Register of packing, conditioning and processing units: number, capacity, location | 4.8 (Table 9), 5 | No verified count; one unverified figure (303 operators, 2008) | Official request and site visits | DSA; Directorate of Commerce; CNRC register; ANDI | units, tonnes per year | 1 |
| G06 | Current fate of residues: burnt, fed, sold, left on plot | 4.8, 6 | No local figure | Grower survey (about 150 holdings, stratified by commune and size) | Authors | % of residue by fate | 1 |
| G07 | Prices of low-grade dates, pits, fronds, compost and concentrate feed | 5.3, 6 | Deglet Nour price range 2016-2017 only | Monthly market survey over one season | Wholesale markets of El Oued; feed traders | DZD per kg | 1 |
| G08 | Livestock numbers (sheep, goats, camels) and purchased feed use | 4.4, 5.3 | None in database | Official request; breeder survey | DSA El Oued; breeders' associations | head; tonnes of feed per year | 2 |
| G09 | Area under potato and vegetables, and organic fertiliser use | 4.4, 5.3 | National potato share (about 45%) only | Official request; grower survey | DSA El Oued | hectares; tonnes of manure and compost | 2 |
| G10 | Composition of El Oued residue classes: moisture, sugars, fibre, protein, contaminants | 4.7 (Table 8) | Measurements on other varieties and regions | Laboratory analysis of graded samples | Authors (Faculty of Natural and Life Sciences) | % dry matter | 2 |
| G11 | Labelled image set of rejected fruit and residue classes from El Oued | 2.3 (Table 1), 5.2 | None; published sets cover marketable fruit of other varieties | Image capture on sorting lines and at collection points | Packing units; authors | images per class | 2 |
| G12 | Plot locations, distances and transport cost per tonne-kilometre | 5.2 (routing) | None | GIS layer from agricultural services; survey of transporters | DSA; transporters | coordinates; DZD per t-km | 2 |
| G13 | Willingness to pay for graded feed and compost | 7.1 (Propositions 1-2) | None | Choice experiment with breeders and vegetable growers | Authors | DZD per tonne premium | 2 |
| G14 | Digital readiness of growers: smartphone, internet, mobile payment use | 6 | None at local level | Items added to the grower survey | Authors | % of holdings | 3 |
| G15 | Regulatory texts on compost and feed standards and on open burning | 6 | Not compiled | Documentary search | Journal Officiel; ministries of agriculture and environment | list of texts | 3 |
| G16 | Eligibility of residue ventures for public support schemes | 6 | Not compiled | Documentary search and interviews | ANADE; agricultural support funds; banks | list of schemes and conditions | 3 |
| G17 | Date exports by HS 080410: volume, value and partner, 2015-2025, from one consistent source | 4.3 (Table 4) | Three compilations that disagree | Download from UN Comtrade (reporter and mirror data) | UN Comtrade | tonnes; USD | 3 |

*Note.* Priority 1: drives the widest uncertainty in the chapter's estimates. Priority 3: documentary.

Suggested sequence of collection: (1) one official request to the Directorate of Agricultural Services of El Oued covering G02, G03, G05, G08 and G09; (2) one season of fieldwork, organised around pruning and the conditioning season, for G01, G04, G06, G07, G10 and G11; (3) a single survey of growers and breeders for G06, G13 and G14; (4) documentary work for G15-G17. Each item, once collected, enters the database with status `observed_field` and replaces the corresponding range.

# Data compiled in November 2026

Table: **Table A15** Date palm statistics by wilaya, 2020 (MADR; pre-2021 boundaries)

| Wilaya | Area (ha) | Palms planted | Palms productive | Production (t) | Share (%) | Deglet Nour (qx) | Ghars (qx) | Degla Beida (qx) | Yield (qx/ha) | kg per productive palm |
|------------------|------------|---------------|----------------|---------------|------------|----------------|------------|----------------|-------------|----------------------|
| Biskra | 44,051 | 4,448,867 | 4,360,000 | 476,929 | 41.4 | 3,080,000 | 600,000 | 1,089,287 | 109.4 | 109.4 |
| El Oued | 38,495 | 4,017,770 | 3,852,520 | 277,550 | 24.09 | 1,835,800 | 502,400 | 437,300 | 72.0 | 72.0 |
| Adrar | 28,320 | 3,798,759 | 2,825,633 | 93,568 | 8.12 | 0 | 0 | 935,681 | 33.1 | 33.1 |
| Ouargla | 22,909 | 2,680,749 | 2,466,474 | 169,317 | 14.7 | 982,514 | 612,638 | 98,019 | 68.6 | 68.6 |
| Ghardaia | 11,439 | 1,305,510 | 1,148,486 | 61,200 | 5.31 | 245,000 | 100,700 | 266,300 | 53.3 | 53.3 |
| Algeria (national) | 170,501 | 19,194,753 | 16,730,434 | 1,151,909 | 100.0 | - | - | - | - | 68.9 |

*Note.* Source: MADR (2020) and ITDAS Biskra, as reproduced in Tables 04-05 of Maachi (2022). El Oued includes El Meghaier, Biskra includes Ouled Djellal, Ouargla includes Touggourt. The last column is derived. One quintal = 0.1 tonne.

Table: **Table A16** Indicators compiled in November 2026, with verification status

| Item | Value | Unit | Scope | Status | Source |
|--------------------------------------|--------------------------------------|------------------------|--------------------------------------|-------------------------|--------------------------------------|
| Downgraded Deglet Nour (h'chef) as share of production, upper value | up to 30 | % of production | Algeria, varies with the year's climate; no region stated | literature_secondary | Djerbi (1994), cited in Benyahia-Krid et al. (2021), Food and Nutrition Sciences 12(6) |
| Production shares of the main wilayas | Biskra 31; Ouargla 19; El Oued 27 | % of national production | Algeria; year not stated | observed_secondary | CARI / OSSMENA-DELP (2023) |
| Average productive palms 2010-2019 | 14,840,209 | palms | Algeria | collected_unverified | ONS (2020), Retrospective agriculture 2010-2019 |
| Average productive palms 2010-2019 by type: Deglet Nour; soft; dry | 6,075,200; 3,008,424; 5,756,584 | palms | Algeria | collected_unverified | ONS (2020), Retrospective agriculture 2010-2019 |
| Defective or rejected fruit share | 5.55-26.77 | % of fruit | Egypt, 2015/16-2016/17, by variety and season | collected_unverified | Applied Ecology and Environmental Research 17(3) |
| Harvest loss; post-harvest loss | 10-15; 8.1 | % | Comparative only; reference does not match the country stated | not_verified | Reference to be identified; the link given concerns Saudi Arabia |
| Cellulose; lignin in empty fruit bunch fibres, five cultivars | 33.08-49.28; 20.19-40.50 | % dry matter | Southeast Algeria | collected_unverified | Study of date palm empty fruit bunch fibres, Southeast Algeria |
| Sheep flock | more than 28 million; about 60% in the steppe | head | Algeria, 2017 | collected_unverified | Cahiers Agricultures (2020) |
| NPK 15-15-15 applied to potato | 220 | kg per hectare | El Oued sample, 2004 | collected_unverified | FAO, Fertilizer use by crop in Algeria |
| Bioenergy capacity targets | 360 (2015-2020); 640 (2021-2030) | MW | Algeria, renewable energy programme | collected_unverified | Algerian energy policy review; Journal Officiel 2017 no. 31 |
| Internet subscriptions; share mobile | 57,536,959; 89.20 | subscriptions; % | Algeria, end of Q4 2024 | collected_unverified | ARPCE, Internet market Q4 2024 |
| General framework law on waste management and valorisation | Law 01-19 of 12 December 2001 | legal text | Algeria | collected_unverified | Journal Officiel 2001 no. 77 |
| Composting duration; total P, one palm-frond mixture | 136; 0.52 | days; % | Experimental | collected_unverified | Biomass Conversion and Biorefinery (2022) |
| Biogas yield; methane share, date palm wastes | up to 342.2; up to 50 | L per kg VS; % | Experimental | collected_unverified | BioResources |
| Share of rejected dates in production attributed to Chehma (2001) | about 25 | % | Southeast Algeria | not_verified | Not found in the documents cited for it; not used |
| Packing units linked to date conditioning, El Oued (DSASI 2008); units in Biskra (2021) | 303; 78 | operators; units | El Oued 2008; Biskra 2021 | not_verified | Ben-Sayah, University of Ouargla; document could not be opened |

*Note.* observed_secondary and literature_secondary: checked against the document cited. collected_unverified: transcribed from the collection, not re-checked. not_verified: not found in, or not checkable against, the document cited; not used in the chapter.

# Access

Database: Bousbia Laiche, R., & Belmessaoud, R. (2026). *Date-palm residue database for Saharan Algeria, 2015–2025 (corrected and documented)* (Version 1.5.0) [Data set]. Zenodo. [DOI to be inserted after deposit]. Source files, build and validation scripts: GitHub [repository URL to be inserted].
