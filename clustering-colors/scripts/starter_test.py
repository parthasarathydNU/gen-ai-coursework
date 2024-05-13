import pandas as pd

def main():
    try:
        # Load the data
        data = pd.read_csv('data/sample-data.csv')

        # Display the first few rows of the data frame
        print("Succesfully loaded data:")
        print(data.head())

        # Basic Operation: Calculate the total number of samples
        total_samples = data.shape[0]
        print(f"Total  number of samples: {total_samples}")

        # If everything went well
        print("Initial test passed. Docker container is running succesfully.")
    
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()
