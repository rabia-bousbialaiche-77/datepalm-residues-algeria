#!/usr/bin/env python3
"""Write the data appendix (Online Resource 1) as Markdown and Excel from
the processed tables, so that every figure is identical to the database.

Usage:  python scripts/build_appendix.py <out_dir>
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "data" / "processed"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "appendix"
OUT.mkdir(parents=True, exist_ok=True)


def rows(name):
    return list(csv.DictReader(open(P / name, encoding="utf-8")))


def fmt(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return v
    if f.is_integer() and abs(f) >= 1000:
        return f"{int(f):,}"
    if f.is_integer():
        return str(int(f))
    return f"{f:,.2f}".rstrip("0").rstrip(".") if abs(f) >= 1 else f"{f:.3f}".rstrip("0")


def md_table(header, body):
    # dash counts set relative column widths in pandoc (with a small --columns)
    w = []
    for j, h in enumerate(header):
        cells = [str(h)] + [str(r[j]) for r in body]
        longest = max(len(c) for c in cells)
        word = max(len(t) for c in cells for t in (c.split() or [""]))
        w.append(min(max(longest, word + 5, 12), 38))
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("-" * x for x in w) + "|"]
    for r in body:
        out.append("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
    return "\n".join(out)


TABLES = []   # (id, title, header, body, note) -- reused for Excel


def add(tid, title, header, body, note=""):
    TABLES.append((tid, title, header, body, note))


# A1 national production
add("A1", "National date production, Algeria, 2015-2024",
    ["Year", "Production (t)", "Status", "Source"],
    [[r["year"], fmt(r["production_t"]), r["status"], r["source"]] for r in rows("national_production.csv")],
    "2024 refers to the 2024-2025 campaign where the source says so.")
# A2 world position
add("A2", "World production and Algeria's share, 2021-2023",
    ["Year", "World (t)", "Algeria (t)", "Share (%)", "Source"],
    [[r["year"], fmt(r["world_production_t"]), fmt(r["algeria_production_t"]), r["algeria_share_pct"], r["source"]] for r in rows("world_position.csv")])
# A3 exports
add("A3", "Date exports, 2023-2025, as reported by three compilers",
    ["Year", "Volume (t)", "Value (M USD)", "Unit value (USD/t)", "Share of production (%)", "Source"],
    [[r["year"], fmt(r["export_volume_t"]), r["export_value_musd"], fmt(r["unit_value_usd_per_t"]), r["share_of_production_pct"] or "n.a.", r["source"]] for r in rows("exports.csv")],
    "Compilers disagree by a factor of 2.5 on the 2024 volume. All are reported; none is preferred.")
# A4 structure, yields, prices
body = [[r["wilaya"], "Share of palm area (%)", r["share_of_palm_area_pct"], "MADRP (2017)"] for r in rows("regional_structure_2017.csv")]
body += [[r["wilaya"], "Share of palms (%)", r["share_of_palms_pct"], "MADRP (2017)"] for r in rows("regional_structure_2017.csv")]
body += [[r["wilaya"], "Share of production (%)", r["share_of_production_pct"], "MADRP (2017)"] for r in rows("regional_structure_2017.csv")]
body += [[r["wilaya"], f'{r["indicator"]} ({r["unit"]})', f'{r["low"]}-{r["high"]}', "ITDAS (2016-2017)"] for r in rows("yields_prices_2016_2017.csv")]
add("A4", "Regional structure (2017), Deglet Nour yields and local prices (2016-2017)",
    ["Wilaya", "Indicator", "Value", "Source"], body, "Pre-2021 administrative boundaries.")
# A5 benchmarks
add("A5", "Official statements on production, palm stock and area, national and by wilaya",
    ["Area", "Period", "Indicator", "Value", "Unit", "Boundary and qualifiers", "Source"],
    [[r["wilaya"], r["period"], r["indicator"].replace("_", " "), fmt(r["value"]), r["unit"], r["boundary_note"], r["source"]] for r in rows("wilaya_official_benchmarks.csv")],
    "Source links for every row are in wilaya_official_benchmarks.csv. One quintal = 0.1 tonne.")
# A6 governance (all years, estimate only, compact)
g = rows("governance_wgi.csv")
years = sorted({r["year"] for r in g})
body = []
for dim in ["Government effectiveness", "Regulatory quality", "Rule of law", "Control of corruption"]:
    for c in ["DZA", "EGY", "TUN", "QAT"]:
        vals = {r["year"]: float(r["estimate"]) for r in g if r["dimension"] == dim and r["economy_code"] == c}
        body.append([{"Government effectiveness": "GE", "Regulatory quality": "RQ", "Rule of law": "RL", "Control of corruption": "CC"}[dim], {"DZA": "Algeria", "EGY": "Egypt", "TUN": "Tunisia", "QAT": "Qatar"}[c]] + [f"{vals[y]:+.2f}" if y in vals else "" for y in years])
add("A6", "Worldwide Governance Indicators, estimates, 2015-2024",
    ["Dimension", "Country"] + years, body,
    "GE: government effectiveness; RQ: regulatory quality; RL: rule of law; CC: control of corruption. Scale about -2.5 (weak) to +2.5 (strong). World Bank, WGI 2025 release. 90 % confidence intervals and 0-100 scores in governance_wgi.csv.")
# A7 coefficients
add("A7", "Residue coefficients",
    ["Coefficient", "Description", "Value", "Unit", "Status", "Source"],
    [[r["coefficient_id"], r["description"], r["value"], r["unit"], r["status"], r["source"]] for r in rows("residue_coefficients.csv")])
# A8 composition
add("A8", "Measured composition and conversion yields",
    ["Material", "Property", "Value", "Unit", "Source"],
    [[r["material"], r["property"], r["value"], r["unit"], r["source"]] for r in rows("composition_conversion.csv")])
# A9 AI
add("A9", "Reported accuracy of date-grading models",
    ["Study", "Task", "Images or samples", "Model", "Reported performance (%)"],
    [[r["study"], r["task"], fmt(r["images_or_samples"]) or "not stated", r["model"], r["reported_performance"]] for r in rows("ai_date_grading_studies.csv")])
# A10 scenarios
add("A10", "Derived residue scenarios for El Oued (tonnes per year)",
    ["Scenario", "Production (t)", "Alpha", "Productive palms", "Beta (kg/palm)", "Fruit-linked (t)", "Palm-linked (t)", "Total (t)"],
    [[r["scenario"], fmt(r["production_t_official"]), r["alpha_fruit_linked"], fmt(r["productive_palms_assumed"]), r["beta_kg_per_palm"],
      fmt(r["fruit_linked_residues_t"]), fmt(r["palm_linked_residues_t"]), fmt(r["total_residues_t"])] for r in rows("el_oued_residue_scenarios.csv")],
    "R = alpha x P + beta x N / 1000, with R and P in tonnes, N the number of productive palms and beta in kg per palm. Derived; not measured. Totals mix a dry-matter coefficient (low), a coefficient of unstated basis (central) and an as-collected one (high). Assumptions: " + " ".join(
        f"{r['scenario'].capitalize()}: {r['assumption_note']}." for r in rows("el_oued_residue_scenarios.csv")))
add("A11", "One-at-a-time sensitivity of the central scenario",
    ["Parameter", "Low", "High", "Total at low (t)", "Total at high (t)", "Swing (t)"],
    [[r["parameter"], fmt(r["low_value"]), fmt(r["high_value"]), fmt(r["total_residues_t_at_low"]), fmt(r["total_residues_t_at_high"]), fmt(r["swing_t"])] for r in rows("el_oued_sensitivity.csv")],
    "Central scenario: " + fmt(rows("el_oued_sensitivity.csv")[0]["central_total_t"]) + " t.")
# A12 audit
add("A12", "Audit of the source workbook (Dataset_Residus_Dattes_Sahariennes_Algerie_2020-2025)",
    ["Item", "In file", "Reference", "Ratio", "Reference source", "Verdict"],
    [[r["item"], fmt(r["value_in_file"]), fmt(r["reference_value"]), r["ratio_file_to_reference"], r["reference_source"], r["verdict"]] for r in rows("audit_dataset_residus.csv")])
add("A13", "Ten-wilaya working panel against official statements",
    ["Wilaya", "Panel year", "Panel (t)", "Official (t)", "Official period", "Ratio", "Comparable"],
    [[r["wilaya"], r["panel_year"], fmt(r["panel_production_t"]), fmt(r["official_production_t"]), r["official_period"], r["panel_to_official_ratio"], r["comparable"]] for r in rows("panel_vs_official.csv")])
# A14 gaps
add("A14", "Data not yet available to the study, and how to obtain them",
    ["ID", "Variable", "Section", "Best available now", "How to collect", "Holder", "Unit", "Priority"],
    [[r["gap_id"], r["variable"], r["chapter_section"], r["best_available_now"], r["collection_method"], r["holder_or_responsible"], r["unit_and_granularity"], r["priority"]] for r in rows("data_gaps.csv")],
    "Priority 1: drives the widest uncertainty in the chapter's estimates. Priority 3: documentary.")

# A15 MADR 2020
add("A15", "Date palm statistics by wilaya, 2020 (MADR; pre-2021 boundaries)",
    ["Wilaya", "Area (ha)", "Palms planted", "Palms productive", "Production (t)", "Share (%)", "Deglet Nour (qx)", "Ghars (qx)", "Degla Beida (qx)", "Yield (qx/ha)", "kg per productive palm"],
    [[r["wilaya"], fmt(r["palm_area_ha"]), fmt(r["palms_planted"]), fmt(r["palms_productive"]), fmt(r["production_t"]), r["production_share_pct"],
      fmt(r["deglet_nour_qx"]) or "-", fmt(r["ghars_qx"]) or "-", fmt(r["degla_beida_qx"]) or "-", r["yield_qx_per_ha"] or "-", r["kg_per_productive_palm_derived"]] for r in rows("madr_2020_wilaya.csv")],
    "Source: MADR (2020) and ITDAS Biskra, as reproduced in Tables 04-05 of Maachi (2022). El Oued includes El Meghaier, Biskra includes Ouled Djellal, Ouargla includes Touggourt. The last column is derived. One quintal = 0.1 tonne.")
add("A16", "Indicators compiled in November 2026, with verification status",
    ["Item", "Value", "Unit", "Scope", "Status", "Source"],
    [[r["item"], r["value"], r["unit"], r["scope"], r["status"], r["source"]] for r in rows("collected_indicators_nov2026.csv")],
    "observed_secondary and literature_secondary: checked against the document cited. collected_unverified: transcribed from the collection, not re-checked. not_verified: not found in, or not checkable against, the document cited; not used in the chapter.")

# ------------------------------------------------------------ Markdown
intro = """---
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
7. *Gaps.* Variables required by the chapter but absent from any located source were listed with their holder and collection method (Table A14).\n8. *Compilation of November 2026.* A secondary-data search against the collection plan was checked against its documents. Verified ministry statistics for 2020 by wilaya are in Table A15; the other indicators are in Table A16 with their verification status. Seven of its claims were corrected or set aside, and the boundary basis of the 2020 figures was added (database corrections log, items 16-23).

