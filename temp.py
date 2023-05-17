import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Value': [10, 20, 30],
    'Subcategory': ['A1', 'B1', 'C1'],
    'Subvalue': [5, 15, 25]
})

# Render the initial pie chart
def render_chart(df):
    fig = go.Figure(data=[go.Pie(labels=df['Category'], values=df['Value'])])
    st.plotly_chart(fig)

# Render the subcategory pie chart
def render_subchart(df):
    fig = go.Figure(data=[go.Pie(labels=df['Subcategory'], values=df['Subvalue'])])
    st.plotly_chart(fig)

# Main app
def main():
    st.title("Pie Chart Drilldown")

    # Render the initial pie chart
    render_chart(data)

    # Check if the user wants to drill down
    if st.button("Drill down"):
        # Render the subcategory pie chart
        render_subchart(data)

if __name__ == '__main__':
    main()
