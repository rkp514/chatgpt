import streamlit as st
import altair as alt
from vega_datasets import data

# Load data
source = data.stocks()

# Define a selection
symbol_selection = alt.selection_multi(fields=['symbol'])

# Define the chart
chart = alt.Chart(source).mark_line().encode(
    x='date:T',
    y='price:Q',
    color=alt.condition(symbol_selection, 'symbol:N', alt.value('lightgray'), legend=None),
    opacity=alt.condition(symbol_selection, alt.value(1), alt.value(0.1))
).add_selection(
    symbol_selection
).properties(
    width=800,
    height=400
)

# Add the legend
legend = alt.Chart(source).mark_point().encode(
    y=alt.Y('symbol:N', axis=alt.Axis(orient='right')),
    color=alt.Color('symbol:N', legend=None),
    size=alt.value(50),
    opacity=alt.condition(symbol_selection, alt.OpacityValue(1), alt.OpacityValue(0.1))
).add_selection(
    symbol_selection
)

# Combine the chart and the legend
combined_chart = chart | legend

# Display the chart in Streamlit
st.altair_chart(combined_chart, use_container_width=True)
