def clean_columns(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("-", "")
    return df


def create_total_workers(df):
    df['total_workers'] = df['main_workers__total___persons']
    return df