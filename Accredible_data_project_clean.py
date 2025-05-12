import pandas as pd
json_file_path = '/Users/beth/Documents/Projects/Accredible project December 2024/accredible_sample_20221108(1).json'
df = pd.read_json(json_file_path)


from pandas import json_normalize
# Assuming 'results' is the column containing the nested JSON
df_normalized = json_normalize(df['results'])
# Now, df_normalized will contain separate columns for each key in the JSON
#within my 'current experience column, I have a list of dictionaries. 

# Create a new dataframe
df_new = pd.DataFrame(df_normalized)

# Extract 'title' and 'start' values safely
df_new['current role'] = df_new['current_experience'].apply(lambda x: x[0]['title'] if len(x) > 0 else None)
df_new['current role1'] = df_new['current_experience'].apply(lambda x: x[1]['title'] if len(x) > 1 else None)
df_new['current role2'] = df_new['current_experience'].apply(lambda x: x[2]['title'] if len(x) > 2 else None)
df_new['current role3'] = df_new['current_experience'].apply(lambda x: x[3]['title'] if len(x) > 3 else None)

df_new['start date for current role'] = df_new['current_experience'].apply(lambda x: x[0]['start'] if len(x) > 0 else None)
df_new['start date for current role1'] = df_new['current_experience'].apply(lambda x: x[1]['start'] if len(x) > 1 else None)
df_new['start date for current role2'] = df_new['current_experience'].apply(lambda x: x[2]['start'] if len(x) > 2 else None)
df_new['start date for current role3'] = df_new['current_experience'].apply(lambda x: x[3]['start'] if len(x) > 3 else None)

#Remove rows that have NaN values in 'start dates...' column. Do this before converting unix time stamps.

import numpy as np

# Count NaN values in a specific column
nan_count_start_date_for_current_role = df_new['start date for current role'].isna().sum()
nan_count_start_date_for_current_role1 = df_new['start date for current role1'].isna().sum()
nan_count_start_date_for_current_role2 = df_new['start date for current role2'].isna().sum()
nan_count_start_date_for_current_role3 = df_new['start date for current role3'].isna().sum()

# Print the result
print(f'Number of NaN values in start date for current role: {nan_count_start_date_for_current_role}')
print(f'Number of NaN values in start date for current role1: {nan_count_start_date_for_current_role1}')
print(f'Number of NaN values in start date for current role2: {nan_count_start_date_for_current_role2}')
print(f'Number of NaN values in start date for current role3: {nan_count_start_date_for_current_role3}')

# remove 74 NaN values (can't use no start date in current role), and run numbers again

df_new.dropna(subset=['start date for current role'], axis=0, inplace=True)

# Count NaN values in a specific column
nan_count_start_date_for_current_role = df_new['start date for current role'].isna().sum()
nan_count_start_date_for_current_role1 = df_new['start date for current role1'].isna().sum()
nan_count_start_date_for_current_role2 = df_new['start date for current role2'].isna().sum()
nan_count_start_date_for_current_role3 = df_new['start date for current role3'].isna().sum()

# Print the result
print(f'Number of NaN values in start date for current role: {nan_count_start_date_for_current_role}')
print(f'Number of NaN values in start date for current role1: {nan_count_start_date_for_current_role1}')
print(f'Number of NaN values in start date for current role2: {nan_count_start_date_for_current_role2}')
print(f'Number of NaN values in start date for current role3: {nan_count_start_date_for_current_role3}')

# Count NaN values in a specific column
nan_count_current_role = df_new['current role'].isna().sum()
nan_count_current_role1 = df_new['current role1'].isna().sum()
nan_count_current_role2 = df_new['current role2'].isna().sum()
nan_count_current_role3 = df_new['current role3'].isna().sum()

# Print the result
print(f'Number of NaN values in current role: {nan_count_current_role}')
print(f'Number of NaN values in current role1: {nan_count_current_role1}')
print(f'Number of NaN values in current role2: {nan_count_current_role2}')
print(f'Number of NaN values in current role3: {nan_count_current_role3}')


