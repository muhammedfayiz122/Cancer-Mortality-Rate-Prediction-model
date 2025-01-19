import pandas as pd
import os

class DataLoader():
    def __init__(self, path):
        """
        Intialize data path and load the dataset.

        Parameters:
        path (str): Path to the data source.

        Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        ValueError: If the file format is not supported
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file at {path} does not exists.")
        if not path.endswith('.csv'):
            raise ValueError("Only CSV file are supported.")
        
        self.df = pd.read_csv(path)
    
    def load_data(self):
        """
        Return the loaded dataset

        Returns:
        df (pd.Dataframe) : the Dataframe used as dataset in this project
        """
        return self.df
        
    def preview_data(self):
        """
        Provides a quick preview of the data

        Returns:
        None
        """
        print(f"Dataset quick preview:\n{self.df.head(5)} ")
        print(f"Shape : {self.df.shape}")
        print(f"Columns :\n{self.df.columns}")
        
    