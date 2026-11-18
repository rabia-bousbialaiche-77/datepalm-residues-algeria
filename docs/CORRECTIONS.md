# Corrections log

This file records every change made to the original working files
(`data/raw/`) when the processed tables (`data/processed/`) were built.
No original value was overwritten: the originals are kept in `data/raw/`
and every processed value carries a status flag.

| # | Problem found in the original workbook | What was done |
|---|---|---|
| 1 | The ten-wilaya production panel sums to more than national output in every year that can be checked (excess of 64,597 t to 112,500 t, 2020-2024), although it omits several producing wilayas. | The panel is kept but relabelled `unverified_working_estimate`. Each row now carries the panel sum, the national figure and their ratio. The panel must not be cited as observed data. |
| 2 | Wilaya values diverge from published official statements: El Oued is about half the official figure (60,000 t against 120,000 t), Ouargla about three times (260,000 t against 90,449 t), Biskra about twice a published lower bound. | A new table, `wilaya_official_benchmarks.csv`, records the official statements with their source links and boundary basis. `panel_vs_official.csv` reports the ratios. The panel values were not rescaled, because rescaling would manufacture numbers. |
| 3 | 2024 and 2025 rows are projections, not observations. | Flagged `projection`. |
| 4 | Residues were not measured. They are the product of fixed coefficients (12 % pits, 8 % pedicels, 5 % rejects, 50 kg of fronds per palm), so the perfect fit (R² = 1) reported in the workbook is an identity, not a statistical result. | Columns renamed to show the coefficient used (`*_orig_coef`). The coefficients are listed in `residue_coefficients.csv` with status `unverified_working`. |
| 5 | The frond coefficient of 50 kg per palm per year has no stated source. Published values range from 20 kg to 65 kg, so a single value hides a threefold uncertainty. | Frond residues recomputed for three literature coefficients (20, 35 and 65 kg). The original 50 kg column is kept for traceability. Version 1.0.0 of this log described 50 kg as above the literature range; that statement was wrong and was corrected in version 1.1.0 after a measurement of 65 kg per palm in Adrar (Djaafri et al., 2024) was added. |
| 6 | The workbook contains sheets with simulated measurement noise (Gaussian, CV = 8 %) and cross-validation results computed on that simulated noise. | Excluded from the database. Simulated values are not data. |
| 7 | The valorisation table sums potentials across twelve pathways (3,022,000 t), counting the same feedstock up to four times. | No grand total is published. Each pathway is tagged with its feedstock stream; distinct feedstock is 156,000 t of pits, 282,000 t of fronds, 26,000 t of molasses and 500,000 t for "all residues". All values remain `unverified_working_estimate`. |
| 8 | El Oued had no local figure; its values were a fixed share of national totals. | A separate table, `el_oued_residue_scenarios.csv`, derives a low, central and high scenario (32,000 t, 70,500 t, 166,000 t) from the official production statement, palm-stock bounds implied by official figures and literature coefficients only. `el_oued_sensitivity.csv` shows which parameter drives the range. Status `derived_scenario`. |
| 9 | Administrative boundaries changed in 2021 (El Meghaier separated from El Oued, Touggourt from Ouargla, Ouled Djellal from Biskra). The original workbook does not say which boundaries it uses. | Every benchmark row states its boundary basis. |

## Audit of the source workbook (version 1.2.0)

The ten-wilaya panel was found to be copied from a second workbook,
`Dataset_Residus_Dattes_Sahariennes_Algerie_2020-2025.xlsx` (all 60
production values are identical). That workbook was audited in full; the
results are in `data/processed/audit_dataset_residus.csv`.

| # | Problem | What was done |
|---|---|---|
| 10 | The series labelled "FAO" is flat at 1,192,000 t from 2020 to 2023; FAOSTAT gives 1,151,909 t, 1,188,803 t, 1,242,304 t and about 1.32 Mt. | Not used. FAOSTAT values are in `national_production.csv`. |
| 11 | Exports for 2023 are given as 130,000 t and 310 million USD; the national statistics office reports 83,000 t and about 73 million USD. | Not used. Official figures are in `exports.csv`. |
| 12 | Biskra is said to supply about 60 % of national production; the ministry's 2017 figure is 41.2 %. Palm stocks for Biskra and Ouargla exceed DSA figures by 21-166 %. | Not used. Official statements added to `wilaya_official_benchmarks.csv`. |
| 13 | Two sheets of the workbook disagree on dry fronds by a factor of 3.2 (270,000 t against 866,000 t for 2020), and the wastewater rate (25 %) is inconsistent with the wastewater quantity given. | Not used. |
| 14 | Energy and biogas potentials are computed with conversion factors that are not stated. | Not used. |
| 15 | The sources sheet lists institutions and report series without document references for most entries; no figure can be traced to a specific document. | Recorded; no value from the workbook is used as evidence. |

Two values of the workbook are consistent in order of magnitude with
official figures: the national palm stock (18 million) and palm area
(170,000 ha). They are not used either, because the official figures
themselves are available.

## Verification of the November 2026 collection (version 1.3.0)

A secondary-data search filled part of the 31-item collection plan. Its
main figures were checked against the documents cited.

