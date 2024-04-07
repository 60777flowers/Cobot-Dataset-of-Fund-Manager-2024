from Data import *

from scipy.stats import pearsonr
import numpy as np
import pandas as pd


Time_Data = Get_Data('Time_Data')
Labor_Time = pd.DataFrame(Time_Data['L'])


def partial_correlation(C):
    """
    Returns the matrix of partial correlations given the correlation matrix C.
    """
    P_corr = np.zeros_like(C)
    for i in range(len(C)):
        for j in range(len(C)):
            if i == j:
                P_corr[i, j] = 1
            else:
                idx = np.ones(len(C), dtype=bool)
                idx[i] = False
                idx[j] = False
                beta_i = np.linalg.lstsq(C[idx][:, idx], C[idx, j], rcond=None)[0]
                beta_j = np.linalg.lstsq(C[idx][:, idx], C[i, idx], rcond=None)[0]
                P_corr[i, j] = C[i, j] - C[i, idx].dot(beta_i)
                P_corr[i, j] /= np.sqrt(C[i, i] - C[i, idx].dot(beta_j))
                P_corr[i, j] /= np.sqrt(C[j, j] - C[j, idx].dot(beta_i))
    return P_corr


def calculate_kmo(dataset):
    """
    Calculates the Kaiser-Meyer-Olkin criterion for a dataset.
    """
    corr_matrix = np.corrcoef(dataset, rowvar=False)
    partial_corr_matrix = partial_correlation(corr_matrix)

    # Calculate the KMO statistic
    ais = np.sum(corr_matrix ** 2, axis=1) - np.diag(corr_matrix ** 2)
    d = 1 - np.diag(corr_matrix ** 2)
    kmo_nums = np.sum(ais)
    kmo_denoms = kmo_nums + np.sum(partial_corr_matrix ** 2, axis=1) - np.diag(partial_corr_matrix ** 2)
    kmo = kmo_nums / kmo_denoms
    return kmo


# Calculate KMO for the given dataset
print(calculate_kmo(Labor_Time))
