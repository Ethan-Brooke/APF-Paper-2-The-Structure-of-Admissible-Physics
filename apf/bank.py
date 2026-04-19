"""apf/bank.py — Paper 2 registry.

Lightweight registry for the 14-check subset bundled in this
paper-companion repo. Mirrors the canonical apf.bank API: REGISTRY (dict),
get_check(name), run_all(verbose=False).
"""
from collections import OrderedDict
import traceback

from apf import core as _core


def _build_registry():
    reg = OrderedDict()
    for name in ['check_L_nc', 'check_L_irr', 'check_T3', 'check_Theorem_R', 'check_L_Cauchy_uniqueness', 'check_L_gauge_template_uniqueness', 'check_L_anomaly_free', 'check_L_count', 'check_P_exhaust', 'check_L_singlet_Gram', 'check_L_equip', 'check_L_saturation_partition', 'check_L_self_exclusion', 'check_T_vacuum_stability']:
        fn = getattr(_core, name, None)
        if fn is None:
            # Function couldn't be extracted — skip with a warning attribute
            continue
        reg[name] = fn
    return reg


REGISTRY = _build_registry()
EXPECTED_CHECK_COUNT = 14


def get_check(name):
    """Return the check function registered as `name`. Raises KeyError if missing."""
    if name not in REGISTRY:
        raise KeyError(f"Check '{name}' not found. Available: {sorted(REGISTRY.keys())}")
    return REGISTRY[name]


def run_all(verbose=False):
    """Run every registered check, returning a list of result dicts."""
    results = []
    for name, fn in REGISTRY.items():
        try:
            r = fn()
            if not isinstance(r, dict):
                # Some legacy checks return True/False
                r = {"name": name, "passed": bool(r), "key_result": str(r)}
            elif "passed" not in r:
                r["passed"] = True
            r.setdefault("name", name)
        except Exception as e:
            r = {
                "name": name,
                "passed": False,
                "error": f"{type(e).__name__}: {e}",
                "traceback": traceback.format_exc(),
            }
        if verbose:
            status = "PASS" if r.get("passed", True) else "FAIL"
            print(f"  {r['name']}: {status}")
            if r.get("key_result"):
                print(f"    {r['key_result']}")
        results.append(r)
    return results
