<h1>Twitter Sentiment Forecasting</h1>

<p>The <strong>Twitter Sentiment Forecasting</strong> app predicts the sentiment scores of tweets over a specified number of days using an ARIMA model. Sentiment analysis on Twitter helps to gauge the emotional tone of textual content, categorized as positive, negative, or neutral. This app provides both observed and forecasted sentiment scores over time.</p>

<p>🌐 <a href="https://twitterforecast.streamlit.app">Live App</a></p>

<h2>How It Works</h2>

<p>This Streamlit app forecasts Twitter sentiment for up to 7 days based on historical data. The predictions are visualized through line charts, and users can select the number of forecast days using an interactive sidebar. Here's how it works:</p>

<ul>
  <li><strong>Sentiment Forecasting:</strong> Users select the number of days (1-7) to predict sentiment scores using an ARIMA model.</li>
  <li><strong>Interactive Visualizations:</strong> The app uses Plotly and Altair to generate dynamic charts of forecasted sentiment scores.</li>
  <li><strong>Sentiment Score:</strong> Sentiment scores greater than 0 indicate positive sentiment, while scores less than 0 indicate negative sentiment.</li>
</ul>

<h3>Run the App Locally</h3>

<p>To run the application locally, follow these steps:</p>

<pre><code>
# Clone the repository
git clone https://github.com/your-username/twitter-sentiment-forecast.git

# Navigate into the project directory
cd twitter-sentiment-forecast

# Install required dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
</code></pre>

<p>After running the app, it will be accessible at <strong>http://localhost:8501/</strong>.</p>

<h2>Example Code Snippet</h2>

<p>Here’s an example of how a section of the dashboard’s code might look:</p>

<pre><code>
import pandas as pd
import streamlit as st
from joblib import load

# Load data
data = pd.read_csv('result.csv', parse_dates=['date'], index_col='date').asfreq('D').interpolate()

# Load model
arima_model = load('arima_model.joblib')

# Generate predictions
num_days = 7  # Example for 7 days
predictions, confidence_interval = arima_model.predict(n_periods=num_days, return_conf_int=True)

# Display sentiment score forecast
st.line_chart(predictions)
</code></pre>


<p>The app uses a CSV file (<strong>result.csv</strong>) that contains historical Twitter sentiment data. The ARIMA model generates predictions based on this data. The CSV is expected to have a <strong>date</strong> column and a <strong>sentiment score</strong> column.</p>

<h2>Questions</h2>

<h3>What is the ARIMA model?</h3>
<p>The ARIMA model (AutoRegressive Integrated Moving Average) is used to predict future values based on past data trends. It's effective for time series forecasting, especially for sentiment analysis.</p>

<h3>What do sentiment scores mean?</h3>
<p>Sentiment scores range from -1 to 1, where positive values indicate positive sentiment, and negative values indicate negative sentiment. The further the score is from 0, the stronger the sentiment (positive or negative).</p>

<h3>How do I add new features?</h3>
<p>You can extend the app by adding more data visualization types, incorporating more advanced models, or allowing users to upload custom datasets.</p>

