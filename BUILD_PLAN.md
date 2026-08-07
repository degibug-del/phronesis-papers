# Build Plan: 4 Products, Parallel Development

**Start Date:** 2026-07-16  
**Timeline:** 16 weeks to all 4 MVPs in beta  
**Funding Needed:** $1M (seed round)  
**Team Size:** 1 founder (you) + hiring 4 engineers over 8 weeks

---

## Sprint Structure

**Sprint = 2 weeks**  
**Total = 8 sprints (16 weeks)**

Each sprint has clear deliverables. Multiple products advance in parallel.

---

## PRODUCT 1: Coherence Monitor (Weeks 1-8)

**Goal:** iOS/Android app measuring real-time coherence  
**Target:** 1K beta users, >4.5 App Store rating

### Week 1-2: Foundation
- [ ] Design app architecture (React Native or native iOS first)
- [ ] Integrate spaCy/ICM engine (local, no API)
- [ ] Create eigenvalue computation module
- [ ] Basic UI mockup (coherence dial, history graph)
- **Output:** Working coherence calculation on mock text

### Week 3-4: Core App
- [ ] Real-time text input (speech-to-text or paste)
- [ ] Live coherence score display (0-100)
- [ ] Session recording (start/stop, save history)
- [ ] Analytics tracking (which topics increase/decrease coherence)
- **Output:** Functional iOS app, testable

### Week 5-6: Polish & Features
- [ ] Guided sessions (narrator with optimized text for coherence)
- [ ] Biofeedback (haptic/visual reward on coherence peaks)
- [ ] Coaching mode (therapist dashboard showing client coherence)
- [ ] Onboarding flow (teach users what coherence means)
- **Output:** App ready for TestFlight (iOS beta)

### Week 7-8: Launch & Iterate
- [ ] TestFlight beta (invite 100 users)
- [ ] Android version (parallel build)
- [ ] App Store submission & approval
- [ ] Gather feedback, iterate
- **Output:** Live on App Store, 1K installs target

### Success Metrics
- App Store rating ≥ 4.5
- 7-day retention ≥ 30%
- Session length ≥ 5 minutes average
- Coherence improvement measurable (users report feeling clearer)

---

## PRODUCT 2: Clarity OS (Weeks 2-10)

**Goal:** Browser extension + web app for clarity-through-eigenvalue  
**Target:** 10K active users, >50% retention

### Week 2-3: Browser Extension Foundation
- [ ] Parse web page text via spaCy (local)
- [ ] Compute eigenvalue for each sentence
- [ ] Highlight low-coherence sentences (red → green scale)
- [ ] Show coherence score on toolbar
- **Output:** Working Chrome extension, deployable

### Week 4-5: Suggestions & Rewrites
- [ ] Suggest rewrites for low-coherence sentences
- [ ] Auto-rewrite option (keep meaning, optimize λ₁)
- [ ] Modal showing before/after comparison
- [ ] A/B testing framework (measure readability improvement)
- **Output:** Extension in Chrome Web Store, 1K users

### Week 6-7: Web App
- [ ] Standalone web app (optimize any pasted text)
- [ ] Real-time dashboard (coherence heatmap)
- [ ] Document upload (analyze full articles/emails)
- [ ] Collaboration features (share edits with others)
- **Output:** Web app live, ready for beta

### Week 8-9: Analytics & Scaling
- [ ] Measure reading speed on coherence-optimized text
- [ ] Track user improvements (reading speed, comprehension)
- [ ] Enterprise dashboard (manage users, bulk analysis)
- [ ] API for third-party integration
- **Output:** Enterprise-ready, 10K users

### Week 10: Launch
- [ ] Product Hunt launch
- [ ] LinkedIn/Twitter campaign
- [ ] Blog posts (how grammar = clarity)
- **Output:** 100K+ impressions, 10K+ users target

### Success Metrics
- Extension installs: 10K+
- Daily active users: 5K+
- Avg session time: 8+ minutes
- Readability improvement: measurable in A/B tests

---

## PRODUCT 3: Logic Engine (Weeks 3-12)

