import pandas as pd
from dfply import *
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
source = ColumnDataSource(ds3)
p = figure(x_axis_type='datetime', title="Daily Confirmed Cases")
p.line(x='new_date', y='Alabama', line_width=2, source=source)
hover = HoverTool()
hover.tooltips=[
    ('Confirmed', '@Alabama'),
    ('Date', '@date')
]
p.add_tools(hover)
show(p)

output_file("TsDailyConfirmed.html")











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











