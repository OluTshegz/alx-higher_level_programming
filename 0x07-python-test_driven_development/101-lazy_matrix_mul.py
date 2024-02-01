#!/usr/bin/python3
"""Task 7. Lazy matrix multiplication:
    This module has one function that
    multiplies 2 matrices by using
    the module 'NumPy'"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices
    Args:
        m_a (list of lists of int/float): matrix to be multiplied
        m_b (list of lists of int/float): matrix to be multiplied
    Returns:
        result of multiplication of two matrices (np.matmul(m_a, m_b))"""

    m_1 = np.array(m_a)
    m_2 = np.array(m_b)

    return np.dot(m_1, m_2)
