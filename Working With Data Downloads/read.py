if __name__ == "__main__":
    import pandas as pd
    contents = pd.read_csv('data/CRDC2013_14content.csv')
    print(contents.loc[10])