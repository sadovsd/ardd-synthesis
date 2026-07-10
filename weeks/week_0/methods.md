# Week 0 — Statistical / mathematical / computational methods

Methods encountered across the week's talks and their associated papers.

---

## Fedichev — biophysics of aging

_See talk note: [talks/fedichev.md](talks/fedichev.md)_


# Longitudinal analysis of blood markers reveals progressive loss of resilience and predicts human lifespan limit
Notes added: 2026-06-01

Cox proportional hazards model.


auto-correlation time

We put forward
arguments suggesting that such behavior is typical for
complex systems near a bifurcation (disintegration) point

progressive loss of resilience with age may be a dynamic
origin of the Gompertz law.

# A Minimal Model Explains Aging Regimes and Guides Intervention Strategies

Notes added: 2026-06-02

$$
\dot{z}_0 = \beta Z - \varepsilon_0(Z)\, z_0 + g z_0^2 + J_0 + f_0,
\qquad \varepsilon_0(Z) = \varepsilon_0 - \beta' Z
$$

## PCA, dynamical modes, and what a "mode" is

Fedichev starts with the idea that an organism is a very high-dimensional system:

$$
x = (x_1, x_2, ..., x_n)
$$

where the components could be gene expression levels, methylation states, metabolite concentrations, blood biomarkers, etc.

PCA describes a low-dimensional representation of the data itself. The principal components are directions in biological state space that explain the most variance. A principal component can sometimes be interpreted as a biological process or pathway (e.g. inflammation, metabolic dysfunction, immune activation), but PCA itself is purely statistical and says nothing about causality or dynamics.

The paper instead uses ideas from dynamical systems theory. Rather than asking which directions have the most variance, it asks which directions evolve most slowly over time. These directions are called normal modes or dynamical modes. Mathematically, they are eigenvectors of the Jacobian of the system dynamics rather than eigenvectors of a covariance matrix.

A mode is therefore not a biomarker. It is a coordinate along some collective biological process involving many biomarkers simultaneously. If thousands of biological variables move together, that coordinated motion can be represented by a single mode variable:

$$
z_\alpha
$$

The paper assumes that one particular slow mode,

$$
z_0,
$$

dominates aging-related dynamics. This is a modeling assumption, not something derived from the earlier mathematics.

## Equation (1)

The paper writes

$$
\dot z_\alpha
=============

-\frac{dU(z_\alpha)}{dz_\alpha}
+
J_\alpha
+
f_\alpha.
$$

where:

* $z_\alpha$ = the current state of mode $\alpha$
* $\dot z_\alpha$ = the rate of change of that mode
* $U(z)$ = an effective potential
* $J_\alpha$ = persistent stress
* $f_\alpha$ = stochastic noise

The dot notation means:

$$
\dot z = \frac{dz}{dt}.
$$

Importantly, $\dot z$ is not the mode itself. It is the speed at which the mode is changing.

Near equilibrium, the potential is approximated as

$$
U(z)
\approx
\frac{\varepsilon z^2}{2}.
$$

Taking the derivative gives

$$
\frac{dU}{dz}
=============

\varepsilon z,
$$

so Equation (1) becomes

$$
\dot z
======

-\varepsilon z
+
J
+
f.
$$

This is the Ornstein-Uhlenbeck process, a classic stochastic process used in physics, quantitative finance, signal processing, and many other fields. It can be viewed as Brownian motion with a restoring force pulling the system back toward equilibrium. It is also the continuous-time analogue of the AR(1) process from time-series analysis.

## What does ε represent?

The parameter

$$
\varepsilon
$$

is not exactly resilience itself. It is more accurately a recovery rate, stability parameter, or restoring-force coefficient.

If

$$
\varepsilon > 0,
$$

the restoring force pushes the system back toward equilibrium after perturbations. Recovery is possible and the system is stable.

If

$$
\varepsilon = 0,
$$

there is no restoring force. Recovery time becomes infinite. This is the phenomenon known as critical slowing down.

If

$$
\varepsilon < 0,
$$

the restoring force flips sign and becomes destabilizing:

$$
-\varepsilon z
==============

|\varepsilon| z.
$$

Small perturbations grow rather than decay. The equilibrium is unstable.

A useful mental picture is a ball sitting in a bowl:

* positive $\varepsilon$ = steep bowl
* small positive $\varepsilon$ = shallow bowl
* $\varepsilon = 0$ = flat surface
* negative $\varepsilon$ = upside-down bowl

The paper often interprets resilience in terms of $\varepsilon$ because larger $\varepsilon$ means faster recovery from disturbances.

## From Equation (1) to Equation (2)

One source of confusion is that Equation (2) is not derived algebraically from Equation (1). Fedichev is extending the model by introducing an aging mechanism.

Equation (1) is a generic dynamical mode:

$$
\dot z
======

-\varepsilon z
+
J
+
f.
$$

Equation (2) introduces:

1. a special aging-related mode

$$
z_0
$$

2. a damage variable

$$
Z
$$

that accumulates over time.

The new equation becomes

