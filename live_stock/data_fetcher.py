import random
import time
import pymysql
from config import DB_CONFIG

TABLE_CREATION_QUERY = """
CREATE TABLE IF NOT EXISTS live_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_name VARCHAR(10),
    price FLOAT,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def setup_table(cursor):
    cursor.execute(TABLE_CREATION_QUERY)

def insert_price(cursor, conn):
    stock = random.choice(['AAPL', 'GOOG', 'TSLA'])
    price = round(random.uniform(100, 1000), 2)

    query = "INSERT INTO live_prices (stock_name, price) VALUES (%s, %s)"
    cursor.execute(query, (stock, price))
    conn.commit()

    print(f"Inserted: {stock} = ${price}")

if __name__ == "__main__":
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        setup_table(cursor)  # Ensure table exists

        while True:
            insert_price(cursor, conn)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        try:
            cursor.close()
            conn.close()
            print("Connection closed.")
        except:
            pass
