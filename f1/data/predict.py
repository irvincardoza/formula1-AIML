import pandas as pd

circuits = pd.read_csv('circuits.csv')
constructor_results = pd.read_csv('constructor_results.csv')
constructor_standings = pd.read_csv('constructor_standings.csv')
constructors = pd.read_csv('constructors.csv')
driver_standings = pd.read_csv('driver_standings.csv')
drivers = pd.read_csv('drivers.csv')
lap_times = pd.read_csv('lap_times.csv')
pit_stops = pd.read_csv('pit_stops.csv')
qualifying = pd.read_csv('qualifying.csv')
races = pd.read_csv('races.csv')
results = pd.read_csv('results.csv')
seasons = pd.read_csv('seasons.csv')
sprint_results = pd.read_csv('sprint_results.csv')
status = pd.read_csv('status.csv')


def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

# Apply cleaning to all dataframes
dataframes = {
    'circuits': circuits,
    'constructor_results': constructor_results,
    'constructor_standings': constructor_standings,
    'constructors': constructors,
    'driver_standings': driver_standings,
    'drivers': drivers,
    'lap_times': lap_times,
    'pit_stops': pit_stops,
    'qualifying': qualifying,
    'races': races,
    'results': results,
    'seasons': seasons,
    'sprint_results': sprint_results,
    'status': status
}

for name, df in dataframes.items():
    dataframes[name] = clean_column_names(df)
    dataframes[name].drop_duplicates(inplace=True)

# Optionally, inspect the cleaned data
# for name, df in dataframes.items():
#     print(f"--- Cleaned {name} ---")
#     print(df.head())

# Display the number of missing values in each column for each DataFrame


# Fill missing values in qualifying dataset with 0
dataframes['qualifying'] = dataframes['qualifying'].fillna(0)
# for name, df in dataframes.items():
#     print(f"--- Missing values in {name} ---")
#     print(df.isnull().sum())
#     print("\n")

# Calculate driver experience

##   creating features for  drivers to maximise model efficiency ##
results['driver_experience'] = results.groupby('driverid')['raceid'].transform('nunique')

driver_experience = results[['driverid', 'driver_experience']].drop_duplicates()
# print(driver_experience.head())
# for name, df in dataframes.items():

    
#     print(df.head())

##        fixing "/N" values in position databse
results['position'] = pd.to_numeric(results['position'], errors='coerce')
# Replace NaN values with 0
results['position'] = results['position'].fillna(0)



results['average_points'] = results.groupby('driverid')['points'].transform('mean')

results['total_wins'] = results.groupby('driverid')['position'].transform(lambda x: (x == 1).sum())
results['average_finish_position'] = results.groupby('driverid')['position'].transform('mean')


results['constructor_experience'] = results.groupby('constructorid')['raceid'].transform('nunique')
results['average_constructor_points'] = results.groupby('constructorid')['points'].transform('mean')

results['total_constructor_wins'] = results.groupby('constructorid')['position'].transform(lambda x: (x == 1).sum())

results['total_constructor_wins'] = results.groupby('constructorid')['position'].transform(lambda x: (x == 1).sum())


pit_stops['pit_stops_count'] = pit_stops.groupby(['raceid', 'driverid'])['stop'].transform('count')

# error in position values

# Check for non-numeric values in the 'position' column