| # | Claim in the collection | Finding | What was done |
|---|---|---|---|
| 16 | El Oued 2020: 38,495 ha, 4,017,770 palms, 277,550 t | Confirmed in Tables 04-05 of Maachi (2022), from MADR and ITDAS 2020. The figures cover the wilaya before El Meghaier was separated; the collection did not say so. | Added to `madr_2020_wilaya.csv` with a boundary note. Not comparable with the 120,000 t of the current wilaya. |
| 17 | National production 2020 given as 1,115,909 t | Typing error; FAOSTAT and the source table give 1,151,909 t. | Corrected. |
| 18 | Algeria fourth in the world in 2020, after Egypt, Saudi Arabia and Iran | Not in the document cited. | Not used. |
| 19 | Rejected dates about 25 % of production (Chehma, 2001) | Not in either document cited. | Not used. |
| 20 | Downgraded Deglet Nour up to 30 %, Oued Righ, 2025 | The article is from 2021 (Benyahia-Krid et al.); the 30 % comes from Djerbi (1994) and names no region. | Recorded as `literature_secondary` with the correct citation. |
| 21 | El Oued holds 27 % of the packing industry | The CARI report gives 27 % as El Oued's share of production, not of packing. | Recorded as a production share. |
| 22 | Post-harvest loss 8.1 % (Egypt) | The reference given concerns Saudi Arabia. | Recorded as `not_verified`; not used. |
| 23 | 303 packing operators in El Oued (2008); 78 units in Biskra (2021) | Source could not be opened. | Recorded as `not_verified`; not used. |

The national series 2015-2019 matches the ONS campaign series exactly
(to within 41 t in 2017); the ONS figures are now shown beside it.

## Corrections after peer review (version 1.5.0)

| # | Reviewer's point | What was done |
|---|---|---|
| 24 | The palm stock mixed productive and planted palms and different years. | N is now the number of productive palms in every scenario. Low: 3,852,520 productive palms of the former wilaya in 2020 minus the highest productive count reported for El Meghaier (2.76 million, 2024-2025), rounded to 1.09 million. Central: 120,000 t / 72.0 kg = 1.67 million. High: 120,000 t / 60 kg = 2.0 million. |
| 25 | El Meghaier production attributed to El Ikhbaria (1.8 million quintals) did not match the article. | Article re-read: forecast of more than 2 million quintals for 2025-2026, 1.32 million of them Deglet Nour, 3 million palms of which 2.4 million productive (26 November 2025). The 1.8 million figure was removed. Added: 1.66 million quintals forecast and 2.76 million productive palms for 2024-2025 (El Ittihad), 2.5 million productive palms in 2021 (El Maghreb El Awsat). |
| 26 | Alpha = 0.30 is a chain-wide loss rate; beta values differ in moisture basis and scope. | Coefficient descriptions now state the basis (dry matter, not stated, as collected) and scope. Alpha is restricted to low-grade fruit and pits; stalks and bunch residues are counted in beta. |
| 27 | Two Algerian studies missing from the grading literature; Neji et al. used Saudi and Turkish data. | `ai_date_grading_studies.csv` now has six studies, with the performance metric named. |

Scenarios become 33,800 t (low), 76,450 t (central) and 166,000 t (high); the ratio of high to low falls from 5.2 to 4.9.

## What is still missing

See `docs/DATA_GAPS.md`.

## Version history

- **1.5.0** - Corrections after peer review (items 24-27): productive-palm basis for N, El Meghaier statements re-verified, coefficient bases documented, two Algerian grading studies added. Scenarios 33,800 / 76,450 / 166,000 t.
- **1.4.0** - Central palm stock of El Oued derived from observed data instead of the midpoint of its bounds: 120,000 t divided by the 72.0 kg of dates per productive palm recorded for the former wilaya in 2020 (MADR), grossed up by the 2020 productive share (95.9 %), rounded to 1.74 million. Central scenario 78,900 t (was 70,500 t). Low and high scenarios unchanged; sensitivity recomputed around the new centre.
- **1.3.0** - Verified MADR 2020 statistics for the five main wilayas and the nation (pre-2021 boundaries); ONS campaign series added as a cross-check on national production; 16 indicators from the November 2026 collection recorded with their verification status (items 16-23). Data gaps G02-G05 updated. Scenarios unchanged.
- **1.2.0** - Source workbook audited (items 10-15). Added governance indicators (WGI 2025 release) for Algeria, Egypt, Tunisia and Qatar, 2015-2024; twelve new national and wilaya statements (palm stock, area and production for 2010, 2017, 2021 and about 2022); exports for 2025; the inventory of missing data (`data_gaps.csv`, `docs/DATA_GAPS.md`). Removed one coefficient (beta_field_oasis, 21.2 kg per palm) that no table used. Scenarios unchanged.
- **1.1.0** - National series extended to 2015-2024. Added world position, exports, regional structure (2017), yields and prices (2016-2017), composition and conversion measurements, and reported accuracies of date-grading models. El Oued scenarios rebuilt on literature coefficients only (the unverified workbook coefficients are no longer used) and widened after a 65 kg per palm measurement from Adrar was added: 32,000 / 70,500 / 166,000 t against 32,000 / 51,140 / 86,000 t in version 1.0.0. Sensitivity table added.
- **1.0.0** - First corrected and documented release.
