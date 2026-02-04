import sys
import os

# Path fix to find the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine import DataEngine

def test_buffer_limit():
    print("🧪 Testing Buffer Boundary Logic...")
    
    LIMIT = 60
    engine = DataEngine(buffer_size=LIMIT)
    
    # 1. Fill the buffer beyond the limit (simulating 100 data points)
    for _ in range(100):
        engine.update_buffers()
    
    # 2. Extract the current buffers
    x_data = list(engine.x_buffer)
    y_data = list(engine.y_buffer)
    
    # 3. Assertions (The Test)
    print(f"Current X-Buffer Length: {len(x_data)}")
    print(f"Current Y-Buffer Length: {len(y_data)}")
    
    if len(x_data) == LIMIT and len(y_data) == LIMIT:
        print("✅ SUCCESS: Buffer correctly maintains a 60-point sliding window.")
    else:
        print(f"❌ FAILURE: Buffer size is {len(x_data)}, expected {LIMIT}.")

def test_buffer_sliding_behavior():
    print("\n🧪 Testing Sliding Behavior...")
    engine = DataEngine(buffer_size=5) # Smaller limit for easy testing
    
    # Add 5 points
    for i in range(5):
        engine.x_buffer.append(i)
    
    first_element = engine.x_buffer[0] # Should be 0
    
    # Add 1 more point
    engine.x_buffer.append(5)
    new_first_element = engine.x_buffer[0] # Should now be 1
    
    if new_first_element == 1:
        print("✅ SUCCESS: Oldest data was correctly 'popped' out.")
    else:
        print("❌ FAILURE: Oldest data was not removed.")

if __name__ == "__main__":
    test_buffer_limit()
    test_buffer_sliding_behavior()