import streamlit as st
import altair as alt
import pandas as pd

# Create example data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value1': [10, 20, 30, 40, 50],
    'value2': [20, 30, 40, 50, 60],
    'value3': [30, 40, 50, 60, 70],
})

# Melt the data into long format
melted_data = pd.melt(data, id_vars=['category'], var_name='variable', value_name='value')

# Define a selection
category_selection = alt.selection_multi(fields=['category'])

# Define the chart
chart = alt.Chart(melted_data).mark_bar().encode(
    x='variable:N',
    y='sum(value):Q',
    color=alt.Color('category:N'),
    opacity=alt.condition(category_selection, alt.value(1), alt.value(0.1))
).add_selection(
    category_selection
).properties(
    width=800,
    height=400
)

# Add the legend
legend = alt.Chart(melted_data).mark_rect().encode(
    y=alt.Y('category:N', axis=alt.Axis(orient='right')),
    color=alt.Color('category:N'),
    opacity=alt.condition(category_selection, alt.OpacityValue(1), alt.OpacityValue(0.1))
).add_selection(
    category_selection
)

# Combine the chart and the legend
combined_chart = chart | legend

# Display the chart in Streamlit
st.altair_chart(combined_chart, use_container_width=True)
