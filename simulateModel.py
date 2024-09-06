import time
import random

def simulate_llm(model_name, ttft_mean, tps_mean, rps_limit):
    """Simulates an LLM's performance metrics.

    Args:
        model_name: The name of the LLM.
        ttft_mean: The average time to first token (in seconds).
        tps_mean: The average tokens per second.
        rps_limit: The maximum requests per second.
    """

    print(f"Simulating {model_name}")

    while True:
        start_time = time.time()

        # Simulate TTFT
        ttft = random.gauss(ttft_mean, ttft_mean / 4)
        time.sleep(ttft)

        # Simulate TPS
        tokens = random.randint(100, 200)
        tps = tokens / (time.time() - start_time)

        # Simulate e2e_latency
        e2e_latency = time.time() - start_time

        # Check RPS limit
        if time.time() - start_time < 1 / rps_limit:
            continue

        print(f"TTFT: {ttft:.2f} s, TPS: {tps:.2f}, e2e_latency: {e2e_latency:.2f} s, RPS: {1 / e2e_latency:.2f}")

# Define models and their parameters
models = [
    ("GPT-4o", 0.2, 200, 10),
    ("Llama 3.1 405", 0.5, 150, 5),
    ("Mistral Large2", 0.1, 300, 20)
]

# Run simulations
for model in models:
    simulate_llm(*model)