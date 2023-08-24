import lightgbm as lgb
import shap
import pandas as pd
import numpy as np

# Assuming X_train, y_train, categorical_cols are defined
model = lgb.LGBMClassifier(objective='multiclass', num_class=3, categorical_feature=categorical_cols)
model.fit(X_train, y_train)

# Choose a specific instance for which you want to explain the prediction
sample_idx = 0  # Choose the index of the sample you want to analyze
sample = X_test.iloc[sample_idx]

# Convert categorical features to numerical format
sample_numeric = sample.copy()
for col in categorical_cols:
    sample_numeric[col] = categorical_cols[col].transform([sample[col]])[0]

# Predict for the instance
predicted_class = float(model.predict(sample_numeric.values.reshape(1, -1))[0])

# Calculate SHAP values for all features
explainer = shap.TreeExplainer(model)
shap_values_all = explainer.shap_values(X_test)

# Select only the "worker" related features
worker_feature_names = ['worker', 'worker_duration', 'worker_skill', 'worker_switch']
worker_feature_indices = [X_test.columns.get_loc(col) for col in worker_feature_names]

# Select SHAP values for "worker" related features
shap_values_worker = shap_values_all[predicted_class][:, worker_feature_indices]

# Create a DataFrame from SHAP values
shap_values_fl = pd.DataFrame(shap_values_worker, columns=worker_feature_names)

# Select the instance's data and SHAP values for "worker" related features
sample_worker_features = sample[worker_feature_names].values
shap_values_sample = shap_values_fl.loc[sample_idx].values

# Visualize SHAP values using force plot for the chosen instance and features
shap.initjs()
shap.force_plot(explainer.expected_value[predicted_class], shap_values_sample, sample_worker_features, feature_names=worker_feature_names)
