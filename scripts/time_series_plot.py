import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.palettes import Spectral3



### Confirmed

# Note the data set is cumulative
confirmed_ds = pd.read_csv('files/time_series_covid19_confirmed_US.csv')
cov1 = confirmed_ds.loc[:, "1/22/20":"12/4/20"]
cov2 = confirmed_ds.loc[:, "Province_State"]
cov3 = pd.concat([cov2, cov1], axis=1)

# Compute the cumulative confirmed cases by states
cov_new = cov3.groupby('Province_State').sum() 
cov = cov_new.T

# Compute daily confirmed cases
daily_ds = cov_new.diff(axis=1)
# Transpose data set
daily_ds_T = daily_ds.T
# Make row name as a column
ds2 = daily_ds_T.rename_axis("date").reset_index()

def date_convert(date_to_convert):
    """
    Convert date format to y-m-d
    """
    return datetime.strptime(date_to_convert, '%m/%d/%y')
    
# Convert date format
ds2['new_date'] = ds2['date'].apply(date_convert)
ds3 = ds2.set_index("new_date")
ds3.columns.name = None
ds3.columns = ds3.columns.str.replace(' ', '')
#ds4 = ds3.rename_axis(None, axis = 1)





# Plot cumulative confirmed cases for all states
fontP = FontProperties()
fontP.set_size('small')
cov.plot(figsize=(10, 6), title = "Cumulative Confirmed Cases of Covid-19 in US", 
         xlabel = "date", ylabel = "confirmed case")
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)






# Make interactive time series plot of daily confirmed for states

### West Coast: California, Oregon, Washington, Alaska
output_file("DailyWestCoast.html")

source2 = ColumnDataSource(ds3)

p_westcoast = figure(x_axis_type='datetime', title="Daily Confirmed Cases on West Coast", width = 800)

plot1 = p_westcoast.line(x='new_date', y='California', line_width=2, 
                         source=source2, color='skyblue', legend_label='California')

p_westcoast.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'California'),
                                    ('Confirmed case', '@California'),
                                    ('Date', '@date')
                                ]))

plot2 = p_westcoast.line(x='new_date', y='Oregon', line_width=2, 
                         source=source2, color='orange', legend_label='Oregon')

p_westcoast.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Oregon'),
                                    ('Confirmed case', '@Oregon'),
                                    ('Date', '@date')
                                ]))

plot3 = p_westcoast.line(x='new_date', y='Washington', line_width=2, 
                         source=source2, color='green', legend_label='Washington')

p_westcoast.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Washington'),
                                    ('Confirmed case', '@Washington'),
                                    ('Date', '@date')
                                ]))

plot4 = p_westcoast.line(x='new_date', y='Alaska', line_width=2, 
                         source=source2, color='violet', legend_label='Alaska')

p_westcoast.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Alaska'),
                                    ('Confirmed case', '@Alaska'),
                                    ('Date', '@date')
                                ]))


p_westcoast.legend.location = 'top_left'

show(p_westcoast)



### Northeast: Maine, New Hampshire, Vermont, Massachusetts, Rhode Island, Connecticut,
###            New York, New Jersey, and Pennsylvania.

output_file("DailyNorthEast.html")

source3 = ColumnDataSource(ds3)


p_Northeast = figure(x_axis_type='datetime', title="Daily Confirmed Cases of Northeast", width = 800)


plot1 = p_Northeast.line(x='new_date', y='Maine', line_width=2, 
                         source=source3, color='skyblue', legend_label='Maine')

p_Northeast.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Maine'),
                                    ('Confirmed case', '@Maine'),
                                    ('Date', '@date')
                                ]))

plot2 = p_Northeast.line(x='new_date', y='NewHampshire', line_width=2, 
                         source=source3, color='orange', legend_label='New Hampshire')

p_Northeast.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'New Hampshire'),
                                    ('Confirmed case', '@NewHampshire'),
                                    ('Date', '@date')
                                ]))

plot3 = p_Northeast.line(x='new_date', y='Vermont', line_width=2, 
                         source=source3, color='green', legend_label='Vermont')

p_Northeast.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Vermont'),
                                    ('Confirmed case', '@Vermont'),
                                    ('Date', '@date')
                                ]))

plot4 = p_Northeast.line(x='new_date', y='Massachusetts', line_width=2, 
                         source=source3, color='violet', legend_label='Massachusetts')

p_Northeast.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Massachusetts'),
                                    ('Confirmed case', '@Massachusetts'),
                                    ('Date', '@date')
                                ]))

