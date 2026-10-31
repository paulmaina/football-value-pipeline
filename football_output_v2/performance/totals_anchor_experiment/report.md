# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 12; gameweeks: 2

Excluded forecasts by reason: incoherent_totals_prices: 200, missing_pinnacle_reference: 200, outside_registered_leagues: 82, reference_fixture_mismatch: 200, reference_stale_or_future: 212, stale_or_unsynchronized_production_hda: 67, unreliable_model_identity: 16

{
  "under_3_5": {
    "baseline": {
      "n": 12,
      "log_loss": 0.6330978583120418,
      "brier": 0.21671863562599716,
      "rps": null,
      "calibration": [
        {
          "low": 0.5,
          "high": 0.6,
          "n": 1,
          "mean_probability": 0.5698150907054242,
          "observed_rate": 1.0,
          "overconfidence": -0.43018490929457576,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 2,
          "mean_probability": 0.6479058293479996,
          "observed_rate": 1.0,
          "overconfidence": -0.35209417065200044,
          "observed_wilson95": [
            0.34237195288961925,
            1
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 5,
          "mean_probability": 0.754860392735983,
          "observed_rate": 0.6,
          "overconfidence": 0.15486039273598307,
          "observed_wilson95": [
            0.23071993220883708,
            0.8823817688407467
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 4,
          "mean_probability": 0.8067626816417138,
          "observed_rate": 0.75,
          "overconfidence": 0.05676268164171383,
          "observed_wilson95": [
            0.3006360524426366,
            0.9544139373553637
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 4,
        "mean_probability": 0.8067626816417138,
        "observed_rate": 0.75
      }
    },
    "candidate": {
      "n": 12,
      "log_loss": 0.5565403215412946,
      "brier": 0.18521080894189879,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 1,
          "mean_probability": 0.6911845983950402,
          "observed_rate": 1.0,
          "overconfidence": -0.3088154016049598,
          "observed_wilson95": [
            0.20654329147389294,
            1
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 11,
          "mean_probability": 0.7218369408936687,
          "observed_rate": 0.7272727272727273,
          "overconfidence": -0.005435786379058616,
          "observed_wilson95": [
            0.4343497069897537,
            0.9025411942607853
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.8,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "over_1_5": {
    "baseline": {
      "n": 12,
      "log_loss": 0.5754434030089732,
      "brier": 0.19149421763529204,
      "rps": null,
      "calibration": [
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 6,
          "mean_probability": 0.6710155837630438,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.004348917096377192,
          "observed_wilson95": [
            0.29998832134152864,
            0.9032306674407831
          ]
        },
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 4,
          "mean_probability": 0.7540867753896661,
          "observed_rate": 1.0,
          "overconfidence": -0.24591322461033394,
          "observed_wilson95": [
            0.5100999795960008,
            1
          ]
        },
        {
          "low": 0.8,
          "high": 0.9,
          "n": 2,
          "mean_probability": 0.8392446959290931,
          "observed_rate": 0.5,
          "overconfidence": 0.3392446959290931,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.78,
        "n": 2,
        "mean_probability": 0.8392446959290931,
        "observed_rate": 0.5
      }
    },
    "candidate": {
      "n": 12,
      "log_loss": 0.5536572594600945,
      "brier": 0.1843303032778024,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 12,
          "mean_probability": 0.7522119174651335,
          "observed_rate": 0.75,
          "overconfidence": 0.002211917465133495,
          "observed_wilson95": [
            0.46768966087934005,
            0.9110599603710386
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.78,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "btts_yes": {
    "baseline": {
      "n": 12,
      "log_loss": 0.664662270721687,
      "brier": 0.23588649879842807,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 7,
          "mean_probability": 0.452140030305681,
          "observed_rate": 0.42857142857142855,
          "overconfidence": 0.02356860173425246,
          "observed_wilson95": [
            0.15821692226262685,
            0.7495457695909742
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 3,
          "mean_probability": 0.5462226410747245,
          "observed_rate": 0.3333333333333333,
          "overconfidence": 0.2128893077413912,
          "observed_wilson95": [
            0.0614903152761605,
            0.7923450448735121
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 2,
          "mean_probability": 0.639213200156657,
          "observed_rate": 0.5,
          "overconfidence": 0.13921320015665695,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    },
    "candidate": {
      "n": 12,
      "log_loss": 0.6766383034550508,
      "brier": 0.2418216905605689,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 1,
          "mean_probability": 0.49413662119864793,
          "observed_rate": 0.0,
          "overconfidence": 0.49413662119864793,
          "observed_wilson95": [
            0,
            0.7934567085261071
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 11,
          "mean_probability": 0.535081930660858,
          "observed_rate": 0.45454545454545453,
          "overconfidence": 0.08053647611540343,
          "observed_wilson95": [
            0.21270957543988045,
            0.7199122443100118
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  },
  "over_2_5": {
    "baseline": {
      "n": 12,
      "log_loss": 0.798647558671786,
      "brier": 0.30185858132330007,
      "rps": null,
      "calibration": [
        {
          "low": 0.30000000000000004,
          "high": 0.4,
          "n": 3,
          "mean_probability": 0.3946097246968252,
          "observed_rate": 0.6666666666666666,
          "overconfidence": -0.2720569419698414,
          "observed_wilson95": [
            0.2076549551264879,
            0.9385096847238394
          ]
        },
        {
          "low": 0.4,
          "high": 0.5,
          "n": 5,
          "mean_probability": 0.43683412739308497,
          "observed_rate": 0.6,
          "overconfidence": -0.163165872606915,
          "observed_wilson95": [
            0.23071993220883708,
            0.8823817688407467
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 2,
          "mean_probability": 0.524540600218532,
          "observed_rate": 0.0,
          "overconfidence": 0.524540600218532,
          "observed_wilson95": [
            0,
            0.6576280471103807
          ]
        },
        {
          "low": 0.6000000000000001,
          "high": 0.7000000000000001,
          "n": 2,
          "mean_probability": 0.6262577108957275,
          "observed_rate": 0.0,
          "overconfidence": 0.6262577108957275,
          "observed_wilson95": [
            0,
            0.6576280471103807
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    },
    "candidate": {
      "n": 12,
      "log_loss": 0.7026689591718598,
      "brier": 0.2547538726329868,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 7,
          "mean_probability": 0.4856075747372203,
          "observed_rate": 0.42857142857142855,
          "overconfidence": 0.05703614616579178,
          "observed_wilson95": [
            0.15821692226262685,
            0.7495457695909742
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 5,
          "mean_probability": 0.5158210269880125,
          "observed_rate": 0.4,
          "overconfidence": 0.11582102698801244,
          "observed_wilson95": [
            0.1176182311592533,
            0.769280067791163
          ]
        }
      ],
      "high_confidence": {
        "threshold": 0.7,
        "n": 0,
        "mean_probability": null,
        "observed_rate": null
      }
    }
  }
}
