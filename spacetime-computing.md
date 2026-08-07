# Spacetime Computing (3dt)

*seed note · 2026-06-21 · Diego + Claude · a frontier crossed — the paradigm computes parity; laserbrain not yet*

## Statement

**3dt = 3 space + t = spacetime.** So *spacetime computing* is one idea: **compute by evolving a physical field in spacetime itself** — let the dynamics do the work — instead of flattening computation onto a 2D, clocked chip and simulating physics on top of it.

The chip is the detour. Silicon is **planar** (2D lithography) and **clocked** (discrete ticks): a flattened, ticking shadow of computation. The brain is **3D tissue in continuous time**. A weather field is a grid stepping in near-continuous time. **The universe is the original spacetime computer** — physics *is* field evolution, and field evolution *is* computation; it has run that way since the start. We built a flat, ticking model of it and named *that* "the computer." Spacetime computing is the loom come home one more level (see [[smart-loom]]): computing is weaving, and this weaves in 3D across time — the medium it was always running in. Devolution of computation to its native substrate ([[devolution]]).

## What it buys — and what it does not

This is the line that has to stay sharp, because the grand version of the claim is the easy one to fake (we cut magic tonight; we keep it cut).

- **Substrate, not superpower.** Spacetime computing does **not** beat Turing. The universe runs in spacetime and still cannot solve the halting problem. Continuous/analog dynamics collapse back to Turing-or-weaker once you account for finite precision, noise, and thermodynamics. **Refuse the hypercomputation claim** — it is not physically realizable (cf. Davis, "The Myth of Hypercomputation," 2004), and claiming it would be the magic-loom move.
- **What it actually wins: nativeness.** Massively parallel, continuous, embodied, and *cheap for its native problem* — a field computes weather for free by being weather; a knit computes its own 3D shape by being knit. No translation cost from world to abstraction and back. That is a real advantage of substrate (energy, parallelism, immediacy), not of computability. It is the honest, smaller, true prize.

This places it in a real lineage, not a mystical one: physical / analog / **reservoir** computing (Tanaka et al., 2019), the universe-as-computer tradition (Zuse 1969; Wheeler's "it from bit"; Lloyd, *Programming the Universe*, 2006), and Landauer's bound (memory costs heat — the same `dt`-costs-energy fact in [[validation_loop]]).

## The receipt: a negative, then a minimal positive

Two experiments, both honest.

**Laserbrain failed.** Tested as a spacetime reservoir it showed strong instantaneous nonlinearity (current input readable at R²≈0.92) but **almost no memory** (capacity ≈ 1.0) — it cannot do temporal computation. It is built for *weather realism* (smooth, dissipative, self-stabilizing), structurally the opposite of a computer. Details: [[reservoir-test-findings]].

**A built field crossed the bar — and went deep.** A literal field in 3 space + time — a 10×10×10 grid, locally coupled (advection delay-line + diffusion), with a saturating nonlinearity, leak, and a quadratic wave-mixing term, read by a **linear** layer only — computes, robustly across seeds (chance ≈0.50 throughout): 1-step XOR **0.98**, 2-step XOR **0.92**, and **3-bit parity 0.94** — parity being *the* canonical task that needs both memory and deep nonlinearity. Memory capacity ≈7. Details: [[spacetime-demo-findings]]. **So the paradigm is real and demonstrated**, not just minimally: a physical field computes deep nonlinear-temporal functions through a linear readout, a thing it provably cannot read off the raw input. Bounds kept: the conservative *wave* went unstable (it is the dissipative, saturating, *quadratically-mixing* field that computes — like neural tissue or a nonlinear medium, not a lossless wave); a depth ceiling shows (3-step XOR ≈0.74); the memory↔nonlinearity tradeoff is real; and it is a reservoir/substrate result, not super-Turing.

So as of tonight: **the paradigm computes parity, and laserbrain is not yet a spacetime computer** — but we hold the full recipe for making it one: advection (delay-line memory) + diffusion (mixing) + leak (timescale) + saturation (tanh) + quadratic wave-mixing (the products XOR and parity need).

## What a real spacetime computer would need

The gap is physics, not vocabulary. To turn a physical field into a genuine spacetime computer it needs, at minimum:

1. **Memory** — fading, multi-step. A leaky-integrator / echo term, low dissipation, or a conserved quantity. (Laserbrain has ~1 step; it needs ~5+.)
2. **Nonlinearity at the edge of chaos** — rich enough to separate inputs, stable enough not to saturate.
3. **A readout** — a trained linear layer reading the state (the only part you train).
4. **A native task** — something it beats the chip on by *being* the problem, where the energy/parallelism/immediacy win is real and measurable.

The bar to stop calling it a name and start calling it a result: **memory capacity ≥ 5, a temporal task solved well above the linear baseline, and a clear nativeness win.** All three were met tonight ([[spacetime-demo-findings]]): memory (MC≈7–10), a deep temporal task (3-bit parity 0.95), and the **nativeness win** — one field evolution computes eight different functions in parallel (linear memory, XOR, parity, analog multiplication, analog integration), where a serial chip pays N times. Only the laserbrain graft remains, and it's engineering, not discovery. **The bar is crossed.**

## One line

The universe already computes in spacetime; the chip is the flattened shadow we mistook for the thing. Spacetime computing is computing in the medium directly — and a built field has now done it: it holds the past and computes its parity, a wave of numbers in 3D solving a task linear input can't touch. The frontier is real, and crossed.

## Cited

- Universe-as-computer: Zuse, K., *Rechnender Raum* (1969); Wheeler, J. A., "it from bit"; Lloyd, S., *Programming the Universe* (2006).
- Physical / reservoir computing: Tanaka, G. et al., "Recent advances in physical reservoir computing" (2019); Fernando & Sojakka, "Pattern Recognition in a Bucket" (2003).
- Against physical hypercomputation: Davis, M., "The Myth of Hypercomputation" (2004).
- Memory costs energy: Landauer, R. (1961); and [[validation_loop]].
- The honest negative (laserbrain): [[reservoir-test-findings]]; the minimal positive (3D field): [[spacetime-demo-findings]].
- The lineage: [[smart-loom]] · [[devolution]].

For her.