**Goal:** API + SDK for deterministic reasoning  
**Target:** 3 paying enterprise pilots, >90% accuracy

### Week 3-4: Core Engine
- [ ] Build REST API for reasoning tasks
- [ ] Implement ICM parser (extract logical structure)
- [ ] Eigenvalue-based ranking (coherence scores for solutions)
- [ ] Explanation layer (show reasoning path)
- **Output:** Working API, deployable

### Week 5-6: Benchmarking
- [ ] Create benchmark dataset (financial, legal, scientific)
- [ ] Test against LLMs (GPT-4, Claude) on reasoning tasks
- [ ] Measure accuracy, speed, cost
- [ ] Document results
- **Output:** Competitive benchmark report

### Week 7-8: Enterprise SDK
- [ ] Python SDK (pip install phronesis-logic)
- [ ] Node.js SDK (npm install @phronesis/logic)
- [ ] Full documentation + examples
- [ ] Licensing system (API keys, rate limiting)
- **Output:** SDKs published, ready for integration

### Week 9-10: Sales & Pilots
- [ ] Reach out to 20 financial services companies
- [ ] Reach out to 20 legal tech companies
- [ ] Offer free pilots (3-month unlimited access)
- [ ] Build custom integrations
- **Output:** 3-5 pilot agreements signed

### Week 11-12: Scale
- [ ] Deploy on AWS/GCP (multi-region)
- [ ] Implement monitoring & uptime dashboards
- [ ] Support & maintenance workflow
- [ ] Pricing finalization ($1K-$50K/month depending on volume)
- **Output:** Production-ready, pilots converting to paid

### Success Metrics
- API uptime: 99.9%+
- Response time: <1 second for typical request
- Accuracy: >85% on benchmark
- 3+ paying customers by week 12

---

## PRODUCT 4: Dialogue Coupling Platform (Weeks 4-14)

**Goal:** Real-time coupling measurement for conversations  
**Target:** 100 therapist pilots, measurable outcome improvement

### Week 4-5: Speech-to-Text Pipeline
- [ ] Integrate speech recognition (Apple/Google API)
- [ ] Parse both speakers' speech in real-time
- [ ] Compute eigenvalues for each speaker (λ_E, λ_L)
- [ ] Store transcripts + metadata
- **Output:** Working two-person speech analysis

### Week 6-7: Coupling Analysis
- [ ] Implement coupling calculation (λ_coupled dynamics)
- [ ] Detect entanglement moments (when λ_coupled > λ_E × λ_L)
- [ ] Detect convergence moments (when minds sync)
- [ ] Real-time visualization
- **Output:** Live coupling dashboard

### Week 8-9: Therapist Dashboard
- [ ] Session recording + playback
- [ ] Coupling timeline (show peaks/valleys)
- [ ] Transcript with coherence annotations
- [ ] Post-session analysis (coupling quality score)
- [ ] Client progress tracking (coherence growth over sessions)
- **Output:** Dashboard ready for therapist testing

### Week 10-11: Mobile App
- [ ] iOS/Android app (simple: start session, record, analyze)
- [ ] Real-time coupling display (simple visual: coupled/not coupled)
- [ ] Historical tracking (show progress)
- [ ] Push notifications (coupling peaks)
- **Output:** Mobile apps in TestFlight/beta

### Week 12-13: Therapist Recruitment
- [ ] Contact 100 therapists (LinkedIn, professional networks)
- [ ] Offer free 3-month trial
- [ ] Training webinars (how to use, interpret data)
- [ ] Onboard first 20 pilots
- **Output:** 20+ active therapist pilots

### Week 14: Analysis & Iterate
- [ ] Collect outcome data (client satisfaction, session quality)
- [ ] Measure if coupling predicts therapy success
- [ ] Iterate based on feedback
- [ ] Prepare for Series A story ("coupling predicts outcomes")
- **Output:** Case studies ready, validated product-market fit

### Success Metrics
- Therapist retention: >80% (keep using after trial)
- Session recording: >90% of sessions recorded
- Client NPS: >60
- Coupling correlation with outcomes: measurable