plot5 = p_Northeast.line(x='new_date', y='RhodeIsland', line_width=2, 
                         source=source3, color='orangered', legend_label='Rhode Island')

p_Northeast.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Rhode Island'),
                                    ('Confirmed case', '@RhodeIsland'),
                                    ('Date', '@date')
                                ]))


plot6 = p_Northeast.line(x='new_date', y='Connecticut', line_width=2, 
                         source=source3, color='brown', legend_label='Connecticut')

p_Northeast.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Connecticut'),
                                    ('Confirmed case', '@Connecticut'),
                                    ('Date', '@date')
                                ]))


plot7 = p_Northeast.line(x='new_date', y='NewYork', line_width=2, 
                 source=source3, color='pink', legend_label='New York')

p_Northeast.add_tools(HoverTool(renderers=[plot7], 
                                tooltips=[
                                    ('State', 'New York'),
                                    ('Confirmed case', '@NewYork'),
                                    ('Date', '@date')
                                ]))

plot8 = p_Northeast.line(x='new_date', y='NewJersey', line_width=2, 
                         source=source3, color='grey', legend_label='New Jersey')

p_Northeast.add_tools(HoverTool(renderers=[plot8], 
                                tooltips=[
                                    ('State', 'New Jersey'),
                                    ('Confirmed case', '@NewJersey'),
                                    ('Date', '@date')
                                ]))


plot9 = p_Northeast.line(x='new_date', y='Pennsylvania', line_width=2, 
                         source=source3, color='khaki', legend_label='Pennsylvania')

p_Northeast.add_tools(HoverTool(renderers=[plot9], 
                                tooltips=[
                                    ('State', 'Pennsylvania'),
                                    ('Confirmed case', '@Pennsylvania'),
                                    ('Date', '@date')
                                ]))


p_Northeast.legend.location = 'top_left'

show(p_Northeast)





### Midwest: Ohio, Michigan, Indiana, Illinois, Missouri, Nebraska
output_file("DailyMidwest.html")

source4 = ColumnDataSource(ds3)

p_Midwest = figure(x_axis_type='datetime', title="Daily Confirmed Cases of Midwest", width = 800)


plot1 = p_Midwest.line(x='new_date', y='Ohio', line_width=2, 
                         source=source4, color='skyblue', legend_label='Ohio')

p_Midwest.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Ohio'),
                                    ('Confirmed case', '@Ohio'),
                                    ('Date', '@date')
                                ]))

plot2 = p_Midwest.line(x='new_date', y='Michigan', line_width=2, 
                         source=source4, color='orange', legend_label='Michigan')

p_Midwest.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Michigan'),
                                    ('Confirmed case', '@Michigan'),
                                    ('Date', '@date')
                                ]))

plot3 = p_Midwest.line(x='new_date', y='Indiana', line_width=2, 
                         source=source4, color='green', legend_label='Indiana')

p_Midwest.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Indiana'),
                                    ('Confirmed case', '@Indiana'),
                                    ('Date', '@date')
                                ]))

plot4 = p_Midwest.line(x='new_date', y='Illinois', line_width=2, 
                         source=source4, color='violet', legend_label='Illinois')

p_Midwest.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Illinois'),
                                    ('Confirmed case', '@Illinois'),
                                    ('Date', '@date')
                                ]))

plot5 = p_Midwest.line(x='new_date', y='Missouri', line_width=2, 
                         source=source4, color='orangered', legend_label='Missouri')

p_Midwest.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Missouri'),
                                    ('Confirmed case', '@Missouri'),
                                    ('Date', '@date')
                                ]))


plot6 = p_Midwest.line(x='new_date', y='Nebraska', line_width=2, 
                         source=source4, color='brown', legend_label='Nebraska')

p_Midwest.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Nebraska'),
                                    ('Confirmed case', '@Nebraska'),
                                    ('Date', '@date')
                                ]))


p_Midwest.legend.location = 'top_left'

show(p_Midwest)





### South: Delaware, Maryland, Virginia, Tennessee, Alabama, Florida, Mississippi, Texas

output_file("DailySouth.html")

source5 = ColumnDataSource(ds3)

p_South = figure(x_axis_type='datetime', title="Daily Confirmed Cases of South", width = 800)


plot1 = p_South.line(x='new_date', y='Delaware', line_width=2, 
                         source=source5, color='skyblue', legend_label='Delaware')

