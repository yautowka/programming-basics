import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv('Answers/Answers.csv', encoding='ISO-8859-1')

end = 10**3
df = df[0:end]


def clean_html(html):
    return BeautifulSoup(html, 'html.parser').get_text(separator=' ', strip=True)


df['Body'] = df['Body'].apply(clean_html)

# print(df.Body.head(5))
df.to_csv('output.csv', index=False)