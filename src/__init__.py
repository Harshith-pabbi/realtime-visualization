from data_stream import TelemetryStream # Import your new stream

class DataEngine:
    def __init__(self, buffer_size=60):
        self.buffer_size = buffer_size
        self.x_buffer = deque(maxlen=self.buffer_size)
        self.y_buffer = deque(maxlen=self.buffer_size)
        
        # Use the dedicated stream class
        self.stream = TelemetryStream()

    def fetch_new_data(self):
        # Simply call the stream generator
        return self.stream.generate_point()