$$
\dot z_0
========

## \beta Z

\varepsilon_0(Z) z_0
+
g z_0^2
+
J_0
+
f_0.
$$

This is not an equality transformation of Equation (1). It is a new model built on top of Equation (1).

## Damage versus stress

Fedichev distinguishes between stress and damage.

Stress is represented by

$$
J_0.
$$

Examples might include smoking, obesity, chronic inflammation, illness, or other ongoing physiological insults. Stress is conceptually reversible.

Damage is represented by

$$
Z.
$$

Damage is assumed to accumulate continuously:

$$
\dot Z = \gamma.
$$

Integrating gives

$$
Z(t) = \gamma t.
$$

Unlike stress, damage never decreases in the model. It only accumulates.

## β and β′

There are two different coupling parameters.

The first appears explicitly:

$$
+\beta Z.
$$

This term says accumulated damage directly pushes the aging mode.

The second appears inside

$$
\varepsilon_0(Z).
$$

Fedichev defines

$$
\varepsilon_0(Z)
================

## \varepsilon_0

\beta' Z.
$$

This means accumulated damage weakens the restoring force.

The two couplings therefore have different roles:

* $\beta$ = damage directly pushes the system
* $\beta'$ = damage destroys stability

Substituting gives

$$
\dot z_0
========

## \beta Z

