import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import time
from urllib.parse import quote_plus
from config import DB_CONFIG  

def get_db_url():
    password = quote_plus(DB_CONFIG['password']) 
    return (
        f"mysql+pymysql://{DB_CONFIG['user']}:{password}@{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/{DB_CONFIG['db']}?ssl_ca=./ca.pem"
    )

def fetch_data():
    engine = create_engine(get_db_url())
    query = "SELECT * FROM live_prices ORDER BY ts DESC LIMIT 100"
    df = pd.read_sql(query, engine)
    return df

def live_plot(interval=5):
    sns.set(style="darkgrid")
    plt.ion()  # interactive mode
    fig, ax = plt.subplots(figsize=(12, 6))

    while True:
        df = fetch_data()
        ax.clear()
        sns.lineplot(data=df, x='ts', y='price', hue='stock_name', marker='o', ax=ax)
        ax.set_title("📈 Live Stock Prices")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(interval)  

if __name__ == "__main__":
    live_plot(interval=5)
