import textwrap, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

plt.rcParams.update({"font.family": "Liberation Sans", "mathtext.fontset": "dejavusans",
                     "pdf.fonttype": 42, "svg.fonttype": "none"})

W, H = 7.5, 10.9
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

INK = "#1F2A37"; MUTED = "#4B5563"; LINE = "#9AA5B1"
BAND = {1: "#EEF2F7", 2: "#F4F6F8", 3: "#EEF2F7"}
LOOP = {"A": ("#B7791F", "#FBF1DF"), "B": ("#2F7D4F", "#E5F2EA"), "C": ("#2B6CB0", "#E3EEF9")}
GREY = ("#4A5568", "#EDEFF2")
FS = 6.7  # body font size

def cpi(fs):  # characters per inch, Liberation Sans average
    return 72 / (0.465 * fs)

def wrap(text, width_in, fs=FS, indent="", hang="   "):
    n = max(8, int(width_in * cpi(fs)))
    return textwrap.wrap(text, n, initial_indent=indent, subsequent_indent=hang)

def rbox(x, y, w, h, fc, ec, lw=0.8, r=0.05, z=1, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=z, ls=ls))

def block(x, ytop, w, items, fs=FS, gap=0.035, color=INK, lh=1.28):
    """items: list of (kind, text); kind 'b' bullet, 'p' plain, 'h' bold, 'm' math centred"""
    y = ytop
    step = fs * lh / 72
    for kind, t in items:
        if kind == "m":
            y -= step * 0.95
            ax.text(x + w / 2, y, t, ha="center", va="center", fontsize=fs + 1.3, color=color, zorder=5)
            y -= step * 0.75 + gap
            continue
        if kind == "b":
            lines = wrap(t, w - 0.02, fs, indent="• ", hang="   ")
        else:
            lines = wrap(t, w - 0.02, fs, indent="", hang="")
        for ln in lines:
            y -= step
            ax.text(x, y + step * 0.15, ln, ha="left", va="baseline", fontsize=fs, color=color,
                    fontweight="bold" if kind == "h" else "normal", zorder=5)
        y -= gap
    return y

def arrow(x1, y1, x2, y2, color=MUTED, lw=1.0, ls="-", ms=8, cs="arc3"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=ms,
                                 color=color, lw=lw, ls=ls, connectionstyle=cs, zorder=6,
                                 shrinkA=0, shrinkB=0))

def band(y0, y1, label, n):
    rbox(0.08, y0, W - 0.16, y1 - y0, BAND[n], "#C7D0DB", lw=0.9, r=0.08, z=0)
    ax.add_patch(Rectangle((0.08, y1 - 0.27), W - 0.16, 0.27, fc="#1F3A5F", ec="none", zorder=1))
    ax.text(0.2, y1 - 0.135, label, ha="left", va="center", fontsize=8.2, color="white",
            fontweight="bold", zorder=2)

# ------------------------------------------------------------------ LEVEL 1
L1_top, L1_bot = H - 0.08, H - 1.88
band(L1_bot, L1_top, "LEVEL 1  ·  Institutional diagnosis and graded evidence base  (Sections 2–4)", 1)
bx_top = L1_top - 0.38; bx_bot = L1_bot + 0.1
xs = [0.2, 2.68, 5.16]; bw = [2.2, 2.2, 2.14]
titles = ["1  Institutional diagnosis", "2  Graded evidence base (four tiers)", "3  Mass balance and scenarios"]
contents = [
    [("b", "The missing residue market is an institutional failure, not a technical one"),
     ("b", "Information asymmetry on quality (Akerlof)"),
     ("b", "High cost of measuring heterogeneous lots (Barzel)"),
     ("b", "Hold-up risk on specific investment (Williamson)")],
    [("b", "Tier 1: official statistics (El Oued ≈ 120,000 t of dates)"),
     ("b", "Tier 2: published coefficients (α = 0.10–0.30; β = 20–65 kg per palm)"),
     ("b", "Tier 3: derived scenarios"),
     ("b", "Tier 4: unverified estimates, excluded from the argument")],
    [("m", r"$R = \alpha P + \beta N\,/\,1{,}000$"),
     ("p", "N = productive palms (1.09–2.0 million)"),
     ("b", "Low: 33,800 t per year"),
     ("b", "Central: 76,450 t per year"),
     ("b", "High: 166,000 t per year")],
]
for i in range(3):
    rbox(xs[i], bx_bot, bw[i], bx_top - bx_bot, "white", "#7F8EA3", lw=0.9)
    ax.add_patch(Rectangle((xs[i], bx_top - 0.25), bw[i], 0.25, fc="#DCE4EE", ec="none", zorder=2))
    ax.text(xs[i] + 0.08, bx_top - 0.125, titles[i], ha="left", va="center", fontsize=7.2,
            fontweight="bold", color=INK, zorder=3)
    block(xs[i] + 0.08, bx_top - 0.29, bw[i] - 0.14, contents[i])
