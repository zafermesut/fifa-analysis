import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/data.csv')

st.title('FIFA 2019 Oyuncu Analizi')

player_name = st.selectbox('Select Player', data['Name'])

selected_player = data[data['Name'] == player_name]

if not selected_player.empty:
    st.subheader('Player Info')
    st.write(f"**Name:** {selected_player['Name'].values[0]}")
    st.write(f"**Age:** {selected_player['Age'].values[0]}")
    st.write(f"**Club:** {selected_player['Club'].values[0]}")
    st.write(f"**Position:** {selected_player['Position'].values[0]}")
    st.write(f"**Value:** {selected_player['Value'].values[0]}")
    st.write(f"**Wage:** {selected_player['Wage'].values[0]}")
    st.write(f"**General Evaluation:** {selected_player['Overall'].values[0]}")

    selected_mean = selected_player[['BallControl', 'Dribbling', 'ShortPassing', 'Penalties', 'Curve']].mean()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=selected_mean.index, y=selected_mean.values, palette="Blues_d")
    plt.title(f"{selected_player['Name'].values[0]} Skill Ratings", fontsize=16)
    plt.ylabel("Rating")
    plt.xlabel("Skill")
    plt.xticks(rotation=45)
    
    st.pyplot(plt)