# Country Compatability
Predictive Modeling with World Values Survey data. 

Differences in cultural values and beliefs can cause conflict between people. These conflicts can be as small as awkward moments and as large as multinational wars. The World Values Survey is an international research program devoted to the scientific study of social, political, economic, religious and cultural values of people in the word. Their main research is a survey conducted measuring beliefs and values throughout the world.

Using this data I hope to create statistical models to predict a person's country of residence. This model could be used as a tool for suggested compatability for travel, work, or living. 

<!-- ![](img/fredgraph.png) -->
# Table of Contents
1. [Data](#Data)
2. [Exploratory Analysis](#Exploratory-Data-Analysis)
3. [Conclusion](#Conclusion)

## Data
The data available are results from individual surveys of 70,867 people in 49 different countries. The number of results vary from country to country but is generally between 2,000 to 3,000 samples. Generally surveys are complete but most include missing values; with a survey that includes over 300 questions this isn't surprising. Surveyees can also decide to not answer a question resulting in many missing values. Questions are generally ranges of agreement or importance. Here are the first 6 questions:
For each of the following, indicate how important it is in your life. Would you say it is: Verity important, Rather important, Not very important, Not at all important:
1. Family
2. Friends
3. Leisure time
4. Politics
5. Work
6. Religion

The data set is numbered 1 - 4. 
### Data Selection
#### Data Leakage
Initial predictive models were created using sklearn RandomForestClassifier and GradientBoosingClassifier produced excellent accuracy when using most questions available. Further inspection of the questions showed data leakage from questions that were country specific. Question 223 asked their specific political party (unique to each country). And many questions were less direct forms of data leakage, but were still answered in response to specific governments or environments. When considering the similarity between people, I want to have a more objective view of the people's values that are independent of their environment. 

|  | Random Forest Classifier | Gradient Boosted Classifier |
| All questions included | 88% | 94% |
| Data leakage reduced | 69% | 76% |
| Personal Values Defined | 59% | 57% |


Questions like:  
How many Local authorities are involved in corruption?  
To what degree are you worried about a civil war?  
In the last 12 months how often have you or your family gone without enough food to eat?  

These questions would be answered differently if the person was placed in a different environment and have been removed for modeling. 

#### Missing Values
Because the nature of the survey allows for missing values, there was a significant amount of missing data. Of 70,867 surveys

## Data

