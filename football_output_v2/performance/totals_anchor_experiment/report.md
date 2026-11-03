# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 14; gameweeks: 4

Excluded forecasts by reason: incoherent_totals_prices: 223, missing_pinnacle_reference: 223, no_live_odds: 14, outside_registered_leagues: 101, production_basis_changed: 14, reference_fixture_mismatch: 223, reference_stale_or_future: 235, stale_or_unsynchronized_production_hda: 81, unreliable_model_identity: 16

{
  "under_3_5": {
    "baseline": {
      "n": 14,
      "log_loss": 0.5933081726197987,
      "brier": 0.19848990974631933,
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
          "n": 7,
          "mean_probability": 0.7396075435721993,
          "observed_rate": 0.7142857142857143,
          "overconfidence": 0.025321829286484965,
          "observed_wilson95": [
            0.35892909014821267,
            0.9177828342909844
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
      "n": 14,
      "log_loss": 0.5214565590728896,
      "brier": 0.16903296378349156,
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
          "n": 13,
          "mean_probability": 0.7236049637376831,
          "observed_rate": 0.7692307692307693,
          "overconfidence": -0.04562580549308615,
          "observed_wilson95": [
            0.49743126004873084,
            0.918206209075343
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
      "n": 14,
      "log_loss": 0.5311908322406292,
      "brier": 0.17191497115319768,
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
          "n": 6,
          "mean_probability": 0.7582887220341412,
          "observed_rate": 1.0,
          "overconfidence": -0.24171127796585878,
          "observed_wilson95": [
            0.6096569663469354,
            0.9999999999999999
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
      "n": 14,
      "log_loss": 0.517816096349507,
      "brier": 0.16779679707308778,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 14,
          "mean_probability": 0.7503445708459078,
          "observed_rate": 0.7857142857142857,
          "overconfidence": -0.03536971486837792,
          "observed_wilson95": [
            0.5241027622679172,
            0.9242875166308363
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
      "n": 14,
      "log_loss": 0.6774686518541906,
      "brier": 0.2422339212490876,
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
          "n": 5,
          "mean_probability": 0.5449314949255049,
          "observed_rate": 0.4,
          "overconfidence": 0.14493149492550483,
          "observed_wilson95": [
            0.1176182311592533,
            0.769280067791163
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
      "n": 14,
      "log_loss": 0.6785668127864304,
      "brier": 0.24277519887701934,
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
          "n": 13,
          "mean_probability": 0.5315246656515429,
          "observed_rate": 0.46153846153846156,
          "overconfidence": 0.06998620411308132,
          "observed_wilson95": [
            0.2320575430148814,
            0.7085656756816796
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
      "n": 14,
      "log_loss": 0.7835538615385723,
      "brier": 0.29443915055218783,
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
          "n": 4,
          "mean_probability": 0.5213248952028848,
          "observed_rate": 0.25,
          "overconfidence": 0.27132489520288483,
          "observed_wilson95": [
            0.045586062644636216,
            0.6993639475573634
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
      "n": 14,
      "log_loss": 0.6924371960271996,
      "brier": 0.2496491894737917,
      "rps": null,
      "calibration": [
        {
          "low": 0.4,
          "high": 0.5,
          "n": 8,
          "mean_probability": 0.4814190000865874,
          "observed_rate": 0.375,
          "overconfidence": 0.10641900008658739,
          "observed_wilson95": [
            0.13684175946152105,
            0.6942621454161981
          ]
        },
        {
          "low": 0.5,
          "high": 0.6,
          "n": 6,
          "mean_probability": 0.5159554871191202,
          "observed_rate": 0.5,
          "overconfidence": 0.015955487119120204,
          "observed_wilson95": [
            0.18761280689940868,
            0.8123871931005913
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