#From this, i think I don't need to include role2/3 in my data. Most people have not included info here. For the 20 or so that have, I can look at the data manually (if it's still needed after further data cleaning)
# re-run just looking at role and role1

# Create a new dataframe
df_new = pd.DataFrame(df_normalized)

# Extract 'title' and 'start' values safely
df_new['current role'] = df_new['current_experience'].apply(lambda x: x[0]['title'] if len(x) > 0 else None)
df_new['current role1'] = df_new['current_experience'].apply(lambda x: x[1]['title'] if len(x) > 1 else None)


df_new['start date for current role'] = df_new['current_experience'].apply(lambda x: x[0]['start'] if len(x) > 0 else None)
df_new['start date for current role1'] = df_new['current_experience'].apply(lambda x: x[1]['start'] if len(x) > 1 else None)

#Remove rows that have NaN values in 'start dates...' column. Do this before converting unix time stamps.

# remove 74 NaN values (can't use no start date in current role), and run numbers again

df_new.dropna(subset=['start date for current role'], axis=0, inplace=True)

# need to convert start dates (they are currently unix time stamps) into something useful

# Replace NaN with 0 and ensure the column is of integer type
df_new['start date for current role1'].replace(np.nan, 0, inplace=True)

# Explicitly convert the column to integers
df_new['start date for current role1'] = df_new['start date for current role1'].astype(int)

import datetime

# Convert the 'start' column to a human-readable date
df_new['start date for current role_cleaned'] = df_new['start date for current role'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['start date for current role1_cleaned'] = df_new['start date for current role1'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))


#note all '0' values have now been replaced with '1970-01-01' Given that my credential issue dates are 2013 onward, this isn't a problem.

# Remove time portion of the date column (keep only the date)
df_new['start date for current role_cleaned'] = pd.to_datetime(df_new['start date for current role_cleaned']).dt.date
df_new['start date for current role1_cleaned'] = pd.to_datetime(df_new['start date for current role1_cleaned']).dt.date


#now let's look at the 'experience' column

# Extract 'title', 'start' and 'end' values
df_new['previous role'] = df_new['experience'].apply(lambda x: x[0]['title'] if len(x) > 0 else None)
df_new['previous role1'] = df_new['experience'].apply(lambda x: x[1]['title'] if len(x) > 1 else None)
df_new['previous role2'] = df_new['experience'].apply(lambda x: x[2]['title'] if len(x) > 2 else None)
df_new['previous role3'] = df_new['experience'].apply(lambda x: x[3]['title'] if len(x) > 3 else None)

df_new['start date for previous role'] = df_new['experience'].apply(lambda x: x[0]['start'] if len(x) > 0 else None)
df_new['start date for previous role1'] = df_new['experience'].apply(lambda x: x[1]['start'] if len(x) > 1 else None)
df_new['start date for previous role2'] = df_new['experience'].apply(lambda x: x[2]['start'] if len(x) > 2 else None)
df_new['start date for previous role3'] = df_new['experience'].apply(lambda x: x[3]['start'] if len(x) > 3 else None)

df_new['end date for previous role'] = df_new['experience'].apply(lambda x: x[0]['end'] if len(x) > 0 else None)
df_new['end date for previous role1'] = df_new['experience'].apply(lambda x: x[1]['end'] if len(x) > 1 else None)
df_new['end date for previous role2'] = df_new['experience'].apply(lambda x: x[2]['end'] if len(x) > 2 else None)
df_new['end date for previous role3'] = df_new['experience'].apply(lambda x: x[3]['end'] if len(x) > 3 else None)


#Remove rows that have NaN values in 'start dates...' column. Do this before converting unix time stamps.

