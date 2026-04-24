from src.data_loader import load_data
from src.preprocessing import clean_columns, create_total_workers
from src.nlp_analysis import apply_nlp
from src.visualization import plot_industry_distribution

df = load_data()
df = clean_columns(df)
df = create_total_workers(df)
df = apply_nlp(df)

fig = plot_industry_distribution(df)
fig.show()