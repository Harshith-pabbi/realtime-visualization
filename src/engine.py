import time
from collections import deque
from data_stream import TelemetryStream # This connects to your new file

class DataEngine:
    def __init__(self, buffer_size=60):
        self.buffer_size = buffer_size
        self.x_buffer = deque(maxlen=self.buffer_size)
        self.y_buffer = deque(maxlen=self.buffer_size)
        
        # Initialize the data source
        self.stream = TelemetryStream()

    def update_buffers(self):
        # Get a fresh point from the data_stream.py file
        ts, val = self.stream.generate_point()
        
        self.x_buffer.append(ts)
        self.y_buffer.append(val)
        
        return list(self.x_buffer), list(self.y_buffer)

    def get_stats(self):
        if not self.y_buffer:
            return {"avg": 0, "max": 0}
        return {
            "avg": sum(self.y_buffer) / len(self.y_buffer),
            "max": max(self.y_buffer)
        }