"""
parts = [intro]
sections = {"A1": "# Production, trade and structure", "A6": "# Institutional environment", "A7": "# Residues: coefficients, composition and technology",
            "A10": "# El Oued: derived estimates", "A12": "# Audit of the working files", "A14": "# Data still missing", "A15": "# Data compiled in November 2026"}
for tid, title, header, body, note in TABLES:
    if tid in sections:
        parts.append(sections[tid] + "\n")
    parts.append(f"Table: **Table {tid}** {title}\n\n" + md_table(header, body) + "\n")
    if note:
        parts.append(f"*Note.* {note}\n")
    if tid == "A14":
        parts.append("""Suggested sequence of collection: (1) one official request to the Directorate of Agricultural Services of El Oued covering G02, G03, G05, G08 and G09; (2) one season of fieldwork, organised around pruning and the conditioning season, for G01, G04, G06, G07, G10 and G11; (3) a single survey of growers and breeders for G06, G13 and G14; (4) documentary work for G15-G17. Each item, once collected, enters the database with status `observed_field` and replaces the corresponding range.
""")
parts.append("""# Access

Database: Bousbia Laiche, R., & Belmessaoud, R. (2026). *Date-palm residue database for Saharan Algeria, 2015–2025 (corrected and documented)* (Version 1.5.0) [Data set]. Zenodo. [DOI to be inserted after deposit]. Source files, build and validation scripts: GitHub [repository URL to be inserted].
""")
(OUT / "appendix.md").write_text("\n".join(parts), encoding="utf-8")

# --------------------------------------------------------------- Excel
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
except ImportError:
    sys.exit(0)
wb = Workbook()
ws = wb.active
ws.title = "README"
ws["A1"] = "Online Resource 1 - Data Appendix (database version 1.5.0)"
ws["A1"].font = Font(bold=True, size=13)
ws["A3"] = "Each sheet reproduces one table of the appendix. Status flags and source links are in the CSV files of the database."
ws["A5"], ws["B5"] = "Sheet", "Content"
ws["A5"].font = ws["B5"].font = Font(bold=True)
for i, (tid, title, *_r) in enumerate(TABLES, start=6):
    ws.cell(i, 1, tid)
    ws.cell(i, 2, title)
ws.column_dimensions["A"].width = 10
ws.column_dimensions["B"].width = 95
fill = PatternFill("solid", fgColor="E7EBF2")
for tid, title, header, body, note in TABLES:
    sh = wb.create_sheet(tid)
    sh["A1"] = f"Table {tid}. {title}"
    sh["A1"].font = Font(bold=True)
    for j, h in enumerate(header, start=1):
        c = sh.cell(3, j, h)
        c.font = Font(bold=True)
        c.fill = fill
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, r in enumerate(body, start=4):
        for j, v in enumerate(r, start=1):
            raw = str(v).replace(",", "")
            try:
                val = float(raw) if raw not in ("", "n.a.") else v
                if isinstance(val, float) and val.is_integer():
                    val = int(val)
            except ValueError:
                val = v
            c = sh.cell(i, j, val)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    if note:
        sh.cell(len(body) + 5, 1, "Note. " + note).font = Font(italic=True)
    for j, h in enumerate(header, start=1):
        width = max([len(str(h))] + [len(str(r[j - 1])) for r in body])
        sh.column_dimensions[sh.cell(3, j).column_letter].width = min(max(10, width + 2), 48)
    sh.freeze_panes = "A4"
wb.save(OUT / "Online_Resource_1_Data_Tables.xlsx")
print("appendix written:", len(TABLES), "tables")
