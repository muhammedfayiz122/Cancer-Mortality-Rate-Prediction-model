import pandas as pd
class DataLoader():
    def __init__(self, path):
        self.df = pd.load_csv(path)

    def load_data(self):
        print(f"info :\n{self.df.info}\n \n")
        print(f"describe :\n{self.df.describe}\n \n")
        print(f"first some columns :\n{self.df.head()}\n \n")
        return self.df
    