# Count NaN values in a specific column
nan_count_start_date_for_previous_role = df_new['start date for previous role'].isna().sum()
nan_count_start_date_for_previous_role1 = df_new['start date for previous role1'].isna().sum()
nan_count_start_date_for_previous_role2 = df_new['start date for previous role2'].isna().sum()
nan_count_start_date_for_previous_role3 = df_new['start date for previous role3'].isna().sum()

#note we may not actually need this column, if current role info give us what we need.
#therefore, rather than removing NaN lines, I'm going to set the value to 0.

# need to convert start dates (they are currently unix time stamps) into something useful

# Replace NaN with 0 and ensure the column is of integer type
df_new['start date for previous role'].replace(np.nan, 0, inplace=True)
df_new['start date for previous role1'].replace(np.nan, 0, inplace=True)
df_new['start date for previous role2'].replace(np.nan, 0, inplace=True)
df_new['start date for previous role3'].replace(np.nan, 0, inplace=True)

df_new['end date for previous role'].replace(np.nan, 0, inplace=True)
df_new['end date for previous role1'].replace(np.nan, 0, inplace=True)
df_new['end date for previous role2'].replace(np.nan, 0, inplace=True)
df_new['end date for previous role3'].replace(np.nan, 0, inplace=True)

# Explicitly convert the column to integers
df_new['start date for previous role'] = df_new['start date for previous role'].astype(int)
df_new['start date for previous role1'] = df_new['start date for previous role1'].astype(int)
df_new['start date for previous role2'] = df_new['start date for previous role2'].astype(int)
df_new['start date for previous role3'] = df_new['start date for previous role3'].astype(int)

df_new['end date for previous role'] = df_new['end date for previous role'].astype(int)
df_new['end date for previous role1'] = df_new['end date for previous role1'].astype(int)
df_new['end date for previous role2'] = df_new['end date for previous role2'].astype(int)
df_new['end date for previous role3'] = df_new['end date for previous role3'].astype(int)


