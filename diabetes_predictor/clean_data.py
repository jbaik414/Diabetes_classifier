import pandas as pd

def clean_diabetes_data(df):

    
    df.drop(columns=['bp.2s', 'bp.2d', 'ID'], axis=1, inplace=True)
    df['GENDER'] = df['GENDER'].map({'male': 1, 'female': 0})
    df['FRAME'] = df['FRAME'].map({'small': 0, 'medium': 1, 'large': 2})
    df['LOCATION'] = df['LOCATION'].map({'Buckingham': 0, 'Louisa': 1})  
    df['BMI'] = (df['WEIGHT']/ (df['HEIGHT']) ** 2)* 703
    
    age = [0, 25, 60, 100]   
    age_group = ["Young", "Adult", "Elderly"]
    df["AGE_GROUP"] = pd.cut(df["AGE"], bins = age, labels = age_group, right = False)
    age_group_map = {"Young" :1, "Adult":2, "Elderly":3}
    df['AGE_GROUP'] = df['AGE_GROUP'].map(age_group_map)
    
    return df