import pandas as pd
df=pd.read_csv('file.csv')
df=df.drop("column@",axis=1)
df["new_column"]=df["column1"]+df["column2"]
import argparse
def main():
    parser = argparse.ArgumentParser(description='Process some CSV file.')
    parser.add_argument('--path', type=str, help='Path to the CSV file.')
    parser.add_argument('--number', type=int, help='Number of the column to delete.')
    parser.add_argument('--column1', type=str, help='Name of the first column to add.')
    parser.add_argument('--column2', type=str, help='Name of the second column to add.')
    args = parser.parse_args()
    # Call the function with the arguments from the command line
    df = process_csv(args.path, args.number, args.column1, args.column2)
    # Write the modified DataFrame back to a CSV file
    df.to_csv(args.path, index=False)
if __name__ == "__main__":
    main()
