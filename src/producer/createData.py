def loadData():
    data = open("test",'r')
    size = data.readline().strip().split("=")
    price = data.readline().strip().split("=")
    return [size[1], price[1]]

if __name__ == "__main__": 
    import matplotlib
    matplotlib.use('Qt5Agg')
    import matplotlib.pylab as plt
    import pandas as pd
    
    plt.style.use('ggplot')
    my_data = loadData()
    print(my_data[0].split())

    df = pd.DataFrame({'Price': my_data[1].split() ,'Square_Foot': my_data[0].split()}, columns = ["Price", "Square_Foot"] )
    
    df['Square_Foot'] = df['Square_Foot'].apply(lambda x: int(x)) 
    df['Price'] = df['Price'].apply(lambda x: int(x)/1000) 
    df = df.sort_values(by=['Square_Foot', 'Price'], ascending=[True, True])
    #df = df.cumsum()
    print(df)
    #plt.figure(); 
    df.plot(x='Square_Foot', y='Price', linewidth=2.0)
    plt.show()