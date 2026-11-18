#!/usr/bin/env python3
"""Integrity checks for the processed tables. Exits non-zero on failure.

Usage:  python scripts/validate.py
"""
import csv
import sys
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "data" / "processed"
ALLOWED = {"observed_official", "observed_official_rounded", "observed_secondary", "official_statement_press",
           "literature", "literature_secondary", "grey_literature",
           "unverified_working_estimate", "unverified_working", "projection", "derived_scenario", "observed_field", "collected_unverified", "not_verified"}
errors = []


def rows(name):
    return list(csv.DictReader(open(P / name, encoding="utf-8")))


panel = rows("panel_working_estimates.csv")
if len(panel) != 60:
    errors.append("panel must hold 60 rows")
for r in panel:
    if r["value_status"] not in ALLOWED:
        errors.append(f"bad status {r['value_status']}")
    if (int(r["year"]) >= 2024) != (r["value_status"] == "projection"):
        errors.append(f"projection flag wrong for {r['wilaya']} {r['year']}")
    fruit = int(r["pits_t_orig_coef"]) + int(r["pedicels_t_orig_coef"]) + int(r["culls_t_orig_coef"])
    if fruit != int(r["fruit_linked_residues_t_orig_coef"]):
        errors.append(f"fruit-linked sum mismatch for {r['wilaya']} {r['year']}")
    if not int(r["fronds_t_beta_low"]) <= int(r["fronds_t_beta_central"]) <= int(r["fronds_t_beta_high"]):
        errors.append(f"frond range not ordered for {r['wilaya']} {r['year']}")
for name in ["national_production.csv", "residue_coefficients.csv",
             "el_oued_residue_scenarios.csv", "valorisation_pathways_working.csv"]:
    for r in rows(name):
        s = r.get("status") or r.get("value_status")
        if s not in ALLOWED:
            errors.append(f"{name}: bad status {s}")
for r in rows("wilaya_official_benchmarks.csv"):
    if not r["source_url"].startswith("http"):
        errors.append(f"benchmark without source URL: {r['wilaya']} {r['period']}")
sc = {r["scenario"]: int(r["total_residues_t"]) for r in rows("el_oued_residue_scenarios.csv")}
if not sc["low"] < sc["central"] < sc["high"]:
    errors.append("El Oued scenarios not ordered")
for r in rows("el_oued_residue_scenarios.csv"):
    if int(r["fruit_linked_residues_t"]) + int(r["palm_linked_residues_t"]) != int(r["total_residues_t"]):
        errors.append("scenario total mismatch")
m = rows("madr_2020_wilaya.csv")
five = sum(int(r["production_t"]) for r in m if not r["wilaya"].startswith("Algeria"))
if five != 1078564:
    errors.append("MADR 2020: five-wilaya production must sum to 1,078,564 t")
for r in m:
    if r["deglet_nour_qx"] and abs(int(r["deglet_nour_qx"]) + int(r["ghars_qx"]) + int(r["degla_beida_qx"]) - int(r["production_t"]) * 10) > 10:
        errors.append(f"MADR 2020: variety sum mismatch for {r['wilaya']}")
for r in rows("collected_indicators_nov2026.csv"):
    if r["status"] not in ALLOWED:
        errors.append(f"collected: bad status {r['status']}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All checks passed.")
