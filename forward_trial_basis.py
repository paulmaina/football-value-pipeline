"""Keep preregistered trials on their frozen legacy companion, never relabel production."""
import json


def legacy_basis(row):
    from football_value_pipeline_v2_standalone import LEGACY_MODEL_VERSION, MODEL_PROFILES, FootballValuePipelineV2
    version = row.get('model_version')
    if (version not in MODEL_PROFILES or version == LEGACY_MODEL_VERSION
            or row.get('legacy_status') != 'AVAILABLE'
            or row.get('legacy_model_version') != LEGACY_MODEL_VERSION
            or 'legacy_trial_matrix' not in row):
        return row
    # Missing companion evidence must fail existing gates, never borrow production probabilities.
    return {**row, **{k: row.get('legacy_'+k) for k in FootballValuePipelineV2.LEGACY_COLUMNS},
            'model_version': LEGACY_MODEL_VERSION, 'totals_anchor_applied': False,
            'trial_forecast_model_version': version, 'trial_basis': 'same_run_legacy_companion'}


def bound_inputs(row, matrix=None, inputs=None):
    """Return only the matrix and anchor inputs belonging to the chosen trial basis."""
    if legacy_basis(row) is row:
        return matrix, inputs
    import numpy as np
    try:
        m = json.loads(row.get('legacy_trial_matrix') or 'null')
        data = json.loads(row.get('legacy_trial_inputs') or 'null')
        return None if m is None else np.asarray(m, dtype=float), data
    except (ValueError, TypeError):
        return None, None


def provenance(row):
    if row.get('trial_basis'):
        return {'comparison_basis': row['trial_basis'],
                'forecast_model_version': row['trial_forecast_model_version'],
                'comparison_model_version': row['model_version']}
    return {}
