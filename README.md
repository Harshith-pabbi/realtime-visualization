# Real-Time Data Visualization Framework (RT-Viz)

A high-performance telemetry visualization toolkit built in Python, designed for sub-50ms latency monitoring.

## 🚀 Key Features

- **$O(1)$ Complexity Buffering:** Uses `collections.deque` sliding windows to maintain a consistent 60-point buffer without memory degradation.
- **Dynamic Theming Engine:** Fully configurable UI via `themes.json` (Dark Emerald, Cyber Punk, and Corporate Light).
- **High-Performance Rendering:** Optimized using Matplotlib's `FuncAnimation` with `blit=True` for smooth 20Hz+ refresh rates.
- **Modular Architecture:** Clean separation between Data Ingestion (Engine), Logic (Utils), and Presentation (Dashboard).

## 🛠️ System Architecture

1. **Data Engine**: Generates/Fetches data and manages the memory buffer.
2. **Theme Engine**: Decouples UI styling from the source code using JSON.
3. **Visualization Layer**: Renders real-time telemetry with auto-scrolling axes.

## 📦 Installation & Usage

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. pip install streamlit
4. python src/dashboard.py
