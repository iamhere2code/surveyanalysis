#Import Statements
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("/Users/alishuf/Downloads/mock_survey_data.csv")

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
#plt.hist(Gender)
# Set the title of the graph
def analyzeAge(ageInfo):
    plt.boxplot(ageInfo)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Boxplot of Age in Survey')
    plt.show()  
    mean = ageInfo.mean()
    median = ageInfo.median()
    standard_deviation = ageInfo.std()
    print("The mean is ", mean)
    print("The median is ", median)
    return ("The standard deviation is ", standard_deviation)

def analyzeGender(col):
    unique_values = df[col].unique()
    counts = df[col].value_counts()
    plt.bar(unique_values, counts)
    plt.show()
    
def compareGrants(x, y):
    plt.scatter(x, y)
    plt.xlabel('% Success of Grants')
    plt.ylabel('# of Grants Applied Last Year')
    plt.title("Grants Success vs. Grants Applied")
    plt.show()
    result = df.groupby("Grant Success Rate")["Grants Applied Last Year"].sum()
    print(result)

def appUsability(app):
    unique_values = app.unique()
    counts = app.value_counts()
    plt.bar(unique_values, counts )
    plt.xlabel('Features')
    plt.ylabel('Counts')
    plt.title("Most Preferred App Features")
    plt.show()
    likelihood = df.groupby(["Preferred App Feature","Likelihood to Use App (1-5)"])
    print(likelihood.first())

def analyzeChallengesFeedback(challenges, feedback):
    most_common = challenges.value_counts()
    print("The most common challenges user faced were: ", most_common.head(3))
    unique_values = feedback.unique()
    print("Additional Feedback Given")
    for i in unique_values:
        print(i)
    #print("These are all the unique comments given", unique_values)
     

analyzeChallengesFeedback(Primary_Challenge, Additional_Comments)
    

#analyzeDemographics(Age)
#analyzeGender("Gender", Gender)
#appUsability(App_Feature)



#compareGrants(Grants_Success, Grants_Applied)




'''def check_nulls(df):
    thing =  df.isnull().any()
    print(thing)
    return thing
check_nulls(df)
bool_series = pd.isnull(df)
missing_values_count = bool_series.sum()
print(missing_values_count)
new_thing = pd.isnull(df["Grant Success Rate"])
if False in new_thing
    print("hii")'''

