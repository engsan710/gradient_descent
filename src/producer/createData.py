# Read data from text file
def loadData():
    data = open("test",'r')
    size = data.readline().strip().split("=")
    price = data.readline().strip().split("=")
    return [size[1], price[1]]

# Main entry from command line
if __name__ == "__main__": 
    import matplotlib
    matplotlib.use('Qt5Agg')
    import matplotlib.pylab as plt
    import pandas as pd
    import numpy as np 
    
    plt.style.use('ggplot')
    # Load data
    my_data = loadData()
    
    #Create Pandas Dataframe from data
    df = pd.DataFrame({'Price': my_data[1].split() ,'Square_Foot': my_data[0].split()}, columns = ["Price", "Square_Foot"] )
    
    #Make the data integers
    df['Square_Foot'] = df['Square_Foot'].apply(lambda x: int(x)) 
    df['Price'] = df['Price'].apply(lambda x: int(x)/1000) 
    
    #Sort the data by Square foot then by Price
    df = df.sort_values(by=['Square_Foot', 'Price'], ascending=[True, True])
    print("Initial Data:")
    print(df)
    
    #The next two lines makes a plot
    #df.plot(x='Square_Foot', y='Price', linewidth=2.0, xlim=(1000,2500), ylim=(0,500))
    #plt.show()
    
    # Min-Max standardization 
    X = (df['Square_Foot'] - np.min(df['Square_Foot']) ) / (np.max(df['Square_Foot']) - np.min(df['Square_Foot']))
    Y = (df['Price'] - np.min(df['Price']) ) / (np.max(df['Price']) - np.min(df['Price']))
    
    print("Printing X:")
    print(X.round(2))
    
    print("Printing Y:")
    print(Y.round(2))
    

    
    def calculate_values(a, b):    
        # Ypred is the equation used to create the straight line
        YP = a + b * X 
        
        print("Printing YP:")
        print(YP.round(2))
        
        # SSE is the prediction error using the 1/2 square error equation
        SSE = 0.5 * ( ( Y - YP)**2  )
        
        print("Printing SSE:")
        print(SSE.round(3))
    
        print("Printing the summ SSE:")
        SSE_total = sum( SSE.round(3) )
        print(SSE_total)
        
        # Calculating the error gradient 
        dSSE_da_list = -( Y - YP)
        print("Printing the dSS_da:")
        print(dSSE_da_list.round(2))
        print("Printing the summ dSSE_da:")
        dSSE_da = sum( dSSE_da_list.round(3) )
        print(dSSE_da)
        
        dSSE_db_list = -( Y - YP)*X
        print("Printing the dSS_db:")
        print(dSSE_db_list.round(2))
        print("Printing the summ dSSE_db:")
        dSSE_db = sum( dSSE_db_list.round(3) )
        print(dSSE_db)
        return {'dSSE_da': dSSE_da, 'dSSE_db': dSSE_db, 'SSE': SSE_total}
    

    # a and b are random variables use to create a straight line that goes through the data points
    a = 0.45
    b = 0.75
    SSE = 0
    learning_rate = 0.01
    while SSE < 0.1:
        print("**********************\nRate of learning:")
        print(learning_rate)
        updated_values = calculate_values(a, b)
        
        if updated_values['SSE'] < 0.14 :
            SSE = updated_values['SSE']
         
        #Update the random variables a and b to minimize the error
        a = a - (learning_rate * updated_values['dSSE_da'])
        b = b - (learning_rate * updated_values['dSSE_db'])
        learning_rate = learning_rate + 0.01
        
    
    
    