import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="DS Project Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern, clean CSS styling
st.markdown("""
<style>
    /* Modern color palette */
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --background: #f8fafc;
        --surface: #ffffff;
        --text: #1f2937;
        --text-secondary: #6b7280;
    }

    /* Global styles */
    .main {
        background: var(--background);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Welcome section */
    .welcome-card {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.2);
    }

    .welcome-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .welcome-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-bottom: 1rem;
    }

    /* Quick stats cards */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .stat-card {
        background: var(--surface);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }

    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary);
        margin-bottom: 0.25rem;
    }

    .stat-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Content sections */
    .content-card {
        background: var(--surface);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
    }

    .section-header {
        display: flex;
        align-items: center;
        color: black;
        gap: 0.75rem;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e5e7eb;
    }

    .section-icon {
        font-size: 1.5rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: black;
        margin: 0;
    }

    /* Sidebar improvements */
    .sidebar-header {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        text-align: center;
    }

    .sidebar-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Filter section */
    .filter-section {
        background: #f9fafb;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }

    .filter-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Chart selection */
    .chart-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.75rem;
        margin-bottom: 1rem;
    }

    .chart-option {
        background: var(--surface);
        padding: 0.75rem;
        border-radius: 8px;
        border: 2px solid #e5e7eb;
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: center;
    }

    .chart-option:hover {
        border-color: var(--primary);
        background: #fefefe;
    }

    .chart-option.selected {
        background: var(--primary);
        color: white;
        border-color: var(--primary);
    }

    .chart-icon {
        font-size: 1.5rem;
        margin-bottom: 0.25rem;
    }

    .chart-label {
        font-size: 0.8rem;
        font-weight: 500;
    }

    /* Button improvements */
    .btn-primary {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        width: 100%;
    }

    .btn-primary:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }

    .btn-secondary {
        background: #f3f4f6;
        color: var(--text);
        border: 1px solid #d1d5db;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        width: 100%;
    }

    .btn-secondary:hover {
        background: #e5e7eb;
    }

    /* Loading state */
    .loading {
        text-align: center;
        padding: 2rem;
        color: var(--text-secondary);
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: var(--text-secondary);
    }

    .empty-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .empty-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 0.5rem;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .stats-grid {
            grid-template-columns: 1fr;
        }

        .welcome-title {
            font-size: 2rem;
        }

        .chart-grid {
            grid-template-columns: 1fr;
        }
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
</style>
""", unsafe_allow_html=True)

