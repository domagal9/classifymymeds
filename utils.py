import os

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(CURRENT_FOLDER, 'data')


class DataFrameFeatures(BaseEstimator, TransformerMixin):
    '''
    Features extraction transformer for pandas dataframe.

    DataFrameFeatures transform selected columns of pandas dataframe into numpy
    array.

    Parameters
    ----------
    num_cols : list, default=[]
        List of numerical columns to extract

    cat_cols : list, default=[]
        List of categorical columns to extract

    one_hot_drop : bool, default=True
        Specify whether to drop a category in each categorical feature. If true,
        it drops the last feature after features being sorted.

    Attributes
    ----------
    feature_names_: A list of names corresponding columns of tranformed array.
    '''

    def __init__(self,
                 num_cols=[],
                 cat_cols=[],
                 one_hot_drop=True):
        self.num_cols = num_cols
        self.cat_cols = cat_cols
        self.one_hot_drop = one_hot_drop

    def check_features_existed(self, X):
        if type(X) is not pd.DataFrame:
            raise TypeError(f'Expect {pd.DataFrame}, but get type {type(X)}')

        cols = set(X.columns)
        for c in self.num_cols + self.cat_cols:
            if c not in cols:
                raise ValueError(f'X does not have column `{c}`')

    def check_categorial_labels(self, col_name, all_labels, in_labels):
        for label in in_labels:
            if label not in all_labels:
                raise ValueError(
                    f'Unseen label `{label}` for column `{col_name}`')

    def fit(self, X, y=None):
        self.check_features_existed(X)
        self.feature_names_ = []
        self.feature_names_.extend(self.num_cols)
        self._cat_mapping = {}
        for cat in self.cat_cols:
            all_labels = sorted(X[cat].unique())
            labels = all_labels
            if self.one_hot_drop:
                labels = all_labels[:-1]
            self.feature_names_.extend(f'{cat}_{c}' for c in labels)
            self._cat_mapping[cat] = (all_labels, labels)
        return self

    def transform(self, X, y=None):
        check_is_fitted(self, '_cat_mapping')
        self.check_features_existed(X)

        arr = X[self.num_cols].to_numpy()
        for cat in self.cat_cols:
            all_labels, labels = self._cat_mapping[cat]
            self.check_categorial_labels(cat, all_labels, X[cat].unique())
            one_hot = np.zeros((X.shape[0], len(labels)), dtype=np.int)
            for i, label in enumerate(labels):
                one_hot[:, i] = X[cat] == label
            arr = np.concatenate([arr, one_hot], axis=1)
        return arr


_DEFAULT_DATA_FOLDER = DATA_FOLDER


def _path_for(filename, folder):
    return os.path.join(folder, filename)


_TABLE_CACHES = {}


def load_tables(folder=_DEFAULT_DATA_FOLDER, use_cache=True):
    """Load all CoverMyMeds data into dataframes.

    Args:
        folder (str, optional): path to the data folder. Defaults to `./data`.
        use_cache (bool, optional): Whether or not to use cache. Defaults to True.
            This will make subsequent calls of this function faster.

    Returns:
        dict: A dict of all tables. Here are the available tables:
            dim_date -> dataframe from dim_date.csv
            dim_claims -> dataframe from dim_claims.csv
            dim_pa -> dataframe from dim_pa.csv
            bridge -> dataframe from bridge.csv
            full -> join of all above dataframes
            dim_pa_full -> similar to dim_pa, but with all possible columns from full
            no_pa -> dataframe of approved pharmacy claims
    """

    if use_cache and folder in _TABLE_CACHES:
        return _TABLE_CACHES[folder]

    df_date = pd.read_csv(_path_for('dim_date.csv', folder))
    df_claims = pd.read_csv(_path_for('dim_claims.csv', folder))
    df_pa = pd.read_csv(_path_for('dim_pa.csv', folder))
    df_bridge = pd.read_csv(_path_for('bridge.csv', folder))
    
    df_claims['reject_code'] = df_claims.reject_code.fillna(0).astype(int)
    df_claims['bin'] = df_claims.bin.astype(str)

    df_full = pd.merge(df_claims, df_bridge, on='dim_claim_id')
    df_full = pd.merge(df_full, df_pa, how='left', on='dim_pa_id')
    df_full = pd.merge(df_full, df_date, how='left', on='dim_date_id')

    df_with_pa = df_full[~np.isnan(df_full.pa_approved)].copy()
    pa_cols = ['correct_diagnosis', 'tried_and_failed',
               'contraindication', 'pa_approved']
    for c in pa_cols:
        df_with_pa[c] = df_with_pa[c].astype(int)

    df_without_pa = df_full[np.isnan(df_full.pa_approved)].copy()
    df_without_pa = df_without_pa.drop(pa_cols, axis=1)

    tables = {
        'dim_date': df_date,
        'dim_claims': df_claims,
        'dim_pa': df_pa,
        'bridge': df_bridge,
        'full': df_full,
        'dim_pa_full': df_with_pa,
        'no_pa': df_without_pa
    }

    _TABLE_CACHES[folder] = tables
    return tables
