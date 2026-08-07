# One-Piece Knit by Hand Crank — Feasibility Verdict

*the knit face of the [Smart Loom](smart-loom.md) · grounded research, cited · 2026-06-21*

## 1. Verdict by rung

| Rung | Verdict | One-line |
|---|---|---|
| **Seamless tube** (plain stockinette circle) | **EXISTS** | Hand-crank CSMs ship today; Erlbacher $2,198–$2,448 metal, Addi/Sentro ~$50 plastic. |
| **Patterned tube** (jacquard color/texture on a tube) | **REACHABLE** | Each half exists separately — flatbed punchcard does selection, CSM does the tube — but no hand-crank machine fuses them. |
| **Tube-garment** (one shaped 3D piece off the machine) | **EXISTS for socks/hats; REACHABLE for sweater-grade** | CSM short-rows a true 3D heel by hand today; on-machine end-closure and tube-joining stay manual. |
| **Fully-shaped whole garment** (body + sleeves joined, one piece, patterned) | **FRONTIER** | Bounded by per-loop holddown under tension during shaping; Courtaulds patented the method 1967 (US3668898A), Shima shipped 1995. |

## 2. The real bottleneck — *correction to the working thesis*

"Jacquard is solved, shaping is the wall" is **right in spirit, wrong in the named mechanism.**

- **Jacquard / needle selection: SOLVED and hand-driveable.** 50-year-old commodity (punchcard domestics; AYAB re-homes it onto a ~$30 Arduino, full 200-needle width). The card already came home. No caveat.
- **Stitch transfer is ALSO solved and hand-driveable** — the correction. The Brother **KA-8300** transfers a full course of loops between two beds, purely mechanical, hand-pushed, zero servos. Lace carriages do card-controlled intra-bed transfer by hand. Double-cylinder CSMs transferred between opposed beds a century ago. "Transfer is the wall" does not survive scrutiny.
- **The actual wall: keeping every loop alive under correct, independently-zoned tension while the fabric is a moving tube of changing width** — the **sinker + holddown + takedown** subsystem, plus long-range racking to bring sleeve-tubes adjacent to the body. It is the part with no free human hand to manage dozens of simultaneously-slipping loops; the recurring Shima upgrade target 1995→2022 (movable sinkers, dual takedown); the exact failure mode the cheap projects name (Kniterate: center short-rows >2–3 rows "not recommended," no sinkers → fabric lifts off). **This, not jacquard or transfer, is what wants active per-needle elements rather than a crank.**

## 3. Who's already close

| Project | Proves | Missing | Price |
|---|---|---|---|
| **AYAB / Knitic** | Patterning fully devolved — hand-driven computer needle selection on a used Brother | Single-bed; flat panels only; no shaping | ~$50 board + used machine (<$600 all-in) |
| **CSM (Erlbacher, Addi)** | Hand-crank shaping — seamless tube + true 3D heel via held-needle short-rows | No needle selection; no end-closure; no tube-joining | $2,198–$2,448 / ~$50 |
| **Brother KA-8300** | Inter-bed full-course transfer is hand-driveable, no servos | A unit operation, not a garment system; no takedown control | used, low hundreds |
| **OpenKnit** | The only cheap *double-bed* one-piece attempt | Stalled — finicky, motorized; creator left for a $16k machine | ~€550 BOM |
| **Kniterate** | Desktop double-bed does real transfer + fully-fashioned shaping | Motor-driven not hand-crank; whole-garment "untested, would produce very small results" | **$15,999** |
| **CMU autoknit** | Shaping is software-solvable — arbitrary 3D mesh → machine instructions | Runs only on $50k+ Shima iron; output has **no patterning** | industrial |

**The clean split that proves the diagnosis:** AYAB = patterning, no shaping. autoknit = shaping, no patterning. The two halves were solved by different communities on different hardware and **have never been cheaply united.** That gap *is* the opportunity.

## 4. The realistic devolved product

**A hand-crank circular machine with electronic per-needle selection — a "patterned tube-garment" machine.**

- **Architecture:** CSM-style cylinder (the living hand-crank shaping precedent) + AYAB-style solenoid/servo needle selection (the living hand-crank patterning precedent) + manual held-needle short-rowing for heels/crowns + a static ribber dial for cuffs.
- **Ships:** seamless tubes with real jacquard color/texture AND hand-shaped 3D ends — patterned socks, hats, cowls, fitted tubes. Fuses the two lineages that have never been fused at hand scale. That fusion alone is novel and sellable.
- **Honest ceiling — three hard stops:**
  1. **Both tube ends still need hands** — toe/crown closure is a manual post-process on every CSM.
  2. **No tube-joining** — sleeves-to-body, the literal definition of "whole garment," has no hand-crank precedent. You ship shaped tubes, not assembled garments.
  3. **Patterning-on-circular is itself real work** — per-needle selection is a *flatbed* achievement; porting it to a rotating cylinder is engineering, not a parts swap.

Ambitious-but-real. Not a devolved Shima Seiki — a patterned sock/hat machine. An honest, shippable product, not the dream.

## 5. The gap to the dream

**One mechanism, if cracked at hand scale, unlocks fully-shaped whole garments: per-loop holddown — a passive, hand-driven sinker/takedown that keeps every loop tensioned and on its needle during transfer and short-rowing on a tube of changing width.**