---

## Shared Infrastructure (Parallel)

**Every week, all products benefit:**

### ICM Engine (Shared Core)
- [ ] Week 1-2: Core parser + eigenvalue computation
- [ ] Week 3-4: Optimization + caching
- [ ] Week 5-6: GPU acceleration (optional)
- [ ] Week 7-8: Benchmarking + validation
- **Output:** Production-ready ICM library used by all 4 products

### Theory Integration
- [ ] Week 1: Document ICM formalism
- [ ] Week 4: Validate against real EEG data (ds002315 results)
- [ ] Week 8: Publish blog posts explaining theory
- [ ] Week 12: Conference talk (why this approach beats LLMs)
- **Output:** Thought leadership, credibility

### Data & Benchmarks
- [ ] Week 2: Create benchmark datasets (coherence)
- [ ] Week 4: Collect real user data (anonymized)
- [ ] Week 8: Publish benchmark report
- [ ] Week 12: Open-source dataset (research community)
- **Output:** Validation, industry credibility

---

## Team Hiring Plan

**Week 1:** You (founder) + 1 senior engineer (full-stack)  
**Week 3:** +1 iOS engineer, +1 backend engineer  
**Week 5:** +1 product designer, +1 data scientist  
**Week 8:** +1 DevOps engineer

**By Week 16:** 6-person team  
**Salary:** $100K-150K each ($6-9M annual run rate, plus equity)  
**Funding:** $1M seed covers 1 year fully loaded

---

## Weekly Sync Structure

**Every Monday:** All-hands standup
- 5 min each product (what shipped, blockers, next week)
- 10 min shared infrastructure (ICM, data)
- 5 min overall progress

**Every Wednesday:** Product reviews (rotating)
- Week 1-2: Coherence Monitor
- Week 3-4: Clarity OS
- Week 5-6: Logic Engine
- Week 7-8: Dialogue Platform

**Every Friday:** Strategy + metrics
- Revenue forecast
- User metrics (DAU, retention, NPS)
- Technical metrics (uptime, performance)
- Funding runway

---

## Funding Allocation ($1M Seed)

| Category | Amount | Notes |
|----------|--------|-------|
| Salaries (4 eng @ 125K avg, 1 yr) | $500K | Fully loaded with benefits |
| Infrastructure (cloud, APIs) | $50K | AWS, Stripe, monitoring |
| Legal/Compliance | $50K | Incorporation, IP, terms |
| Marketing/Launch | $100K | Product Hunt, ads, content |
| Contingency (5 mo runway) | $300K | Buffer for extra hiring, experimentation |

---

## Milestone Gates

**Gate 1 (Week 4):** All 4 products have working prototypes
- [ ] Coherence Monitor calculates coherence ✓
- [ ] Clarity OS highlights coherence issues ✓
- [ ] Logic Engine API returns ranked solutions ✓
- [ ] Dialogue Platform measures coupling ✓
- **Go/No-Go:** If all 4 shipping, proceed to scale

**Gate 2 (Week 8):** All 4 products in beta
- [ ] Coherence Monitor: 1K TestFlight users
- [ ] Clarity OS: 5K extension users
- [ ] Logic Engine: 3 pilot contracts signed
- [ ] Dialogue Platform: 20 therapist pilots
- **Go/No-Go:** If metrics strong, proceed to launch

**Gate 3 (Week 12):** Validation from real data (ds002315 results arrive)
- [ ] EEG validation complete (r > 0.65?)
- [ ] Theory fully vindicated
- [ ] Press release ready ("Theory validated on real brains")
- [ ] Series A pitch ready
- **Go/No-Go:** If validated, Series A conversation begins

**Gate 4 (Week 16):** All 4 products ready for wider launch
- [ ] App Store live, >1K users
- [ ] Extension >10K users
- [ ] 3 logic engine customers paying
- [ ] 100+ therapists in platform
- **Go/No-Go:** Series A ($5M) close by month 6

---

## Success Criteria (End of Sprint 8)

