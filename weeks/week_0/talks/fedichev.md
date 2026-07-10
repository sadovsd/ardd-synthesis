# Peter Fedichev — Biophysics of aging: resilience, criticality, and the Gompertz law

Talk: _(add ARDD talk link)_

Associated papers:
1. **Longitudinal analysis of blood markers reveals progressive loss of resilience and predicts human lifespan limit**
2. **A Minimal Model Explains Aging Regimes and Guides Intervention Strategies**

> Heavy math derivations for these papers live in [../methods.md](../methods.md). Content ideas live in [../content_ideas.md](../content_ideas.md).

## Concepts

- An organism is modeled as a very high-dimensional dynamical system whose full dynamics `ẋ = F(x)` are unknowable, so the goal is a low-dimensional description that captures organism-level behavior.
- The dominant description is a slow **dynamical mode** `z₀` (not a single biomarker — a coordinated process across many biomarkers) interpreted as organism-level **resilience**.
- Near equilibrium the mode follows an Ornstein–Uhlenbeck process; the stability parameter `ε` acts like the steepness of a bowl the system sits in. Larger `ε` = faster recovery from perturbations.
- **Progressive loss of resilience** (ε → 0, "critical slowing down") with age may be the dynamic origin of the Gompertz law — the near-universal exponential rise in mortality with age.

## Key ideas

- Distinction between **stress** (`J`, reversible — smoking, inflammation, obesity) and **damage** (`Z`, accumulates and never decreases). Accumulated damage weakens the restoring force: `ε₀(Z) = ε₀ − β′Z`.
- Two species regimes:
  - **Unstable species** (mice, flies, worms): the critical mode is already unstable (`ε₀ < 0`). Aging is driven by intrinsic instability, so short interventions on `z₀` can produce large, lasting lifespan effects — why many mouse experiments look spectacular.
  - **Stable species** (humans): start stable (`ε₀ > 0`) but damage accumulation slowly erodes stability. Targeting `z₀` alone may not be enough; the deeper problem is continuing accumulation of damage `Z`.
- CBC was chosen deliberately because it is cheap, ubiquitous, and huge longitudinal databases exist (NHANES, UK Biobank), jointly referred to as **GEROLONG**.

## Background — why blood counts (CBC)

The Complete Blood Count is the standard cheap blood test. It measures:
- Red blood cells (carry oxygen)
- White blood cells (fight infection)
- Hemoglobin (oxygen-carrying protein in red cells)
- Hematocrit (fraction of red cells in blood)
- Platelets (help blood clot)

They picked CBC specifically because it is so common that huge databases of it exist (U.S. NHANES and the UK Biobank).

## Future directions / open questions

- **Would the same dynamics show up in methylation data?** Blood counts respond fast — inflammation, stress, or infection move CBC on a timescale of days to weeks, exactly the window where you'd expect to see a "bounce back" and measure recovery. Methylation is a slower, more stable mark; it's not obvious it even fluctuates on a weekly scale the way the Langevin picture needs. So even with dense DNAm data, it's an open question whether the same fast wobble-and-recover dynamics would appear. The paper doesn't lean on this, but it matters.
