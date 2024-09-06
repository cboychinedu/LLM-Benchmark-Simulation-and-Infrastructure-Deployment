#!/usr/bin/env python3

# Importing the necessary modules
import sqlite3

# Connect to an SQLite database
conn = sqlite3.connect("llmBenchmark.db")

# Create a curor object using the curosr() method
cursor = conn.cursor()

# Create a table
cursor.execute("""
        CREATE TABLE llm_benchmark_results (
        llm_name VARCHAR(255) NOT NULL,
        metric_name VARCHAR(255) NOT NULL,
        result DECIMAL(10, 6) NOT NULL);
""")

# Save the changes
conn.commit()

# Close the connection
conn.close()
