
# Modelling-airbnbs-property-listing-dataset-
This project fulfills the data science component of the AiCore data career accelerator program. It aims to build a powerful and user-friendly framework for training, 

tuning, and evaluating models on various tasks handled by the Airbnb team. 


## Milestone 1
- Two python files were produced, tabular_data.py and prepare_image_data.py to clean and prepare both the tabular data and image data in this project using pandas
- The os context manager package and the PIL package from pillow was used to prepare the image data.


### Cleaning the tabular data
- Data with missing values were dropped form the df, text data was formatted and cleaned and the data.
- The data was returned as tuples (features and labels) to be used by a machine learning model.


<img width="828" alt="Screenshot 2023-06-26 at 16 12 53" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/6a8fbd39-c68e-4f9c-844a-8090a7b2a855">

## Milestone 2

This project focused on building a regression model to predict the price per night using various features. The dataset was divided into train, validation, and test sets (70%, 15%, and 15% respectively).

Multiple regression algorithms were employed, including Stochastic Gradient Descent Regressor, Random Forest Regressor, Decision Tree Regressor, and Gradient Boosting Regressor. Each algorithm utilized different techniques to predict the price per night.

These models were trained, evaluated, and compared based on their performance in predicting the price per night accurately.

<img width="836" alt="Screenshot 2023-06-26 at 16 08 34" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/49471656-2a2a-4b02-b258-ecb43069d06a">


# Finetuning of model parameters

In addition, hyperparameter tuning was performed for each model using grid search to find the optimal hyperparameters. The evaluation metrics of each model were calculated and saved in the repository for further analysis.

Finally, the evaluation metrics were analyzed to identify the model with the highest accuracy. This model would be considered the best performer among the regression models tested.

<img width="1060" alt="Screenshot 2023-06-26 at 16 09 09" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/602f7a28-824d-4b91-8634-de3336fef24a">


## Milestone 3 
A classification model was developed to predict the property category. Various classification algorithms, including Logistic Regression, Decision Tree, Gradient Boosting Classifier, and Random Forest Classifier, were trained and evaluated.

To build this module, several functions from the linear regression model were adapted. The main modifications involved changing the error measure of the model and the evaluation metrics used. The scoring measure for the grid search conducted in this case was f1_micro.

By implementing these changes, the classification model was tailored to suit the specific task of predicting property categories based on the given features.

<img width="1056" alt="Screenshot 2023-06-26 at 16 09 32" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/1f39c6ca-0c59-410b-aceb-c5fe69de39a3">

## Milestone 4


<img width="1112" alt="Screenshot 2023-06-26 at 16 09 59" src="https://github.com/pearlroys/modelling-airbnbs-property-listing-dataset-/assets/103274172/745f8f16-0164-45bb-a685-be1c6c637715">



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

In this milestone, I leveraged the existing neural network code structure to develop a multiclass classification model. The objective was to predict the number of bedrooms for each property in the dataset. By reusing the neural network framework, I was  able to efficiently adapt it to the new classification task. The steps included:

- Implementing a multiclass classification neural network using the existing code structure from the previous milestone
- Predicting the number of bedrooms for each property using the neural network model
- Including the property category data as a feature in the model
- Utilizing One Hot Encoding to convert the categorical data into numerical format
- Expanding the feature set by adding 5 additional features after the One Hot Encoding process and
- Evaluating the model's performance using accuracy, precision, and recall metrics