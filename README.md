# Telco Customer Churn Reduction

## Project Description
Telco wants you to find what drives customer churn at the company. Churn is defined as the rate at which customers leave a company. We know that new customer acquisition can cost five times more than retaining an existing customer. We also know that increasing customer retention by 5% can increase profits from 25-95%. Therefore, it is important to determine and target what is causing the largest source of churn, so that the company can reduce it. 

## Objectives
- Find the drivers for customer churn at Telco.
- Construct a model to predict customer churn using classifcation techniques.
- Document code, process (data acquistion, preparation, exploration and testing, modeling, and evaluating, and findings and key takeaways in a Jupyter Notebook report.
- Present a high-level notebook walkthrough targeted to your audience.
- Answer panel questions about your code, process, findings and key takeaways, and model.

## Goals
- Find drivers for customer churn.
- Construct a ML classification model that accurately predicts customer churn.
- Create modules that make your process repeateable.
- Document your process well enough to be presented or read like a report.

## Audience
- Your target audience for your notebook walkthrough is the Codeup Data Science team. This should guide your language and level of explanations in your walkthrough.

## Data Dictionary
### Field Name                 
<b>customer_id:</b>             An alpha-number number used to identify customer  
             
<b>gender:</b>                  Labels customer male or female                        
<b>is_senior_citizen:</b>       Labels customer senior or not senior             
<b>partner:</b>                 Labels customer with or without partner	                   
<b>dependents:</b>              Labels customer with or wihtout dependents	                
<b>contract_type:</b>           Month-to-month, 1-year, or 2-year contract	
<b>payment_type:</b>            Electronic, Mailled Check, or Bank transfer payment	
<b>monthly_charges:</b>         Amount of monthly charges	
<b>total_charges:</b>           Amount of total charges	
<b>churn:</b>                   Yes/No rate at which customers leave company	
<b>tenure:</b>                  Number of months customer has been with company	
<b>is_female:</b>               T/F whether female or not female	
<b>has_churned:</b>             T/F whether churned or not churned	
<b>has_phone:</b>               T/F whether has phone or does not have phone	
<b>has_internet:</b>            T/F whether has internet or does not have internet	
<b>has_phone_and_internet:</b>  T/F whether has phone and internet service or not
<b>start_date:</b>              Date when individual become customer with company             
<b>phone_type:</b>              No phone service, one-line, two or more lines	
<b>internet_type:</b>           No internet service, DSL, or fiber optic	

## Project Planning
### Data Science Pipeline:
- Planning
- Acquisition
- Preparation
- Exploration
- Modeling 
- Delivery 

## Deliverables 
- Jupyter Notebook (presentation)
- README.md
- csv
- acquire.py
- prepare.py
- model.py

## Hypothesis
- The largest source of churn is coming from month-to-month contracts because of increasing monthly charges. Specifically, the phone and internet bundle customers are churning the most. 

## Key Findings 
- Internet customers are increasingly paying more over time
- Remember that customer will not switch backwards to DSL