p_South.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Delaware'),
                                    ('Confirmed case', '@Delaware'),
                                    ('Date', '@date')
                                ]))

plot2 = p_South.line(x='new_date', y='Maryland', line_width=2, 
                         source=source5, color='orange', legend_label='Maryland')

p_South.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Maryland'),
                                    ('Confirmed case', '@Maryland'),
                                    ('Date', '@date')
                                ]))

plot3 = p_South.line(x='new_date', y='Tennessee', line_width=2, 
                         source=source5, color='green', legend_label='Tennessee')

p_South.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Tennessee'),
                                    ('Confirmed case', '@Tennessee'),
                                    ('Date', '@date')
                                ]))

plot4 = p_South.line(x='new_date', y='Virginia', line_width=2, 
                         source=source5, color='violet', legend_label='Virginia')

p_South.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Virginia'),
                                    ('Confirmed case', '@Virginia'),
                                    ('Date', '@date')
                                ]))

plot5 = p_South.line(x='new_date', y='Alabama', line_width=2, 
                         source=source5, color='orangered', legend_label='Alabama')

p_South.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Alabama'),
                                    ('Confirmed case', '@Alabama'),
                                    ('Date', '@date')
                                ]))


plot6 = p_South.line(x='new_date', y='Florida', line_width=2, 
                         source=source5, color='brown', legend_label='Florida')

p_South.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Florida'),
                                    ('Confirmed case', '@Florida'),
                                    ('Date', '@date')
                                ]))


plot7 = p_South.line(x='new_date', y='Mississippi', line_width=2, 
                         source=source5, color='pink', legend_label='Mississippi')

p_South.add_tools(HoverTool(renderers=[plot7], 
                                tooltips=[
                                    ('State', 'Mississippi'),
                                    ('Confirmed case', '@Mississippi'),
                                    ('Date', '@date')
                                ]))


plot8 = p_South.line(x='new_date', y='Texas', line_width=2, 
                         source=source5, color='grey', legend_label='Texas')

p_South.add_tools(HoverTool(renderers=[plot8], 
                                tooltips=[
                                    ('State', 'Texas'),
                                    ('Confirmed case', '@Texas'),
                                    ('Date', '@date')
                                ]))



p_South.legend.location = 'top_left'

show(p_South)












### Deaths

# Note the data set is cumulative
death_ts = pd.read_csv('files/time_series_covid19_deaths_US.csv')
death1 = death_ts.loc[:, "1/22/20":"12/4/20"]
death2 = death_ts.loc[:, "Province_State"]
death3 = pd.concat([death2, death1], axis=1)

# Compute the cumulative deaths by states
death_new = death3.groupby('Province_State').sum() 
death_cum = death_new.T

# Compute daily death cases
daily_death = death_new.diff(axis=1)

# Transpose data set
daily_death_T = daily_death.T
# Make row name as a column
dth2 = daily_death_T.rename_axis("date").reset_index()

# Convert date format
dth2['new_date'] = dth2['date'].apply(date_convert)
dth3 = dth2.set_index("new_date")
dth3.columns.name = None
dth3.columns = ds3.columns.str.replace(' ', '')



# Plot cumulative deaths for all states
fontP1 = FontProperties()
fontP1.set_size('small')
death_cum.plot(figsize=(10, 6), title = "Cumulative Deaths of Covid-19 in US", 
                   xlabel = "date", ylabel = "death")
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP1)





# Make interactive time series plot of daily deaths for states

### West Coast: California, Oregon, Washington, Alaska
output_file("DeathWestCoast.html")

source22 = ColumnDataSource(dth3)

d_westcoast = figure(x_axis_type='datetime', title="Daily Deaths on West Coast", width = 800)

plot1 = d_westcoast.line(x='new_date', y='California', line_width=2, 
                         source=source22, color='skyblue', legend_label='California')

d_westcoast.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'California'),
                                    ('Death', '@California'),
                                    ('Date', '@date')
                                ]))

plot2 = d_westcoast.line(x='new_date', y='Oregon', line_width=2, 
                         source=source22, color='orange', legend_label='Oregon')

d_westcoast.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Oregon'),
                                    ('Death', '@Oregon'),
                                    ('Date', '@date')
                                ]))

plot3 = d_westcoast.line(x='new_date', y='Washington', line_width=2, 
                         source=source22, color='green', legend_label='Washington')

d_westcoast.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Washington'),
                                    ('Death', '@Washington'),
                                    ('Date', '@date')
                                ]))

