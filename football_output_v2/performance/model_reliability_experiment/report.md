# Model reliability trials

Two separate one-factor trials against actual production, not a combined configuration. First eligible snapshot freezes missing candidates too. Primary 1X2 week-block intervals use 97.5% per trial (familywise 95%); other markets/calibration are guardrails and descriptive. No automatic promotion or betting-edge claim.

| Candidate | Status | Paired fixtures | Gameweeks | Verified coverage |
|---|---|---:|---:|---:|
| stronger_l2 | COLLECT_MORE_DATA | 22/300 | 1/6 | 0.9166666666666666 |

## stronger_l2

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9192203121980871 | 0.9232750382262604 | 0.5448968721723673 | 0.5469576780660881 |
| over_1_5 | 0.6181810143981351 | 0.6300813788449918 | 0.2126625942768694 | 0.21788410128977118 |
| under_3_5 | 0.6448352714650573 | 0.626565701708927 | 0.22206800931670684 | 0.21755518129546034 |
| btts_yes | 0.6692206012442674 | 0.6585458573442117 | 0.23771057516484523 | 0.23287563374980563 |
| over_2_5 | 0.6443168710708914 | 0.6417954998370662 | 0.22696638107866696 | 0.2258297197405198 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

| fixed_half_life | COLLECT_MORE_DATA | 22/300 | 1/6 | 0.9166666666666666 |

## fixed_half_life

| Market | Baseline log loss | Candidate log loss | Baseline Brier | Candidate Brier |
|---|---:|---:|---:|---:|
| 1x2 | 0.9192203121980871 | 0.9167164359964564 | 0.5448968721723673 | 0.5435891133113966 |
| over_1_5 | 0.6181810143981351 | 0.6131356147160738 | 0.2126625942768694 | 0.21129120129875584 |
| under_3_5 | 0.6448352714650573 | 0.6411270916871715 | 0.22206800931670684 | 0.22050655072028819 |
| btts_yes | 0.6692206012442674 | 0.6660532817088635 | 0.23771057516484523 | 0.23621676600824876 |
| over_2_5 | 0.6443168710708914 | 0.6335357750650091 | 0.22696638107866696 | 0.22148793978755502 |

Primary familywise 95% gain interval: None
Evidence: NO_CLEAR_PROMOTION_EVIDENCE. Calibration and league breakdowns: summary.json.

