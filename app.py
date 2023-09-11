import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
st.set_page_config(page_icon="bar_chart",
                   page_title="Forbes 2022 Billionaire list Analysis",layout="wide",
                   initial_sidebar_state="collapsed")
st.title("FORBES 2022 BILLIONAIRES LISTS")
df= pd.read_csv("forbes_2022_billionaires.csv")
df["Networth"] = df["Networth"].apply(lambda x: float(x.split(" ")[0].replace("$"," ").strip()))
df["Age"] = df["Age"].apply(lambda x:np.nan if x == 0 else x)
col1,col2=st.columns(2)
with col1:
    sorted_by_age = df.sort_values("Age", ascending=False)
    oldest_billionares = sorted_by_age.head(10)
    fig = px.bar(oldest_billionares, x="Name", y="Networth", color="Age", title="Top 10 oldest Billionaires",
                 hover_name="Age")
    fig.update_layout(title=dict(xanchor='center', yanchor="top", x=0.4, y=0.9, font=dict(size=30)),
                      font_color="blueviolet",
                      legend_title_font_color="Black", title_font_color="lightblue",
                      height=500,width=500)
    fig.update_layout( {'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
    fig.update_yaxes(title="Networth in Billions", title_font_color="blueviolet", tickfont=dict(color="darkblue"))
    fig.update_xaxes(title="Bilionaires names", title_font_color="blueviolet", tickfont=dict(color="darkblue"))
    st.plotly_chart(fig)
    st.write("The oldest billionaire is George Joseph with a networth of 1.8 Billions and is aged 100 years old,fellowed by Robert kuok whose networth is 11.7 Billions and aged 98 years old")

with col2:
    sort_age = df.sort_values("Age", ascending=True)
    top_10 = sort_age.head(10)
    fig = px.bar(top_10, x="Name", y="Networth", color="Age", title="Top 10 Youngest Billionaires", hover_name="Age")
    fig.update_layout(title=dict(xanchor='center', yanchor="top", x=0.4, y=0.9, font=dict(size=30)),
                      font_color="blueviolet",
                      legend_title_font_color="Black", title_font_color="lightblue",
                      width=500,
                      height=500)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
    fig.update_yaxes(title="Networth in Billions", title_font_color="blueviolet", tickfont=dict(color="darkblue"))
    fig.update_xaxes(title="Bilionaires names", title_font_color="blueviolet", tickfont=dict(color="darkblue"))
    st.plotly_chart(fig)
    st.write(
        "The Youngest billionaire is Kevin David Lehmann with a networth of 2.4 Billions and is aged 19 years old,fellowed by Pedro Faranceschi whose networth is 1.5 Billions and aged 25 years old")

age_distribution = df.groupby(["Age"]).size().reset_index()
fig = px.histogram(df, x="Age", color="Age", title="Age distribution")
fig.update_layout(title=dict(xanchor='center', yanchor="top", x=0.5, y=0.9, font=dict(size=30)),
                  font_color="blueviolet",
                  title_font_color="lightblue",
                  height=600,
                  width=1200)
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
fig.update_xaxes(title_font_color="blueviolet", tickfont=dict(color="darkblue"))
fig.update_yaxes(title_font_color="blueviolet", tickfont=dict(color="darkblue"))
st.plotly_chart(fig)
st.write("The youngest Billionaire is aged 19 Years old ,while oldest Billionaire is aged 100 Years old")
st.write("Most of the Billionaires are aged between 50 and 80 years old")
st.write("Most of top Billionaires are aged 64 years")
col5,col6=st.columns(2)
with col5:
    st.subheader("The number of Male vs Female Billionares")
    m_vs_f = df.groupby(["Gender"]).size().reset_index(name="Numbers")
    fig = px.pie(m_vs_f, names="Gender", values="Numbers", color="Numbers")
    fig.update_traces(hole=.5, textinfo='percent+label')
    fig.update_layout(
                      font_color="blueviolet",
                      legend=dict(title="Gender", title_font_color="black"))
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
    st.plotly_chart(fig)
    st.write("There are more Male Billionaires than Female Billionaires")
    st.write("Male are represented with a percentage of 88.3% while Female are 11.7%")
    st.write ("The total number of Male Billionaires are 2341 while The total number of Female Billionaires is 311")
with col6:
    st.subheader("Countries with highest number of female billionaires")
    female = df[df["Gender"] == "F"]
    contries_f = female.groupby(["Country"]).size().reset_index(name="Number of females")
    sorted = contries_f.sort_values('Number of females', ascending=False)
    top_10 = sorted.head(10)
    fig = fig = px.pie(top_10, values='Number of females', names='Country',
                       hover_data=['Country', 'Number of females'], color="Country")
    fig.update_layout(
                      font_color="blueviolet",
                      legend=dict(title="Gender", title_font_color="black"))
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)
    st.write("United States of America has highest numbers of female Billionaires with 36.2% and is followed by China with 21.8%,then Germany with 11.1% ")

indst_hight_no = df.groupby(["Industries"]).size().reset_index(name="Total numbers")
fig = px.bar(indst_hight_no, x="Industries", y="Total numbers",
                 title="The number of Billionaires in each industry", color="Industries",
                 hover_data=(["Industries", "Total numbers"]))
fig.update_layout(title=dict(xanchor='center', yanchor="top", x=0.4, y=0.9, font=dict(size=30)),
                  font_color="blue violet",
                  legend=dict(title_font_color="black", font_color="green"),
                  height=600,
                  width=1200
                  )
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
fig.update_yaxes(title="Total number of Billionaires", title_font_color="blueviolet",
                     tickfont=dict(color="darkblue"))
fig.update_xaxes(title_font_color="blueviolet", tickfont=dict(color="darkblue"))
st.plotly_chart(fig)
st.write("Finance and Investments is the industry with highest numbers of Billionaires ,followed by Technology and Manufacturing")
st.write("Gambling and Casinos is the industry with the least numbers of Billionaires")
st.write("Best industries to consider are Finance and Investments,Technology and Manufacturing")
female=df[df["Gender"]=="F"]
indt_most_f=female.groupby(["Industries"]).size().reset_index(name="Number of Females")
fig=px.line(indt_most_f,x="Industries",y="Number of Females",color="Industries",text="Industries",markers=True,
            symbol="Industries",title="industries with highest number of female billionaires")
fig.update_layout(title=dict(xanchor='center',yanchor="top",x=0.5,y=0.9,font=dict(size=30)),
                  title_font_color="lightblue",
                  legend=dict(title="Gender",title_font_color="black",font_color="green"),
                  font_color="blueviolet",
                  width=1200,
                  height=600)
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
fig.update_traces(textposition="middle right")
fig.update_xaxes(title_font_color="blueviolet",tickfont=dict(color="darkblue"))
fig.update_yaxes(title_font_color="blueviolet",tickfont=dict(color="darkblue"))
st.plotly_chart(fig)
st.write("Manufacturing is the industry with highest numbers of Female Billionaires,folowed by Food and Beverages")
st.write("Telecom is the industry with the least numbers of Female Billionaires")
countries=df.groupby(["Country"]).size().reset_index(name="Number of Billionaires")
sourted_countries=countries.sort_values("Number of Billionaires",ascending=False)
top_10_countries=sourted_countries.head(10)
fig=px.bar(top_10_countries,x='Country',y="Number of Billionaires",
        title="Top 10 countries with highest number of Billionaires",color="Country")
fig.update_layout(title=dict(xanchor='center', yanchor="top", x=0.4, y=0.9, font=dict(size=30)),
                  font_color="blue violet",
                  legend=dict(title_font_color="black", font_color="green"),
                  height=600,
                  width=1200)
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.2)'})
fig.update_xaxes(title_font_color="blueviolet",tickfont=dict(color="darkblue"))
fig.update_yaxes(title_font_color="blueviolet",tickfont=dict(color="darkblue"))
st.plotly_chart(fig)
st.write("United States of America has highest number of Billionaires,Followed by China and then India")
countries=df.groupby(["Country"]).size().reset_index(name="Number of Billionaires")
fig = px.choropleth(
        countries,
        locations='Country',
        locationmode="country names",
        color='Number of Billionaires',
        hover_name='Country',
        projection='natural earth1',
        hover_data=["Number of Billionaires", "Country"],
        color_continuous_scale="viridis",
        title='Distribution of Billionaires by Country',
    )
