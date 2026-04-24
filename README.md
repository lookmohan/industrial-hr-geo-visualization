# 📊 Industrial Human Resource Geo-Visualization

## 🧭 Problem Statement

In India, the industrial classification of the workforce is essential for understanding the distribution of the labor force across various sectors. The classification of **main workers** and **marginal workers** (other than cultivators and agricultural laborers) by sex, section, division, and class has traditionally been used to understand economic status and employment trends. However, current data may not accurately reflect the present state of the workforce.

This project aims to update, clean, and visualize this data to provide relevant and accurate insights for **policy making and employment planning**.

---

## 🛠️ Tools & Technologies

| Category       | Tools / Libraries                          |
|----------------|--------------------------------------------|
| Language       | Python 3.10+                               |
| Dashboard      | Streamlit                                  |
| Visualization  | Plotly Express                             |
| Data Handling  | Pandas, NumPy                              |
| NLP            | Custom keyword-based NLP (NLTK-compatible) |
| Storage        | CSV files (state-wise)                     |

---

## 📁 Project Structure

```
Industrial_HR_Geo_Visualization MP 6/
│
├── app.py                  # Main Streamlit dashboard application
├── test.py                 # Script to test the pipeline independently
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
│
├── data/                   # State-wise CSV datasets
│   ├── TAMIL_NADU.csv
│   ├── GUJARAT.csv
│   ├── JHARKHAND.csv
│   ├── ARUNACHAL_PRADESH.csv
│   ├── MANIPUR.csv
│   ├── PUDUCHERRY.csv
│   └── TRIPURA.csv
│
├── src/                    # Modular source code
│   ├── data_loader.py      # Loads and merges all CSV files
│   ├── preprocessing.py    # Cleans column names, derives total workers
│   ├── nlp_analysis.py     # NLP-based industry category classification
│   └── visualization.py   # Plotly chart functions
│
└── notebooks/              # (Reserved for EDA notebooks)
```

---

## ⚙️ Workflow & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Industrial_HR_Geo_Visualization.git
cd Industrial_HR_Geo_Visualization
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

### 5. (Optional) Run the Pipeline Test

```bash
python test.py
```

This runs the full data pipeline and opens a standalone Plotly chart to verify everything works.

---

## 🔄 Pipeline Overview

```
data/*.csv
    └──▶ data_loader.py      (merge all CSVs, add state_name column)
              └──▶ preprocessing.py  (normalize column names, derive total_workers)
                        └──▶ nlp_analysis.py   (classify NIC names into industry categories)
                                  └──▶ visualization.py  (generate Plotly charts)
                                            └──▶ app.py          (Streamlit dashboard)
```

---

## 📊 Dashboard Features

- **State-level filter** — select any state from the sidebar
- **KPI cards** — total, male, and female worker counts
- **Top industries table** — ranked by total workers in selected state
- **Workers by Industry Category** — bar chart (NLP-classified sectors)
- **Male vs Female distribution** — pie chart
- **Top 5 Detailed Industries** — horizontal bar chart by NIC name
- **Rural vs Urban Workers** — pie chart

---

## 🧠 NLP Industry Classification

Industry names (`NIC Name` column) are classified into the following categories using keyword-based NLP:

| Category         | Keywords matched                                      |
|------------------|-------------------------------------------------------|
| Agriculture      | crop, animal, farming, growing, agriculture           |
| Manufacturing    | manufacturing                                         |
| Retail           | retail, trade                                         |
| Construction     | construction, building                                |
| Poultry/Fishery  | fish, poultry                                         |
| Other            | everything else                                       |

---

## 📦 Dataset

The dataset contains **state-wise counts** of industrial classification of main and marginal workers (males and females) across various NIC (National Industrial Classification) categories — including manufacturing of plastic products, rubber, chemicals, furniture, construction, retail trade, and more.

Each CSV file corresponds to one Indian state/union territory.

---

## 📋 Coding Standards

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python coding standards:
- Functions are modular and single-responsibility
- All source logic is separated into `src/` modules
- Column names are normalized to `snake_case`
- No hardcoded paths — data folder is scanned dynamically

