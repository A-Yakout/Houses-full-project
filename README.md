# 🏡 Property Finder Data Analysis & Price Prediction

This project is a complete data analysis and machine learning pipeline focused on real estate listings
from [Property Finder](https://www.propertyfinder.eg/).
The goal is to analyze property data and build a model to predict housing prices.

## 📌 Project Highlights

- 🔍 **Web Scraping**: Collected data using web scraping from Property Finder.
- 🧹 **Data Cleaning**: Cleaned and preprocessed the scraped data.
- 📊 **EDA (Exploratory Data Analysis)**: Visualized trends and relationships in the data.
- 🤖 **Machine Learning**: Trained a predictive model to estimate property prices.
- 📈 **Model Evaluation**: Evaluated the performance of the model using appropriate metrics.

## ⚙️ Tools & Libraries

- `Python`
- `BeautifulSoup`, `Selenium` – For web scraping
- `Pandas`, `NumPy` – For data manipulation
- `Matplotlib`, `Seaborn` – For data visualization
- `Scikit-learn` – For machine learning

## 🏗️ Workflow

1. **Data Collection**  
   Scraped data from multiple pages of Property Finder including:
   - Property title
   - Price
   - Location
   - Area (m²)
   - Bedrooms, bathrooms, etc.
   - Telephone number

2. **Data Cleaning & Processing**  
   - Converted prices and areas to numeric format.
   - Handled missing values and outliers.
   - Feature engineering.
   - One Hot Encoding.
   - Feature Scaling.

3. **Exploratory Data Analysis (EDA)**  
   - Distribution of prices by location.
   - Correlation between area and price.
   - Insights into market trends.

4. **Model Building & Prediction**  
   - Split data into train/test sets.
   - Applied regression models (e.g., Linear Regression, Random Forest).
   - Evaluated models using RMSE and R².

## 🔮 Results

The final model achieved reasonable accuracy in predicting property prices based on features like location, area, and number of rooms. The insights can be useful for both buyers and real estate analysts.

## 🚀 Future Improvements

- Add more features (e.g., proximity to amenities).
- Deploy the model using a web app (e.g., Streamlit or Flask).
- Automate scraping for real-time updates.

## Author

Eng.Abdelrhman Mohamed Yakout

## 📬 Contact

https://www.linkedin.com/in/abdelrhman-yakout-3099a932a/

01005846630


Feel free to reach out for any questions or collaborations!

---