(\varepsilon_0 - \beta' Z) z_0
+
g z_0^2
+
J_0
+
f_0.
$$

The second effect appears to be the more important one conceptually. The entire aging mechanism is based on the idea that accumulated damage causes

$$
\varepsilon_0
\downarrow
$$

over time.

As damage accumulates, the bowl becomes flatter, recovery becomes slower, and eventually stability disappears.

## Stable vs unstable species

The paper argues that species fall into two broad regimes.

### Unstable species

Examples include mice, flies, and worms.

In these species the critical mode is assumed to be unstable from the beginning:

$$
\varepsilon_0 < 0.
$$

The system is already sitting on top of a hill rather than inside a bowl. Small perturbations naturally grow over time.

Aging is therefore driven primarily by the intrinsic instability of the mode itself. The damage variable $Z$ plays a relatively minor role.

This is important because it implies that interventions acting on

$$
z_0
$$

can produce large lifespan effects. Short interventions can generate lasting changes, which may explain why some mouse longevity experiments look extremely impressive.

### Stable species

Humans are proposed to belong to this category.

Initially,

$$
\varepsilon_0 > 0.
$$

The organism starts with a stable homeostatic state and can recover from perturbations.

However, damage accumulates:

$$
Z = \gamma t,
$$

and gradually weakens stability:

$$
\varepsilon_0(Z)
================

## \varepsilon_0

\beta' Z.
$$

As a result, resilience slowly declines. Recovery becomes slower, variability increases, and eventually the system approaches critical slowing down.

The key implication is that targeting the aging mode

$$
z_0
$$

alone may not be enough in humans. According to the model, the deeper problem is the continuing accumulation of damage

$$
Z.
$$

Unless damage accumulation is slowed or reversed, stability continues to erode over time.


# A Minimal Model Explains Aging Regimes and Guides Intervention Strategies
Notes added: 2026-06-02

pca describes a low dimensional representation of the data itself. each dimension can potentially be a certain biologcal pathway like... ? dynamic modes is like same thing but with element of time added in. they also have derivatives for this reason?

z˙α = −
dU(zα)
dzα
+ Jα + fα,

becomes:

z˙=−εz+J+f

this Ornstein-Uhlenbeck process. it is a stochastic process with usual applications in finanacial and ?... Over time, the process tends to drift towards its mean function: such a process is called mean-reverting.. It can also be can also be considered as the continuous-time analogue of the discrete-time AR(1) process, which i learned in time series modeling class at CU Denver.

the value of z˙ represents ? The dot means rate of change

epsilon represents the degree of resiliance?? of a system. if it is postivbe it would subtyract from the bad stuff that J and f adds? if it is negative it means? if it is 0 it means?

next, fedichev rewrites the z expression with with extra information that tells us how the epsilon, or degree of resilance, gets worse over time as we age. Beta and Z represent? he considers just z0 as a modeling assumption, which is the 'slow mode' - a particular biolgoical process that dominates aging.??

Fedichev defines

ε
0
	​

(Z)=ε
0
	​

−β
′
Z.

This means:

damage weakens the restoring force.
The first:

+βZ

is a direct force.

The second:

−β
′
Z

damage is Z, stress is J, which is reversible.

changes the stability coefficient itself.

but how exactly does the original −εz become zβZ − ε0(Z) z0??? is it supposed to be like an equality or soemthihing?


now new sectiona bout stable vs unstable species: For unstable species:

changing z
0
	​

 can dramatically change lifespan
short interventions can have long-lasting effects

This is why many mouse experiments look amazing.



## GPT notes

## Core idea

Fedichev models an organism as a very high-dimensional dynamical system.

Let

$$
x = (x_1, x_2, ..., x_n)
$$

represent all biological variables (methylation, gene expression, metabolites, physiology, etc.).

The full dynamics are

$$
\dot{x} = F(x).
$$

The exact form of $F$ is unknown and far too complicated to model directly.

The goal is to find a lower-dimensional description that captures the dominant organism-level behavior.

## PCA vs dynamical modes

The paper briefly mentions dimensionality reduction and biological modules, which makes it sound similar to PCA.

PCA diagonalizes a covariance matrix:

$$
\Sigma v_i = \lambda_i v_i.
$$

The resulting components are directions of maximum variance. But the paper is actually using a dynamical systems approach.

Near a homeostatic state $x^*$, the system is linearized:

$$
\dot{x} \approx J(x - x^*),
$$

where $J$ is the Jacobian matrix.

The Jacobian is then diagonalized:

$$
Jv_\alpha = \lambda_\alpha v_\alpha.
$$

The eigenvectors $v_\alpha$ are called normal modes (or eigenmodes).

These are collective patterns involving many biological variables moving together.

The coordinates along those directions are denoted

$$
z_\alpha.
$$

The state can be written as

$$
x = \sum_\alpha z_\alpha v_\alpha.
$$

A mode is therefore not a single biomarker but a coordinated biological process.

## Why modes matter

Each mode evolves approximately independently:

$$
\dot z_\alpha = \lambda_\alpha z_\alpha.
$$

The eigenvalue determines the timescale.

- Large negative eigenvalue → fast recovery.
- Small negative eigenvalue → slow recovery.
- Eigenvalue near zero → very slow dynamics.

The slowest modes dominate long-term behavior.

This is why the paper focuses on them.

A key claim (not a theorem) is that there exists a particularly important slow mode, later called $z_0$, that captures organism-level resilience.

## Equation (1)

The paper writes

$$
\dot z_\alpha
=
-\frac{dU(z_\alpha)}{dz_\alpha}
+
J_\alpha
+
f_\alpha.
$$

This is a Langevin-type stochastic differential equation.

It describes how each mode changes over time.

### Restoring force

$U(z)$ is an effective potential.

The term

$$
-\frac{dU}{dz}
$$

is the restoring force.

A useful picture is a ball in a bowl.

- $z$ is the ball position.
- $U(z)$ is the bowl shape.
- $-\frac{dU}{dz}$ pushes the ball downhill toward equilibrium.

### Persistent stress

$J_\alpha$ is a constant external force.

Examples:

- smoking
- chronic inflammation
- obesity
- long-term physiological stress

This shifts the equilibrium away from its healthy state.

Note: this $J_\alpha$ is unrelated to the Jacobian matrix despite using the same letter.

### Noise

$f_\alpha$ represents random fluctuations.

Examples:

- molecular noise
- stochastic gene expression
- environmental perturbations
- physiological variability

This is the stochastic part of the model.

## Near equilibrium

Near a stable equilibrium, the potential is approximated by a quadratic:

$$
U(z_\alpha)
\approx
\frac{\varepsilon_\alpha z_\alpha^2}{2}.
$$

Taking the derivative:

$$
\frac{dU}{dz_\alpha}
=
\varepsilon_\alpha z_\alpha.
$$

Equation (1) becomes

$$
\dot z_\alpha
=
-\varepsilon_\alpha z_\alpha
+
J_\alpha
+
f_\alpha.
$$

This is the Ornstein-Uhlenbeck process.

## Interpretation of ε

$\varepsilon_\alpha$ measures the strength of the restoring force.

If

$$
\varepsilon_\alpha > 0
$$

the mode is stable and perturbations decay.

If

$$
\varepsilon_\alpha = 0
$$

there is no restoring force.

Recovery becomes infinitely slow ("critical slowing down").

If

$$
\varepsilon_\alpha < 0
$$

perturbations grow exponentially.

The equilibrium is unstable.

## What has happened so far?

Up to Equation (1), everything is standard dynamical systems theory and statistical physics.

No aging model has appeared yet.

The actual aging hypothesis begins when the paper introduces:

- a special slow mode $z_0$ (resilience)
- a damage variable $Z$
- a coupling where accumulated damage gradually reduces the stability parameter $\varepsilon_0$
---

## Data sources & replication


## Longitudinal analysis of blood markers reveals progressive loss of resilience and predicts human lifespan limit

Complete blood
counts (CBC) measurements are most frequently included in
standard blood tests and thus comprise a large common subset of
physiological indices reported across UKB (471473 subjects, age
range 39–73 y.o.) and NHANES datasets (72,925 subjects, age
range 1–85 y.o., see Supplementary Table 1 for the description
of the data fields).

two large longitudinal datasets, jointly referred to and available as GEROLONG


# A Minimal Model Explains Aging Regimes and Guides Intervention Strategies

DNA methylation (DNAm)
data in mice, which reveal two major signatures: (i) a linear
component linked to damage accumulation (Z) and
(ii) an exponential trend reflecting intrinsic instability
along z0 [55]. A similar exponential component was recovered
from longitudinal blood cell counts in the Mouse
Phenome Database