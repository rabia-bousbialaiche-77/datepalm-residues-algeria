#!/usr/bin/env python3
"""Build the corrected and documented date-palm residue database.

Reads the original working files in data/raw/ and writes the processed
tables in data/processed/. Every value carries a status flag so that
observed figures, literature coefficients, unverified working estimates
and derived scenarios can never be confused.

Usage:  python scripts/build_database.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

QX_TO_T = 0.1  # 1 quintal = 100 kg = 0.1 tonne


def write(name, header, rows):
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ---------------------------------------------------------------- 1. national
NATIONAL = [
    # year, production_t, status, source, url
    (2015, 990377, "observed_official", "FAOSTAT, reproduced by Knoema", "https://d3fqfiq2w1ez7u.cloudfront.net/nmx/timeseries/algeria-dates-production"),
    (2016, 1029596, "observed_official", "FAOSTAT, reproduced by Knoema", "https://d3fqfiq2w1ez7u.cloudfront.net/nmx/timeseries/algeria-dates-production"),
    (2017, 1058600, "observed_official", "FAO-based series, reproduced by Knoema", "https://d3fqfiq2w1ez7u.cloudfront.net/nmx/timeseries/algeria-eu-dates-production"),
    (2018, 1094700, "observed_official", "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2019, 1136025, "observed_official", "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2020, 1151909, "observed_official", "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2021, 1188803, "observed_official", "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2022, 1242304, "observed_official", "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2023, 1320000, "observed_official_rounded", "FAO figure as charted by Statista (1.32 Mt, rounded)",
     "https://statista.com/chart/amp/29563/biggest-producers-of-dates"),
    (2024, 1337301, "observed_secondary", "FAO-based figure reported by Selina Wamucii",
     "https://www.selinawamucii.com/fr/connaissances/prix/algerie/dattes/"),
]
ONS_QX = {2015: 9903770, 2016: 10295957, 2017: 10585587, 2018: 10947000, 2019: 11360249}  # campaigns 2014/15-2018/19
write("national_production.csv",
      ["year", "production_t", "status", "source", "source_url", "ons_campaign_t", "ons_source"],
      [list(r) + ([round(ONS_QX[r[0]] * QX_TO_T), "ONS (2020), Retrospective agriculture 2010-2019, campaign ending in this year"] if r[0] in ONS_QX else ["", ""])
       for r in NATIONAL])
NAT = {r[0]: r[1] for r in NATIONAL}

# ------------------------------------------------------ 2. wilaya benchmarks
# wilaya, period, indicator, value, unit, boundary, source, url
BENCH = [
    ("Biskra", "2017", "production", 4380000, "quintal", "pre-2021 boundaries (incl. Ouled Djellal)",
     "Algerie-Eco, ministry figures", "https://algerie-eco.com/?p=33277"),
    ("El Oued", "2017", "production", 2600000, "quintal", "pre-2021 boundaries (incl. El Meghaier)",
     "Algerie-Eco, ministry figures", "https://algerie-eco.com/?p=33277"),
    ("Ouargla", "2017", "production", 1400000, "quintal", "pre-2021 boundaries (incl. Touggourt)",
     "Algerie-Eco, ministry figures", "https://algerie-eco.com/?p=33277"),
    ("El Oued", "2019", "productive_palms", 4000000, "palm", "pre-2021 boundaries (Souf and Oued Righ)",
     "APS, Chamber of Agriculture statement", "https://www.aps.dz/ar/economie/69083-2019-04-05-14-13-08"),
    ("El Oued", "2019", "production", 3000000, "quintal", "pre-2021 boundaries (Souf and Oued Righ); stated as 'more than'",
     "APS, Chamber of Agriculture statement", "https://www.aps.dz/ar/economie/69083-2019-04-05-14-13-08"),
    ("El Oued", "2019", "palm_area", 40000, "hectare", "pre-2021 boundaries (Souf and Oued Righ)",
     "APS, Chamber of Agriculture statement", "https://www.aps.dz/ar/economie/69083-2019-04-05-14-13-08"),
    ("El Oued", "2021", "palms_total", 4600000, "palm", "boundary basis not stated; consistent with pre-2021 boundaries",
     "An-Nasr, April 2021", "https://www.annasronline.com/%D8%B1%D9%88%D8%A8%D9%88%D8%B1%D8%AA%D8%A7%D8%AC/%D9%85%D9%84%D9%81%D8%A7%D8%AA/175200-2021-04-14-10-52-52"),
    ("El Oued", "2021", "production", 2800000, "quintal", "boundary basis not stated; consistent with pre-2021 boundaries",
     "An-Nasr, April 2021", "https://www.annasronline.com/%D8%B1%D9%88%D8%A8%D9%88%D8%B1%D8%AA%D8%A7%D8%AC/%D9%85%D9%84%D9%81%D8%A7%D8%AA/175200-2021-04-14-10-52-52"),
    ("El Oued", "season before May 2023", "production", 1200000, "quintal", "current boundaries (after separation of El Meghaier)",
     "APS dispatch reproduced by allAfrica, May 2023", "https://fr.allafrica.com/stories/202305140064.html"),
    ("El Oued", "season before May 2023", "production_deglet_nour", 728000, "quintal", "current boundaries",
     "APS dispatch reproduced by allAfrica, May 2023", "https://fr.allafrica.com/stories/202305140064.html"),
    ("El Meghaier", "2021", "productive_palms", 2500000, "palm", "current boundaries; 20,000 ha; 1.4 million Deglet Nour palms",
     "El Maghreb El Awsat (20 March 2021)", "https://elmaghrebelawsat.dz/2021/03/20/%D9%88%D9%84%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D8%B1%D8%A7%D9%87%D9%86-%D8%B9%D9%84%D9%89-%D9%82%D8%AF%D8%B1%D8%A7%D8%AA-%D9%81%D9%84%D8%A7%D8%AD%D9%8A%D8%A9-%D9%87%D8%A7/"),
    ("El Meghaier", "2024-2025", "productive_palms", 2760000, "palm", "current boundaries; stated as 'more than'",
     "El Ittihad, DSA El Meghaier", "https://www.elitihadcom.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%88%D9%82%D8%B9-%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D8%A3%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-6%D8%B11-%D9%85%D9%84%D9%8A%D9%88%D9%86-%D9%82%D9%86%D8%B7%D8%A7/"),
    ("El Meghaier", "2024-2025", "production", 1660000, "quintal", "current boundaries; forecast stated as 'at least'",
     "El Ittihad, DSA El Meghaier", "https://www.elitihadcom.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%88%D9%82%D8%B9-%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D8%A3%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-6%D8%B11-%D9%85%D9%84%D9%8A%D9%88%D9%86-%D9%82%D9%86%D8%B7%D8%A7/"),
    ("El Meghaier", "2025-2026", "production", 2000000, "quintal", "current boundaries; forecast stated as 'more than'",
     "El Ikhbaria (26 November 2025), citing APS", "https://elikhbaria.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%86%D8%AA%D8%AC-%D8%A3%D9%83%D8%AB%D8%B1-%D9%85%D9%86-%D9%85%D9%84%D9%8A%D9%88%D9%86%D9%8A-%D9%82%D9%86%D8%B7%D8%A7%D8%B1-%D9%85%D9%86-%D8%A7%D9%84%D8%AA/"),
    ("El Meghaier", "2025-2026", "production_deglet_nour", 1320000, "quintal", "current boundaries; forecast",
     "El Ikhbaria (26 November 2025), citing APS", "https://elikhbaria.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%86%D8%AA%D8%AC-%D8%A3%D9%83%D8%AB%D8%B1-%D9%85%D9%86-%D9%85%D9%84%D9%8A%D9%88%D9%86%D9%8A-%D9%82%D9%86%D8%B7%D8%A7%D8%B1-%D9%85%D9%86-%D8%A7%D9%84%D8%AA/"),
    ("El Meghaier", "2025-2026", "palms_total", 3000000, "palm", "current boundaries",
     "El Ikhbaria (26 November 2025), citing APS", "https://elikhbaria.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%86%D8%AA%D8%AC-%D8%A3%D9%83%D8%AB%D8%B1-%D9%85%D9%86-%D9%85%D9%84%D9%8A%D9%88%D9%86%D9%8A-%D9%82%D9%86%D8%B7%D8%A7%D8%B1-%D9%85%D9%86-%D8%A7%D9%84%D8%AA/"),
    ("El Meghaier", "2025-2026", "productive_palms", 2400000, "palm", "current boundaries",
     "El Ikhbaria (26 November 2025), citing APS", "https://elikhbaria.dz/%D8%A7%D9%84%D9%85%D8%BA%D9%8A%D8%B1-%D8%AA%D9%86%D8%AA%D8%AC-%D8%A3%D9%83%D8%AB%D8%B1-%D9%85%D9%86-%D9%85%D9%84%D9%8A%D9%88%D9%86%D9%8A-%D9%82%D9%86%D8%B7%D8%A7%D8%B1-%D9%85%D9%86-%D8%A7%D9%84%D8%AA/"),
    ("Touggourt", "season not dated", "production", 1042711, "quintal", "current boundaries",
     "AlgeriaInvest", "https://algeriainvest.com/premium-news/production-de-dattes-oued-righ-pole-dinvestissement-prometteur-pour-le-developpement-de-la-filiere"),
    ("Ouargla", "2018-2019", "production", 1650164, "quintal", "pre-2021 boundaries (incl. Touggourt)",
     "Journal article, University of Ouargla authors", "https://iasj.rdd.edu.iq/journals/uploads/2024/12/08/de8e5b105a677f38d9e4ac9616806c7e.pdf"),
    ("Ouargla", "2024-2025", "production", 904489, "quintal", "current boundaries",
     "Radio Algerie, DSA Ouargla", "https://news.radioalgerie.dz/ar/node/83255"),
    ("Ouargla", "2025-2026", "production", 920142, "quintal", "current boundaries",
     "Radio Algerie, DSA Ouargla", "https://news.radioalgerie.dz/ar/node/83255"),
    ("Ouargla", "2025-2026", "palms_total", 1259632, "palm", "current boundaries",
     "Radio Algerie, DSA Ouargla", "https://news.radioalgerie.dz/ar/node/83255"),
    ("Ouargla", "2025-2026", "palm_area", 11451, "hectare", "current boundaries",
     "Radio Algerie, DSA Ouargla", "https://news.radioalgerie.dz/ar/node/83255"),
    ("Biskra", "2023-2024", "production", 4000000, "quintal", "current boundaries; forecast stated as 'more than'",
     "Awras, DSA Biskra", "https://www.awras.com/%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D8%A7%D9%84%D8%AA%D9%85%D9%88%D8%B1-%D9%81%D9%8A-%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%D8%A6%D8%B1-%D9%82%D8%AF-%D9%8A%D8%AA%D8%AC%D8%A7%D9%88%D8%B2-4-%D9%85%D9%84%D8%A7%D9%8A/"),
    ("Biskra", "2026", "palms_total", 4200000, "palm", "current boundaries; stated as 'more than'",
     "El Massa", "https://www.el-massa.com/dz/%D8%B1%D9%88%D8%A8%D9%88%D8%B1%D8%AA%D8%A7%D8%AC%D8%A7%D8%AA-%D8%A7%D8%B3%D8%AA%D8%B7%D9%84%D8%A7%D8%B9%D8%A7%D8%AA/%D8%AA%D9%88%D9%82%D8%B9-%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D8%A3%D9%83%D8%AB%D8%B1-%D9%85%D9%86-4-%D9%85%D9%84%D8%A7%D9%8A%D9%8A%D9%86-%D9%82%D9%86%D8%B7%D8%A7%D8%B1-%D9%85%D9%86-%D8%A7%D9%84%D8%AA%D9%85%D9%88%D8%B1-%D8%A8%D8%A8%D8%B3%D9%83%D8%B1%D8%A9"),
    ("Ouled Djellal", "2025-2026", "production", 900000, "quintal", "current boundaries; forecast stated as 'more than'",
     "Horizons, APS", "https://www.horizons.dz/language/ar/2025/12/%D8%A3%D9%88%D9%84%D8%A7%D8%AF-%D8%AC%D9%84%D8%A7%D9%84-%D8%AA%D9%88%D9%82%D8%B9-%D8%A5%D9%86%D8%AA%D8%A7%D8%AC-%D8%A3%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-900-%D8%A3%D9%84%D9%81-%D9%82%D9%86%D8%B7%D8%A7/"),
    ("Algeria", "2010", "production", 644740, "tonne", "national",
     "FAO figures cited in a paper of the 5th International Date Palm Conference", "https://iraqi-datepalms.net/wp-content/uploads/2018/10/FifthInternationalConference10.pdf"),
    ("Algeria", "2010", "palm_area", 161090, "hectare", "national",
     "FAO figures cited in a paper of the 5th International Date Palm Conference", "https://iraqi-datepalms.net/wp-content/uploads/2018/10/FifthInternationalConference10.pdf"),
    ("Algeria", "2017", "palm_area", 167000, "hectare", "national",
     "MADRP (2017), as reproduced in a University of Biskra thesis", "http://archives.univ-biskra.dz/bitstream/123456789/13293/1/Aksa_Abderrahmane.pdf"),
    ("Algeria", "2017", "palms_total", 18600000, "palm", "national; stated as 'more than'",
     "MADRP (2017), as reproduced in a University of Biskra thesis", "http://archives.univ-biskra.dz/bitstream/123456789/13293/1/Aksa_Abderrahmane.pdf"),
    ("Algeria", "2017", "production", 990000, "tonne", "national; stated as 'nearly'",
     "MADRP (2017), as reproduced in a University of Biskra thesis", "http://archives.univ-biskra.dz/bitstream/123456789/13293/1/Aksa_Abderrahmane.pdf"),
    ("Algeria", "about 2022", "palms_total", 20000000, "palm", "national; stated as 'nearly'; 17 producing wilayas",
     "El Moudjahid", "https://www.elmoudjahid.dz/fr/actualite/dattes-algeriennes-l-or-inepuisable-du-desert-198623"),
    ("Algeria", "about 2022", "palm_area", 170000, "hectare", "national",
     "El Moudjahid", "https://www.elmoudjahid.dz/fr/actualite/dattes-algeriennes-l-or-inepuisable-du-desert-198623"),
    ("Biskra", "about 2022", "palms_total", 4500000, "palm", "current boundaries",
     "El Moudjahid", "https://www.elmoudjahid.dz/fr/actualite/dattes-algeriennes-l-or-inepuisable-du-desert-198623"),
    ("Biskra", "2021", "palms_total", 4345045, "palm", "boundary basis not stated",
     "DSA figures (2021) reproduced in a University of Ouargla doctoral thesis", "https://dspace.univ-ouargla.dz/jspui/bitstream/123456789/31770/1/HADDOU_Messaouda_Doctorat.pdf"),
    ("Ouargla", "2021", "palms_total", 2568511, "palm", "boundary basis not stated",
     "DSA Ouargla (2021) reproduced in a University of Ouargla doctoral thesis", "https://dspace.univ-ouargla.dz/jspui/bitstream/123456789/31770/1/HADDOU_Messaouda_Doctorat.pdf"),
    ("Ouargla", "2021", "productive_palms", 2133184, "palm", "boundary basis not stated",
     "DSA Ouargla (2021) reproduced in a University of Ouargla doctoral thesis", "https://dspace.univ-ouargla.dz/jspui/bitstream/123456789/31770/1/HADDOU_Messaouda_Doctorat.pdf"),
    ("Biskra", "2023-2024", "production_deglet_nour", 2400000, "quintal", "current boundaries; forecast; 60% of the total",
     "Algerie-Eco, DSA Biskra", "https://www.algerie-eco.com/2023/09/11/dattes-une-production-de-4-millions-de-quintaux-attendue-a-biskra/"),
    ("Algeria (five main wilayas)", "2019", "palms_total", 19063249, "palm", "Biskra, El Oued, Adrar, Ouargla, Ghardaia; pre-2021 boundaries",
     "Journal article citing MADR (2022)", "https://cyberleninka.ru/article/n/determinants-of-the-strategies-adopted-by-companies-exporting-dates-in-algeria-state-of-biskra-as-a-case-study"),
]
rows = []
for b in BENCH:
    tonnes = round(b[3] * QX_TO_T) if b[4] == "quintal" else ""
    rows.append(list(b[:5]) + [tonnes if b[4] == "quintal" else (b[3] if b[4] == "tonne" else "")] + list(b[5:]))
write("wilaya_official_benchmarks.csv",
      ["wilaya", "period", "indicator", "value", "unit", "value_tonnes",
       "boundary_note", "source", "source_url"], rows)

# ------------------------------------------------------- 3. coefficients
COEF = [
    # id, description, value, unit, status, source, url
    ("beta_low", "Dry frond and leaf residues per palm per year; dry-matter basis", 20, "kg/palm/year", "literature",
     "Faiad et al. (2022), Sustainability 14(3):1134", "https://mdpi.com/2071-1050/14/3/1134"),
    ("beta_central", "Palm residues per tree per year (El-Juhany 2001, as cited); moisture basis not stated", 35, "kg/palm/year", "literature_secondary",
     "Nasser (2014), BioResources 9(3)", "https://bioresources.cnr.ncsu.edu/wp-content/uploads/2016/06/BioRes_09_3_4343_Nasser_Eval_Midrib_Date_Palm_5650.pdf"),
    ("beta_high", "Biowaste per palm per year from annual cleaning, Adrar (Algeria); as collected; includes palms, petioles, bunches and bunch peduncles", 65, "kg/palm/year", "literature",
     "Djaafri et al. (2024), Energies 17(11):2520", "https://doi.org/10.3390/en17112520"),
    ("beta_original", "Dry fronds per palm per year used in the original workbook", 50, "kg/palm/year", "unverified_working",
     "Original workbook; no primary source located; inside the 20-65 range of the literature", ""),
    ("alpha_low", "Low-grade dates and pits as share of production, lower bound", 0.10, "t/t fruit", "literature",
     "Shi et al. (2023), Applied Sciences 13(22):12315", "https://doi.org/10.3390/app132212315"),
    ("alpha_central", "Low-grade dates and pits as share of production, upper bound", 0.15, "t/t fruit", "literature",
     "Shi et al. (2023), Applied Sciences 13(22):12315", "https://doi.org/10.3390/app132212315"),
    ("alpha_high", "Share of Algerian date production lost during picking, storage and marketing; chain-wide, not only at packing units", 0.30, "t/t fruit", "literature",
     "Boulal et al. (2016), African Journal of Biotechnology", "https://doi.org/10.5897/AJB2016.15368"),
    ("pits_original", "Pits as share of fruit mass used in the original workbook", 0.12, "t/t fruit", "unverified_working",
     "Original workbook; no primary source located", ""),
    ("pedicels_original", "Pedicels as share of fruit mass used in the original workbook", 0.08, "t/t fruit", "unverified_working",
     "Original workbook; no primary source located", ""),
    ("culls_original", "Sorting rejects as share of fruit mass used in the original workbook", 0.05, "t/t fruit", "unverified_working",
     "Original workbook; no primary source located", ""),
]
write("residue_coefficients.csv",
      ["coefficient_id", "description", "value", "unit", "status", "source", "source_url"], COEF)
C = {c[0]: c[2] for c in COEF}

# ------------------------------------------------- 4. working panel, flagged
panel = list(csv.DictReader(open(RAW / "panel_original.csv", encoding="utf-8")))
sums = {}
for r in panel:
    sums[int(r["year"])] = sums.get(int(r["year"]), 0) + int(r["production_t"])
rows = []
for r in panel:
    y, p, n = int(r["year"]), int(r["production_t"]), int(r["palms_n"])
    status = "unverified_working_estimate" if y <= 2023 else "projection"
    fruit_res = int(r["pits_t"]) + int(r["pedicels_t"]) + int(r["culls_t"])
    rows.append([
        r["wilaya"], y, p, n, status,
        r["pits_t"], r["pedicels_t"], r["culls_t"], fruit_res,
        r["fronds_t"],
        round(n * C["beta_low"] / 1000), round(n * C["beta_central"] / 1000), round(n * C["beta_high"] / 1000),
        sums[y], NAT.get(y, ""), (round(sums[y] / NAT[y], 3) if y in NAT else ""),
    ])
write("panel_working_estimates.csv",
      ["wilaya", "year", "production_t_working", "palms_working", "value_status",
       "pits_t_orig_coef", "pedicels_t_orig_coef", "culls_t_orig_coef", "fruit_linked_residues_t_orig_coef",
       "fronds_t_orig_coef_50kg",
       "fronds_t_beta_low", "fronds_t_beta_central", "fronds_t_beta_high",
       "panel_sum_production_t", "national_production_t", "panel_to_national_ratio"], rows)

# ------------------------------------- 5. panel versus official benchmarks
CMP = [
    # wilaya, panel year, official tonnes, official period, comparable?, note
    ("El Oued", 2022, 120000, "season before May 2023", "yes", "current boundaries on both sides"),
    ("Ouargla", 2024, 90449, "2024-2025", "yes", "current boundaries on both sides"),
    ("Ouargla", 2025, 92014, "2025-2026", "yes", "current boundaries on both sides"),
    ("Biskra", 2023, 400000, "2023-2024 (forecast, 'more than')", "approx", "official figure is a lower bound"),
    ("Touggourt", 2023, 104271, "season not dated", "approx", "season of the official figure is not dated"),
]
pidx = {(r["wilaya"], int(r["year"])): int(r["production_t"]) for r in panel}
rows = []
for w, y, off, per, comp, note in CMP:
    p = pidx[(w, y)]
    rows.append([w, y, p, off, per, round(p / off, 2), comp, note])
write("panel_vs_official.csv",
      ["wilaya", "panel_year", "panel_production_t", "official_production_t", "official_period",
       "panel_to_official_ratio", "comparable", "note"], rows)

# ---------------------------------------------------- 6. El Oued scenarios
P_ELOUED = 120000  # tonnes, official statement, current boundaries
# N is the number of PRODUCTIVE palms in all three scenarios.
# Low: productive palms of the former wilaya in 2020 (MADR) minus the highest
#      productive count reported for El Meghaier (2.76 million, 2024-2025).
# Central: official production of the current wilaya divided by the output per
#      productive palm observed for the former wilaya in 2020 (MADR).
# High: official production divided by the lowest yield on record for the
#      wilaya (60 kg per palm, Deglet Nour, ITDAS 2016-2017).
KG_PER_PRODUCTIVE_2020 = 277550 * 1000 / 3852520      # about 72.0 kg
N_LOW = int(round(3852520 - 2760000, -4))
N_CENTRAL = int(round(P_ELOUED * 1000 / KG_PER_PRODUCTIVE_2020, -4))
N_HIGH = int(round(P_ELOUED * 1000 / 60, -4))
SCEN = [
    # name, alpha (fruit-linked: low-grade fruit and pits), productive palms, beta kg
    ("low", C["alpha_low"], N_LOW, C["beta_low"],
     "alpha: lower bound of Shi et al. (2023); palms: 3,852,520 productive palms of the former wilaya in 2020 (MADR) minus 2.76 million productive palms reported for El Meghaier in 2024-2025; beta: Faiad et al. (2022), dry matter"),
    ("central", C["alpha_central"], N_CENTRAL, C["beta_central"],
     "alpha: upper bound of Shi et al. (2023); palms: 120,000 t at 72.0 kg per productive palm (MADR 2020, former wilaya); beta: El-Juhany (2001) as cited in Nasser (2014), basis not stated"),
    ("high", C["alpha_high"], N_HIGH, C["beta_high"],
     "alpha: chain-wide loss share of Boulal et al. (2016), an upper bound that includes dispersed field and marketing losses; palms: 120,000 t at 60 kg per productive palm (lowest yield on record, ITDAS); beta: Djaafri et al. (2024), as-collected cleaning waste including bunches and peduncles"),
]
rows = []
for name, a, n, b, note in SCEN:
    fruit = round(P_ELOUED * a)
    palm = round(n * b / 1000)
    rows.append(["El Oued", name, P_ELOUED, round(a, 2), n, b, fruit, palm, fruit + palm, "derived_scenario", note])
write("el_oued_residue_scenarios.csv",
      ["wilaya", "scenario", "production_t_official", "alpha_fruit_linked", "productive_palms_assumed", "beta_kg_per_palm",
       "fruit_linked_residues_t", "palm_linked_residues_t", "total_residues_t", "value_status", "assumption_note"], rows)

# ------------------------------------------------- 7. valorisation pathways
EN = {
    "Alimentation animale (noyaux broyés)": ("Animal feed (ground pits)", "pits"),
    "Charbon actif (noyaux carbonisés)": ("Activated carbon (carbonised pits)", "pits"),
    "Biocarburant (noyaux)": ("Biofuel (pits)", "pits"),
    "Cosmétiques (huile de noyaux)": ("Cosmetics (pit oil)", "pits"),
    "Compostage (tous résidus organiques)": ("Composting (all organic residues)", "all residues"),
    "Biogaz / Méthanisation (résidus organiques)": ("Biogas / anaerobic digestion", "all residues"),
    "Artisanat (palmes tressées)": ("Handicraft (woven fronds)", "fronds"),
    "Construction (palmes + terre)": ("Construction (fronds and earth)", "fronds"),
    "Alimentation animale (mélasse)": ("Animal feed (molasses)", "molasses"),
    "Éthanol (mélasse fermentée)": ("Ethanol (fermented molasses)", "molasses"),
    "Engrais organique (compost)": ("Organic fertiliser (compost)", "all residues"),
    "Pâte à papier (fibres de palmes)": ("Paper pulp (frond fibres)", "fronds"),
}
rows = []
feed = {}
for r in csv.DictReader(open(RAW / "valorisation_pathways_original.csv", encoding="utf-8")):
    name, stream = EN[r["pathway_fr"]]
    feed.setdefault(stream, float(r["potential_t_per_year"]))
    rows.append([name, stream, r["potential_t_per_year"], r["current_rate_pct"],
                 r["currently_valorised_t"], "unverified_working_estimate",
                 "competes for the same feedstock as the other pathways of this stream; do not sum across pathways"])
write("valorisation_pathways_working.csv",
      ["pathway", "feedstock_stream", "feedstock_potential_t_per_year", "current_uptake_rate_pct",
       "currently_valorised_t", "value_status", "note"], rows)

# ------------------------------------------------------ 7b. sensitivity
base = {r[1]: r for r in csv.reader(open(OUT / "el_oued_residue_scenarios.csv", encoding="utf-8")) if r[0] == "El Oued"}
ca, cn, cb = C["alpha_central"], N_CENTRAL, C["beta_central"]
def total(a_, n_, b_):
    return round(P_ELOUED * a_ + n_ * b_ / 1000)
SENS = [
    ("alpha (fruit-linked coefficient)", C["alpha_low"], C["alpha_high"], total(C["alpha_low"], cn, cb), total(C["alpha_high"], cn, cb)),
    ("N (productive palms)", N_LOW, N_HIGH, total(ca, N_LOW, cb), total(ca, N_HIGH, cb)),
    ("beta (kg of pruning residue per palm)", C["beta_low"], C["beta_high"], total(ca, cn, C["beta_low"]), total(ca, cn, C["beta_high"])),
]
write("el_oued_sensitivity.csv",
      ["parameter", "low_value", "high_value", "total_residues_t_at_low", "total_residues_t_at_high", "swing_t", "central_total_t"],
      [list(x) + [x[4] - x[3], total(ca, cn, cb)] for x in SENS])

# ------------------------------------------------------ 9. world position
WORLD = [
    (2021, 9656378, 1188803, "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates/"),
    (2022, 9747570, 1242304, "FAOSTAT, reproduced by HelgiLibrary", "https://www.helgilibrary.com/charts/which-country-produces-the-most-dates-55/"),
    (2023, 9820000, 1320000, "FAO figures as charted by Statista (rounded)", "https://statista.com/chart/amp/29563/biggest-producers-of-dates"),
]
write("world_position.csv", ["year", "world_production_t", "algeria_production_t", "algeria_share_pct", "source", "source_url"],
      [[y, w, a_, round(100 * a_ / w, 1), src, u] for y, w, a_, src, u in WORLD])

# ------------------------------------------------------------ 10. trade
TRADE = [
    (2023, 83000, 73.0, "ONS, as reported by TSA", "https://www.tsa-algerie.com/tebboune-devoile-le-prix-choquant-des-dattes-algeriennes-a-lexport/"),
    (2024, 66948, 108.4, "Trade Map, as reported by Agence Ecofin", "https://www.agenceecofin.com/actualites-agro/1206-129130-l-algerie-prepare-une-offensive-pour-accroitre-ses-exportations-de-dattes"),
    (2024, 26481, 87.1, "UN Comtrade, as reported by Selina Wamucii", "https://www.selinawamucii.com/fr/connaissances/prix/algerie/dattes/"),
    (2025, 185000, 184.0, "Trade Map, as reported by CapMad ('near' 185,000 t, 'about' 184 M USD)", "https://www.capmad.com/article/filiere-dattes-lalgerie-veut-franchir-un-nouveau-palier-a-linternational"),
]
write("exports.csv", ["year", "export_volume_t", "export_value_musd", "unit_value_usd_per_t", "share_of_production_pct", "source", "source_url"],
      [[y, v, m, round(m * 1e6 / v), (round(100 * v / NAT[y], 1) if y in NAT else ''), src, u] for y, v, m, src, u in TRADE])

# ------------------------------------------- 11. regional structure, 2017
STRUCT = [
    ("Biskra", 27.4, 23.1, 41.2),
    ("El Oued", 22.0, 22.4, 25.0),
]
write("regional_structure_2017.csv",
      ["wilaya", "share_of_palm_area_pct", "share_of_palms_pct", "share_of_production_pct", "boundary_note", "source", "source_url"],
      [list(x) + ["pre-2021 boundaries", "MADRP (2017), as reproduced by SIDAB-CACI", "https://sidab.caci.dz/?page_id=427"] for x in STRUCT])

# ------------------------------------------------ 12. yields and prices
YP = [
    ("Biskra", "Deglet Nour yield", 80, 85, "kg/palm"), ("Ouargla", "Deglet Nour yield", 70, 76, "kg/palm"),
    ("El Oued", "Deglet Nour yield", 60, 65, "kg/palm"),
    ("Biskra", "Deglet Nour price on branch, local market", 300, 450, "DZD/kg"),
    ("El Oued", "Deglet Nour price on branch, local market", 130, 250, "DZD/kg"),
]
write("yields_prices_2016_2017.csv", ["wilaya", "indicator", "low", "high", "unit", "source", "source_url"],
      [list(x) + ["ITDAS Biskra conjuncture note 2016-2017, as reported by Algerie-Eco", "https://algerie-eco.com/?p=23966"] for x in YP])

# ------------------------------------------ 13. composition and conversion
COMP = [
    ("Date pits", "Crude fibre", 37.72, "% DM", "CIHEAM Options Mediterraneennes A109 (2014)", "https://ressources.ciheam.org/ressources/om/pdf/a109/00007699.pdf"),
    ("Date pits", "Crude protein", 8.87, "% DM", "CIHEAM Options Mediterraneennes A109 (2014)", "https://ressources.ciheam.org/ressources/om/pdf/a109/00007699.pdf"),
    ("Date pits", "Fat", 6.29, "% DM", "CIHEAM Options Mediterraneennes A109 (2014)", "https://ressources.ciheam.org/ressources/om/pdf/a109/00007699.pdf"),
    ("Date pits", "In vitro dry matter digestibility", 22.78, "%", "CIHEAM Options Mediterraneennes A109 (2014)", "https://ressources.ciheam.org/ressources/om/pdf/a109/00007699.pdf"),
    ("Palm leaves", "Neutral detergent fibre", 609, "g/kg DM", "Boufennara et al. (2016)", "https://doi.org/10.9755/EJFA.2016-01-104"),
    ("Palm leaves", "Acid detergent fibre", 435, "g/kg DM", "Boufennara et al. (2016)", "https://doi.org/10.9755/EJFA.2016-01-104"),
    ("Palm leaves", "Lignin", 84, "g/kg DM", "Boufennara et al. (2016)", "https://doi.org/10.9755/EJFA.2016-01-104"),
    ("Palm leaves", "Crude protein", 64, "g/kg DM", "Boufennara et al. (2016)", "https://doi.org/10.9755/EJFA.2016-01-104"),
    ("Low-value dates (Degla Beida)", "Total sugars in juice", 62.89, "%", "Guetni et al. (2024)", "https://doi.org/10.54966/jreen.v1i1.1256"),
    ("Low-value dates (Degla Beida)", "Ethanol concentration after fermentation", 86.79, "g/l", "Guetni et al. (2024)", "https://doi.org/10.54966/jreen.v1i1.1256"),
    ("Low-value dates (Timjouhart)", "Ethanol concentration after fermentation", 68.64, "g/l", "Guetni et al. (2024)", "https://doi.org/10.54966/jreen.v1i1.1256"),
    ("Common date waste", "Ethanol yield", 250, "ml/kg", "Boulal et al. (2016)", "https://doi.org/10.5897/AJB2016.15368"),
    ("Low-quality dates", "Ethanol yield", 350, "ml/kg", "Oucif Khaled and Segni (2014)", "https://doi.org/10.5897/AJAR2014.8765"),
]
write("composition_conversion.csv", ["material", "property", "value", "unit", "source", "source_url"], COMP)

# ------------------------------------------------- 14. AI grading studies
AI = [
    ("ElHelew et al. (2024)", "Accepted versus rejected fruit; three Egyptian varieties", 5945, "Inception-ResNet-v2", "98.99 (accuracy)", "https://doi.org/10.21608/mjae.2024.286079.1137"),
    ("Almutairi et al. (2024)", "Detection and classification of nine Saudi varieties", 1735, "YOLOv8", "99.1 (precision)", "https://doi.org/10.1109/access.2024.3433485"),
    ("Alhamdan and Howe (2021)", "Nine varieties, controlled environment", 1658, "Convolutional neural network", "97 (accuracy)", "https://doi.org/10.1007/978-3-030-69717-4_16"),
    ("Neji et al. (2024)", "Variety identification on two public data sets, Saudi Arabia and Turkey", "", "DenseNet121 + Vision Transformer + XGBoost", "99.93 (Saudi set); 99.65 (Turkish set), accuracy", "https://doi.org/10.1016/j.neucom.2024.127976"),
    ("Aiadi et al. (2022)", "Variety classification; public benchmark of 20 date varieties, Algerian authors", "", "VGG-F and PCANet features fused by discriminant correlation analysis", "benchmark introduced", "https://doi.org/10.1109/access.2022.3194550"),
    ("Boumaraf et al. (2026)", "Eight quality grades, Deglet Nour and Mech-Degla, samples from an industrial sorting facility in Algeria", 853, "Multi-view RGB, with and without thermal image and weight", "fusion outperforms RGB alone for every architecture", "https://doi.org/10.1007/s11694-026-04193-1"),
]
write("ai_date_grading_studies.csv", ["study", "task", "images_or_samples", "model", "reported_performance", "source_url"], AI)


# ------------------------------------------------- 15. governance (WGI)
WGI_DIM = {"ge": "Government effectiveness", "rq": "Regulatory quality", "rl": "Rule of law", "cc": "Control of corruption"}
wgi = [r for r in csv.DictReader(open(RAW / "wgi" / "wgi_2025_DZA_EGY_TUN_QAT_ge_rq_rl_cc.csv", encoding="utf-8"))
       if int(r["year"]) >= 2015]
write("governance_wgi.csv",
      ["economy_code", "economy", "year", "dimension_code", "dimension", "estimate", "ci90_low", "ci90_high",
       "score_0_100", "n_sources", "status", "source", "source_url"],
      [[r["economy_code"], r["economy"], r["year"], r["dimension"], WGI_DIM[r["dimension"]],
        round(float(r["estimate"]), 3), round(float(r["ci90_low"]), 3), round(float(r["ci90_high"]), 3),
        round(float(r["score_0_100"]), 1), r["n_sources"], "observed_official",
        "World Bank, Worldwide Governance Indicators, 2025 release", "https://www.worldbank.org/en/publication/worldwide-governance-indicators"]
       for r in wgi])

# ------------------------------- 16. audit of the Dataset_Residus workbook
DR = RAW / "dataset_residus_2020_2025"
reg = list(csv.reader(open(DR / "regional.csv", encoding="utf-8")))[1:]
rbr = list(csv.reader(open(DR / "residues_by_region.csv", encoding="utf-8")))[1:]
est = list(csv.reader(open(DR / "residue_estimates.csv", encoding="utf-8")))[1:]
regsum = {}
for w_, y_, p_, *_ in reg:
    regsum[int(y_)] = regsum.get(int(y_), 0) + int(float(p_))
fr2020 = sum(int(float(r[8])) for r in rbr if r[1] == "2020")
fr2020_s3 = int(float([r for r in est if r[0].startswith("Palmes") and r[1] == "2020"][0][3]))
ww2020 = [r for r in est if r[0].startswith("Eaux") and r[1] == "2020"][0]
def regval(w_, y_, col):
    return int(float([r for r in reg if r[0] == w_ and r[1] == str(y_)][0][col]))
AUD = [
    ("National production 2020 (labelled FAO)", 1192000, 1151909, "FAOSTAT", "Series labelled FAO is flat at 1,192,000 t for 2020-2023 and does not match FAOSTAT"),
    ("National production 2022 (labelled FAO)", 1192000, 1242304, "FAOSTAT", "Does not match FAOSTAT"),
    ("National production 2023 (labelled FAO)", 1192000, 1320000, "FAO, as charted by Statista", "Does not match FAO"),
    ("Exports 2023, tonnes", 130000, 83000, "ONS, in TSA (2025)", "Overstated"),
    ("Exports 2023, million USD", 310, 73, "ONS, in TSA (2025)", "Overstated by a factor of about four"),
    ("Biskra share of national production (%)", 60, 41.2, "MADRP (2017)", "Overstated"),
    ("Biskra palm stock 2021", regval("Biskra", 2021, 4), 4345045, "DSA (2021), in Haddou thesis", "Overstated"),
    ("Ouargla palm stock 2021", regval("Ouargla", 2021, 4), 2568511, "DSA Ouargla (2021), in Haddou thesis", "Overstated"),
    ("Ouargla palm stock 2025", regval("Ouargla", 2025, 4), 1259632, "DSA Ouargla, Radio Algerie (2026)", "Overstated; current boundaries"),
    ("El Oued production 2022", regval("El Oued", 2022, 2), 120000, "APS (2023)", "Understated by half"),
    ("Ouargla production 2024", regval("Ouargla", 2024, 2), 90449, "DSA Ouargla, Radio Algerie (2026)", "Overstated"),
    ("Biskra production 2023", regval("Biskra", 2023, 2), 400000, "DSA Biskra forecast, 'more than'", "Nearly twice an official lower bound; not strictly testable"),
    ("Ten-wilaya production 2021", regsum[2021], 1188803, "FAOSTAT (national total)", "Regional sum exceeds the national total"),
    ("National palm stock 2020", 18000000, 18600000, "MADRP (2017), 'more than'", "Consistent in order of magnitude; unverified"),
    ("National palm area 2020 (ha)", 170000, 167000, "MADRP (2017)", "Consistent in order of magnitude; unverified"),
    ("Dry fronds 2020: sheet 3 total vs sum of sheet 4", fr2020_s3, fr2020, "Internal check", "Two sheets of the same file disagree"),
    ("Wastewater 2020: stated rate applied to production vs stated quantity", round(0.25 * 1192000), int(float(ww2020[3])), "Internal check", "Stated rate (25%) and stated quantity are inconsistent"),
]
write("audit_dataset_residus.csv",
      ["item", "value_in_file", "reference_value", "ratio_file_to_reference", "reference_source", "verdict"],
      [[i, v, r, round(v / r, 2), src, ver] for i, v, r, src, ver in AUD])

# --------------------------------------------------------- 17. data gaps
GAPS = [
    ("G01", "Pruning residue per palm in the Souf (kg/palm/year) by variety and age class", "4.6, 4.7 (Table 6, Fig. 2)", "Literature range 20-65 kg; no local measurement", "Field measurement at annual pruning on 30-60 palms in 3 age classes and 2 varieties; weigh fronds, petioles, fibre; oven moisture", "Authors (Faculty of Natural and Life Sciences); grower cooperatives", "kg dry matter per palm", "1"),
    ("G02", "Palm stock of El Oued within current boundaries: total, productive, by variety and commune", "4.4, 4.6", "Former wilaya, 2020: 4,017,770 planted, 3,852,520 productive (MADR 2020); current boundaries bounded at 1.09-2.0 million productive palms", "Official request", "DSA El Oued", "palms, by commune", "1"),
    ("G03", "Date production by season and variety, El Oued current boundaries, 2015-2025", "4.4", "Former wilaya, 2020: 277,550 t by variety (MADR 2020); current boundaries: one season (about 120,000 t, reported May 2023)", "Official request", "DSA El Oued; Chamber of Agriculture", "tonnes per season and variety", "1"),
    ("G04", "Share of fruit rejected at sorting and conditioning, by defect class", "4.6, 5.2", "Literature 10-15% (grade losses), 30% (all losses), h'chef up to 30% (Djerbi 1994)", "Weighing of reject streams at 3-5 packing units over one season", "Packing and conditioning units", "% of intake, by class and week", "1"),
    ("G05", "Register of packing, conditioning and processing units: number, capacity, location", "4.8 (Table 9), 5", "No verified count; one unverified figure (303 operators, 2008)", "Official request and site visits", "DSA; Directorate of Commerce; CNRC register; ANDI", "units, tonnes per year", "1"),
    ("G06", "Current fate of residues: burnt, fed, sold, left on plot", "4.8, 6", "No local figure", "Grower survey (about 150 holdings, stratified by commune and size)", "Authors", "% of residue by fate", "1"),
    ("G07", "Prices of low-grade dates, pits, fronds, compost and concentrate feed", "5.3, 6", "Deglet Nour price range 2016-2017 only", "Monthly market survey over one season", "Wholesale markets of El Oued; feed traders", "DZD per kg", "1"),
    ("G08", "Livestock numbers (sheep, goats, camels) and purchased feed use", "4.4, 5.3", "None in database", "Official request; breeder survey", "DSA El Oued; breeders' associations", "head; tonnes of feed per year", "2"),
    ("G09", "Area under potato and vegetables, and organic fertiliser use", "4.4, 5.3", "National potato share (about 45%) only", "Official request; grower survey", "DSA El Oued", "hectares; tonnes of manure and compost", "2"),
    ("G10", "Composition of El Oued residue classes: moisture, sugars, fibre, protein, contaminants", "4.7 (Table 8)", "Measurements on other varieties and regions", "Laboratory analysis of graded samples", "Authors (Faculty of Natural and Life Sciences)", "% dry matter", "2"),
    ("G11", "Labelled image set of rejected fruit and residue classes from El Oued", "2.3 (Table 1), 5.2", "None; published sets cover marketable fruit of other varieties", "Image capture on sorting lines and at collection points", "Packing units; authors", "images per class", "2"),
    ("G12", "Plot locations, distances and transport cost per tonne-kilometre", "5.2 (routing)", "None", "GIS layer from agricultural services; survey of transporters", "DSA; transporters", "coordinates; DZD per t-km", "2"),
    ("G13", "Willingness to pay for graded feed and compost", "7.1 (Propositions 1-2)", "None", "Choice experiment with breeders and vegetable growers", "Authors", "DZD per tonne premium", "2"),
    ("G14", "Digital readiness of growers: smartphone, internet, mobile payment use", "6", "None at local level", "Items added to the grower survey", "Authors", "% of holdings", "3"),
    ("G15", "Regulatory texts on compost and feed standards and on open burning", "6", "Not compiled", "Documentary search", "Journal Officiel; ministries of agriculture and environment", "list of texts", "3"),
    ("G16", "Eligibility of residue ventures for public support schemes", "6", "Not compiled", "Documentary search and interviews", "ANADE; agricultural support funds; banks", "list of schemes and conditions", "3"),
    ("G17", "Date exports by HS 080410: volume, value and partner, 2015-2025, from one consistent source", "4.3 (Table 4)", "Three compilations that disagree", "Download from UN Comtrade (reporter and mirror data)", "UN Comtrade", "tonnes; USD", "3"),
]
write("data_gaps.csv",
      ["gap_id", "variable", "chapter_section", "best_available_now", "collection_method", "holder_or_responsible", "unit_and_granularity", "priority"],
      GAPS)


# ------------------------------------------- 18. MADR 2020 by wilaya
MADR = [
    # wilaya, area_ha, palms_planted, palms_productive, production_t, dn_qx, ghars_qx, db_qx, yield_qx_ha
    ("Biskra", 44051, 4448867, 4360000, 476929, 3080000, 600000, 1089287, 109.4),
    ("El Oued", 38495, 4017770, 3852520, 277550, 1835800, 502400, 437300, 72.0),
    ("Adrar", 28320, 3798759, 2825633, 93568, 0, 0, 935681, 33.1),
    ("Ouargla", 22909, 2680749, 2466474, 169317, 982514, 612638, 98019, 68.6),
    ("Ghardaia", 11439, 1305510, 1148486, 61200, 245000, 100700, 266300, 53.3),
    ("Algeria (national)", 170501, 19194753, 16730434, 1151909, "", "", "", ""),
]
NATL = MADR[-1]
rows = []
for w_, a_, pl, pr, t_, dn, gh, db, y_ in MADR:
    rows.append([w_, 2020, a_, round(100 * a_ / NATL[1], 2), pl, round(100 * pl / NATL[2], 2), pr, round(100 * pr / NATL[3], 2),
                 t_, round(100 * t_ / NATL[4], 2), dn, gh, db, y_, round(1000 * t_ / pr, 1), round(100 * pr / pl, 1),
                 "pre-2021 boundaries (El Oued includes El Meghaier, Biskra includes Ouled Djellal, Ouargla includes Touggourt)",
                 "observed_official", "MADR (2020) and ITDAS Biskra, Tables 04-05 in Maachi (2022), Master's dissertation, University of Biskra",
                 "http://archives.univ-biskra.dz/bitstream/123456789/22522/1/lillia_maachi.pdf"])
write("madr_2020_wilaya.csv",
      ["wilaya", "year", "palm_area_ha", "area_share_pct", "palms_planted", "planted_share_pct", "palms_productive", "productive_share_pct",
       "production_t", "production_share_pct", "deglet_nour_qx", "ghars_qx", "degla_beida_qx", "yield_qx_per_ha",
       "kg_per_productive_palm_derived", "productive_share_of_planted_pct_derived", "boundary_note", "status", "source", "source_url"], rows)

# ------------------------------- 19. indicators compiled in November 2026
COLL = [
    # item, value, unit, scope, status, source_id, source, url
    ("Downgraded Deglet Nour (h'chef) as share of production, upper value", "up to 30", "% of production", "Algeria, varies with the year's climate; no region stated", "literature_secondary", "S39",
     "Djerbi (1994), cited in Benyahia-Krid et al. (2021), Food and Nutrition Sciences 12(6)", "https://doi.org/10.4236/fns.2021.126047"),
    ("Production shares of the main wilayas", "Biskra 31; Ouargla 19; El Oued 27", "% of national production", "Algeria; year not stated", "observed_secondary", "S40",
     "CARI / OSSMENA-DELP (2023)", "https://www.cariassociation.org/wp-content/uploads/2023/09/OSSMENA-DELP_Approche-filiere.pdf"),
    ("Average productive palms 2010-2019", "14,840,209", "palms", "Algeria", "collected_unverified", "S1",
     "ONS (2020), Retrospective agriculture 2010-2019", "https://www.ons.dz/IMG/pdf/retrospective_agricultures2010_2019.pdf"),
    ("Average productive palms 2010-2019 by type: Deglet Nour; soft; dry", "6,075,200; 3,008,424; 5,756,584", "palms", "Algeria", "collected_unverified", "S1",
     "ONS (2020), Retrospective agriculture 2010-2019", "https://www.ons.dz/IMG/pdf/retrospective_agricultures2010_2019.pdf"),
    ("Defective or rejected fruit share", "5.55-26.77", "% of fruit", "Egypt, 2015/16-2016/17, by variety and season", "collected_unverified", "S4",
     "Applied Ecology and Environmental Research 17(3)", "https://aloki.hu/pdf/1703_59655974.pdf"),
    ("Harvest loss; post-harvest loss", "10-15; 8.1", "%", "Comparative only; reference does not match the country stated", "not_verified", "S5",
     "Reference to be identified; the link given concerns Saudi Arabia", "https://ijoear.com/article-details/assessment-of-postharvest-loss-and-waste-for-date-palms-in-the-kingdom-of-saudi-arabia"),
    ("Cellulose; lignin in empty fruit bunch fibres, five cultivars", "33.08-49.28; 20.19-40.50", "% dry matter", "Southeast Algeria", "collected_unverified", "S11",
     "Study of date palm empty fruit bunch fibres, Southeast Algeria", "https://www.researchgate.net/publication/365829053"),
    ("Sheep flock", "more than 28 million; about 60% in the steppe", "head", "Algeria, 2017", "collected_unverified", "S13",
     "Cahiers Agricultures (2020)", "https://www.cahiersagricultures.fr/articles/cagri/full_html/2020/01/cagri190226/cagri190226.html"),
    ("NPK 15-15-15 applied to potato", "220", "kg per hectare", "El Oued sample, 2004", "collected_unverified", "S17",
     "FAO, Fertilizer use by crop in Algeria", "https://openknowledge.fao.org/bitstreams/00bc0eea-ffe9-4c7d-b9c9-ed68a786146d/download"),
    ("Bioenergy capacity targets", "360 (2015-2020); 640 (2021-2030)", "MW", "Algeria, renewable energy programme", "collected_unverified", "S18-S19",
     "Algerian energy policy review; Journal Officiel 2017 no. 31", "https://www.joradp.dz/FTP/jo-francais/2017/F2017031.pdf"),
    ("Internet subscriptions; share mobile", "57,536,959; 89.20", "subscriptions; %", "Algeria, end of Q4 2024", "collected_unverified", "S21",
     "ARPCE, Internet market Q4 2024", "https://www.arpce.dz/fr/file/x6v1d6"),
    ("General framework law on waste management and valorisation", "Law 01-19 of 12 December 2001", "legal text", "Algeria", "collected_unverified", "S27",
     "Journal Officiel 2001 no. 77", "https://www.joradp.dz/FTP/jo-francais/2001/F2001077.pdf"),
    ("Composting duration; total P, one palm-frond mixture", "136; 0.52", "days; %", "Experimental", "collected_unverified", "S33",
     "Biomass Conversion and Biorefinery (2022)", "https://link.springer.com/article/10.1007/s13399-022-03387-z"),
    ("Biogas yield; methane share, date palm wastes", "up to 342.2; up to 50", "L per kg VS; %", "Experimental", "collected_unverified", "S34",
     "BioResources", "https://bioresources.cnr.ncsu.edu/resources/biogas-production-through-the-anaerobic-digestion-of-date-palm-tree-wastes-process-optimization/"),
    ("Share of rejected dates in production attributed to Chehma (2001)", "about 25", "%", "Southeast Algeria", "not_verified", "-",
     "Not found in the documents cited for it; not used", ""),
    ("Packing units linked to date conditioning, El Oued (DSASI 2008); units in Biskra (2021)", "303; 78", "operators; units", "El Oued 2008; Biskra 2021", "not_verified", "S41",
     "Ben-Sayah, University of Ouargla; document could not be opened", "https://dspace.univ-ouargla.dz/jspui/bitstream/123456789/37516/1/BEN-SAYAH-FAIZA.pdf"),
]
write("collected_indicators_nov2026.csv",
      ["item", "value", "unit", "scope", "status", "source_id", "source", "source_url"], COLL)

# ------------------------------------------------------------- 8. checks
checks = {
    "panel_rows": len(panel),
    "panel_sum_vs_national": {str(y): {"panel_sum_t": sums[y], "national_t": NAT.get(y),
                                       "excess_t": (sums[y] - NAT[y]) if y in NAT else None}
                              for y in sorted(sums)},
    "pathways_naive_total_t": sum(float(r[2]) for r in rows),
    "pathways_distinct_feedstock_t": {k: v for k, v in feed.items()},
    "el_oued_scenarios_total_t": {s[0]: None for s in SCEN},
}
for r in csv.DictReader(open(OUT / "el_oued_residue_scenarios.csv", encoding="utf-8")):
    checks["el_oued_scenarios_total_t"][r["scenario"]] = int(r["total_residues_t"])
json.dump(checks, open(OUT / "consistency_checks.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(json.dumps(checks, indent=2, ensure_ascii=False))
