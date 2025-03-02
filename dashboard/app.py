import streamlit as st
import pandas as pd

st.set_page_config(page_title ="Data Analyst Project : University and Vocational schools admission",layout="wide",initial_sidebar_state="expanded")

st.title("Data Analyst Project : University and Vocational schools admission")
st.caption("By : Zakky")

question_1_higher_education = pd.read_csv('question_1_higher_education.csv',delimiter=',')
question_1_higher_education['Acceptance Rate (In Percent)'] = question_1_higher_education['Acceptance Rate (In Percent)'].round(2)

question_1_vocational_education = pd.read_csv("question_1_Vocational_education.csv",delimiter=',')
question_1_vocational_education['Acceptance Rate (In Percent)'] = question_1_vocational_education['Acceptance Rate (In Percent)'].round(2)

question_2 = pd.read_csv("question_2.csv",delimiter=',')

question_3 = pd.read_csv("question_3.csv",delimiter=',')

question_4 = pd.read_csv("question_4.csv",delimiter=',')

with st.container(border=True):
    st.header("Group of professions with smallest acceptance rate every year based on Education level")
    with st.container():
        st.subheader("Higher Education")
        st.bar_chart(data=question_1_higher_education,x = "Year",y="Acceptance Rate (In Percent)",color="Group of Professions")
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("DataFrame"):
                st.dataframe(question_1_higher_education)
        with col2:
            with st.expander("Insight"):
                for index,row in question_1_higher_education.iterrows():
                    st.write(f"* Group of Professions with smallest acceptance rate in{row['Year']} was {row['Group of Professions']} with {row['Acceptance Rate (In Percent)']}%")
    
    with st.container():
        st.subheader("Vocational Education")
        st.bar_chart(data=question_1_vocational_education,x = "Year",y="Acceptance Rate (In Percent)",color="Group of Professions")
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("DataFrame"):
                st.dataframe(question_1_vocational_education)
        with col2:
            with st.expander("Insight"):
                for index,row in question_1_vocational_education.iterrows():
                    st.write(f"* Group of Professions with smallest acceptance rate in {row['Year']} was {row['Group of Professions']} with {row['Acceptance Rate (In Percent)']}%")

with st.container(border=True):
    st.header("Most favorite Group of Professions in every Education level based on Number of Applications")
    st.bar_chart(data=question_2.sort_values(by="Number of Applications",ascending=False),color = "Education level",y="Number of Applications",x="Group of Professions")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("DataFrame"):
            st.dataframe(question_2)
    with col2:
        with st.expander("Insights"):
            st.metric(label="Total Number of Applications", value=question_2["Number of Applications"].sum(),border=True)
            st.metric(label="The Highest Number of Applications", value=question_2["Number of Applications"].nlargest(1),border=True)
            st.metric(label="The Lowest Number of Applications", value=question_2["Number of Applications"].nsmallest(1),border=True)
            st.metric(label="Average Number of Applications", value=question_2["Number of Applications"].mean().__round__(2),border=True)

with st.container(border=True):
    st.header("Percentage Number of Students by Branches of Science")
    fig,ax = plt.subplots()
    plt.pie(question_3['Number of Students'],
            labels=None,
            )
    labels_legend = [f"{j} ({p}%)" for j, p in zip(
        question_3['Branches of Science'], question_3['Percentage'])]
    plt.legend(title="Branches of Science",
            labels=labels_legend,
            loc="best",
            bbox_to_anchor=(0, 0, 0, 1))
    plt.title("Percentage Number of Students by Branches of Science")
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("DataFrame"):
            st.dataframe(question_3)
    with col2:
        with st.expander("Details"):
            for index,row in question_3.iterrows():
                st.metric(f"{row['Branches of Science']} have {int(row['Number of Students'])} number of students which :",f"{row['Percentage']}% of all students",border=True)
        
with st.container(border=True):
    st.header("Most consistent Branches of Science based on Percentage Increase")
    st.line_chart(data=question_4,x="Year",y="Number of Applications",color="Branches of Science")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("DataFrame"):
            st.dataframe(question_4)
    with col2:
        with st.expander("See the increase"):
            Branches_of_Science_filter = st.selectbox('Choose Branches of Science',question_4['Branches of Science'].unique(),placeholder="choose the Branches of Science")
            Year_filter = st.selectbox('Choose Year',question_4['Year'].unique(),placeholder="choose the Year")
            result_of_filter = question_4[(question_4["Branches of Science"] == Branches_of_Science_filter) & (question_4["Year"] == Year_filter)]

            st.metric(f"{Branches_of_Science_filter}", f"{Year_filter}",f"{result_of_filter['Percentage Increase'].values[0]}%",delta_color="normal",border=True)

st.link_button(label="Visit My Github Account",url="https://github.com/zakkyyy-ar")