for i in range(2):
    arrow(xs[i] + bw[i] + 0.02, (bx_top + bx_bot) / 2 - 0.1, xs[i + 1] - 0.02, (bx_top + bx_bot) / 2 - 0.1, ms=9)

# ------------------------------------------------------------------ LEVEL 2
L2_top = L1_bot - 0.24
L2_hdr = ("LEVEL 2  ·  Operating matrix: five components × three valorisation loops  (Section 5)")

x0 = 0.2; lw_ = 1.32; gx = 0.06
cw = (W - 0.2 - x0 - lw_ - 3 * gx) / 3
cx = [x0 + lw_ + gx + k * (cw + gx) for k in range(3)]
hdr_top = L2_top - 0.34; hdr_h = 0.42
heads = [("A", "Loop A · Feed", "Short term · ready now"),
         ("B", "Loop B · Soil and compost", "Medium term · largest volume"),
         ("C", "Loop C · Energy and biochemicals", "Long term · highest value")]
for k, (key, t1, t2) in enumerate(heads):
    dark, light = LOOP[key]
    rbox(cx[k], hdr_top - hdr_h, cw, hdr_h, dark, dark, r=0.04, z=2)
    ax.text(cx[k] + cw / 2, hdr_top - 0.15, t1, ha="center", va="center", fontsize=7.4,
            fontweight="bold", color="white", zorder=3)
    ax.text(cx[k] + cw / 2, hdr_top - 0.31, t2, ha="center", va="center", fontsize=6.4,
            color="white", style="italic", zorder=3)
ax.text(x0 + lw_ / 2, hdr_top - hdr_h / 2, "Components  ↓\n Loops  →", ha="center", va="center",
        fontsize=6.6, color=MUTED, style="italic")

rows = [
    ("1|Inputs and\ndata flows", 0.7, [
        [("b", "Sound fruit rejected on size or colour; pits; press cake"), ("p", "Source: packing units")],
        [("b", "Fronds, petioles, fibre, emptied bunches"), ("b", "Fermented or infested fruit"), ("p", "Source: dispersed plots")],
        [("b", "Sugar-rich rejected fruit; clean, dry pits"), ("p", "Source: strict sorting at intake")]]),
    ("2|AI functions\nlowering\nmeasurement and\ncoordination costs", 1.0, [
        [("b", "Grading: computer vision with rapid sub-sample tests (Brix, moisture, mycotoxins)"),
         ("b", "Forecasting breeders' demand")],
        [("b", "Phone-based residue classification (type, dryness, sand)"),
         ("b", "Collection routing (CVRP):"), ("m", r"$\min \sum_{k}\sum_{(i,j)} c_{ij}\,x_{ijk}$"),
         ("b", "Chipping on the plot or at the collection point")],
        [("b", "Strict grading for purity and sugar content"),
         ("b", "Multi-year supply forecasting to size the plant")]]),
    ("3|Valorisation\nloops (cascade)", 0.92, [
        [("p", "Products: feed blocks, concentrate supplement"), ("p", "Buyers: sheep, goat and camel breeders"),
         ("p", "Capital intensity: low")],
        [("p", "Products: compost and mulch for sandy soils"),
         ("p", "Buyers: potato and vegetable growers under pivot irrigation; palm growers"),
         ("p", "Capital intensity: medium")],
        [("p", "Products: bio-ethanol (250–350 mL/kg), syrup, activated carbon from pits"),
         ("p", "Buyers: industry, fuel blenders, water treatment"), ("p", "Capital intensity: high")]]),
]
span_rows = [
    ("4|Governance\nmechanisms\n(all loops)", 0.66, [
        ("b", "Shared grade standard set by the parties and applied by the algorithms"),
        ("b", "Cooperative data stewardship, so that no single party controls the data"),
        ("b", "Forward contracts with grade-indexed prices and seasonal volume bands"),
        ("b", "Intake inspection and direct digital payment to the originating grower (BaridiMob / CIB)")]),
    ("5|Performance\nindicators\n(Table 11)", 0.64, None),
]
gy = 0.075
y = hdr_top - hdr_h - gy
row_bounds = []
for label, h, cells in rows:
    rbox(x0, y - h, lw_, h, "#E2E8F0", "#A0AEC0", lw=0.7, r=0.03, z=2)
    num, lab = label.split("|")
    ax.text(x0 + 0.07, y - h / 2, num, ha="left", va="center", fontsize=8, fontweight="bold",
            color="#1F3A5F", zorder=3)
    ax.text(x0 + 0.22, y - h / 2, lab, ha="left", va="center", fontsize=6.8, fontweight="bold",
            color=INK, zorder=3, linespacing=1.18)
    for k, key in enumerate("ABC"):
        dark, light = LOOP[key]
        rbox(cx[k], y - h, cw, h, light, dark, lw=0.7, r=0.03, z=2)
        block(cx[k] + 0.06, y - 0.03, cw - 0.1, cells[k], fs=6.4, gap=0.02)
    row_bounds.append((y, y - h)); y -= h + gy

