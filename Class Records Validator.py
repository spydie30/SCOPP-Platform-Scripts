# %%
import pandas as pd
import re

# %% [markdown]
# ##Assumming github usernames are in form BR123456-FirstLast
# where BR123456 reprents rollnumber "0818BR123456"
# and name of student is "First Last"

# %%
import re
def is_valid_username(username):
    # Regular expression pattern for the username format BR123456-FirstLast.
    pattern = r"^[A-Z]{2}\d{6}-[A-Z][a-z]+[A-Z][a-z]+$"
    # Use the re.match function to check if the username matches the pattern.
    if re.match(pattern, username):
        return True
    else:
        return False


# # List of test cases
# test_cases = [
#     "AB123456-JohnDoeAa",      # Valid username
#     "CD987654-JaneSmithBb",    # Valid username
#     "EF123456-Invalid",        # Invalid username (doesn't end with two uppercase+lowercase letters)
#     "GH12345-InvalidUser",     # Invalid username (less than 8 digits)
#     "IJ123456-InvalidUser",    # Invalid username (first name doesn't start with an uppercase letter)
#     "KL123456-JohnDoe",        # Invalid username (last name is missing)
#     "MN123456-JaneSmithAaA",   # Invalid username (last name has more than one uppercase letter)
#     "OP123456-JaneSmithB",     # Invalid username (first name has only one character)
#     "QR123456-InvalidUserAbc", # Invalid username (last name starts with uppercase, should be lowercase)
#     "ST123456-InvalidUserABC", # Invalid username (first name ends with uppercase, should be lowercase)
#     "UV123456-JohnSmithAaAa",  # Invalid username (last name has more than two uppercase letters)
#     "WX123456-JohnDoeA",       # Invalid username (last name doesn't have two lowercase letters)
#     "YZ123456-JOHNDOEAA",       # Invalid username (first and last name should have lowercase letters)
#     "AB123456-JOHNDOEaa",       # Invalid username (first name should start with uppercase letter)
#     "CD123456-JaneSmithbb",     # Invalid username (last name should start with uppercase letter)
#     "EF123456-JohnDoeAaA",      # Invalid username (last name has more than one uppercase letter)
#     "GH123456-JaneSmithBbBb",   # Invalid username (last name has more than two uppercase letters)
#     "IJ123456-JohnDoeAaa",      # Invalid username (last name has more than two lowercase letters)
#     "KL123456-JaneSmithA",      # Invalid username (last name doesn't have two lowercase letters)
# ]

# # Loop through test cases and validate
# for index, username in enumerate(test_cases):
#     result = is_valid_username(username)
#     print(f"Test Case {index + 1}: {username} - {'Valid' if result else 'Invalid'}")


# %%
def separate_parts(username):
    # Define a regular expression pattern to extract enrollment and name parts.
    pattern = r"^([A-Z]{2}\d{6})-([A-Z][a-z]+)([A-Z][a-z]+)$"
    
    # Use re.match to find the parts.
    match = re.match(pattern, username)
    
    if match:
        enrollment_part = match.group(1)
        first_name = match.group(2)
        last_name = match.group(3)
        # Split the name part into first and last names.
        
        
        return enrollment_part, first_name, last_name
    else:
        return None, None, None

# # Example usage:
# username = "AB123456-JohnDoe"
# enrollment, first_name, last_name = separate_parts(username)

# if enrollment:
#     enrollment=enrollment
#     print(f"Enrollment: {enrollment}")
#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")
# else:
#     print("Invalid username format.")

# %% [markdown]
# ##Assumming That there are no records with same roll number
# 
# should Find way around for scenerio where students may use same roll numbers in their username 

# %%

# Sample DataFrame
# data = {
#     'Enrollment': [101, 102, 103, 104],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Surname': ['Johnson', 'Smith', 'Brown', 'Lee']
# }

# df = pd.DataFrame(data)

def search_and_match(enrollment, name, surname, dataframe):
    status_flags = {
        'enrollment_not_in_records': False,
        'name_mismatch': False,
        'match_successful': False,
        'correct_name': None,
    }

    # Check if the enrollment number exists in the records
    if enrollment not in dataframe['Enrollment'].values:
        status_flags['enrollment_not_in_records'] = True
        return status_flags
    
    # Retrieve the record for the given enrollment number
    student_record = dataframe[dataframe['Enrollment'] == enrollment].iloc[0]
    record_name = student_record['Name']
    
    # Compare provided name and surname with the records
    name = name+' '+surname
    if name != record_name:
        status_flags['name_mismatch'] = True
        status_flags['correct_name'] = record_name
    if not status_flags['name_mismatch']:
        status_flags['match_successful'] = True
    
    return status_flags

