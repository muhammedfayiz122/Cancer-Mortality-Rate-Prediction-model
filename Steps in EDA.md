Steps in EDA:
1. analyze missing values
	df.isnull().sum()
2. further  analysis of data
	df.info()
	df.describe()
3. Analyze each variables / features 
	eg. histogram
	plt.hist()
	
4.Eliminate outliers
	box plots


steps in Data Processing:
1.data ingestion
2.delete columns with fewer unique values. (if most of the values in a column is repeated , then it would lead to inaccuracy , right? )
3.delete duplicate rows

project steps:
1.EDA
2.data processing test
3.Feature Engineering
	1 : deals with cells like (143,234]
	this cell cant be directly fed into model creation. we can only give numbers to it.

	2 : deals with feature splitting and deconstruction
	if there like a cell [kerala , india] then both will be stored in different columns 	

	3 : deals with hot encoding
	if there is string or object columns , convert to number

	def one_hot_encoding(X):
   	    # select categorical columns
    	    categorical_columns = X.select_dtypes(include=["object"]).columns
   	    # one hot encode categorical columns
    	    one_hot_encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
    	    one_hot_encoded = one_hot_encoder.fit_transform(X[categorical_columns])
    	    # convert the one hot encoded array to a dataframe
    	    one_hot_encoded = pd.DataFrame(
        	one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_columns)
    	    )
    	    # drop the categorical columns from the original dataframe
    	    X = X.drop(categorical_columns, axis=1)
    	    # concatenate the one hot encoded dataframe to the original dataframe
    	    X = pd.concat([X, one_hot_encoded], axis=1)
    	    return X

	4 : deal with missing value , and fill it
	if there is columns with more than 50% values are missing ,then it will be eliminated.
	there is more methods in dealing with missing values.

	5 : dealing with outliers
	box plot 

preprocessing steps:
	1. how individual variaables look like
	2. what is the distribution
	3. whata is the mean
	4. what is the stndrd deviation
	5. what is the corelation coefficiant
	6. what is its corelattion with target variable
	7. what is the outliers present
	etc

	1. histogram - to analyse dirstribution
	2. boxplot - to find outliers
	3. scatter plot to find relations

	































# Bar Chart of Top 10 Glass Types

def plot_top_glass_types(df):
    plt.figure(figsize=(12, 6))
    top_glasses = df['glass'].value_counts().nlargest(10)
    sns.barplot(x=top_glasses.index, y=top_glasses.values)
    plt.title('Top 10 Glass Types Used in Cocktails')
    plt.xlabel('Glass Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_top_glass_types(df)

1
lowercase_titles = df['title'].str.lower()

2
first_words = df['title'].str.split().str[0]
first_words

3
total_ingredients = df['ingredients'].str.len().sum()
ingredient_length_ratio = df['ingredients'].str.len() / total_ingredients
ingredient_length_ratio

5
recipe_length = df['ingredients'].str.len()

# Standardize the lengths by centering around the mean and scaling by the standard deviation
recipe_length_standardized = ( recipe_length - recipe_length.mean() ) / recipe_length.std()
recipe_length
recipe_length_standardized

#Pie Chart of Top 10 Garnishes

def plot_top_garnishes(df):
    plt.figure(figsize=(10, 10))
    top_garnishes = df['garnish'].value_counts().nlargest(10)
    plt.pie(top_garnishes.values, labels=top_garnishes.index, autopct='%1.1f%%', startangle=90)
    plt.title('Top 10 Garnishes Used in Cocktails')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

plot_top_garnishes(df)


6.
total_recipes = df['ingredients'].str.split().count()
glass_popularity_ratio = df['glass'].value_counts() 
glass_popularity_ratio

7.
garnish_counts = df['garnish'].value_counts()
total_garnishes = garnish_counts.sum()
garnish_effectiveness_index = garnish_counts * 100 / total_garnishes
garnish_effectiveness_index


