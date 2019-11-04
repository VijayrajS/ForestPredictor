import pandas as pd


def anomaly_func(data):
    # check for positive anomaly
    print(data)
    for row in data.iterrows():
        country_name = row[1][0]
        
        data_list = list(row[1][1:])
        positive_epochs = 0
        
        for i in range(1, len(data_list)):
            pass 
        # exit()


if __name__ == "__main__":
    d = pd.read_csv('deforest_data.csv')

    # print(d.head())
    year_range = ["Country Name"] + [str(u) for u in range(1990, 2017)]
    d_years = d[year_range]

    print(d_years.head())

    anomaly_func(d_years)
