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

# Create subplot figure with 3 subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('연간 GDP 추이', '분기별 GDP 성장률', 'GDP 부문별 구성'),
    specs=[[{"type": "scatter"}, {"type": "bar"}],
           [{"type": "pie"}, None]],
    vertical_spacing=0.15,
    horizontal_spacing=0.1
)

# Add annual GDP line plot
fig.add_trace(
    go.Scatter(
        x=annual_gdp['Year'],
        y=annual_gdp['GDP_USD_Billions'],
        name="연간 GDP",
        line=dict(color='blue')
    ),
    row=1, col=1
)

# Add quarterly GDP bar plot
fig.add_trace(
    go.Bar(
        x=quarterly_gdp['Quarter'],
        y=quarterly_gdp['GDP_Growth'],
        name="분기별 성장률",
        marker_color='green'
    ),
    row=1, col=2
)

# Add sector distribution pie chart
fig.add_trace(
    go.Pie(
        labels=sector_gdp['Sector'],
        values=sector_gdp['Percentage'],
        name="부문별 비중"
    ),
    row=2, col=1
)

# Update layout
fig.update_layout(
    height=900,
    width=1200,
    title_text="한국 GDP 분석",
    showlegend=True,
    font=dict(family="Arial", size=12)
)

# Update axes labels
fig.update_xaxes(title_text="연도", row=1, col=1)
fig.update_xaxes(title_text="분기", row=1, col=2)
fig.update_yaxes(title_text="GDP (십억 달러)", row=1, col=1)
fig.update_yaxes(title_text="성장률 (%)", row=1, col=2)

# Show the figure
fig.show()

# Save as HTML file
fig.write_html("한국_gdp_대시보드.html")