fig.update_layout(
        title=dict(
            font=dict(color="#9C9C9C"),
            x=0.33
        ),
        paper_bgcolor="#F5F5F5",
        geo_bgcolor="#F5F5F5",
        margin=dict(l=100, r=100),
        width=1200,
        height=600
    )
st.plotly_chart(fig)
st.subheader("In Conclusion")
st.write("Most of the billionaires featured on the Forbes list in 2022 were male."
"The Technology industry drives most of the philanthropic billionaires."
"The average worth of a billionaire on the list is 4.76 billion."
"Only 396 out of the 2668 billionaires had a high philanthropic score."
"Most Male billionaires are self-made, whereas most female billionaires are not self-made")
st.sidebar.header("Project Description")
st.sidebar.write("Forbes World’s Billionaires is a documented report of an annual ranking of the net worth of the wealthiest billionaires in the world. The information is usually compiled and published every year since March 1987. Estimates of the net worth of each billionaire are cited in United States dollars regarding their documented assets while accounting for debts and other factors. On Forbes's 36th annual ranking, there were 2668 billionaires listed, 87 fewer than the previous year, 2021. In this project, I analyzed the Forbes Billionaires list 2022")
names = df["Name"].dropna(axis=0).values
name = st.sidebar.selectbox(label="Check your favorite Billionaire Rank (2022)", options=names)
columns = df.loc[:, ["Name", "Rank", "Networth", "Country"]]
favorite_billionaire = columns[columns["Name"] == name]
st.sidebar.subheader(f"RANK: {favorite_billionaire['Rank'].values[0]}")
st.sidebar.subheader(f"NETWORTH: {favorite_billionaire['Networth'].values[0]}")
st.sidebar.subheader(f"Country: {favorite_billionaire['Country'].values[0]}")
