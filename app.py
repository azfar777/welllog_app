import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import welly
from welly import Well
import streamlit as st
from io import StringIO
from plotly.subplots import make_subplots

#Creating functions

def home_page():
    from PIL import Image
    image = Image.open("image.jpg")
    st.image(image, caption = "Basic well log interpretation")
    
def metadata():
    st.write("Meta data of the well")
    st.write("Please use the double arrow beside the data frame to expand the data frame")
    st.write("You can also drag the columns of the data frame to adjust the size of the columns")
    meta = well.header
    meta= meta.astype(str)
    st.write(meta)
    csv = meta.to_csv().encode('utf-8')
    st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
    
def wellinfo():
    st.write(well)

def datasummary():
    st.header("Summary of your log curve data")
    st.write(df.describe())
    st.write("Please use the double arrow beside the data frame to expand the data frame")
    st.write("You can also drag the columns of the data frame to adjust the size of the columns")
    a = df.describe()
    csv = a.to_csv().encode('utf-8')
    st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

def datahead():
    st.header("Log curve Data")
    st.write("Please use the double arrow beside the data frame to expand the data frame")
    st.write("You can also drag the columns of the data frame to adjust the size of the columns")
    st.write(df)
    csv = df.to_csv().encode('utf-8')
    st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
    
def indilog():
    st.header("Please select any log to display its information")
    value = st.selectbox('Select log',options = df.columns)
    a = well.data[value]
    st.write(a)
    
    
def plot():
    st.header("Please select the x-axis")
    col1, col2,col3,col4 = st.columns(4)
    a = df.reset_index()
    
    x_axis_val1 = col1.selectbox('Select the X-axis of first graph', options=a.columns)
    x_axis_val2 = col2.selectbox('Select the X-axis of second graph', options=a.columns)
    x_axis_val3 = col3.selectbox('Select the X-axis of third graph', options=a.columns)
    x_axis_val4 = col4.selectbox('Select the X-axis of fourth graph', options=a.columns)

    fig = make_subplots(rows=1, cols=4)

    fig.add_trace(
        go.Scatter(x=a[x_axis_val1], y=a["DEPT"]),
        row=1, col=1
        )

    fig.add_trace(
        go.Scatter(x=a[x_axis_val2], y=a["DEPT"]),
        row=1, col=2
        )
    fig.add_trace(
        go.Scatter(x=a[x_axis_val3], y=a["DEPT"]),
        row=1, col=3
        )
    fig.add_trace(
        go.Scatter(x=a[x_axis_val4], y=a["DEPT"]),
        row=1, col=4
        )
    fig.update_xaxes(title_text=x_axis_val1, row=1, col=1)
    fig.update_xaxes(title_text=x_axis_val2,row=1, col=2)
    fig.update_xaxes(title_text=x_axis_val3,row=1, col=3)
    fig.update_xaxes(title_text=x_axis_val4, row=1, col=4)

    fig.update_layout(height = 600, width = 800, title_text="Well log plots")
    st.plotly_chart(fig)
    
 


#Page title
st.title("Explore Your Well log data")
st.write("This is a web application where you can explore your well log data")
st.write("Please open the navigation bar to upload your file")

#Creating a sidebar
st.sidebar.title('Navigation')

uploaded_file = st.sidebar.file_uploader("Please upload your file here")



#Creating options for displaying information
options = st.sidebar.radio('Select what you want to display:', 
                           ['Home',"Metadata",'Well information','Curve Data','Curve data summary',
                            "Individual log information","Plots",'Parameters'])

#Opening the las file
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    well = Well.from_las(string_data)
    df = well.df()


    
    
if options == "Home":
    home_page()

elif options == "Metadata":
    metadata()

elif options == "Well information":
    wellinfo()
    
elif options == 'Curve data summary':
    datasummary()

elif options == "Curve Data":
    datahead()

elif options == "Plots":
    plot()
    
elif options == "Individual log information":
    indilog()
    
    
