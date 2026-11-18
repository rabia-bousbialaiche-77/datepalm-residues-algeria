# Date-Palm Residue Database for Saharan Algeria, 2015-2025 (corrected and documented)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24327791.svg)](https://doi.org/10.5281/zenodo.24327791)

Companion data for the book chapter *AI-Driven Circular Business Models for
Date Palm Waste Valorization in Algeria's El Oued Region* (in
*From Linear to Circular Business Models: AI-Driven Sustainable Growth in
Emerging Markets*, Palgrave Macmillan, forthcoming).

**Authors:** Rabiaa Bousbia Laiche (University of El Oued,
ORCID [0000-0002-0150-4310](https://orcid.org/0000-0002-0150-4310)) and
Rachid Belmessaoud (University of El Oued).

## What this database is

A small, fully traceable set of tables on date production and date-palm
residues in Saharan Algeria, with El Oued as the focus. Every value carries
a status flag that says whether it is an official figure, a coefficient from
the literature, an unverified working estimate, a projection or a derived
scenario.

## What it is not

It is not a field survey. No residue quantity in this database was measured.
The ten-wilaya panel is an unverified working estimate that fails a basic
consistency check against national statistics (see `docs/CORRECTIONS.md`),
and it must not be cited as observed data.

## Source files and what became of them

| File received | What it is | Use |
|---|---|---|
| `Dataset_Residus_Dattes_Sahariennes_Algerie_2020-2025.xlsx` | Working workbook, 7 sheets | Kept unchanged in `data/raw/dataset_residus_2020_2025/`; audited in `audit_dataset_residus.csv`; not used as evidence |
| `Classeur_PIML_v2_Panel60.xlsx` | Ten-wilaya panel derived from the workbook above (all 60 production values identical) | Kept in `data/raw/`; flagged in `panel_working_estimates.csv` |
| `wgidataset_with_sourcedata-2025.xlsx` | World Bank WGI, 2025 release | Four dimensions for four countries extracted to `data/raw/wgi/` and `governance_wgi.csv` |
| `WGI_data_2000_2023.xlsx` | Earlier WGI extract | Superseded by the 2025 release; not used |
| Collected-data sheet (November 2026) and its update script | Results of a secondary-data search against the 31 items of the collection plan, sources S1-S41 | Original kept in `data/raw/collected_nov2026/`; verified figures in `madr_2020_wilaya.csv` and `collected_indicators_nov2026.csv` |
| `comtrade_values_raw.csv`, `UN_Comtrade_SoP_Mapping_2000_2022.xlsx` | Exports of minerals and metals (HS chapters 25-28, 72-81, 85); no date products | Not related to this database; not included |

## Contents

| File | Rows | Content | Evidence level |
|---|---|---|---|
| `data/processed/national_production.csv` | 10 | National date production, 2015-2024, with the ONS campaign series for 2015-2019 as a cross-check | Official |
| `data/processed/world_position.csv` | 3 | World production and Algeria's share, 2021-2023 | Official |
| `data/processed/exports.csv` | 4 | Export volume, value and unit value, 2023-2025, three compilers | Official, as reported |
| `data/processed/regional_structure_2017.csv` | 2 | Shares of Biskra and El Oued in area, palms and production | Official |
| `data/processed/yields_prices_2016_2017.csv` | 5 | Deglet Nour yield per palm and local price by wilaya | Official, as reported |
| `data/processed/madr_2020_wilaya.csv` | 6 | Area, palms, production by variety and yield for the five main wilayas and the nation, 2020 (pre-2021 boundaries) | Official |
| `data/processed/wilaya_official_benchmarks.csv` | 35 | Published statements on production, palm stock and area, national and by wilaya, with source links and boundary basis | Official statements |
| `data/processed/governance_wgi.csv` | 160 | Government effectiveness, regulatory quality, rule of law and control of corruption: Algeria, Egypt, Tunisia, Qatar, 2015-2024 | Official |
| `data/processed/residue_coefficients.csv` | 10 | Residue coefficients from the literature and from the original workbook | Literature / unverified |
| `data/processed/composition_conversion.csv` | 13 | Measured composition of residues and ethanol yields | Literature |
| `data/processed/ai_date_grading_studies.csv` | 4 | Reported accuracy of date-grading models | Literature |
| `data/processed/el_oued_residue_scenarios.csv` | 3 | Low, central and high residue scenarios for El Oued | Derived |
| `data/processed/el_oued_sensitivity.csv` | 3 | One-at-a-time sensitivity of the central scenario | Derived |
| `data/processed/panel_working_estimates.csv` | 60 | Ten wilayas by six years, flagged, with consistency columns | Unverified / projection |
| `data/processed/panel_vs_official.csv` | 5 | Working panel against official statements | Check |
| `data/processed/audit_dataset_residus.csv` | 17 | Seventeen claims of the source workbook checked against official figures or against itself | Check |
| `data/processed/collected_indicators_nov2026.csv` | 16 | Indicators compiled in November 2026, each with its verification status | Mixed; see status |
| `data/processed/valorisation_pathways_working.csv` | 12 | Twelve valorisation pathways tagged by feedstock stream | Unverified |
| `data/processed/data_gaps.csv` | 17 | Seventeen variables the study needs but cannot yet obtain, with collection method, holder and priority | Inventory |
| `data/processed/consistency_checks.json` | - | Output of the build-time checks | Check |
| `data/raw/` | - | Original files, unchanged: the two working workbooks and the WGI extract | - |

Column definitions are in `docs/DATA_DICTIONARY.md`. All changes made to the
original files are listed in `docs/CORRECTIONS.md`.

## Headline results

- El Oued, within its current boundaries, produced about 120,000 t of dates
  in the season reported in May 2023, of which about 72,800 t of Deglet Nour.
- Algeria has the lowest regulatory-quality estimate of the four countries
  compared (Algeria, Egypt, Tunisia, Qatar) in 2015, 2019 and 2024 (WGI),
  although it improved from -1.13 to -0.75 between 2019 and 2024.
- In 2020 the former wilaya of El Oued (including El Meghaier) had 38,495 ha,
  4.02 million palms and 277,550 t of dates, 24.1 % of national output
  (MADR); these figures predate the 2021 boundary change.
- Derived residue scenarios for El Oued: 33,800 t (low), 76,450 t (central),
  166,000 t (high) per year. The pruning coefficient per palm (20 to 65 kg)
  drives most of the range.
- The original working panel overstates national output by 64,597 t to
  112,500 t a year and diverges from official wilaya figures by a factor of
  0.5 to 3.

## Reproduce

```
python scripts/build_database.py   # rebuilds data/processed/ from data/raw/
python scripts/validate.py         # integrity checks
python scripts/build_appendix.py appendix   # appendix tables (Markdown, Excel)
```

Python 3.8 or later; the database scripts use the standard library only, the Excel output of the appendix needs openpyxl.

## How to cite

Bousbia Laiche, R., & Belmessaoud, R. (2026). *Date-palm residue database for Saharan Algeria, 2015–2025 (corrected and documented)* (Version 1.5.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.24327791

DOI for all versions: https://doi.org/10.5281/zenodo.24327790. See also `CITATION.cff`.

## Licence

Data and documentation: CC BY 4.0. Code: MIT. See `LICENSE`.

## Data still missing

`docs/DATA_GAPS.md` lists the seventeen variables that the study needs and
cannot yet obtain, with the holder of each and how to collect it.

## Known limits

See `docs/CORRECTIONS.md` and `docs/DATA_GAPS.md`.
