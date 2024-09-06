#!/usr/bin/env python3 

# Importing the necessary modules 
import random

def generate_random_data(llm_name, metric_name, data_points):
    results = []
    for _ in range(data_points):
        if metric_name == "TTFT":
            result = random.uniform(0.01, 0.5)  # Adjust range as needed
        elif metric_name == "TPS":
            result = random.randint(100, 500)
        elif metric_name == "e2e_latency":
            result = random.uniform(0.1, 2.0)
        elif metric_name == "RPS":
            result = random.randint(5, 20)
        else:
            raise ValueError("Invalid metric name")
        results.append(result)
    return results