# cascade note under loops row
cas_y = y + gy / 2 + 0.005
for label, h, items in span_rows:
    rbox(x0, y - h, lw_, h, "#E2E8F0", "#A0AEC0", lw=0.7, r=0.03, z=2)
    num, lab = label.split("|")
    ax.text(x0 + 0.07, y - h / 2, num, ha="left", va="center", fontsize=8, fontweight="bold",
            color="#1F3A5F", zorder=3)
    ax.text(x0 + 0.22, y - h / 2, lab, ha="left", va="center", fontsize=6.8, fontweight="bold",
            color=INK, zorder=3, linespacing=1.18)
    sx, sw = cx[0], cx[2] + cw - cx[0]
    rbox(sx, y - h, sw, h, GREY[1], GREY[0], lw=0.7, r=0.03, z=2)
    if items:
        half = sw / 2
        block(sx + 0.07, y - 0.03, half - 0.12, items[:2], fs=6.4, gap=0.02)
        block(sx + half + 0.03, y - 0.03, half - 0.1, items[2:], fs=6.4, gap=0.02)
    else:
        groups = [("Circularity", "Valorisation rate; cascade quality"),
                  ("Market formation", "Graded share; contract compliance"),
                  ("Economic and environmental", "Net revenue per tonne; collection cost per t-km; burning avoided"),
                  ("Social and learning", "Grower participation; forecast error (WAPE)")]
        q = sw / 4
        for j, (g, t) in enumerate(groups):
            gx0 = sx + j * q + 0.06
            ax.text(gx0, y - 0.12, g, fontsize=6.4, fontweight="bold", color=INK, va="center", zorder=4)
            block(gx0, y - 0.18, q - 0.1, [("p", t)], fs=6.3, gap=0.0)
            if j:
                ax.plot([sx + j * q, sx + j * q], [y - h + 0.07, y - 0.07], color="#B8C2CC", lw=0.6, zorder=4)
    row_bounds.append((y, y - h)); y -= h + gy

# flow chevrons between rows inside each column
for (t1, b1), (t2, b2) in zip(row_bounds[:-1], row_bounds[1:]):
    for k in range(3):
        xm = cx[k] + cw / 2
        arrow(xm, b1 - 0.004, xm, t2 + 0.004, color="#718096", lw=0.9, ms=6)
    arrow(x0 + lw_ / 2, b1 - 0.004, x0 + lw_ / 2, t2 + 0.004, color="#718096", lw=0.9, ms=6)

L2_bot = y + gy - 0.27
arrow(W / 2, L1_bot - 0.01, W / 2, L2_top + 0.01, color="#1F3A5F", lw=1.6, ms=11)
band(L2_bot, L2_top, L2_hdr, 2)
ax.text(cx[0], L2_bot + 0.08,
        "Cascade rule: each graded lot goes to the highest-value loop for which it qualifies; each loop takes what the others cannot.",
        fontsize=6.3, style="italic", color=MUTED, va="bottom")

# ------------------------------------------------------------------ LEVEL 3
L3_top = L2_bot - 0.24
arrow(W / 2, L2_bot - 0.01, W / 2, L3_top + 0.01, color="#1F3A5F", lw=1.6, ms=11)
L3_bot = L3_top - 2.72
band(L3_bot, L3_top, "LEVEL 3  ·  Enabling conditions, feedback and testable propositions  (Sections 6–7)", 3)

