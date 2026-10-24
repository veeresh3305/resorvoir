**Reservoir Water Safety Classification Using Machine Learning**

**Overview**

The **Reservoir Water Safety Classification System** is a machine learning project that analyzes reservoir operating parameters and predicts the reservoir's dynamic status using a Random Forest Classifier.

The project uses water-level measurements and water-flow rates to identify patterns associated with different reservoir status categories. It also performs exploratory data analysis, visualizes feature correlations, and evaluates the model using standard classification metrics.

**Objectives**

- Analyze reservoir water-level and water-flow data.
- Clean and prepare the dataset for machine learning.
- Visualize the distribution of reservoir status categories.
- Study correlations between reservoir operating parameters.
- Train a Random Forest classification model.
- Evaluate model performance using accuracy, a classification report, and a confusion matrix.

**Features**

- **Data preprocessing:** Loads an Excel dataset and removes rows containing missing values.
- **Data visualization:** Displays the distribution of reservoir status categories.
- **Correlation analysis:** Generates a heatmap showing relationships between selected numerical parameters.
- **Machine learning:** Uses a Random Forest Classifier with 300 estimators and a maximum tree depth of 12.
- **Model evaluation:** Reports accuracy, precision, recall, F1-score, and a confusion matrix.

**Technologies Used**

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Microsoft Excel

**File Descriptions**

- reservoir.py — Contains the Python code for data preprocessing, visualization, model training, prediction, and evaluation.
- dataset.xlsx — Contains the reservoir dataset used by the machine learning model.
- Project PPT.pptx — Contains the project presentation.
- README.md — Provides project documentation and setup instructions.

**Dataset Description**

The project uses an Excel dataset named dataset.xlsx.

The following columns are used by the Python script:

| **Feature**            | **Description**                                               |
| ---------------------- | ------------------------------------------------------------- |
| upstream_water_level   | Water-level measurement upstream of the reservoir structure   |
| downstream_water_level | Water-level measurement downstream of the reservoir structure |
| inflow_rate            | Rate of water entering the reservoir                          |
| outflow_rate           | Rate of water leaving the reservoir                           |
| dynamic_storage        | Reservoir storage measurement used in correlation analysis    |
| status_dynamic         | Target category predicted by the classification model         |

The model uses the four water-level and flow-rate features to predict status_dynamic.

**Machine Learning Algorithm**

**Random Forest Classifier**

The project uses a Random Forest Classifier, an ensemble learning algorithm that combines predictions from multiple decision trees to classify observations.

The model is configured with:

- Number of estimators: 300
- Maximum tree depth: 12
- Random state: 42
- Class weights: Balanced

**Model Workflow**

1. Load the dataset from the Excel file.
2. Remove rows containing missing values.
3. Visualize the distribution of target categories.
4. Generate a correlation heatmap for selected numerical features.
5. Separate the input features and target variable.
6. Split the dataset into training and testing sets using an 80:20 ratio.
7. Train the Random Forest Classifier on the training data.
8. Generate predictions for the test data.
9. Evaluate the predictions using classification metrics and a confusion matrix.

The train-test split uses stratification to help preserve class proportions in both sets.

**Model Evaluation**

The model is evaluated using the following metrics:

- **Accuracy:** Measures the proportion of test observations classified correctly.
- **Precision:** Measures how many predictions for a particular class are correct.
- **Recall:** Measures how many actual observations of a particular class are identified correctly.
- **F1-score:** Combines precision and recall into a single metric.
- **Confusion matrix:** Shows the number of correct and incorrect predictions for each class.

The actual performance depends on the dataset and should be determined by running the script. No fixed accuracy value is assumed in this documentation.

**Applications**

Potential applications of reservoir status classification include:

- Supporting analysis of reservoir operating conditions.
- Identifying patterns in historical reservoir measurements.
- Exploring relationships between water levels, inflow, and outflow.
- Supporting research into data-driven reservoir monitoring.

The current implementation is an offline classification experiment. It does not directly connect to live sensors, automatically issue alerts, or establish real-world dam safety.

**Limitations**

- The model's performance depends on the quality and representativeness of the dataset.
- Rows containing missing values are removed, which may reduce the available training data.
- The current implementation does not save the trained model for later use.
- The script does not provide a web interface or real-time predictions.
- Predictions should not be treated as certified engineering or emergency safety assessments.

**Future Enhancements**

- Add more reservoir parameters and historical measurements.
- Compare Random Forest with other classification algorithms.
- Perform hyperparameter tuning and cross-validation.
- Add feature importance analysis.
- Save the trained model for reuse.
- Develop a dashboard for interactive predictions and visualizations.
- Integrate validated real-time sensor data.
- Add monitoring and alerting features after appropriate engineering validation.

**Conclusion**

This project demonstrates how machine learning can be applied to reservoir data to classify operating status categories. By combining data preprocessing, visualization, Random Forest classification, and model evaluation, it provides a foundation for further research into data-driven reservoir monitoring.