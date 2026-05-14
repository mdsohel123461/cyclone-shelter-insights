# Gender-Based Analysis of Cyclone Shelter Accessibility

### Brief One Line Summary
A data-driven investigation into the socio-economic and gender-specific barriers influencing evacuation behavior in coastal Bangladesh.

---

## Table of Contents
* [Overview](#overview)
* [Problem Statement](#problem-statement)
* [Dataset](#dataset)
* [Tools and Technologies](#tools-and-technologies)
* [Methods](#methods)
* [Key Insights](#key-insights)
* [Dashboard/Model/Output](#dashboardmodeloutput)
* [Results & Conclusion](#results--conclusion)
* [Future Work](#future-work)
* [Author & Contact](#author--contact)

---

## Overview
This research examines the multifaceted challenges faced by coastal communities during cyclone events, specifically focusing on how gendered accessibility to emergency shelters impacts survival.

## Problem Statement
Despite infrastructure availability, female participation in evacuation remains low. This study identifies the specific socio-economic deterrents, such as sanitation and privacy, that prevent women from seeking safety.

## Dataset
The project utilizes a primary dataset consisting of household surveys from coastal Unions, including demographic profiles and qualitative responses regarding shelter barriers.

## Tools and Technologies
* **Language:** Python
* **Environment:** Jupyter Notebook
* **Libraries:** Pandas, Matplotlib, Seaborn, Scipy

## Methods
* **Data Cleaning:** Processing survey responses and handling missing values.
* **Descriptive Analysis:** Visualizing age and gender distributions.
* **Statistical Correlation:** Using Spearman correlation to link income levels with access difficulty.
* **Thematic Analysis:** Identifying primary barriers through frequency of mention.

## Key Insights

### 1. Demographic Distribution
The study captured a significant female perspective (56.2%), ensuring gender-specific challenges are accurately represented.

![Age Distribution](output-analysis-result/age_distribution.png)
### 2. Primary Deterrents to Evacuation
Overcrowding, lack of privacy, and poor sanitation were identified as the leading reasons women avoid shelters.

![Gender Barriers](Analysis_result/gender_based_barriers_fixed.png)

### 3. Safety vs. Comfort
While most respondents feel shelters are physically safe, the qualitative environment—specifically sanitation—creates a barrier for women across all age groups.

![Safety Perception](Analysis_result/is_women_feel_safe.png)
![Sanitation Barriers](Analysis_result/age_gender_distribution.png)

## Dashboard/Model/Output

### Socio-Economic Correlation
Statistical analysis reveals a moderate correlation ($0.46$) between household size and access difficulty, with lower-income households reporting the highest difficulty.

![Correlation Heatmap](Analysis_result/correlation_heatmap_45_both_axes.png)
![Income vs Difficulty](Analysis_result/income_vs_difficulty_professional(1).png)

### Decision-Making Authority
In 55.2% of households, the male head of household makes the final evacuation decision, though 44.8% report joint decision-making.

![Decision Authority](Analysis_result/distribution_of_decision_making_authority.png)
![Agency Analysis](Analysis_result/agency_analysis.png)

## Results & Conclusion
The study concludes that physical proximity to a shelter is insufficient if privacy and sanitation needs are unmet. To increase evacuation rates, infrastructure must be gender-mainstreamed and asset protection strategies (for livestock) must be integrated.

## Future Work
* Integrating **Geographic Information Systems (GIS)** to map exact distances from households to shelters.
* Developing a predictive model for evacuation probability based on household assets.

## Author & Contact
**Md. Sohel**
* Faculty of Environmental Science and Disaster Management (ESDM)
* Patuakhali Science and Technology University (PSTU)

Mail: ug2306062@esdm.pstu.ac.bd

WhatsApp: 01756012047

Linkedin: [Visit](https://www.linkedin.com/in/mdsohel-gisanalyst/)
