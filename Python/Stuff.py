# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:23:43 2019

@author: u2jd7fu
"""

# python general ----------------------------------------------------------------------------------------

#variables changed in a function are partly unchanged; tired it with np array -> unchanged; list -> changed - outside of the function

# dataframes ------------------------------------------------------------------------------------------------

# pd.set_option('display.max_rows', 500)


# list_mcc = df_mcc_sum['mcc'][:20].values slicing dataframes
#syntax: df[slice/list or single column_name][slice of integer positions of rows]
# this works as well: df[slice of integer positions of rows] ... selects the rows for the whole df

# df.loc[slice/list or sthg of row labels, slice/list of column labels] ... these are really the labels, not the integer positions
# df.iloc[slice/list single intger row position, slice/list or single integer column position] 0-based indexing. When slicing, the start bound is included, while the upper bound is excluded.


# def is_hot_dry(temp, humid):
#     if (temp > 0.8) & (humid < -0.5):
#         return 1
#     else:
#         return 0
# df['hot'] = df.apply(lambda x: is_hot_dry(x['avgTemp'], x['avgHumidity']), axis =  1) put output of function with 2 df columsn as arguments into new column

# group df by 1 column and get a new df for which you specify how the columns are aggregated
# column_list = ['city_id',  'purchases', '_year', '_month', '_day', '_date', 'Transaktionscode', 'MCC',  'umsatz', 'online', 'mobilfunker']
# agg_dict = { 'city_id': 'first',  'purchases': 'sum', '_year': 'first', '_month': 'first', '_day': 'first', '_date': 'first', 'Transaktionscode': 'first', 'MCC': 'first',  'umsatz': 'sum', 'online': 'first', 'mobilfunker': 'first' }
# df = df.groupby('_date')[column_list].agg( agg_dict ).reset_index(drop=True)

#df = df.loc[ df['Merchantname'].str.contains('Shop', case=False) ] loc on part of string ignoring upper and lower case
#df = df.loc[ ~df['Merchantname'].str.contains('Shop', case=False) ] same for excluding these elements



# df_shop = df_join_weekday.loc[ df_join['dealerID_Long'] == 2870000, 'dealerID_Long':'wind' ]
# gb_join_weekday = df_join.groupby('weekday')['purchases'].sum()
# gb_weekday.plot(kind='bar')
# gb_weekday = df.groupby('_month')[['purch_ga_hvv_res','purch_ae_access_bbi','purch_ga_netcube']].sum().plot(kind='bar') more than 1 bar per group
# df_agg.set_index("dealerID_Long", inplace=True)
# print(df_orig.groupby('DealerID_Long').count()) count unique values in dataframe column
# df.purchases.sum(axis=0) sum over 1 column
# df_cat = df_date.loc[ (df_date['Kategorie'] == 'None') | (df_date['Kategorie'].isnull()) ] # select compley boolean statement for loc with | and & not (or, and)

# for ind,row in df_merged.iterrows(): iterating over dataframes rows and in the process adding values to a new column
#     df_merged.loc[ind,'new-column_name'] = counter

# df_shop_station_match = pd.DataFrame(columns=[ 'city_id', '_city_name', 'Dealer_latitude','Dealer_longitude', 'dealer_name', 'DealerID_Long'])
# df_shop_station_match.loc[counter] = [close_city_id, close_city_name, row['Dealer_latitude'],row['Dealer_longitude'], row['dealer_name'], row['DealerID_Long']]
    # using loc to iteratively fill a dataframe

# df_city.loc[ : , new_target_name ] = pd.Series(new_target_data[:,0], index=df_city.index) using loc for filling a df column with a numpy array

# df_east_1.loc[:, 'holiday_week'] = df_east_1['calendar_week'].values - 26 # setting values for new column with another column
# df['kda'] = np.where(df['deaths']>0, (df['kills'] + df['assists']) / df['deaths'], df['kills'] + df['assists']) # set new column values with condition on old column

#df.loc[:, target_variable] = df[target_name_list].sum(axis=1) new column as sum of several other columns


# df_new = df_f.iloc[0:0] erase all data in a dataframe

# df_new = df.iloc[0:0] 
# df_new.loc[:,'A'] = df.loc[:,'A'] copy values for the whole column from df to df new; also copies index from df

#corrMatrix = df_shop.corr() 
#sns.heatmap(corrMatrix,annot=True)
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)

# pd.plotting.scatter_matrix(df)
# pd.plotting.autocorrelation_plot(df_f[variable_to_plot])


#corrList = df_join_weekday.corr()['purchases'][1:] only correlation with 1 variable
#corrList.plot(kind='bar')

# dum = df.groupby( ['_year','_weekday'] )['purchases_total'].sum().unstack(level=0) plot heatmap of data grouped by 2 attributes
# sns.heatmap(dum, cmap='viridis',annot=True)
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)

# df_city.plot(x='_date', y=target_variable, style='.') point plot with datetime x axis (parse dates in read statement); not possible to use c= column
# style format = marker line color '.-g'

# df.boxplot('in_count_mall', by='_month') # box plot a dataframe


#plotting ------------------------------------------------------------------------------------------------

# fig, axs = plt.subplots(1,3)
# axs[0].scatter(x,y)
# axs[0].set(xlabel='x', ylabel='y')

#scatter plot with trend line:
# xString = 'unixTime'
# yString = 'purchases'
# x=df_join_weekday[xString]
# y=df_join_weekday[yString]
# plt.scatter(x, y)
# plt.xlabel(xString)
# plt.ylabel(yString)
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plb.plot(x, p(x), 'm-')
# plt.show()

# pd.plotting.scatter_matrix(df_draw, alpha=0.2, figsize=(10, 10),diagonal='kde') # plotting a scatter matrix from a data frame
# plt.show()

# plot all columns of df with labels and stuff
#df_weather.plot('DATE')

# plot all the columns of a groupby object (= without selection of a column after ('_weekday'))
# gb = df.groupby('_weekday').count()

# for i in range(6): plotting several subplots in 1 figure
#     ax = plt.subplot(3, 2, i+1)
#     df.plot.scatter(x=column_list[i],y='purchases_mall',c='_weekday', colormap = 'viridis', ax=ax)

# fig, ax = plt.subplots()
# for name, group in df.groupby('_year'):
#     group.plot(x='day_year', y='purchases_total', ax=ax, label=name) plot values of a column grouped by values of another column into a single plot

# df['N'].hist(by=df['Letter']) hists of column N grouped by the column letter - seperate hist for each letter

# gb = df.groupby(['Kategorie','_month'],as_index='False')[['purchases']].sum()
# gb.unstack(level=0).plot(kind='bar', subplots=True) plot multiindex dataframe from line above as barplot with several subplots

# fig, ax1 = plt.subplots() plot a second column with seperate y axis in same plot
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
# df.plot(x='_date', y= 'in_counts', ax = ax1, color = 'tab:blue')
# df.plot(x='_date', y= 'avgTemp', ax = ax2, color = 'tab:red')
# plt.show()

# df.plot(y = 'in_counts', ax = ax1, color = 'tab:blue', use_index = True) plot column vs index


# params = {'font.size': 10, #adjusting plot properties
#         'legend.fontsize': 'xx-small',
#         'axes.labelsize': 'xx-small',
#         'axes.titlesize':'xx-small',
#         'xtick.labelsize':'xx-small',
#         'ytick.labelsize':'xx-small'}
# plt.rcParams.update(params)
# plt.subplots_adjust(wspace=0.4, hspace=0.4) # width and height space
# plt.savefig( pltString, dpi=300 )

# fit data with self defined function
# from scipy.optimize import curve_fit 
# def func(x, a, b, c):
#     return a / x + b + c * x
# popt, pcov = curve_fit(func, df['shop_sum_scaled'], df['in_buy_ratio'])
# plt.plot(df['shop_sum_scaled'], func(df['shop_sum_scaled'], *popt), 'r.')


# datetime stuff ---------------------------------------------------------

# date_list = df['_date'].unique()  select unique dates and convert to pandas datetime
# date_list = pd.to_datetime(date_list)

# or date_list = date_list.astype('M8[D]')

# import matplotlib.dates as mdates #formatting date axis
# months = mdates.MonthLocator()
# days = mdates.DayLocator(interval = 10)
# months_fmt = mdates.DateFormatter('%Y-%m')
# days_fmt = mdates.DateFormatter('%d')
# ax.xaxis.set_major_locator(months)
# ax.xaxis.set_minor_locator(days)
# ax.xaxis.set_major_formatter(months_fmt)
# ax.xaxis.set_minor_formatter(days_fmt)


# Lists -----------------------------------------------------------------------------------------------

# list_not_mall = [sum(a) for a in zip(list_urban, list_periphery)] elementwise summation of 2 lists
# sort_ind[-10:] last 10 elemnts of numpy array
# a = [2 if x < 4 else x for x in a ]
# b = [2 for x in a if x < 4]

# new_infections = [y - x for x,y in zip(tot_infections,tot_infections[1:])] # subtract preious element in list


# groupby -----------------------------------------------------------------------------------------------------------

# df.groupby(pd.cut( df["avgTemp"], np.arange(15, 40, 5) ))['purchases_mall'].mean() groupby numerical value (avgTemp)


# dicts -------------------------------------------------------------------

# {key: value for (key, value) in iterable}

# statistics ----------------------------------------------------------------

# r, pval_p = stat.pearsonr(df['in_counts'].values, df['purchases5651'].values)
# print('pearson r:', r, 'pearson pval:', pval_p)

# rho, pval = stat.spearmanr(df['in_counts'].values, df['purchases5651'].values)
# print('spearman rho:', rho, 'spearman pval:', pval )


# strings -------------------------------------------------------------------

# axs[2].set_title('pearson_r: ' + str( np.around(r1,3) ) + ' , p_val: ' +  '{:.1e}'.format(pval_p3) )
