
# Modelling-airbnbs-property-listing-dataset-
This project fulfills the data science component of the AiCore data career accelerator program. It aims to build a powerful and user-friendly framework for training, 

tuning, and evaluating models on various tasks handled by the Airbnb team. 


## Milestone 1
- Two python files were produced, tabular_data.py and prepare_image_data.py to clean and prepare both the tabular data and image data in this project using pandas
- The os context manager package and the PIL package from pillow was used to prepare the image data.


### Cleaning the tabular data
- Data with missing values were dropped form the df, text data was formatted and cleaned and the data.
- The data was returned as tuples (features and labels) to be used by a machine learning model.

<img width="848" alt="Screenshot 2023-06-26 at 15 30 25" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/73abcc21-9c36-4f05-bf65-2940620e2ab2">

## Milestone 2

This project focused on building a regression model to predict the price per night using various features. The dataset was divided into train, validation, and test sets (70%, 15%, and 15% respectively).

Multiple regression algorithms were employed, including Stochastic Gradient Descent Regressor, Random Forest Regressor, Decision Tree Regressor, and Gradient Boosting Regressor. Each algorithm utilized different techniques to predict the price per night.

These models were trained, evaluated, and compared based on their performance in predicting the price per night accurately.

<img width="818" alt="Screenshot 2023-06-26 at 15 37 19" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/d55dc820-5ad0-4003-a996-bb7380f07284">

# finetuning

In addition, hyperparameter tuning was performed for each model using grid search to find the optimal hyperparameters. The evaluation metrics of each model were calculated and saved in the repository for further analysis.

Finally, the evaluation metrics were analyzed to identify the model with the highest accuracy. This model would be considered the best performer among the regression models tested.

<img width="1057" alt="Screenshot 2023-06-26 at 15 39 59" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/4364603d-79b2-42a2-a7d2-7ef630b13eb7">

## Milestone 3 
A classification model was developed to predict the property category. Various classification algorithms, including Logistic Regression, Decision Tree, Gradient Boosting Classifier, and Random Forest Classifier, were trained and evaluated.

To build this module, several functions from the linear regression model were adapted. The main modifications involved changing the error measure of the model and the evaluation metrics used. The scoring measure for the grid search conducted in this case was f1_micro.

By implementing these changes, the classification model was tailored to suit the specific task of predicting property categories based on the given features.

<img width="1106" alt="Screenshot 2023-06-26 at 15 41 56" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/a3126adc-20ad-4d49-8419-787d7c135c1a"> 
