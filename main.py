import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the CSV files
annual_gdp = pd.read_csv('korea_annual_gdp.csv')
quarterly_gdp = pd.read_csv('korea_quarterly_gdp.csv')
sector_gdp = pd.read_csv('korea_sector_gdp.csv')

# Korean translation dictionary
sector_korean = {
    'Manufacturing': '제조업',
    'Services': '서비스업',
    'Agriculture': '농업',
    'Construction': '건설업',
    'Others': '기타'
}

# Translate sector names
sector_gdp['Sector'] = sector_gdp['Sector'].map(sector_korean)

# Custom color scheme
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']

# Create subplot figure with 3 subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('<b>연간 GDP 추이</b>', '<b>분기별 GDP 성장률</b>',
                    '<b>GDP 부문별 구성</b>'),
    specs=[[{"type": "scatter"}, {"type": "bar"}],
           [{"type": "pie"}, None]],
    vertical_spacing=0.2,
    horizontal_spacing=0.15
)

# Add annual GDP line plot with enhanced styling
fig.add_trace(
    go.Scatter(
        x=annual_gdp['Year'],
        y=annual_gdp['GDP_USD_Billions'],
        name="연간 GDP",
        line=dict(color='#003f5c', width=3),
        mode='lines+markers',
        marker=dict(size=8),
        hovertemplate='연도: %{x}<br>GDP: %{y:.1f}십억 달러<extra></extra>'
    ),
    row=1, col=1
)

# Add quarterly GDP bar plot with enhanced styling
fig.add_trace(
    go.Bar(
        x=quarterly_gdp['Quarter'],
        y=quarterly_gdp['GDP_Growth'],
        name="분기별 성장률",
        marker_color='#58508d',
        marker_line_width=1.5,
        marker_line_color='white',
        hovertemplate='분기: %{x}<br>성장률: %{y:.1f}%<extra></extra>'
    ),
    row=1, col=2
)

# Add sector distribution pie chart with enhanced styling
fig.add_trace(
    go.Pie(
        labels=sector_gdp['Sector'],
        values=sector_gdp['Percentage'],
        name="부문별 비중",
        marker=dict(colors=colors),
        textinfo='label+percent',
        hole=0.3,
        hoverinfo='label+percent',
        textfont_size=14
    ),
    row=2, col=1
)

# Update layout with enhanced styling
fig.update_layout(
    height=1200,
    width=1600,
    title_text="<b>한국 GDP 분석 대시보드</b>",
    title_x=0.5,
    title_font_size=24,
    showlegend=True,
    font=dict(family="Arial", size=14),
    template="plotly_white",
    paper_bgcolor='white',
    plot_bgcolor='white'
)

# Update axes labels with enhanced styling
fig.update_xaxes(title_text="<b>연도</b>", title_font=dict(size=16),
                 row=1, col=1, gridcolor='lightgray')
fig.update_xaxes(title_text="<b>분기</b>", title_font=dict(size=16),
                 row=1, col=2, gridcolor='lightgray')
fig.update_yaxes(title_text="<b>GDP (십억 달러)</b>",
                 title_font=dict(size=16), row=1, col=1, gridcolor='lightgray')
fig.update_yaxes(title_text="<b>성장률 (%)</b>",
                 title_font=dict(size=16), row=1, col=2, gridcolor='lightgray')

# Show the figure
fig.show()

# Save as HTML file with improved resolution
fig.write_html("한국_gdp_대시보드.html", include_plotlyjs=True)
