# Import Statements
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Importing Dataset
df = pd.read_csv("/Users/alishuf/Downloads/mock_survey_data.csv")

def check_nulls(df):
    thing =  df.isnull().any()
    print(thing)
    return thing
check_nulls(df)
bool_series = pd.isnull(df)
missing_values_count = bool_series.sum()
print(missing_values_count)
new_thing = pd.isnull(df["Grant Success Rate"])
if False in new_thing:
    print("hii")

# Turning column into variables for ease of use later
Age = df["Age"]
Gender = df["Gender"]
Years_In_Research = df["Years in Research"]
Discipline = df["Discipline"]
Grants_Applied = df["Grants Applied Last Year"]
Grants_Success = df["Grant Success Rate"]
App_Feature = df["Preferred App Feature"]
Likelihood = df["Likelihood to Use App (1-5)"]
Primary_Challenge = df["Primary Challenge"]
Additional_Comments = df["Additional Comments"]

# Analyzing Age
def analyzeAge(ageInfo):
    # Use age info --> turn into boxplot
    plt.boxplot(ageInfo)
    # Set labels and title
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Boxplot of Age in Survey')
    plt.show()  
    # Compute mean, median and standard deviation
    mean = ageInfo.mean()
    median = ageInfo.median()
    standard_deviation = ageInfo.std()
    # Print our info
    print("The mean is ", mean)
    print("The median is ", median)
    return ("The standard deviation is ", standard_deviation)

# Analyzing Gender
def analyzeGender(genderInfo):
    # Seperate unique values
    unique_values = genderInfo.unique()
    # How many times each valyue shows up
    counts = genderInfo.value_counts()
    # Plot the bar plot that counts instances of unique values
    plt.bar(unique_values, counts)
    plt.show()
    
def compareGrants(x, y):
    # Scatter plot that compares two values
    plt.scatter(x, y)
    # Axis label and graph titles
    plt.xlabel('% Success of Grants')
    plt.ylabel('# of Grants Applied Last Year')
    plt.title("Grants Success vs. Grants Applied")
    plt.show()
    # Print relationship between the Grant Success Rate and Grants applied last year
    result = df.groupby("Grant Success Rate")["Grants Applied Last Year"].sum()
    print(result)

# Function to determine best features
def appUsability(app):
    # Find unique features
    unique_values = app.unique()
    # Count instances of feature
    counts = app.value_counts()
    # Labels and title
    plt.bar(unique_values, counts )
    plt.xlabel('Features')
    plt.ylabel('Counts')
    plt.title("Most Preferred App Features")
    plt.show()
    # Use groupby() to see relationship between preferred app feature and likelihood to use app
    likelihood = df.groupby(["Preferred App Feature","Likelihood to Use App (1-5)"])
    print(likelihood.first())

# Function to analyze challenges and feedback
def analyzeChallengesFeedback(challenges, feedback):
    # Find the most common challenges
    most_common = challenges.value_counts()
    print("The most common challenges user faced were: ", most_common.head(3))
    # Find all unique instances of additional comments
    unique_values = feedback.unique()
    print("Additional Feedback Given")
    for i in unique_values:
        print(i)
    #print("These are all the unique comments given", unique_values)
     

analyzeChallengesFeedback(Primary_Challenge, Additional_Comments)
    
# Run functions
#analyzeDemographics(Age)
#analyzeGender("Gender", Gender)
#appUsability(App_Feature)



#compareGrants(Grants_Success, Grants_Applied)

# Questions
    #1. Null stuff --> how to replace nulls
    #2. How to make multiple graphs appear
    #3. Averaging the likelihood