| Product | Metric | Target | Status |
|---------|--------|--------|--------|
| Coherence Monitor | App Store rating | 4.5+ | TBD |
| | DAU | 500+ | TBD |
| | Revenue (MRR) | $5K | TBD |
| Clarity OS | Extension users | 10K+ | TBD |
| | Retention (7d) | 40%+ | TBD |
| | Revenue (MRR) | $3K | TBD |
| Logic Engine | Paying customers | 3+ | TBD |
| | API calls/day | 10K+ | TBD |
| | Revenue (MRR) | $10K+ | TBD |
| Dialogue Platform | Therapist pilots | 100+ | TBD |
| | Sessions recorded | 1K+ | TBD |
| | Outcome correlation | Measurable | TBD |

**Total Revenue Target (Week 16):** $18K MRR ($216K ARR)  
**Burn Rate:** ~$80K/month  
**Runway Remaining:** 4 months → Series A urgency

---

## Technical Decisions

### Architecture Philosophy
- **Local-first:** All core logic runs on-device (no API dependency)
- **Offline mode:** Full functionality without internet
- **Privacy-first:** Minimal data sent to cloud
- **Modular:** Each product can run independently or integrated

### Tech Stack
- **ICM Engine:** Python (spacy, scipy, numpy)
- **Coherence Monitor:** React Native (cross-platform iOS/Android)
- **Clarity OS:** TypeScript (browser extension + web app)
- **Logic Engine:** Python FastAPI (REST), Node.js/Python SDKs
- **Dialogue Platform:** React (web), React Native (mobile)
- **Backend:** AWS (compute, database, storage)
- **Monitoring:** Datadog, Sentry

### Data Strategy
- **Collection:** Anonymized, user-consented
- **Storage:** Encrypted, AWS S3
- **Retention:** 90 days default, 7 years with consent
- **Sharing:** Only aggregated, statistical
- **Research:** Open-source dataset available (privacy-preserved)

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| EEG validation fails (r < 0.65) | 20% | High | Products still work on theory; pivot to research funding |
| Market doesn't adopt coherence concept | 30% | Medium | Rebrand as "clarity/focus"; target therapists first (B2B2C) |
| Competitive threats (LLM-based) | 70% | Medium | Emphasize explainability, determinism, privacy, on-device |
| Key engineer leaves | 40% | High | Document everything; pair programming on critical code |
| Funding gap | 10% | Medium | Bootstrap revenue from Coherence Monitor, Clarity OS |
| Regulatory issues (medical claims) | 15% | Medium | Don't claim to diagnose; position as wellness/optimization tool |

---

## Next Steps (This Week)

1. [ ] Read this plan (you're here)
2. [ ] Identify first engineer hire (technical cofounder type)
3. [ ] Create GitHub org: phronesis-products
4. [ ] Set up Slack, Notion, Linear (project management)
5. [ ] Book intros with 10 potential investors (seed round)
6. [ ] Week 1 sprint planning call with first hire (if found)

**By end of Week 1:**
- [ ] First engineer onboarded
- [ ] ICM engine core deployed to all 4 projects
- [ ] Coherence Monitor architecture decided (React Native vs native iOS)
- [ ] Clarity OS browser extension first commit
- [ ] Logic Engine API skeleton live

**By end of Week 4:**
- [ ] All 4 products have working MVPs
- [ ] Seed funding raised ($1M) or committed
- [ ] Full team hired + onboarded

---

## Appendix: Resource Links

**Design Inspiration:**
- Clarity → Apple Health (beautiful real-time metrics)
- Monitor → Peloton (biofeedback + community)
- Engine → Midjourney API (fast, reliable, simple pricing)
- Platform → Calendly (therapist scheduling with data)

**Competitive Analysis:**
- Headspace (coherence monitor positioning)
- Grammarly (clarity OS positioning)
- OpenAI API (logic engine positioning)
- Talkspace (dialogue platform positioning)

**Theory Reference:**
- Published paper: 10.5281/zenodo.21403447
- Simulations: simulate_experiments.py
- Real EEG validation: ds002315 (incoming)

---

**Status:** Ready to build.

**Go signal:** Execute.
