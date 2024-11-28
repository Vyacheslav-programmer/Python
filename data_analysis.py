import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    try:
        print(f"Loading dataset from {file_path}...")
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Ensure the scraping script ran successfully.")
        return None
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def explore_data(df):
    print("\n--- Dataset Overview ---")
    print(df.info())
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Dataset Statistics ---")
    print(df.describe(include='all'))

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

def visualize_data(df):
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

    if not numeric_columns.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    df = load_dataset(file_path)
    if df is not None:
        explore_data(df)
        visualize_data(df)
