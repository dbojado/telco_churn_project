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
<b>customer_id:</b>            An alpha-number number used to identify customer               
gender:                 Labels customer male or female                        
is_senior_citizen:      Labels customer senior or not senior             
partner:                Labels customer with or without partner	                   
dependents:             Labels customer with or wihtout dependents	                
contract_type:          Month-to-month, 1-year, or 2-year contract	
payment_type:           Electronic, Mailled Check, or Bank transfer payment	
monthly_charges:        Amount of monthly charges	
total_charges:          Amount of total charges	
churn:                  Yes/No rate at which customers leave company	
tenure:                 Number of months customer has been with company	
is_female:              T/F whether female or not female	
has_churned:            T/F whether churned or not churned	
has_phone:              T/F whether has phone or does not have phone	
has_internet:           T/F whether has internet or does not have internet	
has_phone_and_internet: T/F whether has phone and internet service or not
start_date:             Date when individual become customer with company             			
phone_type:             No phone service, one-line, two or more lines	
internet_type:          No internet service, DSL, or fiber optic	

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
