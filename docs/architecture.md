# System Architecture

## Overview
The RT-Viz Framework is built on a modular, three-layer architecture to ensure high performance and maintainability.

### 1. Data Layer (`data_stream.py`)
- Acts as a **Producer**.
- Uses a Python generator to simulate telemetry data.
- Decoupled from the engine, allowing for easy integration with hardware APIs or WebSockets.

### 2. Logic Layer (`engine.py`)
- Acts as a **Processor**.
- Implements a `collections.deque` buffer for $O(1)$ time complexity on sliding window updates.
- Calculates real-time statistics (Avg/Max/Min).

### 3. Presentation Layer (`dashboard.py`)
- Acts as a **Consumer**.
- Uses Matplotlib's `FuncAnimation` with `blit=True` to minimize CPU usage.
- Loads UI configurations from the Dynamic Theming Engine.