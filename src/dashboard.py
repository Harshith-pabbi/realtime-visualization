import matplotlib
# Use TkAgg backend to ensure a window pops up on all operating systems
matplotlib.use('TkAgg') 

import os
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- PATH FIX: Ensures imports work correctly ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from engine import DataEngine
from utils import load_theme_config

class RealTimeDashboard:
    def __init__(self, theme_key="dark_emerald"):
        # 1. Initialize Engine & Theme
        self.engine = DataEngine(buffer_size=60)
        self.theme = load_theme_config(theme_key)
        
        # 2. Setup Figure and Axes
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.line, = self.ax.plot([], [], 
                                 color=self.theme['line_color'], 
                                 marker='o', 
                                 markersize=4,
                                 markerfacecolor=self.theme['marker_color'],
                                 lw=2)
        
        self.apply_styles()

    def apply_styles(self):
        """Applies JSON theme settings to the plot."""
        self.fig.patch.set_facecolor(self.theme['bg_color'])
        self.ax.set_facecolor(self.theme['ax_color'])
        self.ax.set_xlabel("Time (Seconds)", color=self.theme['text_color'])
        self.ax.set_ylabel("Telemetry Value", color=self.theme['text_color'])
        self.ax.grid(True, linestyle='--', alpha=0.3, color=self.theme['grid_color'])
        self.ax.tick_params(colors=self.theme['text_color'])

    def animate(self, frame):
        """Main loop called every 50ms."""
        # Update data via the Engine
        x, y = self.engine.update_buffers()
        stats = self.engine.get_stats()
        
        # Update the line data
        self.line.set_data(x, y)
        
        # Auto-scroll the X-axis
        if x:
            self.ax.set_xlim(x[0], x[-1] + 1)
            self.ax.set_ylim(0, 100)
            
            # Update Title with Live Stats
            title = f"RT-Telemetry | Avg: {stats['avg']:.1f} | Max: {stats['max']:.1f}"
            self.ax.set_title(title, color=self.theme['text_color'], fontsize=12)
            
        return self.line,

    def run(self):
        """Starts the real-time animation loop."""
        # interval=50 provides the sub-50ms refresh rate
        self.ani = FuncAnimation(self.fig, self.animate, interval=50, blit=True)
        plt.show()

if __name__ == "__main__":
    # Options: "dark_emerald", "cyber_punk", "corporate_light"
    app = RealTimeDashboard(theme_key="dark_emerald")
    app.run()