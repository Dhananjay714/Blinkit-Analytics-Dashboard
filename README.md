Blinkit Real-Time Analytics Dashboard 🚀

This is a real-time data analytics dashboard project inspired by Blinkit (India's instant grocery delivery app). It is designed to provide real-time insights into order volume, revenue, delivery times, top products, and customer behavior using simulated data.

![Dashboard Preview](assets/dashboard_screenshots/ride_sharing_dashboard1.png)

> ⚡ Built for learning data analytics, dashboard design, and Python API integration.

---

📊 Features

- 📦 **Live Order Simulation** using a Python API (`Faker` generated data)
- 📈 **Revenue & Order Trends** over time
- 🧈 **Top Products Analysis** (donut & bar charts)
- 📍 **City-wise Order Breakdown** with map visualization
- 💳 **Payment Method Share** using donut charts
- ⏱️ **Average Delivery Time Monitoring**
- 🧠 **Real-Time Filtering** by product, city, and payment method

---

🛠️ Tech Stack

| Frontend         | Backend & Data     | Visualization     |
|------------------|--------------------|--------------------|
| Power BI         | Python + Flask API | Power BI Service   |
| DAX (Power BI)   | Faker + Pandas     | Map, Donut, KPI    |
| Live Filters     | JSON API responses | Clean UX layout    |

---

📦 Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/Dhananjay714/Blinkit-Analytics-Dashboard.git
   cd Blinkit-Analytics-Dashboard/backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   python app.py
   ```

4. Import the PBIX file into Power BI Desktop.
5. Connect it to the running API (`http://127.0.0.1:5000/data`).

---

📌 Use Case

This dashboard simulates a Blinkit-like grocery delivery system and is useful for:

- Practicing **real-time data analysis**
- Building **interactive dashboards**
- Demonstrating **data-driven decision making**
- Strengthening your **data analyst/data engineer portfolio**

---

🙋‍♂️ Author

Dhananjay Wadhi**  
Final Year Computer Engineering Student  
📍 G.V. Acharya Institute of Engineering (Mumbai University)  
📫 [LinkedIn](https://www.linkedin.com/in/dhananjay-wadhi-058961237/) • [GitHub](https://github.com/Dhananjay714)



⭐ Star this repo if it helped you!
