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
for name, df in dataframes.items():
    print(f"--- Missing values in {name} ---")
    print(df.isnull().sum())
    print("\n")
