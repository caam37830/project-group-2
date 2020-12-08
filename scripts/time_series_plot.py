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
#ds4 = ds3.rename_axis(None, axis = 1)


# Make interactive time series plot for states
source = ColumnDataSource(ds3)
p = figure(x_axis_type='datetime')
p.line(x='new_date', y='Alabama', line_width=2, source=source)
hover = HoverTool()
hover.tooltips=[
    ('Confirmed', '@Alabama'),
    ('Date', '@date')
]
p.add_tools(hover)
show(p)












### Deaths













