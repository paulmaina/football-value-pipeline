# Pinnacle totals anchoring trial

Separate proportional intensity scaling to fresh Pinnacle O/U 2.5, fitted rho and production HDA preserved. Primary Under 3.5 log loss; other markets are guardrails. No bets, automatic promotion or backfill.

Status: COLLECT_MORE_DATA; paired fixtures: 13; gameweeks: 3

Excluded forecasts by reason: incoherent_totals_prices: 200, missing_pinnacle_reference: 200, outside_registered_leagues: 82, reference_fixture_mismatch: 200, reference_stale_or_future: 212, stale_or_unsynchronized_production_hda: 67, unreliable_model_identity: 16

{
  "under_3_5": {
    "baseline": {
      "n": 13,
      "log_loss": 0.6115856038039065,
      "brier": 0.20686671453774214,
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
          "n": 6,
          "mean_probability": 0.7460951849312268,
          "observed_rate": 0.6666666666666666,
          "overconfidence": 0.07942851826456021,
          "observed_wilson95": [
            0.29998832134152864,
            0.9032306674407831
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
      "n": 13,
      "log_loss": 0.5407134209199637,
      "brier": 0.1776975438074086,
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
          "n": 12,
          "mean_probability": 0.7203614603199134,
          "observed_rate": 0.75,
          "overconfidence": -0.029638539680086562,
          "observed_wilson95": [
            0.46768966087934005,
            0.9110599603710386
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
      "n": 13,
      "log_loss": 0.5518834990325052,
      "brier": 0.18104756739137295,
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
          "n": 5,
          "mean_probability": 0.7560729100744943,
          "observed_rate": 1.0,
          "overconfidence": -0.2439270899255057,
          "observed_wilson95": [
            0.5655085052479191,
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
      "n": 13,
      "log_loss": 0.5319209471818847,
      "brier": 0.17448810907031753,
      "rps": null,
      "calibration": [
        {
          "low": 0.7000000000000001,
          "high": 0.8,
          "n": 13,
          "mean_probability": 0.7530072718421899,
          "observed_rate": 0.7692307692307693,
          "overconfidence": -0.016223497388579422,
          "observed_wilson95": [
            0.49743126004873084,
            0.918206209075343
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
      "n": 13,
      "log_loss": 0.6645360168845854,
      "brier": 0.2358138109371066,
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
          "n": 4,
          "mean_probability": 0.5384900552485015,
          "observed_rate": 0.5,
          "overconfidence": 0.038490055248501465,
          "observed_wilson95": [
            0.15003570882017148,
            0.8499642911798285
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
      "n": 13,
      "log_loss": 0.6758424789700214,
      "brier": 0.24141817558768225,
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
          "n": 12,
          "mean_probability": 0.5332925376736893,
          "observed_rate": 0.5,
          "overconfidence": 0.03329253767368934,
          "observed_wilson95": [
            0.2537781703934222,
            0.7462218296065778
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
      "n": 13,
      "log_loss": 0.7877351956940835,
      "brier": 0.29647161843593917,
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
          "n": 3,
          "mean_probability": 0.5225319773105922,
          "observed_rate": 0.3333333333333333,
          "overconfidence": 0.18919864397725888,
          "observed_wilson95": [
            0.0614903152761605,
            0.7923450448735121
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
      "n": 13,
      "log_loss": 0.6994200092383891,
      "brier": 0.2531303974728817,
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
