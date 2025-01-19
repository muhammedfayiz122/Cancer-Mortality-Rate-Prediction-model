class DataPreprocess:
    def __init__(self, df):
        """
        Load dataset

        Parameters:
        df (pd.DataFrame) : The loaded dataset
        """
        self.df = df

    def split_and_deconst(self):
        """
        splitting and de-construction of features to remove object columns

        Parameters:

        Returns:
        df (pd.DataFrame) : return dataset after splitting adn de-construction
        """
        pass

    def deal_const_columns(self):
        pass

    def deal_few_val(self):
        pass

    def deal_dupplicate_rows(self):
        pass

    def handle_missing_values(self):
        pass

    def encode_catogorical_values(self):
        pass

    def split_features(self, target_variable):
        """
        Split dataset into input variables and target variables

        Parameters:
        target (str) : target variable

        Returns:
        X (pd.DataFrame) : input dataframe
        y (pd.Dataframe) : target dataframe
        """
        try: 
            self.X = self.df.drop(target_variable,axis=1)
            self.y = self.df[target_variable]
        except KeyError as e:
            print(f"Column not found : {e}")
            exit()
        return self.X, self.y

        

