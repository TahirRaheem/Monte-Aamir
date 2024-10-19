import numpy as np
import plotly.figure_factory as ff
import streamlit as st

# Your simulation code remains the same...

if st.sidebar.button("Run Simulation"):
    # After running the simulation...
    
    # Plot total costs distribution using Plotly
    hist_data_cost = [total_costs]
    group_labels_cost = ['Total Costs']
    
    fig_cost = ff.create_distplot(hist_data_cost, group_labels_cost, bin_size=100)
    fig_cost.update_layout(title_text='Distribution of Total Project Costs')
    st.plotly_chart(fig_cost)
    
    # Plot total durations distribution using Plotly
    hist_data_duration = [total_durations]
    group_labels_duration = ['Total Durations']
    
    fig_duration = ff.create_distplot(hist_data_duration, group_labels_duration, bin_size=1)
    fig_duration.update_layout(title_text='Distribution of Total Project Durations (days)')
    st.plotly_chart(fig_duration)
