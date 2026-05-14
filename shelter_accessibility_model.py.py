#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from scipy.stats import spearmanr

# Setup for high-quality plots in Jupyter
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="whitegrid")


# In[5]:


# Load the master dataset
df = pd.read_csv("F:/All_Project/Khadija_apu/Survey_data/final_10.csv",  encoding="latin1")


# In[6]:


print(df.shape)


# In[7]:


df.head(5)


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[10]:


df.isnull().sum()


# In[11]:


df.duplicated()


# In[37]:


# 2. Helper function to find columns by keyword
def find_col(keyword):
    for col in df.columns:
        if keyword.lower() in col.lower():
            return col
    return None

col_income = find_col('Monthly Household Income')
col_safety = find_col('Women feel comfortable and safe')
col_access = find_col('Difficulty in accessing shelter')
col_mobility = find_col('mobility') 

# 3. Define Mappings
income_map = {'<5,000': 1, '5,000–10,000': 2, '10,000–15,000': 3, '15,000–20,000': 4, '>20,000': 5}
likert_map = {'Strongly agree': 5, 'Agree': 4, 'Neutral': 3, 'Disagree': 2, 'Strongly disagree': 1}
difficulty_map = {'Very easy': 1, 'Easy': 2, 'Moderate': 3, 'Difficult': 4, 'Very difficult': 5}

# 4. Prepare Correlation Dataframe
corr_df = pd.DataFrame()
corr_df['Age'] = df['Age']
corr_df['Household Size'] = df['Household Size']

if col_income: corr_df['Income Level'] = df[col_income].map(income_map)
if col_safety: corr_df['Safety Perception'] = df[col_safety].map(likert_map)
if col_access: corr_df['Access Difficulty'] = df[col_access].map(difficulty_map)
if col_mobility: corr_df['Mobility Restriction'] = df[col_mobility].map(likert_map)

# 5. Plotting
plt.figure(figsize=(12, 10))
correlation_matrix = corr_df.corr()

# Create heatmap with line spacing for a cleaner look
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', center=0, fmt=".2f", linewidths=1.5)

# --- PROFESSIONAL ROTATION ---
# Rotate X-axis labels 45 degrees (ha='right' aligns the text to the tick)
plt.xticks(rotation=45, ha='right', fontsize=11, weight='bold')

# Rotate Y-axis labels 45 degrees (va='center' keeps them aligned)
plt.yticks(rotation=45, fontsize=11, weight='bold')

plt.title('Correlation Matrix of Gender-Based Barrier Factors', fontsize=16, weight='bold', pad=30)
plt.tight_layout()

# Save for high-quality report inclusion
plt.savefig('correlation_heatmap_45_both_axes.png', dpi=1200)
plt.show()


# **Demographic Profiling**

# In[38]:


# Create a figure with two subplots for Age and Gender distribution
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Age Distribution
sns.histplot(df['Age'], bins=10, kde=True, color='teal', ax=ax[0])
ax[0].set_title('Age Distribution of Respondents')

# Plot 2: Gender Distribution
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], ax=ax[1])
ax[1].set_title('Gender Distribution (Female vs Male)')
plt.savefig('age_distribution.png', dpi = 1200)

plt.tight_layout()
plt.show()


# **Gender-Based Perceptions of Safety**

# In[39]:


# Cross-tabulate Safety Perception by Gender
safety_cross = pd.crosstab(df['Gender'], df['Women feel comfortable and safe in cyclone shelters'], normalize='index') * 100

# Visualize as a Stacked Bar Chart
safety_cross.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#e74c3c','#2ecc71','#f1c40f'])
plt.title('Do Respondents Feel Women are Safe in Shelters? (by Gender)')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Response', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('is_women_feel_safe.png', dpi = 1200)
plt.show()


# **Statistical Significance**

# In[15]:


