import pandas as pd
import matplotlib.pyplot as plt

def anomaly_func(data):
    # check for positive anomaly

    p_coun = []
    s_c_coun = []
    for row in data.iterrows():
        country_name = row[1][0]
        
        data_list = list(row[1][1:])
        positive_epochs = 0
        
        sign = -1

        f = 0

        for i in range(1, len(data_list)):
            diff = data_list[i] - data_list[i-1]
            sign_now = 1 if diff > 0 else -1

            if diff > 0:
                positive_epochs += 1
            
            if sign_now != sign:
                f = 1
            sign = sign_now

        if positive_epochs > 12:
            p_coun.append(country_name)
            
        if f and country_name not in p_coun:
            s_c_coun.append(country_name)
    

    print(p_coun)
    print(s_c_coun)
    
    x_axis = list(data.columns[1:])
    slope = ()
    
    for row in data.iterrows():
        if row[1][0] == 'Kenya':
        # if row[1][0] in s_c_coun:
            dat = list(row[1][1:])
            print(dat[-1])
            
            try:
                plt.title(row[1][0])
                plt.axes().set_ylim([0, 1.5*max(dat)])
                plt.plot(x_axis, dat)
                plt.show()
            except:
                print(row[1][0])
                continue
    
if __name__ == "__main__":
    d = pd.read_csv('deforest_data.csv')
    year_range = ["Country Name"] + [str(u) for u in range(1990, 2017)]
    d_years = d[year_range]

    anomaly_func(d_years)
