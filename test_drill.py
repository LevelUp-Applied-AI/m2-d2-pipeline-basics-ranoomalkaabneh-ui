"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue




def test_clean_column():
    s = pd.Series([1, 2, None, 4])
    cleaned = clean_column(s)

   
    assert cleaned.isna().sum() == 0

    
    assert cleaned[2] == s.median()


def test_compute_revenue():
    quantity = pd.Series([1, 2, 3])
    price = pd.Series([10, 20, 30])

    revenue = compute_revenue(quantity, price)

    expected = pd.Series([10, 40, 90])
    assert revenue.equals(expected)