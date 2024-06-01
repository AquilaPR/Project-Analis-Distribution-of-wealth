import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs4

countries_score_page = requests.get("https://en.wikipedia.org/wiki/Distribution_of_wealth")
countries_score_soup = bs4(countries_score_page.content, 'lxml')

countries_score_table = countries_score_soup.find('table', class_='wikitable')
countries_score_table

countries_score_df = pd.read_html(str(countries_score_table))
countries_score_df

countries_score_df = pd.read_html(str(countries_score_table))
countries_score_df

countries_score_df = countries_score_df[0]
countries_score_df

countries_score_df.to_csv('Data_DistribusiKekayaan.csv', index=False)
countries_score_df