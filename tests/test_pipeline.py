
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from pipeline import validate


# Test 1: Valid data 
def test_valid_data():
    data = {
        "start_date": [pd.Timestamp("2026-01-01")],
        "end_date": [pd.Timestamp("2026-02-01")],
        "therms": [100.0],
        "cost": [50.0]
    }

    df = pd.DataFrame(data)

    result = validate(df)

    assert len(result) == 1


# Test 2: Invalid date 
def test_invalid_date_range():
    data = {
        "start_date": [pd.Timestamp("2026-01-01")],
        "end_date": [pd.Timestamp("2026-01-01")],
        "therms": [100.0],
        "cost": [50.0]
    }

    df = pd.DataFrame(data)

    with pytest.raises(ValueError):
        validate(df)

# Test 3: Negative therms
def test_negative_therms():
    df = pd.DataFrame({
        "start_date": [pd.Timestamp("2026-01-01")],
        "end_date": [pd.Timestamp("2026-02-01")],
        "therms": [-100.0],
        "cost": [50.0]
    })

    with pytest.raises(ValueError):
        validate(df)

 #Test 3: Negative cost
def test_negative_cost():
    df = pd.DataFrame({
        "start_date": [pd.Timestamp("2025-02-25")],
        "end_date": [pd.Timestamp("2026-02-27")],
        "therms" : [100.0],
        "cost": [-50.0]
    })
    with pytest.raises(ValueError):
        validate(df)

#Test 4: Duplicate billing
def test_duplicate_billing_periods():
     df = pd.DataFrame ({
        "start_date": [
            pd.Timestamp("2026-01-01"),
            pd.Timestamp("2026-01-01")
        ],
        "end_date": [
            pd.Timestamp("2026-02-01"),
            pd.Timestamp("2026-02-01")
        ],
        "therms": [100.0, 200.0],
        "cost": [50.0, 100.0]
    })
     
     with pytest.raises(ValueError):
        validate(df)