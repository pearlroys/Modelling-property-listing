
import joblib
import json
import torch
import datetime
import os
import torch.nn as nn
from torch.nn import Module

def save_neural_model(model, hyperparameters, metrics, folder):
    """This function saves a trained model, its associated hyperparameters and performance metrics to a specified folder.
    Parameters:
        model: Machine learning model name
        hyperparameters: A dictionary of the best hyperparameters used to train the model
        metrics: A dictionary of the performance metrics of the model on test and validation sets
        folder: A string specifying the directory path where the model and associated files will be saved."""
    
    # Create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Save the model
    if isinstance(model,torch.nn.Module):
        folder_path = folder + 'model.pt'
        torch.save(model.state_dict(), folder_path)

    else:
        pass
        # # Save the trained model
        # model_path = os.path.join(folder, "model.joblib")
        # joblib.dump(model, model_path)

    # Save the hyperparameters as a JSON file
    hyperparameters_path = os.path.join(folder, "hyperparameters.json")
    with open(hyperparameters_path, "w") as f:
        json.dump(hyperparameters, f)

    # Save the performance metrics as a JSON file
    metrics_path = os.path.join(folder, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f) 
            
    print ('Model is saved')


   
    
