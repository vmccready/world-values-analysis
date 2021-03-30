
import pandas as pd 

def pipeline(data):

    data_cleaned = data.copy()


    return data_cleaned

def create_Xy(data):
    """ Create X and y variables for use by models. 

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

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
    return X


def get_country_codes():
    """ Get dictionary of country codes for xlsx file. 

    Returns:
        dictionary: keys - country codes
                    values - country names
    """
    variables = pd.read_excel('data/F00011221-WVS-7_Variables_Report_Annex.xlsx')
    country = variables[['Country/ territory', 'ISO 3166-1 numeric code']].set_index('ISO 3166-1 numeric code')
    return country.to_dict()['Country/ territory']