plot4 = d_westcoast.line(x='new_date', y='Alaska', line_width=2, 
                         source=source22, color='violet', legend_label='Alaska')

d_westcoast.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Alaska'),
                                    ('Death', '@Alaska'),
                                    ('Date', '@date')
                                ]))


d_westcoast.legend.location = 'top_left'

show(d_westcoast)



### Northeast: Maine, New Hampshire, Vermont, Massachusetts, Rhode Island, Connecticut,
###            New York, New Jersey, and Pennsylvania.

output_file("DeathNorthEast.html")

source33 = ColumnDataSource(dth3)


d_Northeast = figure(x_axis_type='datetime', title="Daily Deaths of Northeast", width = 800)


plot1 = d_Northeast.line(x='new_date', y='Maine', line_width=2, 
                         source=source33, color='skyblue', legend_label='Maine')

d_Northeast.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Maine'),
                                    ('Death', '@Maine'),
                                    ('Date', '@date')
                                ]))

plot2 = d_Northeast.line(x='new_date', y='NewHampshire', line_width=2, 
                         source=source33, color='orange', legend_label='New Hampshire')

d_Northeast.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'New Hampshire'),
                                    ('Death', '@NewHampshire'),
                                    ('Date', '@date')
                                ]))

plot3 = d_Northeast.line(x='new_date', y='Vermont', line_width=2, 
                         source=source33, color='green', legend_label='Vermont')

d_Northeast.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Vermont'),
                                    ('Death', '@Vermont'),
                                    ('Date', '@date')
                                ]))

plot4 = d_Northeast.line(x='new_date', y='Massachusetts', line_width=2, 
                         source=source33, color='violet', legend_label='Massachusetts')

d_Northeast.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Massachusetts'),
                                    ('Death', '@Massachusetts'),
                                    ('Date', '@date')
                                ]))

plot5 = d_Northeast.line(x='new_date', y='RhodeIsland', line_width=2, 
                         source=source33, color='orangered', legend_label='Rhode Island')

d_Northeast.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Rhode Island'),
                                    ('Death', '@RhodeIsland'),
                                    ('Date', '@date')
                                ]))


plot6 = d_Northeast.line(x='new_date', y='Connecticut', line_width=2, 
                         source=source33, color='brown', legend_label='Connecticut')

d_Northeast.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Connecticut'),
                                    ('Death', '@Connecticut'),
                                    ('Date', '@date')
                                ]))


plot7 = d_Northeast.line(x='new_date', y='NewYork', line_width=2, 
                 source=source33, color='pink', legend_label='New York')

d_Northeast.add_tools(HoverTool(renderers=[plot7], 
                                tooltips=[
                                    ('State', 'New York'),
                                    ('Death', '@NewYork'),
                                    ('Date', '@date')
                                ]))

plot8 = d_Northeast.line(x='new_date', y='NewJersey', line_width=2, 
                         source=source33, color='grey', legend_label='New Jersey')

d_Northeast.add_tools(HoverTool(renderers=[plot8], 
                                tooltips=[
                                    ('State', 'New Jersey'),
                                    ('Death', '@NewJersey'),
                                    ('Date', '@date')
                                ]))


plot9 = d_Northeast.line(x='new_date', y='Pennsylvania', line_width=2, 
                         source=source33, color='khaki', legend_label='Pennsylvania')

d_Northeast.add_tools(HoverTool(renderers=[plot9], 
                                tooltips=[
                                    ('State', 'Pennsylvania'),
                                    ('Death', '@Pennsylvania'),
                                    ('Date', '@date')
                                ]))


d_Northeast.legend.location = 'top_left'

show(d_Northeast)




### Midwest: Ohio, Michigan, Indiana, Illinois, Missouri, Nebraska
output_file("DeathMidwest.html")

source44 = ColumnDataSource(dth3)

d_Midwest = figure(x_axis_type='datetime', title="Daily Deaths of Midwest", width = 800)


plot1 = d_Midwest.line(x='new_date', y='Ohio', line_width=2, 
                         source=source44, color='skyblue', legend_label='Ohio')

d_Midwest.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Ohio'),
                                    ('Death', '@Ohio'),
                                    ('Date', '@date')
                                ]))

plot2 = d_Midwest.line(x='new_date', y='Michigan', line_width=2, 
                         source=source44, color='orange', legend_label='Michigan')

