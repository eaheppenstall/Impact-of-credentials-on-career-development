# Impact-of-credential-on-career-development
A project to determine if gaining an Accredible credential influenced a persons career within 12 months of gaining that credential

Git-hub repository at:
https://github.com/eaheppenstall/Impact-of-credential-on-career-development

- Python file: **tips-data-analysis.ipynb**
- data set: data\tips.csv  **Need to update this**

# Table of contents
1. [Introduction](#introduction)

2. [Description of the data set](#section2)
    1. [Initial steps: data cleaning of the json file](#sec2p1)
    2. [Initial steps: data cleaning of the csv file](#sec2p2)

3. [Combining the two datasets](#section3)
    
4. [Writing functions](#section4)
    1. [Writing a function to determine the job role on the Credential Issue Date](#sec4p1)
    2. [Writing a function to determine if a role change has occurred during the 12 months following the Credential Issue Date](#sec4p2)

5. [Results](#section5)
    
6. [Conclusion](#conclusion)

7. [Next steps](#nextsteps)

## 1. Introduction <a name="introduction"></a>
- This README describes work done to answer the question 'do individuals who interact with the Accredible network secure a promotion within 12 months of that interaction, thereby advancing ahead of their peers who aren't in the network. Resources used include Python and associated packages Pandas and Numpy. The analysis can be found at the filename given above.  


##  2. Description of the data sets <a name="section2"></a>
Two datasets were required for this analysis: 

1) a json file containing sample data from LinkedIn (270 rows). This data contains information regarding current/previous job roles. 
2) a csv file containing sample data from Accredible (1400 rows). This data contains information regarding an individuals interaction with Accredible i.e. the date on which a credential was issued.


### 2.1 Initial steps: data cleaning of the json file <a name="sec2p1"></a>
I loaded the data into a Pandas dataframe. I cleaned the data so that it contained separate columns for current role and previous role entries. Some individuals listed multiple current/previous roles and so each role was given a separate column. Start and end dates for these associated roles were included in most cases. 

74 individuals did not give a start date for their current role and so I changed this to 1 January 2024, which is more than 12 months after the latest credential issue date. This means it won't affect my results, but I don't have to delete the data row.

Some individuals did not give a start date for their previous role and so I changed this to 0 (converts to a timestamp date of 1970-01-01). This is before Accredible started operating, so it shouldn't affect my results and I don't have to delete the data row. 

Some start/end dates are listed as unix timestamps. These have been converted to a human-readable date (not including time)

The dataset looks like: 

![head](images/head.JPG)

### 2.2 Initial steps: data cleaning of the csv file <a name="sec2p2"></a>

I loaded the data into a Pandas dataframe. As I intended to match the dataframes based on surname, I cleaned the dataframe so that surname was captured as a separate column (rather than being included in a fullname column). 

Credential Issue Dates were converted to a human-readable date.

The dataset looks like: 

![head](images/head.JPG)

## 3. Combining the two datasets <a name="section3"></a>

The two datasets were combined using an inner join based on surname. Following this action, I now have 151 rows of data. Multiple data rows were lost in this step and this is likely due to extra spaces, spelling mistakes, etc. in the surname column of either dataframe. 

The dataset looks like: 

![head](images/head.JPG)

## 4. Writing functions <a name="section4"></a>

### 4.1 Writing a function to determine the job role on the Credential Issue Date <a name="sec4p1"></a>

This function takes the Credential Issue Date as the reference point. It then looks through the role title columns (current role, previous role etc.) to see which role was held on the Credential Issue Date. It then creates a data point in a new column entitled 'role_on_credential_date' which lists the role title held on the Credential Issue Date.

### 4.2 Writing a function to determine if a role change has occurred during the 12 months following the Credential Issue Date <a name="sec4p2"></a>

This function defines the 12 month window for each individual as 12 months after the Credential Issue Date. It then looks to see if a role change has occured within each individual's 12 month window. It returns a list of roles started within the 12 month window, or returns [] where no new role has been started.

## 5. Results <a name="section5"></a>

The main finding of this analysis is that only 21 roles changed within 12 months of the Credential Issue Date

## 6. Conclusion <a name="conclusion"></a>

This analysis found that 14% of job roles changed within 12 months of the Credential Issue Date. I would say that this is not a large enough percentage to say that Accredible had an effect on the job role change and that further analysis is needed to draw more solid conclusions. 

## 7. Next Steps <a name="nextsteps"></a>

Further analysis is needed to test this result against a control set (i.e. a group of individuals who haven't interacted with Accredible. Ideally, the control group would be a group of individuals with similar job roles to that in this dataset. 

It would also be interesting to link salary data here, to see how valuable an Accredible credential is.
