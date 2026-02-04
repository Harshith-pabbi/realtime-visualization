import random
import math
import time

class TelemetryStream:
    def __init__(self, noise_level=5.0):
        """
        Simulates a continuous stream of telemetry data.
        :param noise_level: The amount of random fluctuation to add.
        """
        self.noise_level = noise_level
        self.start_time = time.time()

    def generate_point(self):
        """
        Creates a single data point (timestamp, value).
        Logic: A base value with a sine wave pattern plus random noise.
        """
        elapsed = time.time() - self.start_time
        
        # Create a base signal (e.g., a temperature wave)
        base_signal = 50 + (math.sin(elapsed * 2) * 15)
        
        # Add random noise for realism
        noise = random.uniform(-self.noise_level, self.noise_level)
        
        return elapsed, base_signal + noise

    def stream_generator(self):
        """A Python Generator that yields points indefinitely."""
        while True:
            yield self.generate_point()
            # Optional: Slight sleep to prevent CPU spiking
            time.sleep(0.01)