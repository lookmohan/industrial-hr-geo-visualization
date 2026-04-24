import plotly.express as px

def plot_industry_distribution(df):
    result = df.groupby('industry_category')['total_workers'].sum().reset_index()
    fig = px.bar(result, x='industry_category', y='total_workers',
                 title='Workers by Industry Category')
    return fig


def plot_gender_distribution(df):
    male = df['main_workers__total__males'].sum()
    female = df['main_workers__total__females'].sum()

    data = {
        "Gender": ["Male", "Female"],
        "Workers": [male, female]
    }

    fig = px.pie(data, names="Gender", values="Workers",
                 title="Male vs Female Workers")
    return fig


def plot_top_industries(df):
    top = (
        df.groupby('nic_name')['total_workers']
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig = px.bar(top, x='total_workers', y='nic_name',
                 orientation='h', title='Top 5 Detailed Industries')
    return fig


def plot_rural_urban(df):
    rural = df['main_workers__rural___persons'].sum()
    urban = df['main_workers__urban___persons'].sum()

    data = {
        "Type": ["Rural", "Urban"],
        "Workers": [rural, urban]
    }

    fig = px.pie(data, names="Type", values="Workers",
                 title="Rural vs Urban Workers")
    return fig