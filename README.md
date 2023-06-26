
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

## Milestone 4

<img width="1112" alt="Screenshot 2023-06-26 at 15 52 45" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/12a76bac-d53f-46f8-b00f-1056cda68406">


In this milestone, a neural network was developed using PyTorch. The neural network architecture was designed specifically for the airbnb dataset used in this project. A custom dataset was created to handle the data appropriately. To do this I:

-Developed a neural network using PyTorch for the airbnb dataset
-Created a custom dataset to handle the airbnb data appropriately
-Implemented a linear regression model with 11 numerical features as inputs and price per night as the target label
-Utilized the ReLU activation function for introducing non-linearity in the model
-Incorporated dropout to prevent overfitting
-Conducted hyperparameter tuning to optimize the model's performance
-Trained multiple models with different hyperparameters using a training loop
-Calculated train and validation loss using mean squared error (MSE) as the loss function
-Assessed model performance based on validation root mean squared error (RMSE)
-Selected the model with the lowest validation RMSE as the best model



- The loss of each model was visualised USING a tensorboard:

<img width="736" alt="Screenshot 2023-06-26 at 15 49 33" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/802c6ed8-c9ef-41c3-916a-39ab37185b56">


- The loss for the best performing model can be seen below:

<img width="884" alt="Screenshot 2023-06-26 at 15 51 50" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/206b420a-c4c3-49e0-bd3d-21b66111466c">




## Milestone 5

In this milestone, we leveraged the existing neural network code structure to develop a multiclass classification model. The objective was to predict the number of bedrooms for each property in the dataset. By reusing the neural network framework, we were able to efficiently adapt it to the new classification task. The steps included:

- Implementing a multiclass classification neural network using the existing code structure from the previous milestone
- Predicting the number of bedrooms for each property using the neural network model
- Including the property category data as a feature in the model
- Utilizing One Hot Encoding to convert the categorical data into numerical format
- Expanding the feature set by adding 5 additional features after the One Hot Encoding process and
- Evaluating the model's performance using accuracy, precision, and recall metrics