# Convert the 'start' and 'end' column to a human-readable date
df_new['start date for previous role_cleaned'] = df_new['start date for previous role'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['start date for previous role1_cleaned'] = df_new['start date for previous role1'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['start date for previous role2_cleaned'] = df_new['start date for previous role2'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['start date for previous role3_cleaned'] = df_new['start date for previous role3'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

df_new['end date for previous role_cleaned'] = df_new['end date for previous role'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['end date for previous role1_cleaned'] = df_new['end date for previous role1'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['end date for previous role2_cleaned'] = df_new['end date for previous role2'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
df_new['end date for previous role3_cleaned'] = df_new['end date for previous role3'].apply(lambda x: datetime.datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

#note all '0' values have now been replaced with '1970-01-01' Given that my credential issue dates are 2013 onward, this isn't a problem.

# Remove time portion of the date column (keep only the date)
df_new['start date for previous role_cleaned'] = pd.to_datetime(df_new['start date for previous role_cleaned']).dt.date
df_new['start date for previous role1_cleaned'] = pd.to_datetime(df_new['start date for previous role1_cleaned']).dt.date
df_new['start date for previous role2_cleaned'] = pd.to_datetime(df_new['start date for previous role2_cleaned']).dt.date
df_new['start date for previous role3_cleaned'] = pd.to_datetime(df_new['start date for previous role3_cleaned']).dt.date

df_new['end date for previous role_cleaned'] = pd.to_datetime(df_new['end date for previous role_cleaned']).dt.date
df_new['end date for previous role1_cleaned'] = pd.to_datetime(df_new['end date for previous role1_cleaned']).dt.date
df_new['end date for previous role2_cleaned'] = pd.to_datetime(df_new['end date for previous role2_cleaned']).dt.date
df_new['end date for previous role3_cleaned'] = pd.to_datetime(df_new['end date for previous role3_cleaned']).dt.date


# Create another new dataframe

df_json=df_new[['last_name', 'current role', 'start date for current role_cleaned', 'current role1', 'start date for current role1_cleaned', 'previous role', 'start date for previous role_cleaned', 'end date for previous role_cleaned', 'previous role1', 'start date for previous role1_cleaned', 'end date for previous role1_cleaned', 'previous role2', 'start date for previous role2_cleaned', 'end date for previous role2_cleaned', 'previous role3', 'start date for previous role3_cleaned', 'end date for previous role3_cleaned']]

#*********************************

# now look at CSV file and put into dataframe. This will have credential issue date and email in.


csv_file = '/Users/beth/Documents/Projects/Accredible project December 2024/2022-11-03 - RecipientSample-Cleaned(1).csv'
df = pd.read_csv(csv_file)

# dates are in different time format - need to fix this. 

# Convert 'Credential Issue Date' column to datetime
df['Credential Issue Date'] = pd.to_datetime(df['Credential Issue Date'], format='%d/%m/%Y')

# Remove time portion (if any)
df['Credential Issue Date'] = df['Credential Issue Date'].dt.date


# I'm matching on names. Need to split out Recipient Name column based on spaces. 

# Split 'Recipient Name' into first name and last name (assuming last name is the last word)
df['last_name'] = df['Recipient Name'].str.split().str[-1]

#create new dataframe
df_csv=df[['last_name', 'Credential Issue Date']]

# join two dataframes (df_csv and df_json) based on name match. df_new will always match a name in df. There will be some names in df that don't have a record in df_new

# Merge the DataFrames on the 'last_name' column
merged_df = pd.merge(df_json, df_csv, on='last_name', how='inner')  # 'inner' join by default

# doing this merge lost me another 46 rows. Not quite sure why (possibly things like spelling mistakes, extra spaces etc.) as I was expecting all last_names from df_json to match

# Using the credential dates, we look at the job role on their profile prior to the credential date, and then any change occurring within 12 months of that date.


# Find the most recent date (maximum)
most_recent = merged_df['Credential Issue Date'].max()
print("Most recent Credential Issue Date:", most_recent)

# Find the least recent date (minimum)
least_recent = merged_df['Credential Issue Date'].min()
print("Least recent Credential Issue Date:", least_recent)

#*******************************

# Function to determine the job role held on the credential issue date
def get_role_on_credential_date(row):
    # List of role columns and their respective start and end date columns
    role_columns = [
        ('current role', 'start date for current role_cleaned', None), 
        ('current role1', 'start date for current role1_cleaned', None),
        ('previous role', 'start date for previous role_cleaned', 'end date for previous role_cleaned'),
        ('previous role1', 'start date for previous role1_cleaned', 'end date for previous role1_cleaned'),
        ('previous role2', 'start date for previous role2_cleaned', 'end date for previous role2_cleaned'),
        ('previous role3', 'start date for previous role3_cleaned', 'end date for previous role3_cleaned')
    ]
    
    # Check which role was held on the credential issue date
    for role, start_date_col, end_date_col in role_columns:
        start_date = row[start_date_col]
        end_date = row[end_date_col] if end_date_col else None
        
        # Check if the credential issue date is between the start and end dates
        if start_date <= row['Credential Issue Date'] and (end_date is None or row['Credential Issue Date'] <= end_date):
            return row[role]
    
    return None  # Return None if no role is found

# Apply the function to the DataFrame to determine the role held on the credential issue date
merged_df['role_on_credential_date'] = merged_df.apply(get_role_on_credential_date, axis=1)

#******************************
#*******

#function to see if job role has changed within 12 months of credential issue date

def check_roles_within_12_months(row):
    try: #Converts the credential issue date into a datetime object
        credential_date = pd.to_datetime(row['Credential Issue Date'], errors='coerce')
        if pd.isnull(credential_date):
            return []  # Skip if credential date is invalid

        window_start = credential_date #this part defines the 12 month window
        try:
            window_end = credential_date.replace(year=credential_date.year + 1)
        except ValueError:
            # Handle edge case for leap years
            window_end = credential_date + pd.DateOffset(years=1)

        #this defines the role column as a list
        roles_columns = [
            'current role', 'current role1', 'previous role', 'previous role1',
            'previous role2', 'previous role3'
        ]
        #this defines the date column as a list (which corresponds to the roles in the role column)
        start_date_columns = [
            'start date for current role_cleaned', 'start date for current role1_cleaned',
            'start date for previous role_cleaned', 'start_date for previous role1_cleaned',
            'start date for previous role2_cleaned', 'start date for previous role3_cleaned'
        ]

        roles_within_window = []

#this loops through each role/start date pair
        for role_col, date_col in zip(roles_columns, start_date_columns):
            #convert the start date of the role to a datetime object
            start_date = pd.to_datetime(row.get(date_col), errors='coerce')
            #if the start date is valid and falls within the 12 month window, add a tuple of role title and start date
            if pd.notnull(start_date) and window_start <= start_date <= window_end:
                roles_within_window.append((row.get(role_col, 'Unknown'), start_date))

#this returns a list of roles that started within 12 months of the credential date
        return roles_within_window

    except Exception as e:
        print(f"Unexpected error in row {row.name}: {e}")
        return []

# this applies the function to the dataframe, creating a new column called roles within 12 months
merged_df['roles_within_12_months'] = merged_df.apply(check_roles_within_12_months, axis=1)

# Display key columns for inspection
print(merged_df[['last_name', 'Credential Issue Date', 'role_on_credential_date', 'roles_within_12_months']])



       last_name  ...                    roles_within_12_months
0    Satterfield  ...                                        []
1         Bickle  ...                                        []
2         Miller  ...                                        []
3         Drance  ...                                        []
4          Watts  ...                                        []
..           ...  ...                                       ...
146        Yokum  ...  [(Project Manager, 2021-10-01 00:00:00)]
147         Pier  ...                                        []
148      Bennett  ...                                        []
149      Bennett  ...                                        []
150      Papaiah  ...                                        []

[151 rows x 4 columns]


merged_df['roles_within_12_months'].value_counts()

roles_within_12_months
[]                                                                            130
[(National Stalking Helpline and Advocacy Manager, 2021-04-01 00:00:00)]        1
[(Consultant, 2017-05-01 00:00:00)]                                             1
[(UX Researcher, 2021-11-01 00:00:00), (UX Designer, 2021-09-01 00:00:00)]      1
[(CEO/Interior Designer, 2019-08-01 00:00:00)]                                  1
[(Production and Plant manager, 2019-03-01 00:00:00)]                           1
[(Senior Investment Analyst, 2019-06-01 00:00:00)]                              1
[(Founding Partner, 2021-10-01 00:00:00)]                                       1
[(Independent Business Owner, 2020-04-01 00:00:00)]                             1
[(Content Manager, 2022-01-01 00:00:00)]                                        1
[(Director, UX Design, 2022-03-01 00:00:00)]                                    1
[(People Experience Administrator , 2022-01-01 00:00:00)]                       1
[(Senior Salesforce Administrator, 2022-01-01 00:00:00)]                        1
[(Official Member-Forbes Coaches Council, 2020-01-01 00:00:00)]                 1
[(Lead Product Manager, 2020-08-01 00:00:00)]                                   1
[(Marketing Manager, 2021-01-01 00:00:00)]                                      1
[(Digital Marketing Director | Programs, 2020-02-01 00:00:00)]                  1
[(Senior Accountant, 2017-04-01 00:00:00)]                                      1
[(Emeritus Professor, 2019-05-01 00:00:00)]                                     1
[(Director of Revenue Operations, 2021-07-01 00:00:00)]                         1
[(AVP, Marketing, 2022-01-01 00:00:00)]                                         1
[(Project Manager, 2021-10-01 00:00:00)]                                        1


# This tells me that 130 of my 151 titles didn't change. 21 did. 