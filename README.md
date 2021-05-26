# CoverMyMeds Challenge at The Erdos Institute 2021 Boot Camp
Rachel Domagalski, Rachel Lee, Hannah Pieper and Rongqing Lee

## Overview 
include links to sections of MD file as a table of contents (How to generate this?) 

[Project Description](#headers)  
[Predicting PA Acceptance](#headers)  

## Project Description

When a patient try to get a prescription from a pharmacy, a claim is created against the patient's insurance (payer). Such a pharmacy claim might be rejected for various reasons and might require prior authorization (PA). A PA is a form that providers submit on behalf of a patient to the insurance making a case for the prescribed therapy. In this project, we surveyed many classifiers for predicting how likely a certain PA will be approved, and forecast future volume of PAs with time series analysis techniques. Additionally, we identify the formulary for each payer and predict the number of times certain drugs can be refilled.

### Main Takeaways
Maybe just a sentence for each
> Summarize best classifier 
> Summarize best method for volume prediction 
> Formulary for each payer 
>  Number of fills 
>  Highlight KPIs? 

### Data 
Each event in the dataset corresponds to a prescription written by a provider. For each event, there is information about the patient's insurer, the patient, the drug prescribed and whether or not the original prescription claim was accepted. If it was rejected, the reject code is included as well as whether the subsequent PA was accepted or rejected. Additionally, the month, day and year of the claim is included. The data spans 3 years and our dataset consists of approximately 1 million data points, with roughly half resulting in a PA. 

All of the features for each event are categorical or binary; there are no continuous features. 

See [exploration.ipynb](https://github.com/domagal9/cmm_pa/blob/main/exploration.ipynb)

## Predicting PA Acceptance 

## Predicting PA and Claim Volume 

## Identifying the Formulary for Each Payer 

## Predicting the Number of Refills













