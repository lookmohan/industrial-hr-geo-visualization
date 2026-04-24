import streamlit as st
from src.data_loader import load_data
from src.preprocessing import clean_columns, create_total_workers
from src.nlp_analysis import apply_nlp
from src.visualization import (
    plot_industry_distribution,
    plot_gender_distribution,
    plot_top_industries,
    plot_rural_urban
)

# Page config
st.set_page_config(layout="wide", page_title="Industrial HR Geo-Visualization", page_icon="📊")

# Custom CSS for better UI
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E86AB;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        color: #4A90E2;
        font-size: 1.5em;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .metric-card {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #333;
    }
    .metric-label {
        font-size: 1em;
        color: #666;
    }
    .dataframe {
        font-size: 1.1em;
    }
    .plotly-chart {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>📊 Industrial HR Geo-Visualization</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; color: #666;'>Explore industrial workforce data across Indian states with interactive visualizations and key insights.</p>", unsafe_allow_html=True)

# Load and process data
df = load_data()
df = clean_columns(df)
df = create_total_workers(df)
df = apply_nlp(df)

# Keep only state-level data
df = df[df['india/states'].str.contains("STATE")]

# Sidebar filter
st.sidebar.title("🔍 Filters")
states = df['state_name'].unique()
selected_state = st.sidebar.selectbox("Select State", sorted(states))

filtered_df = df[df['state_name'] == selected_state]

# Show selected state
st.markdown(f"<h2 style='text-align: center; color: #4A90E2;'>📍 Selected State: {selected_state}</h2>", unsafe_allow_html=True)

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["📈 Overview", "🏭 Industries", "👥 Demographics"])

with tab1:
    st.markdown("<h3 class='subheader'>Key Metrics</h3>", unsafe_allow_html=True)
    
    total = int(filtered_df['total_workers'].sum())
    male = int(filtered_df['main_workers__total__males'].sum())
    female = int(filtered_df['main_workers__total__females'].sum())
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{total:,}</div>
            <div class="metric-label">Total Workers</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{male:,}</div>
            <div class="metric-label">Male Workers</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{female:,}</div>
            <div class="metric-label">Female Workers</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h3 class='subheader'>Industry Distribution</h3>", unsafe_allow_html=True)
    fig1 = plot_industry_distribution(filtered_df)
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.markdown("<h3 class='subheader'>Top Industries</h3>", unsafe_allow_html=True)
    
    top_industries = (
        filtered_df.groupby('industry_category')['total_workers']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    top_industries.index += 1
    top_industries.insert(0, "Rank", top_industries.index)
    
    st.dataframe(top_industries, use_container_width=True)
    
    st.markdown("---")
    st.markdown("<h3 class='subheader'>Top 5 Detailed Industries</h3>", unsafe_allow_html=True)
    fig3 = plot_top_industries(filtered_df)
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.markdown("<h3 class='subheader'>Gender Distribution</h3>", unsafe_allow_html=True)
    fig2 = plot_gender_distribution(filtered_df)
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    st.markdown("<h3 class='subheader'>Rural vs Urban Distribution</h3>", unsafe_allow_html=True)
    fig4 = plot_rural_urban(filtered_df)
    st.plotly_chart(fig4, use_container_width=True)