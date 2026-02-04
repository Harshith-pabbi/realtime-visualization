import time
import sys
import os

# Ensure the script can find the 'src' folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine import DataEngine

def run_performance_test():
    print("🚀 Starting Performance Benchmark...")
    
    # Initialize engine with your 60-point buffer
    engine = DataEngine(buffer_size=60)
    iterations = 1000
    latencies = []

    # Run the benchmark
    for _ in range(iterations):
        start = time.perf_counter()
        engine.update_buffers()
        end = time.perf_counter()
        
        # Calculate latency in milliseconds
        latencies.append((end - start) * 1000)

    avg_latency = sum(latencies) / iterations
    max_latency = max(latencies)

    print("-" * 40)
    print(f"Results for {iterations} iterations:")
    print(f"Average Processing Time: {avg_latency:.4f} ms")
    print(f"Max Processing Time:     {max_latency:.4f} ms")
    print("-" * 40)

    # Validation Logic
    if avg_latency < 50:
        print("✅ TEST PASSED: Engine is optimized for sub-50ms refresh rates.")
    else:
        print("❌ TEST FAILED: Performance bottleneck detected.")

if __name__ == "__main__":
    run_performance_test()