Everything else on the path is already hand-proven in isolation:
- selection → AYAB · inter-bed transfer → KA-8300 · 3D short-row shaping → CSM heel · small-range racking → domestic ribbers · the scheduling intelligence → CMU autoknit (open, published — the *cheapest* part).

The single missing primitive is the one a crank can't supply because it needs many independent, simultaneous points of control: **active per-loop tension.** That is what took Courtaulds-1967 → Shima-1995, the recurring Shima upgrade for 30 years, and the named failure mode of every cheap project. Crack a passive/mechanical equivalent of the movable-sinker-plus-takedown stack and the whole garment falls out. Until then: patterned tubes with hand-finished ends.

---

**Net:** the patterning half is free; the wall is **loop-tension-during-shaping**, not stitch transfer (transfer is already hand-driven). A patterned hand-crank tube-garment machine is a real, shippable solo project. A hand-cranked whole-garment machine is gated on one un-devolved mechanism: **active per-loop holddown.**

## 6. The lock, and gravity as the key — a design hypothesis

*(reasoned from the grounding above, not yet itself grounded — a direction to test, not a verdict.)*

Look at the lock again and it rhymes with the machine's own founding trick. The weave face solved tension by hanging weights — gravity, not springs or ratchets, because **gravity is constant-force and self-equalizing.** The knit lock is also a tension problem: keep every loop under its own pull while the fabric shifts. So ask the obvious question — **can gravity hold the loops the same way it tensions the warp?**

It already partly does, and the precedents are humble:

- The **CSM's hanging weight** (the "bonnet") *is* gravity takedown on a tube — passive, hand-scale, proven.
- Machine knitters **hang claw weights on held stitches** during short-rows for exactly this reason — passive per-region holddown, by gravity, today. It's just *placed by a human each time.*
- **Static holding-down sinkers** give a passive per-needle baseline with no servos.

So gravity per-loop holddown is not a new force to invent — it exists in pieces, manually. The invention is **making it distributed and self-managing under a crank**: a static sprung-sinker comb (passive baseline) + a gravity takedown hem (global tension) + the genuinely hard part, holddown that follows the *held/short-rowed* zones without a hand placing weights each row.

The honest envelope — and why this matters more than "match Shima":

- Passive/gravity holddown will **not** give arbitrary couture 3D. Shima went to *active movable* sinkers precisely because passive ones cap out at moderate shaping and speed. That ceiling is real; respect it.
- But it doesn't need to reach couture. It needs to move the hand-crank line from **"tube + heel"** to **"gently fitted one-piece"** — raglan and yoke sweaters, beanies with crowns, mittens, simple set-in shapes. That envelope is *most of what people actually wear.*

So the dream isn't binary. The fully-tailored seamless garment stays industrial; the **gently-fitted everyday garment comes home** the day passive distributed holddown works under a crank — and the candidate for that holddown is the same gravity that started the whole project.

**Gravity is the key, twice: it tensions the weave, and it can hold the knit.** The founding trick may answer both faces. Worth a focused research + bench pass of its own — claw-weight automation, sprung-sinker envelopes, any passive-takedown-during-shaping prior art — before it's more than a hypothesis.

## 7. How the body does it — neurulation

The flat-to-tube move that stops the loom is the move an embryo makes to build its own spinal cord. **Neurulation:** a flat sheet (the neural plate) folds — cells wedge by apical constriction — its edges rise, meet at the midline, and **fuse into a seamless tube** (the neural tube → brain + cord), zipping shut from the middle outward. Flat → fold → seam → tube. The body has run the loom's hardest trick since before it had a spine to show for it.

Three lessons fall out, and each sharpens the lock:

- **The seam closes by fusion, not thread.** The neural folds merge — the two edges become one tissue. In knitting that is grafting / linking, exactly the manual end-closure step. Nature's seam is a zip, not a stitch — which says the machine should *fuse* the edge (link live loops to live loops), not sew a finished one.
- **There is a notochord.** A stiff rod runs the midline, organizing the fold and holding the geometry while it forms. The machine analogue is a central tensioned thread or selvage the tube shapes around — a temporary *spine* for the fabric during shaping.
- **Nothing ever falls off — because the sheet is self-cohesive.** Every cell stays adhered to its neighbors through the entire fold; there is no un-held instant. That reframes the holddown: the deepest answer may be less *external gravity* and more *internal cohesion* — a stitch structure and a sequence in which every loop is always held by a neighbor, or handed off without a gap, the way cells are.

So the holddown hypothesis splits cleanly in two: hold the loops from **outside** (gravity, sinkers — the weave face's instinct) or from **within** (cohesion + a notochord — the body's instinct). The whole garment may want both, and the biological one — self-cohesion during shaping — is the part nobody has tried.

And none of it happens in dry air. The neural tube folds **within atmospheric conditions** — suspended in amniotic fluid: warm, damp, buoyant, chemically held. The medium is a *third* holder, **around** the structure, cradling the soft sheet while it is still too delicate to hold its own shape. The manufacturing echo is exact: textile mills are climate-controlled because yarn only behaves at the right warmth and humidity; and soft-tissue bioprinting forms its structures inside a gel **support bath** that holds them as they print, then melts away (FRESH — from the same CMU lab that wrote the knitting compiler). So the holders are three, not two: **outside** (gravity), **within** (cohesion), **around** (the medium). The body uses all three at once, in a warm wet field — and the spine already said why: dry space is neat and dead; *the alive is always a little wet.* A garment formed the way a body forms would form damp, warm, and held on every side — which is, precisely, *within atmospheric conditions.*
