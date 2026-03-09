import streamlit as st
import matplotlib
matplotlib.use("Agg")

import os
import sys
import time
import matplotlib.pyplot as plt

# ---- Fix import path ----

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from engine import DataEngine
from utils import load_theme_config

class RealTimeDashboard:
    def __init__(self, theme_key="dark_emerald"):
        self.engine = DataEngine(buffer_size=60)
        self.theme = load_theme_config(theme_key)

        self.fig, self.ax = plt.subplots(figsize=(10, 6))

        self.line, = self.ax.plot(
            [],
            [],
            color=self.theme['line_color'],
            marker='o',
            markersize=4,
            markerfacecolor=self.theme['marker_color'],
            lw=2
        )

        self.apply_styles()

    def apply_styles(self):
        self.fig.patch.set_facecolor(self.theme['bg_color'])
        self.ax.set_facecolor(self.theme['ax_color'])

        self.ax.set_xlabel("Time (Seconds)", color=self.theme['text_color'])
        self.ax.set_ylabel("Telemetry Value", color=self.theme['text_color'])

        self.ax.grid(True, linestyle='--', alpha=0.3, color=self.theme['grid_color'])
        self.ax.tick_params(colors=self.theme['text_color'])

    def update_plot(self):
        x, y = self.engine.update_buffers()
        stats = self.engine.get_stats()

        self.line.set_data(x, y)

        if len(x) > 0:
            self.ax.set_xlim(x[0], x[-1] + 1)
            self.ax.set_ylim(0, 100)

            title = f"RT Telemetry | Avg: {stats['avg']:.1f} | Max: {stats['max']:.1f}"
            self.ax.set_title(title, color=self.theme['text_color'], fontsize=12)

            return self.fig

def main():
    st.set_page_config(page_title="Real Time Sensor Dashboard", layout="wide")

    st.title("📡 Real Time Sensor Data Visualizer")

    dashboard = RealTimeDashboard()

    chart = st.empty()

    while True:
        fig = dashboard.update_plot()

        chart.pyplot(fig)

        time.sleep(0.5)

if __name__ == "__main__":
    main()