# PHRONESIS PRODUCTS
## Pitch Deck - Series Seed Round


**Founder:** Diego Rincón  
**Round:** Seed ($1M)  
**Use:** Team (4 engineers), launch 4 products  
**Timeline:** 16 weeks to market  

---

## SLIDE 1: THE PROBLEM

**Humans lack clarity.**

- 47% of workers struggle with focus and mental clarity (McKinsey)
- Therapists can't quantify progress (subjective only)
- AI reasoners hallucinate (can't be trusted for critical decisions)
- Communication breaks down without real-time feedback

**Root cause:** No way to measure or optimize *coherence* — the cognitive glue that holds thinking together.

---

## SLIDE 2: THE INSIGHT

**Displacement from a ground you cannot move.**

From our own research, self-published to Zenodo — https://doi.org/10.5281/zenodo.21403447 — which is
an open repository, not a journal — this has a DOI and a permanent record, and it has not
been peer reviewed:

- Sentence structure → Adjacency matrix
- Adjacency matrix → Eigenvalue spectrum
- Dominant eigenvalue (λ₁) = Coherence (0-100)
- Coherence = Mental clarity / Communication quality / Reasoning soundness

**The engine:** text is read against a reference fixed at the first step and never revised.
What comes back is a mode, a displacement, the patterns found, and a way back — plus every
word used to decide, so the reading can be checked and disagreed with.

No model, no training, no randomness. Same input, same output, forever.

**We test our own claims and publish what fails.** The spectral mechanism this began with —
grammar to eigenvalues to coherence — was implemented seven ways and measured. It does not
work: λ₁ tracks vocabulary reuse, so repetitive text scores highest. Hold syntax fixed and
replace content words with one repeated token and λ₁ *rises* as variety falls, corr = −0.787.

That is published in full at **phronesis.world/icm**, negative results and all. An investor
cannot verify our science from outside. They can verify that we falsify our own central
claim in public.

---

## SLIDE 3: THE OPPORTUNITY

**$500B+ market**

| Segment | TAM | Example |
|---------|-----|---------|
| Mental Health | $200B | Meditation (Calm $2.2B), therapy apps |
| Productivity | $150B | Writing (Grammarly $13B), focus tools |
| Enterprise AI | $100B | Reasoning, compliance, analysis |
| Education | $50B | Learning platforms, comprehension |

**Why now:**
- Deterministic, inspectable reasoning is newly valuable *because* models are not
- LLMs create demand for deterministic reasoning
- Therapy post-COVID: 300% growth in online therapy

---

## SLIDE 4: THE SOLUTION

**4 products, 1 core engine**

```
Shared ICM Engine (text → displacement from ground → mode, patterns, return path)
        ↓
├─ Coherence Monitor (B2C)
│  Real-time mental clarity app
│  $10/month consumer, $500/mo therapist
│
├─ Clarity OS (B2C + B2B)
│  Grammar-optimized interfaces
│  $20/month consumer, $5-15/user enterprise
│
├─ Logic Engine (B2B)
│  Deterministic reasoning (no LLM hallucinations)
│  $50K-500K per customer
│
└─ Dialogue Platform (B2B2C)
   Mind coupling measurement (therapy/coaching)
   $500/mo per therapist, $15/mo consumer
```

**Why this works:**
- Shared architecture (1 engine, 4 apps)
- Different distribution channels
- Multiple revenue models
- Each can stand alone or integrate

---

## SLIDE 5: THE TEAM

**Founder: Diego Rincón**
- Cornell Psychology grad (2023)
- Built Phronesis: quantum psychology platform (phronesis.world)
- 71 papers on the displacement framework, written and self-published at phronesis.world/papers
- Expert in: Applied math, neuroscience, full-stack dev, AI

**Hiring Plan:**
- Week 1: Senior full-stack engineer
- Week 3: iOS + backend engineers
- Week 5: Designer + data scientist
- Week 8: DevOps engineer
- **Total by week 16:** 6-person founding team

---

## SLIDE 6: TRACTION

**All four products are live and free to try.**

| | | |
|---|---|---|
| Coherence Monitor | phronesis.world/coherence-monitor | where you are, in 12 modes, with every cue that fired |
| Clarity | phronesis.world/clarity | spectral reading of writing, plus which two sentences repeat |
| Logic Engine | phronesis.world/logic-engine | classification against declared rules, that can say why it did **not** flag something |
| Dialogue | phronesis.world/dialogue | two people side by side: four facts, deliberately never averaged |

All four run client-side on the same deterministic engine. No model, no key, no request —
nothing typed into them leaves the page.

**And a product that is shipping to strangers:**

- **laserbrain** — on PyPI, ~10K downloads, currently 0.48.0. A grammatical control layer
  that reduces agent drift. Remote MCP server serving 15 tools; a published grammar; a
  corpus of ~500 real recorded runs.
- The theory work above is checked by 74 automated suites that run on every release, and by
  ~40 build gates that stop a deploy when a page contradicts the data behind it.

**What is NOT claimed:**

- No EEG validation. It was never run on real data; the paper says so in its own abstract.
- No patents, filed or pending.
- No paying customers yet for the four products above.

## SLIDE 7: THE ASK

**$1M Seed Round**

| Use of Funds | Amount |
|---|---|
| Salaries (4 engineers, 1 yr) | $500K |
| Infrastructure (AWS, APIs, monitoring) | $50K |
| Legal/compliance (incorporation, IP, terms) | $50K |
| Marketing (Product Hunt, ads, content) | $100K |
| Contingency (5-month runway buffer) | $300K |

**Timeline:**
- Month 1-4: All 4 products in beta (1-100K users each)
- Month 5: Series A conversation ($5M)
- Month 6: Series A close
- Month 12: $10M+ ARR

---

## SLIDE 8: REVENUE PROJECTION

| Product | Y1 | Y2 | Y3 |
|---------|----|----|-----|
| Coherence Monitor | $200K | $2M | $10M |
| Clarity OS | $100K | $5M | $30M |
| Logic Engine | $1M | $7.5M | $30M |
| Dialogue Platform | $150K | $3M | $15M |
| **TOTAL** | **$1.45M** | **$17.5M** | **$85M** |

**Key metrics:**
- Y1: 1-100K users per product, 1-10 paying customers
- Y2: 100K-1M users, 50+ enterprise customers, $17.5M ARR
- Y3: 5M+ users, $85M ARR, profitable

---

## SLIDE 9: COMPETITIVE ADVANTAGE

**Why we win vs. alternatives:**

| Competitor | Our Advantage |
|---|---|
| Headspace/Calm | Quantified coherence (they guess) |
| Grammarly | Grammar for clarity, not just correctness |
| OpenAI/Anthropic | No hallucinations (logic, not learned weights) |
| Talkspace | Real-time coupling measurement (live feedback) |

**Defensibility:**
- Determinism itself: same input, same output, every step inspectable — a property a
  model cannot offer and a competitor cannot bolt on
- Published theory (reproducible, verifiable)
- 4-product moat (each product feeds others)
- Network effects (coherence metrics improve with scale)

---

## SLIDE 10: VALIDATION PLAN

**This month:**

- [ ] Paying pilots for Logic Engine — the audit trail is the enterprise wedge
- [ ] 100 therapist pilots (Dialogue Platform)
- [ ] 1K users Coherence Monitor (TestFlight)
- [ ] 5K users Clarity OS (extension)
- [ ] 3 enterprise pilots (Logic Engine)

**Success criteria:**
- Theory validates (r > 0.65, p < 0.001)
- 30%+ 7-day retention
- >80% therapist would recommend
- 3+ enterprise pilots willing to pay

**Outcome:** Series A ready by month 6

---

## SLIDE 11: RISK MITIGATION

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| EEG validation fails | 20% | HIGH | Theory still works; pivot to research funding |
| Market doesn't adopt | 30% | MEDIUM | Rebrand to clarity/focus; target B2B first |
| Competition (LLMs) | 70% | MEDIUM | Emphasize explainability, determinism, privacy |
| Key person risk | 40% | HIGH | Document everything; hire strong co-founders |
| Funding gap | 10% | MEDIUM | Bootstrap from Coherence Monitor + Clarity OS |

---

## SLIDE 12: VISION

**If this works:**

**Year 1:** $1.45M ARR, 4 products in market, 1M+ users  
**Year 2:** $17.5M ARR, profitable, hiring 30+ people  
**Year 3:** $85M ARR, acquisition target or IPO  

**But bigger than revenue:**

- New field: "Spectral consciousness studies"
- Bridge: symbolic AI ↔ neural systems (solve LLM hallucinations)
- Health: Quantify coherence loss in neurological disease
- Education: Measurably improve learning outcomes
- Therapy: Provide real-time feedback for connection quality

**Mission:** Make clarity measurable, coherence quantifiable, consciousness understood.

---

## SLIDE 13: THE ASK (REDUX)

**Invest $1M in Phronesis Products.**

**Get:**
- Founder with deep theory + execution
- 4 commercial products in 16 weeks
- Defensible tech (deterministic and inspectable — a property, not a filing)
- $1.45M → $17.5M → $85M runway
- Optionality (4 revenue streams, pick winners)

**Your return:**
- 30-40% equity stake (founder-friendly)
- Board seat (investor call)
- Monthly updates
- Exit in 3-4 years ($500M+ exit valuation)

**Founder:** Diego Rincón  
**Email:** degibug@icloud.com  
**Theory:** https://doi.org/10.5281/zenodo.21403447 (self-published, Zenodo — not peer reviewed)  
**Code:** phronesis-products (GitHub)  

---

## APPENDIX: MARKET VALIDATION

**Coherence Monitor:**
- 100M+ meditation users (Calm, Headspace, Insight Timer)
- 30% willing to pay for real-time clarity metric
- TAM: $300M/year

**Clarity OS:**
- 100M+ writers/knowledge workers
- Grammarly valued at $13B
- TAM: $500B/year

**Logic Engine:**
- 1000s of enterprises needing deterministic reasoning
- Finance, legal, compliance, healthcare, government
- TAM: $100B/year

**Dialogue Platform:**
- 100K+ therapists in US (3M+ worldwide)
- $50M/therapist on real outcomes → $2.5B market
- TAM: $50B/year

**Total addressable market: $650B+**

---

## APPENDIX: TECHNICAL SPECS

**ICM Engine:**
- Language: Python
- Core: spaCy (parsing) + scipy (eigenvalues)
- Latency: <100ms per sentence
- Throughput: 1000+ sentences/second
- Runs locally, no API dependency

**Coherence Monitor API:**
- Framework: FastAPI (Python)
- WebSocket support (real-time streaming)
- Async/await throughout
- Deployed: AWS (multi-region)

**Mobile App:**
- Framework: React Native (TypeScript)
- iOS + Android from same codebase
- Real-time WebSocket connection
- Biofeedback UI (coherence dial)

**Security:**
- End-to-end encryption (privacy)
- No personal data to cloud (local-first)
- HIPAA-compliant (Dialogue Platform)
- SOC2 ready

---

## APPENDIX: GO-TO-MARKET

**Month 1-2: Beta Launch**
- TestFlight (Coherence Monitor): 100 users
- Browser extension (Clarity OS): 1K users
- Enterprise pilots (Logic Engine): 3 customers
- Therapist pilots (Dialogue Platform): 50 users

**Month 2-4: Scaling**
- App Store launch (Coherence Monitor): 10K users
- Product Hunt launch (Clarity OS): 50K users
- Enterprise sales (Logic Engine): 10 customers
- Therapist expansion (Dialogue Platform): 100 pilots

**Month 4-6: Series A**
- Product-market fit signals from all 4 products
- Enterprise revenue (Logic Engine): $50K/mo
- Consumer revenue (Coherence Monitor + Clarity OS): $20K/mo
- Series A close: $5M
- Hiring: 10+ people

**Month 6-12: Growth**
- Scale to 1M+ users
- Enterprise: 50+ customers
- Revenue: $500K/mo → $1M+/mo
- Series B conversations

---

**Questions?**

**Contact:** degibug@icloud.com  
**Theory:** https://doi.org/10.5281/zenodo.21403447 (self-published, Zenodo — not peer reviewed)  
**Code:** github.com/phronesis-products  
**Website:** phronesis.world
