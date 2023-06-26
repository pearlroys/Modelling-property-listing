import re
import requests
import os
import zipfile
import pandas as pd
from datetime import datetime

class TabularDataClean():
    """this class is used to clean the tabular data.
    """
    def __init__(self) -> None:
        pass


    def remove_rows_with_missing_ratings(self, df):
       
       df = df.dropna(subset=['Location_rating'])
       return  df


    def combine_description_strings(self, df):

        df['Description'].str.replace("'About this space',","")
        df['Description'] = df['Description'].str.replace('"',"")
        df['Description'] = df['Description'].str.replace("' '","")
        df['Description'] = df['Description'].str.replace("'","")
        df['Description'] = df['Description'].str.replace(r'\\n', '')
        df['Description'] = df['Description'].str.replace(r'\\n\\', '')
        df['Description'] = df['Description'].str.split(',', n=1).str[-1]
        df['Description'] = df['Description'].str[:-2]
        df= df.dropna(subset=['Description'])
        return df
    

    def set_default_feature_values(self, df):

        df['beds'] = df['beds'].fillna(1)
        df['guests'] = df['guests'].fillna(1)
        df['bathrooms'] = df['bathrooms'].fillna(1)
        df['bedrooms'] = df['bedrooms'].fillna(1)
        return df
    
    def clean_tabular_data(self, df):
        df = self.set_default_feature_values(df)
        df = self.remove_rows_with_missing_ratings(df)
        df = self.combine_description_strings(df)
        df.drop('Unnamed: 19', axis=1, inplace=True)
        return df
    
    def load_airbnb(self):
        df = pd.read_csv('clean_tabular_data.csv')
        features = df.drop(columns= ['ID', 'Category', 'Title', 'Description', 'Amenities', 'Price_Night', 'Location', 'url'])
        labels = df["Price_Night"]
        loaded_data = (features,labels)
        return loaded_data
    




    
if __name__ == "__main__":
    tabula = TabularDataClean()
    df = pd.read_csv('listing.csv') 
    df = tabula.clean_tabular_data(df)
    df.to_csv('clean_tabular_data.csv', index=False)