# Load data with error handling
@st.cache_data
def load_data():
    try:
        daily_metrics = pd.read_csv('daily_metrics.csv')
        fear_greed_df = pd.read_csv('fear_greed_index.csv')

        # Data preprocessing
        if 'leverage_segment' not in daily_metrics.columns:
            daily_metrics['leverage_proxy'] = daily_metrics['avg_position']
            daily_metrics['leverage_segment'] = pd.qcut(daily_metrics['leverage_proxy'], q=2, labels=['Low Leverage', 'High Leverage'])

        if 'frequency_segment' not in daily_metrics.columns:
            daily_metrics['frequency_segment'] = pd.qcut(daily_metrics['num_trades'], q=2, labels=['Infrequent', 'Frequent'])

        return daily_metrics, fear_greed_df
    except FileNotFoundError:
        st.error("📁 Data files not found. Please run the analysis notebook first to generate the required data.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

# Load data
data_loaded = False
try:
    daily_metrics, fear_greed_df = load_data()
    data_loaded = True
except:
    daily_metrics = pd.DataFrame()
    fear_greed_df = pd.DataFrame()

# Welcome Section
if not data_loaded:
    st.markdown("""
    <div class="welcome-card">
        <h1 class="welcome-title">⚠️ Data Not Available</h1>
        <p class="welcome-subtitle">Please run the analysis notebook first to generate the required data files.</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Run <code>DS_project.ipynb</code> to create <code>daily_metrics.csv</code></p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

st.markdown("""
<div class="welcome-card">
    <h1 class="welcome-title">📊DS Project Dashboard</h1>
    <p class="welcome-subtitle">Analyze trading behavior and performance across different market sentiments</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Select charts from the sidebar to explore insights and trends</p>
</div>
""", unsafe_allow_html=True)

# Quick Overview Stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_traders = daily_metrics['account'].nunique()
    st.metric("Total Traders", f"{total_traders:,}")

with col2:
    total_days = daily_metrics['date'].nunique()
    st.metric("Trading Days", f"{total_days:,}")

with col3:
    avg_win_rate = daily_metrics['win_rate'].mean()
    st.metric("Avg Win Rate", f"{avg_win_rate:.1%}")

with col4:
    total_pnl = daily_metrics['total_pnl'].sum()
    st.metric("Total PnL", f"${total_pnl:,.0f}")

# Sidebar Controls
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-title">🎛️ Dashboard Controls</div>
        <p style="font-size: 0.8rem; margin: 0; opacity: 0.9;">Customize your analysis</p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Show All", use_container_width=True, help="Display all available charts"):
            st.session_state.show_all = True
            st.rerun()
    with col2:
        if st.button("🔄 Reset", use_container_width=True, help="Clear all selections"):
            st.session_state.show_all = False
            st.rerun()

    # Chart Selection with visual cards
    st.markdown("### 📈 Select Charts")
    st.markdown('<div class="chart-grid">', unsafe_allow_html=True)

    chart_options = {
        "📊 Overview": "Key performance metrics and summary statistics",
        "🎭 Sentiment": "Market sentiment distribution and analysis",
        "💰 Performance": "PnL distribution and performance metrics",
        "🏆 Win Rates": "Win rate analysis by different segments",
        "⚖️ Leverage": "Leverage-based performance comparison",
        "⏱️ Frequency": "Trading frequency analysis",
        "📈 Trends": "Time-based trends and patterns",
        "📋 Data": "Raw data preview and exploration"
    }

    selected_charts = []
    cols = st.columns(2)
    col_idx = 0

    for chart_name, description in chart_options.items():
        with cols[col_idx % 2]:
            # Create unique key
            key = chart_name.lower().replace(' ', '_').replace('📊', '').replace('🎭', '').replace('💰', '').replace('🏆', '').replace('⚖️', '').replace('⏱️', '').replace('📈', '').replace('📋', '')

            # Check if show all is selected
            default = st.session_state.get('show_all', False)

            if st.checkbox(f"{chart_name}", value=default, key=key, help=description):
                selected_charts.append(chart_name)

        col_idx += 1

    st.markdown('</div>', unsafe_allow_html=True)

    # Progress indicator
    if selected_charts:
        progress = len(selected_charts) / len(chart_options)
        st.progress(progress)
        st.caption(f"{len(selected_charts)} of {len(chart_options)} charts selected")

    # Filters Section
    with st.expander("🔍 Advanced Filters", expanded=False):
        st.markdown("#### 📅 Date Range")
        min_date = pd.to_datetime(daily_metrics['date']).min()
        max_date = pd.to_datetime(daily_metrics['date']).max()
        date_range = st.date_input(
            "Select date range:",
            [min_date, max_date],
            help="Filter data by trading date range"
        )

        st.markdown("#### 🎭 Market Sentiment")
        sentiments = sorted([s for s in daily_metrics['classification'].unique() if pd.notna(s)])
        selected_sentiments = st.multiselect(
            "Select sentiments:",
            sentiments,
            default=sentiments,
            help="Filter by market sentiment"
        )

        st.markdown("#### 👥 Trader Segments")
        col1, col2 = st.columns(2)
        with col1:
            leverages = sorted(daily_metrics['leverage_segment'].unique())
            selected_leverages = st.multiselect(
                "Leverage:",
                leverages,
                default=leverages,
                help="Filter by leverage level"
            )

        with col2:
            frequencies = sorted(daily_metrics['frequency_segment'].unique())
            selected_frequencies = st.multiselect(
                "Frequency:",
                frequencies,
                default=frequencies,
                help="Filter by trading frequency"
            )

    # Apply filters
    filtered_data = daily_metrics[
        (daily_metrics['classification'].isin(selected_sentiments)) &
        (daily_metrics['leverage_segment'].isin(selected_leverages)) &
        (daily_metrics['frequency_segment'].isin(selected_frequencies)) &
        (pd.to_datetime(daily_metrics['date']) >= pd.to_datetime(date_range[0])) &
        (pd.to_datetime(daily_metrics['date']) <= pd.to_datetime(date_range[1]))
    ].copy()

# Main Content Area
if selected_charts:
    chart_list = "".join([
        f"<li style='color:#111827; font-weight:500;'>{c}</li>"
        for c in selected_charts
    ])

    st.markdown(f"""
    <div style="
        background:#ffffff;
        border-radius:12px;
        padding:16px;
        box-shadow:0 4px 12px rgba(0,0,0,0.05);
        margin-bottom:1rem;
    ">
        <h4 style="color:#111827; margin-bottom:8px;">
            📊 Selected Charts ({len(selected_charts)})
        </h4>
        <ul style="margin-left:1rem;">
            {chart_list}
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Add helpful tips
    with st.expander("💡 How to use this dashboard", expanded=False):
        st.markdown("""
        **Quick Tips:**
        - Use the sidebar to select which charts you want to see
        - Apply filters to focus on specific time periods or trader segments
        - Hover over chart elements for detailed information
        - Use the "Show All" button to see everything at once
        - Expand the "Advanced Filters" for more control over your analysis
        """)

    # Overview Section
    if "📊 Overview" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">📊</span>
                <h3 class="section-title">Performance Overview</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Key metrics in a nice grid
        st.markdown('<div class="stats-grid">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{len(filtered_data):,}</div>
                <div class="stat-label">Trading Days</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            avg_pnl = filtered_data['total_pnl'].mean()
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">${avg_pnl:,.0f}</div>
                <div class="stat-label">Avg Daily PnL</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            avg_win_rate = filtered_data['win_rate'].mean()
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{avg_win_rate:.1%}</div>
                <div class="stat-label">Win Rate</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            total_trades = filtered_data['num_trades'].sum()
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{total_trades:,}</div>
                <div class="stat-label">Total Trades</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Sentiment Analysis
    if "🎭 Sentiment" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">🎭</span>
                <h3 class="section-title">Market Sentiment Analysis</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        sentiment_counts = filtered_data['classification'].value_counts()
        fig_sentiment = px.pie(
            values=sentiment_counts.values,
            names=sentiment_counts.index,
            title="Market Sentiment Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.4
        )
        fig_sentiment.update_layout(showlegend=True, title_x=0.5, title_font_color="blue")
        st.plotly_chart(fig_sentiment, use_container_width=True, config={'displayModeBar': False})

    # Performance Analysis
    if "💰 Performance" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">💰</span>
                <h3 class="section-title">Performance Analysis</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        fig_pnl = px.box(
            filtered_data,
            x='classification',
            y='total_pnl',
            title="PnL Distribution by Market Sentiment",
            color='classification',
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        fig_pnl.update_layout(showlegend=False, title_x=0.5, title_font_color="blue")
        st.plotly_chart(fig_pnl, use_container_width=True, config={'displayModeBar': False})

    # Win Rate Analysis
    if "🏆 Win Rates" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">🏆</span>
                <h3 class="section-title">Win Rate Analysis</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        fig_win = px.bar(
            filtered_data.groupby('classification')['win_rate'].mean().reset_index(),
            x='classification',
            y='win_rate',
            title="Win Rate by Market Sentiment",
            color='classification',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_win.update_layout(showlegend=False, title_x=0.5, title_font_color="blue")
        st.plotly_chart(fig_win, use_container_width=True, config={'displayModeBar': False})

    # Leverage Analysis
    if "⚖️ Leverage" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">⚖️</span>
                <h3 class="section-title">Leverage Analysis</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        leverage_data = filtered_data.groupby(['classification', 'leverage_segment']).agg({
            'total_pnl': 'mean',
            'win_rate': 'mean'
        }).round(4).reset_index()

        fig_leverage = px.bar(
            leverage_data,
            x='classification',
            y='total_pnl',
            color='leverage_segment',
            barmode='group',
            title="Performance by Leverage Segment",
            color_discrete_sequence=['#48bb78', '#f56565']
        )
        fig_leverage.update_layout(title_x=0.5, title_font_color="blue")
        st.plotly_chart(fig_leverage, use_container_width=True, config={'displayModeBar': False})

    # Frequency Analysis
    if "⏱️ Frequency" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">⏱️</span>
                <h3 class="section-title">Trading Frequency Analysis</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        freq_data = filtered_data.groupby(['classification', 'frequency_segment']).agg({
            'total_pnl': 'mean',
            'num_trades': 'mean'
        }).round(4).reset_index()

        fig_freq = px.scatter(
            freq_data,
            x='num_trades',
            y='total_pnl',
            color='classification',
            size='num_trades',
            symbol='frequency_segment',
            title="Trading Frequency vs Performance",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_freq.update_layout(title_x=0.5, title_font_color="blue")
        st.plotly_chart(fig_freq, use_container_width=True, config={'displayModeBar': False})

        # Insights
        st.info("💡 **Key Insights:** High leverage traders excel in Greed periods but struggle in Fear. Low leverage traders show more consistent performance. Frequent traders generate higher volume but variable profitability.")

    # Trends Analysis
    if "📈 Trends" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">📈</span>
                <h3 class="section-title">Time-Based Trends</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        time_data = filtered_data.groupby('date').agg({
            'total_pnl': 'mean',
            'win_rate': 'mean',
            'num_trades': 'sum'
        }).reset_index()

        tab1, tab2, tab3 = st.tabs(["📈 PnL Trends", "🏆 Win Rate Trends", "📊 Volume Trends"])

        with tab1:
            fig_time_pnl = px.line(
                time_data,
                x='date',
                y='total_pnl',
                title="Average Daily PnL Over Time",
                markers=True,
                color_discrete_sequence=['#1f77b4']
            )
            fig_time_pnl.update_layout(title_x=0.5, title_font_color="blue")
            st.plotly_chart(fig_time_pnl, use_container_width=True, config={'displayModeBar': False})

        with tab2:
            fig_time_win = px.line(
                time_data,
                x='date',
                y='win_rate',
                title="Win Rate Trend Over Time",
                markers=True,
                color_discrete_sequence=['#ff7f0e']
            )
            fig_time_win.update_layout(title_x=0.5, title_font_color="blue")
            st.plotly_chart(fig_time_win, use_container_width=True, config={'displayModeBar': False})

        with tab3:
            fig_time_volume = px.bar(
                time_data,
                x='date',
                y='num_trades',
                title="Daily Trading Volume Over Time",
                color_discrete_sequence=['#2ca02c']
            )
            fig_time_volume.update_layout(title_x=0.5, title_font_color="blue")
            st.plotly_chart(fig_time_volume, use_container_width=True, config={'displayModeBar': False})

    # Data Preview
    if "📋 Data" in selected_charts:
        st.markdown("""
        <div class="content-card">
            <div class="section-header">
                <span class="section-icon">📋</span>
                <h3 class="section-title">Data Explorer</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(filtered_data.head(20), use_container_width=True)
        st.markdown(f"**Showing first 20 rows of {len(filtered_data):,} total records**")

    # Summary Section
    if len(selected_charts) > 0:
        st.markdown("---")
        st.markdown("### 📋 Analysis Summary")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Data Overview:**")
            st.info(f"""
            - **Time Period:** {date_range[0].strftime('%Y-%m-%d')} to {date_range[1].strftime('%Y-%m-%d')}
            - **Filtered Records:** {len(filtered_data):,}
            - **Selected Sentiments:** {', '.join(selected_sentiments)}
            - **Trader Segments:** {len(selected_leverages)} leverage × {len(selected_frequencies)} frequency types
            """)

        with col2:
            st.markdown("**Key Insights:**")
            if len(filtered_data) > 0:
                best_sentiment = filtered_data.groupby('classification')['total_pnl'].mean().idxmax()
                best_leverage = filtered_data.groupby('leverage_segment')['win_rate'].mean().idxmax()
                st.success(f"""
                - **Best Performing Sentiment:** {best_sentiment}
                - **Most Consistent Segment:** {best_leverage} traders
                - **Analysis Complete:** {len(selected_charts)} visualizations generated
                """)
            else:
                st.warning("No data matches your current filters. Try adjusting the criteria.")

else:
    # Empty state with helpful guidance
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">📊</div>
        <h3 class="empty-title">Ready to Explore!</h3>
        <p>Choose charts from the sidebar to start analyzing your trading data.</p>
        <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 1rem;">
            💡 <strong>Pro Tip:</strong> Start with "📊 Overview" to get a quick summary of your trading performance.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: var(--text-secondary); border-top: 1px solid #e5e7eb; margin-top: 3rem;">
    <p style="margin: 0; font-size: 0.9rem;">
        📊 <strong>DS Project Dashboard</strong> | Built using Streamlit & Plotly<br>
        <span style="font-size: 0.8rem;">Analyze trading behavior and optimize performance across market conditions</span>
    </p>
</div>
""", unsafe_allow_html=True)