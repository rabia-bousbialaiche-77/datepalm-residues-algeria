# Data dictionary

All tables are UTF-8 CSV with a header row and a comma separator.
Masses are in metric tonnes unless a column name says otherwise.
One quintal equals 0.1 tonne.

## Status flags

| Flag | Meaning |
|---|---|
| `observed_official` | Published by an official statistical source (FAOSTAT). |
| `observed_official_rounded` | Official figure available only in rounded form. |
| `observed_secondary` | Official-source figure taken from a secondary compiler. |
| `official_statement_press` | Statement by an agricultural authority, reported in the press. |
| `literature` | Coefficient from a peer-reviewed publication. |
| `literature_secondary` | Coefficient cited at second hand. |
| `grey_literature` | Coefficient from a non-peer-reviewed source. |
| `unverified_working_estimate` / `unverified_working` | Value from the authors' original workbook with no located primary source. Not observed data. |
| `projection` | Forward value (2024-2025) from the original workbook. |
| `observed_secondary` | Official-source figure taken from a secondary compiler or report. |
| `collected_unverified` | Figure from the November 2026 collection whose document was not re-checked. |
| `not_verified` | Figure that could not be found in, or checked against, the document cited. Not used. |
| `derived_scenario` | Computed in `scripts/build_database.py` from the inputs stated in the row. |

## national_production.csv
| Column | Description |
|---|---|
| `year` | Calendar year (2024 = 2024-2025 campaign). |
| `production_t` | National date production. |
| `ons_campaign_t` | ONS campaign series (tonnes), 2015-2019, as a cross-check. |
| `status`, `source`, `source_url` | Provenance. |

## wilaya_official_benchmarks.csv
| Column | Description |
|---|---|
| `wilaya` | Wilaya named in the source. |
| `period` | Year or season as stated in the source. |
| `indicator` | `production`, `production_deglet_nour`, `palms_total`, `productive_palms`, `palm_area`. |
| `value`, `unit` | Value in the unit of the source (quintal, palm, hectare). |
| `value_tonnes` | Value in tonnes when the unit is the quintal or the tonne. |
| `boundary_note` | Administrative boundaries the figure refers to, and qualifiers such as "more than". |
| `source`, `source_url` | Provenance. |

## residue_coefficients.csv
| Column | Description |
|---|---|
| `coefficient_id` | Identifier used in the build script. |
| `description`, `value`, `unit` | Coefficient. |
| `status`, `source`, `source_url` | Provenance. |

## panel_working_estimates.csv
60 rows: 10 wilayas by 6 years (2020-2025).
| Column | Description |
|---|---|
| `wilaya`, `year` | Keys. |
| `production_t_working`, `palms_working` | Values of the original workbook. Unverified. |
| `value_status` | `unverified_working_estimate` (2020-2023) or `projection` (2024-2025). |
| `pits_t_orig_coef`, `pedicels_t_orig_coef`, `culls_t_orig_coef` | Production times 0.12, 0.08 and 0.05. |
| `fruit_linked_residues_t_orig_coef` | Sum of the three previous columns. |
| `fronds_t_orig_coef_50kg` | Palms times 50 kg. |
| `fronds_t_beta_low`, `_central`, `_high` | Palms times 20, 35 and 65 kg. |
| `panel_sum_production_t` | Sum of the ten wilayas for the year. |
| `national_production_t` | National figure for the year, when available. |
| `panel_to_national_ratio` | Ratio of the two. Values above 1 are impossible. |

## panel_vs_official.csv
| Column | Description |
|---|---|
| `panel_production_t`, `official_production_t` | Working value and official statement. |
| `panel_to_official_ratio` | Ratio of the two. |
| `comparable` | `yes` when year and boundaries match, `approx` otherwise. |

## el_oued_residue_scenarios.csv
| Column | Description |
|---|---|
| `production_t_official` | 120,000 t (official statement, current boundaries). |
| `alpha_fruit_linked` | Fruit-linked residue per tonne of fruit. |
| `productive_palms_assumed`, `beta_kg_per_palm` | Productive palms and palm-linked residue per palm. |
| `fruit_linked_residues_t`, `palm_linked_residues_t`, `total_residues_t` | Results. |
| `assumption_note` | Plain statement of the assumptions. |

