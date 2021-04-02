# Country Compatability
Predictive Modeling with World Values Survey data. 

Differences in cultural values and beliefs can cause conflict between people. These conflicts can be as small as awkward moments and as large as multinational wars. The World Values Survey is an international research program devoted to the scientific study of social, political, economic, religious and cultural values of people in the word. Their main research is a survey conducted measuring beliefs and values throughout the world.

Using this data I hope to create statistical models to predict a person's country of residence. This model could be used as a tool for suggested compatability for travel, work, or living. 

# Table of Contents
1. [Data](#Data)
2. [Modeling](#Modeling)
3. [Results](#Results)
4. [Citations](#Citations)

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

**Model Accuracy for Questions selected**
|                       | Random Forest Classifier | Gradient Boosted Classifier |
|-----------------------:|-------------------------:|----------------------------:|
| All questions included | 88%                      |  94%                        |
| Data leakage reduced   | 69%                      | 76%                         |     
| Personal Values Defined| 59%                      | 57%                         |


Questions like:  
How many Local authorities are involved in corruption?  
To what degree are you worried about a civil war?  
In the last 12 months how often have you or your family gone without enough food to eat?  

These questions would be answered differently if the person was placed in a different environment and have been removed for modeling. 

#### Missing Values
Because the nature of the survey allows for missing values, there was a significant amount of missing data. Of the total number of questions for all surveys only 1.5% of answers were missing, but roughly 50% of surveys included atleast one missing data point. Assigning a value of 0 led to better predictive accuracy than using the mean value. 

## Predictive Modeling
### Random Forest
The accuracy of a predictive model using default parameters of SKLearn's RandomForestClassifier gave an accuracy of 58.8%. A grid search of random forest models with performance scoring based on accuracy led to a model that gave 62.4% accuracy on holdout data. 

Below are the feature importances for the random forest model. 
![](img/rf-feature-importance.png)
These questions relate mostly to government. 

### Gradient Boosting
SKLearn's GradientBoostingClassifier gave an accuracy of 67.1%. A grid search of random forest models with performance scoring based on accuracy led to a model that gave % accuracy on holdout data. 
Below are feature importance for the gradient boosted model. 
![](img/gb-feature-importance.png)
These questions are more related to social values. 

## Results
Though this model is predicting the country that the surveyee lives in, its application is better served to show the countries that the person is similar to. The current best model has a 67.1% accuracy for predicting the specific country, but has a 91.1% chance that their resident country is in the top 5 of predicted countries. This model will show similarity to the residents of the country top predicted country and in a certain sense these shared values may indicicate a higher level of compatability. 

Example output for survey results:  
Your 5 most compatible countries are: 
1. China 
2. Macao SAR PRC 
3. Thailand 
4. Philippines 
5. Vietnam 

## Citations
Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano J., M. Lagos, P. Norris, E. Ponarin & B. Puranen et al. (eds.). 2020. World Values Survey: Round Seven – Country-Pooled Datafile. Madrid, Spain & Vienna, Austria: JD Systems Institute & WVSA Secretariat. doi.org/10.14281/18241.1

