import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('your_file.xlsx')

# Create an empty list to store the normalized rows
normalized_rows = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    databases = str(row['database_names']).split(',')  # Split the database names by comma
    
    # If there is only one database, add the row as it is
    if len(databases) == 1:
        normalized_rows.append(row)
    else:
        # Create a new row for each individual database
        for db in databases:
            new_row = row.copy()
            new_row['database_names'] = db.strip()  # Remove leading/trailing whitespaces
            normalized_rows.append(new_row)

# Create a new DataFrame from the normalized rows
normalized_df = pd.DataFrame(normalized_rows)

# Reset the index of the DataFrame
normalized_df.reset_index(drop=True, inplace=True)