## valorisation_pathways_working.csv
| Column | Description |
|---|---|
| `pathway` | Valorisation pathway. |
| `feedstock_stream` | pits, fronds, molasses or all residues. |
| `feedstock_potential_t_per_year` | Feedstock the pathway could draw on. Shared between pathways of the same stream. |
| `current_uptake_rate_pct`, `currently_valorised_t` | Working estimates of current uptake. |

## el_oued_sensitivity.csv
One row per parameter. The parameter moves from its low to its high value while the two others stay at their central value.
| Column | Description |
|---|---|
| `low_value`, `high_value` | Bounds of the parameter. |
| `total_residues_t_at_low`, `_at_high` | Total residues at each bound. |
| `swing_t` | Difference between the two. |
| `central_total_t` | Central scenario total. |

## world_position.csv, exports.csv
World and national production with Algeria's share; export volume (t), value (million USD), unit value (USD per tonne) and share of production. Export sources disagree for 2024 and are all reported.

## regional_structure_2017.csv, yields_prices_2016_2017.csv
Ministry shares of area, palms and production for Biskra and El Oued (pre-2021 boundaries); Deglet Nour yield per palm and local price ranges from the ITDAS conjuncture note.

## composition_conversion.csv
Measured composition of pits, palm leaves and low-value dates, and ethanol yields, each with its source.

## ai_date_grading_studies.csv
Task, number of images or samples, model and reported performance (metric named) of published date-grading models, as reported by the authors on their own data.

## governance_wgi.csv
World Bank Worldwide Governance Indicators, 2025 release, for DZA, EGY, TUN and QAT, 2015-2024.
| Column | Description |
|---|---|
| `dimension_code`, `dimension` | ge, rq, rl, cc. |
| `estimate` | Governance estimate, approximately -2.5 (weak) to +2.5 (strong). |
| `ci90_low`, `ci90_high` | 90 % confidence interval of the estimate. |
| `score_0_100` | Governance score on a 0-100 scale. |
| `n_sources` | Number of underlying data sources. |

## audit_dataset_residus.csv
| Column | Description |
|---|---|
| `item` | Claim checked. |
| `value_in_file` | Value in the source workbook. |
| `reference_value` | Official figure, or the conflicting value from the same workbook. |
| `ratio_file_to_reference` | Ratio of the two. |
| `reference_source`, `verdict` | Where the reference comes from, and the conclusion. |

## data_gaps.csv
| Column | Description |
|---|---|
| `gap_id` | G01 to G17. |
| `variable` | What is missing. |
| `chapter_section` | Where the chapter needs it. |
| `best_available_now` | What the chapter uses in its place. |
| `collection_method`, `holder_or_responsible` | How and from whom to obtain it. |
| `unit_and_granularity` | Form in which it should be collected. |
| `priority` | 1 = needed to replace the widest uncertainty; 3 = documentary. |

## madr_2020_wilaya.csv
MADR and ITDAS statistics for 2020 as reproduced in Tables 04-05 of Maachi (2022). Pre-2021 boundaries.
| Column | Description |
|---|---|
| `palm_area_ha`, `palms_planted`, `palms_productive`, `production_t` | Values and shares of the national total. |
| `deglet_nour_qx`, `ghars_qx`, `degla_beida_qx` | Production by variety group, quintals. |
| `yield_qx_per_ha` | Yield as given in the source. |
| `kg_per_productive_palm_derived` | production_t x 1000 / palms_productive. |
| `productive_share_of_planted_pct_derived` | palms_productive / palms_planted. |

## collected_indicators_nov2026.csv
| Column | Description |
|---|---|
| `item`, `value`, `unit`, `scope` | Indicator as collected. |
| `status` | Verification status (see flags above). |
| `source_id` | Identifier in the collection sheet (S1-S41). |
| `source`, `source_url` | Document cited. |

## consistency_checks.json
Machine-readable output of the checks run at build time.