d_Midwest.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Michigan'),
                                    ('Death', '@Michigan'),
                                    ('Date', '@date')
                                ]))

plot3 = d_Midwest.line(x='new_date', y='Indiana', line_width=2, 
                         source=source44, color='green', legend_label='Indiana')

d_Midwest.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Indiana'),
                                    ('Death', '@Indiana'),
                                    ('Date', '@date')
                                ]))

plot4 = d_Midwest.line(x='new_date', y='Illinois', line_width=2, 
                         source=source44, color='violet', legend_label='Illinois')

d_Midwest.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Illinois'),
                                    ('Death', '@Illinois'),
                                    ('Date', '@date')
                                ]))

plot5 = d_Midwest.line(x='new_date', y='Missouri', line_width=2, 
                         source=source44, color='orangered', legend_label='Missouri')

d_Midwest.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Missouri'),
                                    ('Death', '@Missouri'),
                                    ('Date', '@date')
                                ]))


plot6 = d_Midwest.line(x='new_date', y='Nebraska', line_width=2, 
                         source=source44, color='brown', legend_label='Nebraska')

d_Midwest.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Nebraska'),
                                    ('Death', '@Nebraska'),
                                    ('Date', '@date')
                                ]))


d_Midwest.legend.location = 'top_left'

show(d_Midwest)





### South: Delaware, Maryland, Virginia, Tennessee, Alabama, Florida, Mississippi, Texas

output_file("DeathSouth.html")

source55 = ColumnDataSource(dth3)

d_South = figure(x_axis_type='datetime', title="Daily Deaths of South", width = 800)


plot1 = d_South.line(x='new_date', y='Delaware', line_width=2, 
                         source=source55, color='skyblue', legend_label='Delaware')

d_South.add_tools(HoverTool(renderers=[plot1], 
                                tooltips=[
                                    ('State', 'Delaware'),
                                    ('Death', '@Delaware'),
                                    ('Date', '@date')
                                ]))

plot2 = d_South.line(x='new_date', y='Maryland', line_width=2, 
                         source=source55, color='orange', legend_label='Maryland')

d_South.add_tools(HoverTool(renderers=[plot2], 
                                tooltips=[
                                    ('State', 'Maryland'),
                                    ('Death', '@Maryland'),
                                    ('Date', '@date')
                                ]))

plot3 = d_South.line(x='new_date', y='Tennessee', line_width=2, 
                         source=source55, color='green', legend_label='Tennessee')

d_South.add_tools(HoverTool(renderers=[plot3], 
                                tooltips=[
                                    ('State', 'Tennessee'),
                                    ('Death', '@Tennessee'),
                                    ('Date', '@date')
                                ]))

plot4 = d_South.line(x='new_date', y='Virginia', line_width=2, 
                         source=source55, color='violet', legend_label='Virginia')

d_South.add_tools(HoverTool(renderers=[plot4], 
                                tooltips=[
                                    ('State', 'Virginia'),
                                    ('Death', '@Virginia'),
                                    ('Date', '@date')
                                ]))

plot5 = d_South.line(x='new_date', y='Alabama', line_width=2, 
                         source=source55, color='orangered', legend_label='Alabama')

d_South.add_tools(HoverTool(renderers=[plot5], 
                                tooltips=[
                                    ('State', 'Alabama'),
                                    ('Death', '@Alabama'),
                                    ('Date', '@date')
                                ]))


plot6 = d_South.line(x='new_date', y='Florida', line_width=2, 
                         source=source55, color='brown', legend_label='Florida')

d_South.add_tools(HoverTool(renderers=[plot6], 
                                tooltips=[
                                    ('State', 'Florida'),
                                    ('Death', '@Florida'),
                                    ('Date', '@date')
                                ]))


plot7 = d_South.line(x='new_date', y='Mississippi', line_width=2, 
                         source=source55, color='pink', legend_label='Mississippi')

d_South.add_tools(HoverTool(renderers=[plot7], 
                                tooltips=[
                                    ('State', 'Mississippi'),
                                    ('Death', '@Mississippi'),
                                    ('Date', '@date')
                                ]))


plot8 = d_South.line(x='new_date', y='Texas', line_width=2, 
                         source=source55, color='grey', legend_label='Texas')

d_South.add_tools(HoverTool(renderers=[plot8], 
                                tooltips=[
                                    ('State', 'Texas'),
                                    ('Death', '@Texas'),
                                    ('Date', '@date')
                                ]))



d_South.legend.location = 'top_left'

show(d_South)













