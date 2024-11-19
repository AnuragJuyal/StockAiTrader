# import pandas as pd

# def load_data(file_path):
#     """Load and preprocess stock data from a CSV file."""
#     data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
#     data = data.dropna()  # Remove missing values
#     return data
import pandas as pd

# Function to load and preprocess stock data from a CSV file
def load_data(file_path=None, symbols=None, country=None):
    """Load and preprocess stock data either from a CSV file or Yahoo Finance."""
    
    # Load CSV if file path is provided
    if file_path:
        data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
        data = data.dropna()  # Remove missing values
        return data
    