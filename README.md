# CoverMyMeds Challenge at The Erdos Institute 2021 Boot Camp
Rachel Domagalski, Rachel Lee, Hannah Pieper and Rongqing Lee

## Overview 
[Project Description](#project-description)  
[Main Takeaways](#main-takeaways)  
[Data](#data)  
[Predicting PA Acceptance](#predicting-pa-acceptance)  
[Predicting PA and Claim Volume](#predicting-pa-and-claim-volume)  
[Identifying the Formulary for Each Payer](#identifying-the-formulary-for-each-payer)  
[Predicting the Number of Refills](#predicting-the-number-of-refills)  

## Project Description

When a patient tries to get a prescription from a pharmacy, a claim is created against the patient's insurance (payer). Such a pharmacy claim might be rejected for various reasons and might require prior authorization (PA). A PA is a form that providers submit on behalf of a patient to the insurance making a case for the prescribed therapy. In this project, we surveyed many classifiers for predicting how likely a certain PA will be approved, and forecast future volume of PAs with time series analysis techniques. Additionally, we identify the formulary for each payer and predict the number of times certain drugs can be refilled.

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
The formulary of a payer is list of the preferred drugs each payer has. These lists are often tiered with certain drugs being lower in cost than others, and other drugs needing a prior authorization before the payer will agree to cover them. If an initial pharmacy claim is rejected, a "reject code" is provided which explains why the drug was not covered. In this data, we have three different reject codes: 70, 75, 76. From these codes, we are able to determine the formulary of each payer. 

Each reject code has a different meaning. A code 70 means that the drug is not on the formulary and is not covered by the payer. A code 75 means the drug is on the formulary, but another drug is typically prefered. These drugs will require a prior authorization. A code 76 means that while the drug is covered, plan limitations ahve been exceeded. This typically means the patient is over the number of refills on the prescription. 

Through examining the data from each payer and each drug, we find the following: 
* Payer 417380: Drug A is on formulary, but requires a PA (Code 75), Drug B is on formulary and only requires a PA if the patient is over refills (Code 76), Drug C is not covered (Code 70).
* Payer 417614: Drug A is not covered (Code 70), Drug B is on formulary but requires a PA (Code 75), Drug C is on formulary and only requires a PA if patient is over refills (Code 76). 
* Payer 417740: Drug A is on formulary and only requires a PA if patient is over refills (Code 76), Drug B is not covered (Code 70), Drug C is on formulary but requires a PA (Code 75). 
* Payer 999001: All drugs are on formulary and only require a PA if patient is over refills (Code 76). 

These results can be observed in [exploration.ipynb](exploration.ipynb)

## Predicting the Number of Refills













