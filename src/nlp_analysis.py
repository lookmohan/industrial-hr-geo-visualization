def categorize_industry(text):
    text = str(text).lower()

    if ("crop" in text or "animal" in text or "farming" in text 
        or "growing" in text or "agriculture" in text):
        return "Agriculture"
    
    elif "manufacturing" in text:
        return "Manufacturing"
    
    elif "retail" in text or "trade" in text:
        return "Retail"
    
    elif "construction" in text or "building" in text:
        return "Construction"
    
    elif "fish" in text or "poultry" in text:
        return "Poultry/Fishery"
    
    else:
        return "Other"


def apply_nlp(df):
    df['industry_category'] = df['nic_name'].apply(categorize_industry)
    return df