# import pandas as pd

# # Demo DataFrame
# data = {
#     'Enrollment': [101, 102, 103, 104, 105],
#     'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Lee', 'Eva Clark'],
# }

# df = pd.DataFrame(data)

# # Test Cases
# test_cases = [
#     (101, 'Alice', 'Johnson'),  # Valid enrollment, name, and surname
#     (102, 'John', 'Doe'),        # Invalid enrollment not in records
#     (103, 'Charles', 'Brown'),    # Valid enrollment, mismatched name
#     (104, 'David', 'Jones'),      # Valid enrollment, mismatched surname
#     (105, 'Evelyn', 'Clarkson'),  # Valid enrollment, mismatched name and surname
#     (106, 'Eva', 'Clark'),        # Invalid enrollment not in records
# ]

# Testing Loop
#print(df)
# for index, (enrollment, name,surname) in enumerate(test_cases, start=1):
#     print(df)
#     result = search_and_match(enrollment, name,surname, df)
#     print(f"Test Case {index}:")
#     print(f"Enrollment: {enrollment}")
#     print(f"Name: {(name+' '+surname)}")
#     print("Result:")
#     for k, v in result.items():
#      print (k,':', v)
#     print("-" * 30)


# %%
# Function to match identifier with name and surname
def match_identifier(username, surname, identifier):
    t = username+' '+surname
    t = t.upper()
    identifier = identifier.upper()
    return (t==identifier)
# test_cases = [
#     ('Alice', 'Johnson', 'ALICE JOHNSON'),   # Valid match
#     ('Bob', 'Smith', 'BOB SMITH'),           # Valid match
#     ('Charlie', 'Brown', 'CHARLIE BROWN'),   # Valid match
#     ('David', 'Jones', 'DAVID JONES'),       # Valid match
#     ('Eva', 'Clarkson', 'EVA CLARK'),        # Invalid match
#     ('Eva', 'Clarkson', 'EVA CLARKSON'),    
# ]

# # Testing Loop
# for index, (name, surname, identifier) in enumerate(test_cases, start=1):
#     result = match_identifier(name, surname, identifier)
#     print(f"Test Case {index}:")
#     print(f"Name: {name}")
#     print(f"Surname: {surname}")
#     print(f"Identifier: {identifier}")
#     print("Result: Matched" if result else "Result: Not Matched")
#     print("-" * 30)

# %% [markdown]
# ## Assuming all official roll numbers start with 0818
# and 
# # "identifier","github_username","github_id","name" 
# these columns exist in Github classroom roster CSV
# # "Name","Enrollment"
# these columns exist in Classroom's official record CSV

# %%
# Function to process CSV files
def validate_records(gitClass_file_path , classData_file_path):
    try:
        # Read CSV file into a pandas DataFrame
        gitClass_df = pd.read_csv(gitClass_file_path)
        classData_df = pd.read_csv(classData_file_path)
        
        for index, row in gitClass_df.iterrows():
            username = row['github_username']
            identifier = row['identifier']
            
            # Check proper name convention
            if not is_valid_username(username):
                print(f"Improper name convention for username: {username}")
                continue
            
            # Extract name and surname from username
            enrollment,name, surname = separate_parts(username)
            enrollment="0818"+enrollment

            # Match identifier with name and surname
            if not match_identifier(name, surname, identifier):
                print(f"Identifier mismatch for username: {username}")
                continue
            # Checking with official records
            status_flags = search_and_match(enrollment,name, surname, classData_df )
            if status_flags['enrollment_not_in_records']:
                print(f"enrollment not in records: {enrollment}")
                continue
            if status_flags['name_mismatch']:
                print(f"enrollment : {enrollment} does not correspond to name : {(name+' '+surname)} instead it does to : {(status_flags['correct_name']+' '+status_flags['correct_surname'])}")
                continue
    except KeyError as e:
        print(f"{e} was encounterd during data access and handling. Provided files' columns are not in proper format")
    except FileNotFoundError as e:
        print(f"{e} . Provide correct name or path to the files")
    except Exception as e:
        print(f"Error: {e}")

gitClass_file_path , classData_file_path = input("Please Enter Github Classroom roster CSV File Link") , input("Please Enter Classroom\'s official record CSV File Link")
validate_records(gitClass_file_path , classData_file_path)


