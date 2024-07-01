def prepare_data(training_data, new_data):
    #fill 'housold income'
    my_data = new_data.copy()
    train_median = training_data['household_income'].median()
    my_data['household_income'].fillna(train_median,inplace = True)
    my_data['specialProperty'] = my_data['blood_type'].isin(['O+', 'B+'])
    my_data = my_data.drop('blood_type', axis=1)
    min_max_scale = ['PCR_03', 'PCR_10']
    for column in min_max_scale:
        maxval = training_data[column].max()
        minval = training_data[column].min()
        my_data[column] = -1 + (my_data[column] - minval) * (1 - (-1)) / (maxval - minval)
    standard_scale = ['PCR_01','PCR_02','PCR_04','PCR_05','PCR_06','PCR_07','PCR_08','PCR_09']
    for column in standard_scale:
        average = training_data[column].mean()
        std = training_data[column].std()
        my_data[column] = (my_data[column] - average)/std
    return my_data