# Testing if there is a significant difference in reporting security issues between Men and Women
contingency_table = pd.crosstab(df['Gender'], df['Are there any security issues in cyclone shelters?'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("--- Inferential Statistics ---")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-Value: {p:.4f}")

if p < 0.05:
    print("Result: Significant difference between genders regarding security concerns.")
else:
    print("Result: No significant difference; security is a universal concern across both genders.")


# **Analyzing Multi-Response Barriers for Women**

# In[16]:


# Function to extract and count unique items in multi-response columns
def get_counts(series):
    return series.str.split(',').explode().str.strip().value_counts()

# Filter data for Women to identify gender-specific hurdles
female_data = df[df['Gender'] == 'Female']

# Get counts for the three main research questions
barriers = get_counts(female_data['What are the main barriers to reaching cyclone shelters?'])
avoidance_reasons = get_counts(female_data['In your opinion, why do women avoid cyclone shelters?'])
improvements = get_counts(female_data['Suggested Improvements'])

print("Top 5 Reasons Women Avoid Shelters:\n", avoidance_reasons.head(5))


# **Visualization of Policy-Relevant Findings**

# In[40]:


# 2. Extract multi-response counts for avoidance reasons
# (Assuming 'avoidance_reasons' was calculated in a previous cell)
avoidance_reasons = df['In your opinion, why do women avoid cyclone shelters?'].str.split(',').explode().str.strip().value_counts()

# 3. Plotting
plt.figure(figsize=(12, 10)) # Increased height slightly to accommodate rotated labels
sns.barplot(x=avoidance_reasons.values, y=avoidance_reasons.index, palette='magma')

# --- FIXING THE ROTATION ---
# ha='right' ensures the text aligns correctly with the bar after rotation
plt.yticks(rotation=45, ha='right', fontsize=10, weight='bold')

plt.title('Gender-Based Barriers: Why Women Avoid Cyclone Shelters', fontsize=15, weight='bold', pad=20)
plt.xlabel('Frequency of Mention', fontsize=12)
plt.ylabel('Barrier Identified', fontsize=12)

# --- FIXING THE "CUT OFF" PROBLEM ---
# Option 1: adjust layout within Jupyter
plt.tight_layout()

# Option 2: Save with bbox_inches='tight' ensures nothing is cut in the downloaded file
plt.savefig('gender_based_barriers_fixed.png', dpi=1200, bbox_inches='tight')

plt.show()


# **Decision-Making Agency Analysis**

# In[42]:


# Examining who makes the evacuation decision
decision_makers = df.groupby('Gender')['Who usually makes the decision to evacuate to cyclone shelters?'].value_counts(normalize=True).unstack() * 100

decision_makers.plot(kind='barh', stacked=True, figsize=(12, 6), colormap='Pastel2')
plt.title('Agency Analysis: Evacuation Decision-Makers by Gender')
plt.xlabel('Percentage contribution (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('agency_analysis.png', dpi = 1200, bbox_inches = 'tight')
plt.show()


# **Professional Analysis of Income vs. Access Difficulty**

# In[43]:


# 2. Define Ordinal Mappings (Very important for correlation)
income_order = ['<5,000', '5,000–10,000', '10,000–20,000', '>20,000']
difficulty_order = ['Very easy', 'Easy', 'Moderate', 'Difficult', 'Very difficult']

# Mapping to numbers for calculation
income_map = {val: i+1 for i, val in enumerate(income_order)}
diff_map = {val: i+1 for i, val in enumerate(difficulty_order)}

# Create numerical columns for analysis
df['Income_Rank'] = df['Monthly Household Income (BDT)'].map(income_map)
df['Difficulty_Rank'] = df['Difficulty in accessing shelter during cyclone'].map(diff_map)

# 3. Calculate Spearman Correlation (Best for Ordinal Data)
corr_coeff, p_value = spearmanr(df['Income_Rank'], df['Difficulty_Rank'])

# 4. Create the Visualization
plt.figure(figsize=(12, 7))

# A. Boxplot to show distribution
sns.boxplot(data=df, x='Monthly Household Income (BDT)', y='Difficulty_Rank', 
            order=income_order, palette='Blues_r', showfliers=False)

# B. Swarmplot (Jitter) to show every individual respondent
sns.stripplot(data=df, x='Monthly Household Income (BDT)', y='Difficulty_Rank', 
              order=income_order, color='black', alpha=0.3, size=5)

# C. Add a trend line (Regression on the means)
# We calculate the average difficulty per income group for the line
means = df.groupby('Monthly Household Income (BDT)')['Difficulty_Rank'].mean().reindex(income_order)
plt.plot(range(len(income_order)), means.values, marker='o', color='red', linestyle='--', label='Trend Line (Mean)')

# 5. Formatting for Professional Result
plt.title(f'Income Level vs. Shelter Access Difficulty\n(Spearman Corr: {corr_coeff:.2f}, p-value: {p_value:.4f})', fontsize=14)
plt.xlabel('Monthly Household Income (BDT)', fontsize=12)
plt.ylabel('Access Difficulty Rank (1=Easy, 5=Very Diff)', fontsize=12)
plt.yticks(ticks=[1, 2, 3, 4, 5], labels=difficulty_order)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('income_vs_difficulty_professional.png', dpi = 1200, bbox_inches = 'tight')
plt.show()

print(f"Key Finding: As income increases, the difficulty of accessing shelters decreases (Correlation: {corr_coeff:.2f}).")


# In[20]:


# 2. Define the proper order for the Axis
income_order = ['<5,000', '5,000–10,000', '10,000–20,000', '>20,000']
difficulty_order = ['Very easy', 'Easy', 'Moderate', 'Difficult', 'Very difficult']

# 3. Create a Percentage Crosstab
# This shows: "Out of the people in this income group, what % feel this level of difficulty?"
analysis_table = pd.crosstab(df['Monthly Household Income (BDT)'], 
                             df['Difficulty in accessing shelter during cyclone'], 
                             normalize='index') * 100

# Reorder the table so it flows logically from low to high
analysis_table = analysis_table.reindex(index=income_order, columns=difficulty_order)

# 4. Plot the Simplified Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(analysis_table, annot=True, cmap='YlOrRd', fmt=".1f", cbar_kws={'label': 'Percentage of Respondents (%)'})

plt.title('How Income Affects Shelter Access Difficulty (%)', fontsize=14, pad=20)
plt.xlabel('Access Difficulty Level', fontsize=12)
plt.ylabel('Monthly Household Income', fontsize=12)

plt.tight_layout()
plt.savefig('simplified_income_barrier.png')
plt.show()


# **Advanced Policy-Insight Analysis**

# In[49]:


col = 'Who usually makes the decision to evacuate to cyclone shelters?'
data = df[col].value_counts()

plt.figure(figsize=(10, 7))
plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette('Set3'), explode=[0.05]*len(data))

# Making it a Donut
center_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(center_circle)

plt.title('Distribution of Decision-Making Authority', fontsize=14, weight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('distribution of decision making authority.png', dpi = 1200, bbox_inches = 'tight')
plt.show()


# In[48]:


# Column name
livelihood_col = 'Livelihood factors (e.g., livestock, income source) affect your decision to go to shelter'
livelihood_counts = df[livelihood_col].value_counts()

# Professional Pie Chart
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:len(livelihood_counts)]
explode = [0.05] * len(livelihood_counts) # Slight separation for professional look

plt.pie(livelihood_counts, labels=livelihood_counts.index, autopct='%1.1f%%', 
        startangle=140, colors=colors, explode=explode)

plt.title('Impact of Livelihood Factors (Assets) on Evacuation Decisions', fontsize=14, weight='bold')
plt.axis('equal')
plt.savefig('livelihood_factors.png', dpi = 1200, bbox_inches = 'tight')
plt.show()


# In[46]:


# Extract respondents reporting 'Poor sanitation'
avoidance_col = 'In your opinion, why do women avoid cyclone shelters?'
sanitation_reporters = df[df[avoidance_col].str.contains('Poor sanitation', na=False)]

# Visualizing Age and Gender distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=sanitation_reporters, x='Gender', y='Age', palette='Set2')
# Adding individual data points (jitter) for extra detail
sns.stripplot(data=sanitation_reporters, x='Gender', y='Age', color='black', alpha=0.3)

plt.title('Age and Gender Distribution of those Reporting "Poor Sanitation" as a Barrier', fontsize=13, weight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Age of Respondent', fontsize=12)
plt.savefig('age_gender_distribution.png', dpi = 1200, bbox_inches = 'tight')
plt.show()


# In[47]:


# Create crosstab of Union and Access Difficulty
access_union_cross = pd.crosstab(df['Study area (Union)'], 
                                 df['Difficulty in accessing shelter during cyclone'], 
                                 normalize='index') * 100

# Define the logical order for difficulty progression
diff_order = ['Very easy', 'Easy', 'Moderate', 'Difficult', 'Very difficult']
access_union_cross = access_union_cross.reindex(columns=[c for c in diff_order if c in access_union_cross.columns])

# Plotting Stacked Bar Chart
access_union_cross.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='RdYlGn_r')

plt.title('Comparison of Shelter Access Difficulty Across Unions', fontsize=15, weight='bold')
plt.ylabel('Percentage of Respondents (%)', fontsize=12)
plt.xlabel('Union', fontsize=12)
plt.legend(title='Difficulty Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('shelter access difficulty.png', dpi = 1200, bbox_inches = 'tight')
plt.show()


# In[ ]:




