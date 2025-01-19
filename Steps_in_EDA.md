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
2.delete columns with fewer unique values. (if most of the values in a column is repeated , then it would lead to inaccuracy , right?)
3.delete duplicate rows

project steps:
1.EDA
2.data processing test
3.Feature Engineering

EDA:
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

		5 pre requesties knowledge - remove outliers techniques:
			two techniques:
			-> trimming
				just remove ouliers.
			-> capping
				set the ouliers as maximum allowed value or minimum allowedvalue.
				like :
					if lower value (value that is 3 standard deviation from mean) is 4 . then if there 2 in data set . then we set that 2 as 4.therefore outliers dealed.
		5.1 check for gaussian columns(which follows guassian dirstribution (normal distribution))

		5.2 check for outliers:
		<<-- DIFFERENT DISTRIBUTION DIFFERENT METHODS OF OUTLIER DETECTION-->>
		########research about different distributions.
		if gaussian ,
			use z-score for outlier detection
			( A Z-score measures how many standard deviations a data point is from the mean, helping identify outliers in a dataset. )
			if data point is more than 3 standard deviation from mean , then its oulier.

			[now removed outliers in gaussian distribution ] - move on to other distributions columns in our dataset to remove outliers in those

		if not gaussian,
			use box-plot for outlier detection
				if not gaussian , it may be skewed distribution, so we check for that:
				to identify skewed :
					1> check whether if it is categorical data (we dont take outlier detection of a column of categorical data,(each column in categorical column doesnt make sense, it makes sense when combine - fyz))
						so remove datas that is below 10 varieteies (remove caegorical data)
					2> Identify skewed columns 
					3> draw Box plot
					4> trim data acording to this :
						4.1> take iqr range
						4.2> upper_limit = 75th_percentile + 1.5 * IQR
						4.3> lower_limit = 25th_percentile - 1.5 * IQR
						4.4> trim data that occurs outside the limits between upper limit and lower limit.
						
	6. check corelation among columns
		like removing all columns which corelation with other columns in more than 80 percetage.

		<[ RESEARCH ON CO-RELATION OF CATEGORICAL DATA ]>
		<[ RESEARCH ON WHICH ARE THE COLUMN WHICH ARE SIGNIFICANT ENOUGH FOR MAKING A MODEL BETTER ]>
		? : if p avalue is greater than threshold , that is an significant variable. those are selected as significant variables in a dataset , how????????, whats teh relation btwn them?
		deal with constant columns if there is constant columns in significatn columns.
		--> i dont understand anything on "regression_model.py" last part. 

	

###############<<<<<<<EDA COMPLETED>>>>>>>#####################

		

	































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


