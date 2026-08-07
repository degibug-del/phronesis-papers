# Public Datasets for Grammar-to-Coherence Validation

## EEG Datasets (Sentence Comprehension)

### 1. **UCL Sentence Comprehension Dataset**
- **Source:** OpenNeuro (ds002315)
- **N:** 50 subjects
- **Stim:** 240 sentences (varying complexity)
- **Data:** 64-channel EEG + eye tracking
- **Relevant:** Spectral frequency peaks during different syntactic structures

### 2. **Reading Span Task EEG**
- **Source:** OpenNeuro (ds003144)
- **N:** 90 subjects
- **Stim:** Sentences + number recall (working memory load)
- **Data:** High-density EEG
- **Relevant:** Coherence changes with cognitive load

### 3. **N400 Semantic Anomaly Dataset**
- **Source:** OpenNeuro (ds001477)
- **N:** 30 subjects
- **Stim:** Sentences with semantic violations
- **Data:** 64 EEG channels
- **Relevant:** Eigenvalue "surprise" signature at anomalies

---

## Behavioral Datasets (Reaction Time)

### 1. **Self-Paced Reading Corpus**
- **Source:** MIT Linguistic Databases
- **N:** 1000+ subjects across studies
- **Stim:** Sentences varying in syntactic complexity
- **Data:** Word-by-word reading times
- **Relevant:** Power law between spectral gap and reading latency

### 2. **SQuAD Reading Comprehension**
- **Source:** Stanford NLP (public)
- **N:** 100K+ examples
- **Data:** Question answer latencies, passage complexity
- **Relevant:** Coherence predicts answer speed

---

## Ambiguity & Parsing Datasets

### 1. **Garden Path Sentences (Ferreira)**
- **Source:** Cognitive Science literature
- **N:** 200+ ambiguous sentence pairs
- **Stim:** Temporary ambiguities vs. control
- **Data:** Reading times, eye movements
- **Relevant:** Degeneracy signatures in ambiguous parses

### 2. **MIT Syntactic Ambiguity Corpus**
- **Source:** MIT CSAIL
- **N:** 500 sentences
- **Data:** Multiple valid parses per sentence
- **Relevant:** Compute eigenvalue variance across parses

---

## Dialogue Datasets (Entanglement)

### 1. **SWDA (Switchboard Dialog Act Corpus)**
- **Source:** LDC
- **N:** 1000+ conversations
- **Data:** Dialogue transcripts + timestamps
- **Relevant:** Measure coherence convergence over dialogue

### 2. **MultiWOZ (Task-Oriented Dialogue)**
- **Source:** Cambridge (public)
- **N:** 10K+ dialogues
- **Data:** Turn-by-turn interaction logs
- **Relevant:** Coupling strength in task-driven conversations

---

## Strategy: Immediate Validation

1. **Week 1–2:** Access OpenNeuro EEG datasets
2. **Week 2–3:** Parse stimuli → compute λ₁, λ₂
3. **Week 3–4:** Extract spectral features from raw EEG
4. **Week 4–5:** Correlate grammar eigenvalues with neural frequencies
5. **Week 5–6:** Write up findings, submit to preprint

**Cost:** $0 (all datasets public)
**Timeline:** 6 weeks
**Output:** Validation paper showing theory works on real brain data

