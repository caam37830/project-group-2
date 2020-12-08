import pandas as pd

from datetime import datetime
# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.palettes import Spectral3


### Confirmed
# Note the data set is cumulative
confirmed_ds = pd.read_csv('time_series_covid19_confirmed_US.csv')
cov1 = confirmed_ds.loc[:, "1/22/20":"12/4/20"]
cov2 = confirmed_ds.loc[:, "Province_State"]
cov3 = pd.concat([cov2, cov1], axis=1)

# Compute the cumulative confirmed cases by states
cov_new = cov3.groupby('Province_State').sum()
#cov = cov_new.T





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
death_ts = pd.read_csv('time_series_covid19_deaths_US.csv')
death1 = death_ts.loc[:, "1/22/20":"12/4/20"]
death2 = death_ts.loc[:, "Province_State"]
death3 = pd.concat([death2, death1], axis=1)

# Compute the cumulative deaths by states
death_new = death3.groupby('Province_State').sum()
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

# Make interactive time series plot of daily deaths for states
source2 = ColumnDataSource(dth3)
p2 = figure(x_axis_type='datetime', title="Daily Deaths")
p2.line(x='new_date', y='Alabama', line_width=2, source=source2)
hover2 = HoverTool()
hover2.tooltips=[
    ('Death', '@Alabama'),
    ('Date', '@date')
]
p2.add_tools(hover2)
show(p2)

output_file("TsDailyDeath.html")
