# Smart Loom — Feasibility & Design Brief

*engineering companion to [smart-loom.md](smart-loom.md) and [devolution.md](devolution.md) · 2026-06-21 · grounded research, cited*

## 1. Verdict

Possible, at maker scale, as a **semi-automatic** machine. Genuinely novel: the *specific combination* of per-cartridge gravity weights supplying self-equalizing tension **as the enabler** for tool-free snap-in warp cartridges. Almost everything else is **revival, not invention** — gravity tension is the 6,000-year-old [warp-weighted loom](https://en.wikipedia.org/wiki/Warp-weighted_loom); snap-in warp cartridges already exist in friction form (MIT [US7318456](https://patents.google.com/patent/US7318456), expired) and beading-loom form ([US7677273](https://patents.google.com/patent/US7677273B2), expired); modular reeds are sold today ([Schacht Variable Dent](https://schachtspindle.com/products/variable-dent-reeds)). The crank is the weakest claim: no historical or maker loom uses a crank to drive the shed — cranks wind/tension the beam. A crank *can* drive the shed→pick→beat cycle (every power loom does, off one crankshaft: shed 0–120°, pick 120–240°, beat 240–360°), but automating the **pick** is the historically hardest part and out of scope for v1.

## 2. The buildable design

**One configuration that holds together:** a **vertical rigid-heddle loom, gravity-tensioned by per-cartridge hanging weights, crank-driven for shed + beat, weft hand-passed.**

- **Geometry:** vertical frame. Wood/bamboo uprights + top beam carry the entire hanging load; 3D-printed (PETG/nylon) joints, crank housing, heddle and cartridge interfaces. Warp hangs from the top beam, weights at the bottom, weave proceeds top-down, beaten upward (warp-weighted convention).
- **Shed — rigid heddle.** A single rigid slat with alternating slots and eyes makes both sheds with one up/down motion, and **doubles as reed and beater**. Key simplification: collapses shed + beat + even sett into one part. Cost: sett becomes a fixed cartridge parameter.
- **Crank via a 2-position cam on the axle:** ~0–120° raise heddle (shed), ~120–240° dwell open (hand-pass weft), ~240–360° beat. Standard crankshaft logic, hand-paced, slow. **Pick stays manual in v1.**
- **Gravity-weighted snap-in warp cartridge:** each is a pre-wound warp bundle terminating in its own hanging weight, carrying its **own integrated reed/dent section** (spacing is defined by the cartridge — gravity gives tension, never spacing). Locates via a **kinematic coupling** (dovetail / V-groove + ball), not a generic clip. Load routes weight → yarn → over a bar → frame, so the snap is a **near-zero-load locating feature** ([snap-fit zero-stress rule](https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/)) — what makes it survive years.
- **Weft:** trivial — any yarn hand-passed. Sell "snap-in weft" as the consumable yarn, not a mechanism.
- **Even spacing:** solved inside the cartridge. One **shared dent-pitch module** so adjacent cartridges butt seamlessly (tongue-and-groove the edge half-dents). **Enforce equal grams-per-thread across cartridges** or mixed cartridges weave unevenly.

## 3. Honest risks (ranked)

1. **Distribution, not demand.** Lives or dies on a viral "snap in, weave in 60 seconds" demo. *Mitigation:* make the demo the product; win education/maker spaces first ([SPEERLoom, UIST 2023](https://dl.acm.org/doi/10.1145/3586183.3606724) — Jacquard-as-first-computer story).
2. **The cartridge promise.** If users wind their own warp, it collapses to "a slightly different rigid-heddle." *Mitigation:* ship pre-wound plant-fiber cartridges from day one; DIY winding is a fallback SKU.
3. **Snap precision + cross-printer tolerance.** FDM clearances ~0.4–0.5 mm and vary by printer; sett needs tighter. *Mitigation:* control the snap interface yourself; kinematic location; lock print orientation (deflection plane parallel to bed).
4. **Gravity vs. crank pull opposite.** Gravity = low constant tension, weights hanging free; crank/beat want high advancing tension (why tapestry abandoned gravity for ratchet+screw). Cam-yanked sheds turn weights into pendulums → cyclic tension noise → uneven beat. *Mitigation:* accept **low-tension, warp-faced/tapestry-type fabric**; slow crank; slotted weight guide; add a ratchet take-up only when automating. **Hard no: PLA** for any tensioned part — it creeps/cold-flows. Use PETG, nylon.

## 4. Novelty / IP

Patentable in principle, **not worth it for a solo maker.** The only unclaimed combination — *tool-free snap-in warp cartridge tensioned by per-cartridge gravity weights* — sits one obvious step from MIT [US7318456](https://patents.google.com/patent/US7318456) + the warp-weighted principle → §103 obviousness territory. Utility patent ≈ $8–20k, 2–4 yrs, unenforceable by a solo maker.

**Prior art (all expired/public — free to practice, don't re-claim):** MIT [US7318456](https://patents.google.com/patent/US7318456) (modular warp units, quick-release heddles, modular reed) · [US7677273](https://patents.google.com/patent/US7677273B2) (tool-free peg-snap warp cartridge) · [US7178558](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7178558) · [SAORI slide-on pre-wound warps](https://www.dyeingtoweave.com.au/saori-loom-ch60/) (live consumer precedent) · [Thingiverse Modular Warp-Weighted Loom #4750378](https://www.thingiverse.com/thing:4750378) (gravity + modular, open-source — closest existing thing).

**Better moat:** ship first; brand ("Natural Bias") + the consumable plant-fiber cartridge supply is the razor-blade business. File a **cheap defensive publication** so no one patents it against you.

## 5. First prototype (weekend, prove-or-kill)

**Core hypothesis:** does a pre-wound, self-weighted, snap-in warp cartridge give even-enough tension AND spacing to weave acceptable cloth — without manual tensioning? Everything else is secondary.

**Build, no crank (~$10–20):**
1. A fixed top bar (dowel clamped between two chairs / a doorframe).
2. Two or three pre-wound "cartridges": warp wound on a stick with an integrated comb (3D-printed dent strip, or a hair comb for the weekend), each terminating in a hanging weight — **washers in a hemp pouch, ~15–25 g per thread**.
3. Hang side by side; **check the seam spacing across two adjacent cartridges** (the real failure mode).
4. Weave a few inches by hand — stick shed, hand-passed weft, beat upward.

**Kill** if the cloth bands from uneven tension or the seam shows a fat dent/gap that can't be designed out. **Pass** if even warp-faced cloth across the seam with zero manual tensioning. This isolates the one claim that is both novel and risky before spending a dollar on the crank.

## 6. Price & pitch

- **Hero loom: $120–200**, just under the Schacht Cricket ($229) — "real loom, easier." Below ~$100 is toy-margin.
- **Recurring revenue: pre-wound plant-fiber warp cartridges, $12–30 each** — the actual business, home for the hemp/linen/plant-dyed "Natural Bias" line.
- **Education SKU: $200–350** with a binary/Jacquard curriculum sheet — schools pay for the story + durability; the beachhead.
- **BOM ~$20–50/unit** (wood/bamboo + PETG + ceramic-or-washer weights + steel crank axle/bushing). Real cost driver is PETG **print time** (8–20 hrs/set) → argues for an STL + hardware kit model.

**Pitch:** *"Weaving's worst chore, gone — snap in the warp, gravity tensions it, turn the crank and weave."*

---

*Bottom line: the gravity-tension half is rock-solid revival, the snap-in cartridge half is the real (narrow, unpatentable-in-practice) invention, and the crank drives beat + shed — not the pick. Win education first; live or die by pre-wound cartridges and one visceral demo.*
