# sentinel-findings.md

*Written by Sentinel — WARN-tier findings.*

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.254665+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.449591+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:42.811718+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:44.822958+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:14:45.295418+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:56.975927+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:57.168014+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:14:57.568607+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:14:59.662186+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:15:00.094669+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.596742+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:11.793230+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:12.161817+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:14.293442+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:15:14.667156+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.630784+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:25.817676+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:15:26.237694+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:15:28.565672+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:15:29.081547+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:56`
- **Detail:** pattern matched: for token in ("REPLACE_ME", "__PLACEHOLDER__", "{{REPLACE", "TODO_FILL"):
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:19:13.273291+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.090759+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.311104+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:14.732025+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:16.953032+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:19:17.463546+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:56`
- **Detail:** pattern matched: for token in ("REPLACE_ME", "__PLACEHOLDER__", "{{REPLACE", "TODO_FILL"):
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:19:28.050612+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:28.863679+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:29.045359+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:29.413461+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:31.481658+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:19:31.919526+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:16138`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `CORONARY_IVL_REVIEW.html:22973`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.415558+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `CORONARY_IVL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:50.607102+00:00

## [WARN] P1-fabrication-temporal-impossibility
- **Location:** `CORONARY_IVL_REVIEW.html:7435`
- **Detail:** trial NCT06369142: year=2027 is in the future (current year is 2026)
- **Fix hint:** verify the trial year against the source paper (typo? completion vs registration year confusion?)
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:19:51.067129+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:29963`
- **Detail:** `parseInt(tfResult.k0 ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:35226`
- **Detail:** `parseFloat(r?.i2 ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36912`
- **Detail:** `parseInt(historyTrial?.outcomesUpdateCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:36915`
- **Detail:** `parseInt(historyTrial?.versionCount ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43880`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43924`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:43986`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44318`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `CORONARY_IVL_REVIEW.html:44336`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:19:53.532889+00:00

## [WARN] P0-rapidmeta-data-integrity
- **Location:** `CORONARY_IVL_REVIEW.html:7444`
- **Detail:** NCT NCT06237518 has realData name 'IVL vs Conventional (China)' but nctAcronyms says 'IVL-RCT China'
- **Fix hint:** verify against ClinicalTrials.gov which acronym is correct for NCT06237518; align both maps to that ground truth
- **Source:** lessons.md#data-integrity:pegcetacoplan-oaks-derby-swap-2026-04-28
- **When:** 2026-06-13T12:19:53.999152+00:00