top3 = L3_top - 0.38; h3 = 1.02
e_x, e_w = 0.2, 3.7; f_x = 4.25; f_w = W - 0.2 - f_x
for (bx_, bw_, ttl, items) in [
    (e_x, e_w, "Four enabling conditions (Table 13)", [
        ("b", "Data: a local labelled image set; measured pruning residue per palm (β)"),
        ("b", "Capabilities: simple phone interfaces; university laboratories for calibration"),
        ("b", "Finance: staged, with records from Loops A and B financing Loop C"),
        ("b", "Regulation: approved standards for feed and compost")]),
    (f_x, f_w, "Feedback loop", [
        ("b", "Annual recalibration of grading and forecasting models"),
        ("b", "Revised grade thresholds and contract terms"),
        ("b", "Credit records for banks and investors")])]:
    rbox(bx_, top3 - h3, bw_, h3, "white", "#7F8EA3", lw=0.9)
    ax.add_patch(Rectangle((bx_, top3 - 0.25), bw_, 0.25, fc="#DCE4EE", ec="none", zorder=2))
    ax.text(bx_ + 0.08, top3 - 0.125, ttl, fontsize=7.2, fontweight="bold", color=INK, va="center", zorder=3)
    block(bx_ + 0.08, top3 - 0.3, bw_ - 0.14, items)
arrow(e_x + e_w + 0.02, top3 - h3 / 2, f_x - 0.02, top3 - h3 / 2, ms=9)

# feedback arrow back to level 2 (AI functions row) along right margin
fx = W - 0.13
ytar = (row_bounds[1][0] + row_bounds[1][1]) / 2
ax.plot([f_x + f_w, fx], [top3 - h3 / 2, top3 - h3 / 2], color="#C05621", lw=1.3, ls=(0, (4, 2)), zorder=6)
ax.plot([fx, fx], [top3 - h3 / 2, ytar], color="#C05621", lw=1.3, ls=(0, (4, 2)), zorder=6)
arrow(fx, ytar, cx[2] + cw + 0.01, ytar, color="#C05621", lw=1.3, ms=9)
ax.text(fx - 0.04, (top3 - h3 / 2 + ytar) / 2 + 0.6, "feedback", rotation=90, fontsize=6.4, color="#C05621",
        ha="right", va="center", style="italic",
        bbox=dict(fc=BAND[2], ec="none", pad=0.6))

p_top = top3 - h3 - 0.12; p_h = p_top - (L3_bot + 0.1)
rbox(0.2, L3_bot + 0.1, W - 0.4, p_h, "white", "#1F3A5F", lw=1.0)
ax.add_patch(Rectangle((0.2, p_top - 0.25), W - 0.4, 0.25, fc="#1F3A5F", ec="none", zorder=2))
ax.text(W / 2, p_top - 0.125, "Testable propositions (Section 7)", ha="center", va="center", fontsize=7.4,
        fontweight="bold", color="white", zorder=3)
props = [("P1", "A shared grade standard applied by automated grading raises prices of higher grades, widens the price gap between grades and increases total traded value and volume."),
         ("P2", "AI-enabled grading and forecasting increase the use of forward contracts between growers and processors."),
         ("P3", "The effect of AI on valorisation is larger where growers share in governing data and grading than under a single buyer."),
         ("P4", "Capital-intensive loops (bio-ethanol) become financeable only after simpler loops have built multi-season records of graded supply.")]
yy = p_top - 0.33
for tag, t in props:
    ax.text(0.32, yy, tag, fontsize=6.9, fontweight="bold", color="#1F3A5F", va="top")
    lines = wrap(t, W - 0.4 - 0.62, 6.6, hang="")
    for ln in lines:
        ax.text(0.62, yy, ln, fontsize=6.6, color=INK, va="top"); yy -= 6.6 * 1.3 / 72
    yy -= 0.045
arrow(e_x + e_w / 2, top3 - h3 - 0.005, e_x + e_w / 2, p_top + 0.005, ms=8)

import sys
ax.set_ylim(L3_bot - 0.04, H); fig.set_size_inches(W, H - (L3_bot - 0.04))
out = sys.argv[1] if len(sys.argv) > 1 else "figures/fig3_framework"
for ext, kw in [("png", dict(dpi=600)), ("pdf", {}), ("svg", {}), ("tiff", dict(dpi=600, pil_kwargs={"compression": "tiff_lzw"}))]:
    fig.savefig(f"{out}.{ext}", bbox_inches="tight", pad_inches=0.04, **kw)
print("ok", yy, L3_bot)
