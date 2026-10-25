# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 11; gameweeks: 2

Excluded forecasts by reason: incoherent_totals_prices: 131, missing_pinnacle_reference: 131, outside_registered_leagues: 55, reference_fixture_mismatch: 131, reference_stale_or_future: 134, stale_or_unsynchronized_production_hda: 20, unreliable_model_identity: 16

{
  "under_3_5": {
    "baseline": {
      "n": 11,
      "log_loss": 0.6587200500443084,
      "brier": 0.2284447484646142,
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
          "n": 4,
          "mean_probability": 0.7676242056291189,
          "observed_rate": 0.5,
          "overconfidence": 0.2676242056291189,
          "observed_wilson95": [
            0.15003570882017148,
            0.8499642911798285
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
      "n": 11,
      "log_loss": 0.5759884270380987,
      "brier": 0.1943981760037521,
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
          "n": 10,
          "mean_probability": 0.7230292149657773,
          "observed_rate": 0.7,
          "overconfidence": 0.023029214965777367,
          "observed_wilson95": [
            0.39677321997956516,
            0.892210712513788
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
      "n": 11,
      "log_loss": 0.6032611097532637,
      "brier": 0.20383094684630443,
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
          "n": 3,
          "mean_probability": 0.7508488619038968,
          "observed_rate": 1.0,
          "overconfidence": -0.24915113809610323,
          "observed_wilson95": [
            0.43849391955098227,
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
      "n": 11,
      "log_loss": 0.5789134699195684,
      "brier": 0.19580467074850239,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 11,
          "mean_probability": 0.7516007143555504,
          "observed_rate": 0.7272727272727273,
          "overconfidence": 0.024327987082823133,
          "observed_wilson95": [
            0.4343497069897537,
            0.9025411942607853
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
      "n": 11,
      "log_loss": 0.6563291146488164,
      "brier": 0.23173528910649308,
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
          "n": 2,
          "mean_probability": 0.5540276266850286,
          "observed_rate": 0.5,
          "overconfidence": 0.054027626685028585,
          "observed_wilson95": [
            0.09452865480086614,
            0.9054713451991339
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
      "n": 11,
      "log_loss": 0.6704727029656745,
      "brier": 0.23874778128025584,
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
          "n": 10,
          "mean_probability": 0.5360892006261055,
          "observed_rate": 0.5,
          "overconfidence": 0.036089200626105544,
          "observed_wilson95": [
            0.23658959361548731,
            0.7634104063845126
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
      "n": 11,
      "log_loss": 0.8048497664951326,
      "brier": 0.30487939320174673,
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
          "n": 1,
          "mean_probability": 0.5307862548120977,
          "observed_rate": 0.0,
          "overconfidence": 0.5307862548120977,
          "observed_wilson95": [
            0,
            0.7934567085261071
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
      "n": 11,
      "log_loss": 0.7013144598103978,
      "brier": 0.2540762017555528,
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
          "n": 4,
          "mean_probability": 0.5167605981031465,
          "observed_rate": 0.5,
          "overconfidence": 0.01676059810314645,
          "observed_wilson95": [
            0.15003570882017148,
            0.8499642911798285
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
