import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 12})

annual_gdp = pd.read_csv('korea_annual_gdp.csv')
quarterly_gdp = pd.read_csv('korea_quarterly_gdp.csv')
sector_gdp = pd.read_csv('korea_sector_gdp.csv')

sector_korean = {
    'Manufacturing': '제조업',
    'Services': '서비스업',
    'Agriculture': '농업',
    'Construction': '건설업',
    'Others': '기타'
}
sector_gdp['Sector'] = sector_gdp['Sector'].map(sector_korean)

plt.figure(figsize=(12, 8))
plt.plot(annual_gdp['Year'], annual_gdp['GDP_USD_Billions'],
         marker='o', linewidth=3, markersize=8, color='blue')
plt.title('연간 GDP 추이', pad=20, fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('GDP (십억 달러)', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('연간_gdp_추이.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(12, 8))
plt.bar(range(len(quarterly_gdp)), quarterly_gdp['GDP_Growth'],
        color='skyblue', width=0.6)
plt.title('분기별 GDP 성장률 (%)', pad=20, fontsize=16)
plt.xlabel('분기', fontsize=14)
plt.ylabel('성장률 (%)', fontsize=14)
plt.xticks(range(len(quarterly_gdp)),
           [f'{i+1}분기' for i in range(len(quarterly_gdp))],
           rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('분기별_gdp_성장률.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 10))
plt.pie(sector_gdp['Percentage'],
        labels=sector_gdp['Sector'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['lightblue', 'lightgreen', 'pink', 'orange', 'yellow'])
plt.title('산업별 GDP 구성', pad=20, fontsize=16)
plt.tight_layout()
plt.savefig('산업별_gdp_구성.png', dpi=300, bbox_inches='tight')
plt.show()
