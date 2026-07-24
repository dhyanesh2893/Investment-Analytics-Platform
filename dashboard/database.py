import os

import pandas as pd
import psycopg2


def get_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is missing. Add it in Railway Variables."
        )

    return psycopg2.connect(database_url)


def fetch_trade_summary():
    conn = get_connection()

    try:
        query = """
        SELECT *
        FROM trade_summary
        ORDER BY created_at DESC
        LIMIT 1
        """

        return pd.read_sql(query, conn)
    finally:
        conn.close()


def fetch_symbol_summary():
    conn = get_connection()

    try:
        query = """
        SELECT symbol, trade_value
        FROM symbol_summary
        ORDER BY trade_value DESC
        """

        return pd.read_sql(query, conn)
    finally:
        conn.close()


def fetch_exchange_summary():
    conn = get_connection()

    try:
        query = """
        SELECT exchange, trade_value
        FROM exchange_summary
        ORDER BY trade_value DESC
        """

        return pd.read_sql(query, conn)
    finally:
        conn.close()


def fetch_status_summary():
    conn = get_connection()

    try:
        query = """
        SELECT status, trade_count
        FROM status_summary
        ORDER BY trade_count DESC
        """

        return pd.read_sql(query, conn)
    finally:
        conn.close()
