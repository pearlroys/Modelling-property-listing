# Group by advisor skill and calculate counts of predicted and actual promoters
advisor_skills_grouped = final_df.groupby('advisor_skill').apply(lambda group: {
    'predicted_promoters': (group['predicted'] == 'promoter').sum(),
    'actual_promoters': (group['actual'] == 'promoter').sum()
}).reset_index()


advisor_skills_grouped['ratio_predicted_to_actual'] = (
    advisor_skills_grouped['predicted_promoters'] / advisor_skills_grouped['actual_promoters']
)

import matplotlib.pyplot as plt

# Plot the ratios for each advisor skill
plt.figure(figsize=(10, 6))
plt.bar(advisor_skills_grouped['advisor_skill'], advisor_skills_grouped['ratio_predicted_to_actual'])
plt.xlabel('Advisor Skill')
plt.ylabel('Ratio of Predicted Promoters to Actual Promoters')
plt.title('Impact of Advisor Skills on Predicted/Actual Promoters Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
