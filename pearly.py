coeff correl type =
VAR CorrelationValue = [coeff corr]
VAR CorrelationType =
    SWITCH (
        TRUE (),
        CorrelationValue = -1, "Perfect negative correlation",
        CorrelationValue > -1 && CorrelationValue <= -0.8, "Very strong negative correlation",
        CorrelationValue > -0.8 && CorrelationValue <= -0.6, "Strong negative correlation",
        CorrelationValue > -0.6 && CorrelationValue <= -0.4, "Moderate negative correlation",
        CorrelationValue > -0.4 && CorrelationValue <= -0.2, "Weak negative correlation",
        CorrelationValue > -0.2 && CorrelationValue < 0, "Very weak negative correlation",
        CorrelationValue = 0, "No correlation",
        CorrelationValue > 0 && CorrelationValue < 0.2, "Very weak positive correlation",
        CorrelationValue >= 0.2 && CorrelationValue < 0.4, "Weak positive correlation",
        CorrelationValue >= 0.4 && CorrelationValue < 0.6, "Moderate positive correlation",
        CorrelationValue >= 0.6 && CorrelationValue < 0.8, "Strong positive correlation",
        CorrelationValue >= 0.8 && CorrelationValue < 1, "Very strong positive correlation",
        CorrelationValue = 1, "Perfect positive correlation",
        "Unknown"
    )
RETURN
    CorrelationValue & " (" & CorrelationType & ")"
coeff correl type =
VAR CorrelationValue = ROUND([coeff corr], 2)
VAR CorrelationType =
    SWITCH (
        TRUE (),
        CorrelationValue = -1, "Perfect negative correlation",
        CorrelationValue > -1 && CorrelationValue <= -0.8, "Very strong negative correlation",
        CorrelationValue > -0.8 && CorrelationValue <= -0.6, "Strong negative correlation",
        CorrelationValue > -0.6 && CorrelationValue <= -0.4, "Moderate negative correlation",
        CorrelationValue > -0.4 && CorrelationValue <= -0.2, "Weak negative correlation",
        CorrelationValue > -0.2 && CorrelationValue < 0, "Very weak negative correlation",
        CorrelationValue = 0, "No correlation",
        CorrelationValue > 0 && CorrelationValue < 0.2, "Very weak positive correlation",
        CorrelationValue >= 0.2 && CorrelationValue < 0.4, "Weak positive correlation",
        CorrelationValue >= 0.4 && CorrelationValue < 0.6, "Moderate positive correlation",
        CorrelationValue >= 0.6 && CorrelationValue < 0.8, "Strong positive correlation",
        CorrelationValue >= 0.8 && CorrelationValue < 1, "Very strong positive correlation",
        CorrelationValue = 1, "Perfect positive correlation",
        "Unknown"
    )
RETURN
    CorrelationValue & " (" & CorrelationType & ")"
