import pandas as pd
import streamlit as st
from joblib import load
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from pmdarima import auto_arima


st.set_page_config(
    page_title='Twitter Sentiment Forecasting',
    page_icon="logo.png",
    initial_sidebar_state="expanded"
)


max_width_str = f"max-width: {50}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)



st.write("""
# Twitter Sentiment Forecasting 
""")

st.sidebar.image("logo.png", use_column_width=True)  

num_days = st.sidebar.selectbox('Select number of days to forecast:', options=list(range(1, 8)), index=0)

st.success("Twitter serves as a valuable data source due to its vast and diverse user base and the real-time nature of its content. Sentiment analysis on Twitter involves processing and analyzing tweets to determine the emotional tone behind them, categorizing them as positive, negative, or neutral. The brevity of tweets and the use of informal language, slang, and hashtags present unique challenges and opportunities for natural language processing algorithms.")

data = pd.read_csv("result.csv", parse_dates=['date'], index_col='date').asfreq('D').interpolate()


#Load the model
arima_model = load('arima_model.joblib')

predictions, confidence_interval = arima_model.predict(n_periods=num_days, return_conf_int=True)
predictions = predictions.to_frame().rename(columns={0: 'sent_score'.title()+'_forecasted'})
observed_data = data.rename(columns={'avg sentiment_polarity': 'sent_score'.title()+'_observed'})
combined_data = pd.concat([observed_data, predictions])

st.title("Sentiment Score")

st.line_chart(combined_data, color=["#35A7FF", "#FFE74C"])

st.write("# Predictions")

st.success("Sentiment scores are used to gauge the emotional tone of textual content. Scores greater than 0 indicate positive sentiment, scores less than 0 indicate negative sentiment. The further the score is from 0 in the negative direction, the stronger the negative sentiment. For instance, a score of -0.5 is more negative than a score of -0.1, indicating a more intense negative sentiment. TextBlob provides these sentiment scores by analyzing the words and phrases within the text, offering a straightforward way to quantify the overall sentiment.")

st.table(predictions)

