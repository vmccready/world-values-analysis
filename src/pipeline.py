
import pandas as pd 
import numpy as np


def create_Xy(data):
    """ Create X and y variables for use by models. 

    Args:
        data (pd.DataFrame): Pandas dataframe with all data from source data file. 

    Returns:
        X (pd.DataFrame): Feature matrix for use by models. 
        y (pd.Series): Target series for use by models. 

    """

    # Choosing questions to include
    # qs = ['Q' + str(i) for i in range(1,82)]
    # qs += ['Q' + str(i) for i in range(94,199)]
    qs = ['Q' + str(i) for i in range(1,51)]
    qs += ['Q' + str(i) for i in range(56,63)]
    qs += ['Q' + str(i) for i in range(106,112)]
    # qs += ['Q' + str(i) for i in range(152,199)]
    X = data.loc[:,qs].copy()
    y = data.loc[:,'B_COUNTRY'].copy()

    X = cleaner(X)
    return X, y


def cleaner(X):
    # Change these questions to binary with default value 0
    questions = ['Q' + str(i) for i in range(7,18)]
    X[questions] = X[questions].applymap(lambda x: 1 if x==1 else 0)

    # Fill all null values with 0
    X = X.fillna(0)
    return X

def get_top_5(X, model, names=True):
    """ Get top 5 country codes predicted by model for given set X. 

    Args:
        X (pd.DataFrame): Pandas dataframe with set of data to predict. 
        model (sklearn classifier): Trained sklearn model. 

    Returns:
        top5 (np.array): Array with top 5 countries as codes. 

    """
    countries = get_country_codes()
    classes = model.classes_
    probs = model.predict_proba(X)
    top5 = probs.argsort()[:,-1:-6:-1]
    top5 = [classes[top] for top in top5]
    if names:
        top5 = [countries[codes] for codes in top5]
    return np.array(top5)

def get_bottom_5(X, model):
    probs = model.predict_proba(X)
    bottom5 = probs.argsort()[:,:5]
    return bottom5

def get_top5_countries(top5, model):
    classes = model.classes_
    country = get_country_codes()
    top5_countries = []
    for top in top5:
        codes = classes[top]
        countries = [country[code] for code in codes]
        top5_countries.append(countries)
    return np.array(top5_countries)

def get_country_codes():
    """ Get dictionary of country codes for xlsx file. 

    Returns:
        dictionary: keys - country codes
                    values - country names
    """
    variables = pd.read_excel('data/F00011221-WVS-7_Variables_Report_Annex.xlsx')
    country = variables['Country/ territory']
    country.index = variables['ISO 3166-1 numeric code']
    return country #.to_dict()['Country/ territory']