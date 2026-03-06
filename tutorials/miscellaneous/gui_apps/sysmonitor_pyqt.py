# PyQt System Monitor
# -------------------
# A desktop app using PyQt6 and psutil to monitor system health in real-time.
# Features error handling for OS-specific data like temperatures.

import sys
import psutil
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QProgressBar
from PyQt6.QtCore import QTimer, Qt

class SysMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python System Monitor")
        self.setMinimumWidth(400)

        # 1. Layout and Widgets
        self.layout = QVBoxLayout()
        
        # CPU Info
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.cpu_bar = QProgressBar()
        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.cpu_bar)

        # RAM Info
        self.ram_label = QLabel("RAM Usage: 0%")
        self.ram_bar = QProgressBar()
        self.layout.addWidget(self.ram_label)
        self.layout.addWidget(self.ram_bar)

        # Temperature Info (The "Problematic" one)
        self.temp_label = QLabel("CPU Temperature: N/A")
        self.layout.addWidget(self.temp_label)

        # Set central widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # 2. Timer for Real-Time Updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000) # Update every 1 second

    def update_stats(self):
        # Fetch CPU and RAM (Generally works on all OS)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent

        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")
        self.cpu_bar.setValue(int(cpu_usage))

        self.ram_label.setText(f"RAM Usage: {ram_usage}%")
        self.ram_bar.setValue(int(ram_usage))

        # 3. Try-Catch for Sensors (Temperatures often fail on Windows/certain hardware)
        try:
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                current_temp = temps['coretemp'][0].current
                self.temp_label.setText(f"CPU Temperature: {current_temp}°C")
            elif not temps:
                self.temp_label.setText("CPU Temperature: Sensor not found")
            else:
                # Catch-all for different sensor names on various Linux distros
                first_key = list(temps.keys())[0]
                self.temp_label.setText(f"CPU Temperature: {temps[first_key][0].current}°C")
        
        except (AttributeError, KeyError, IndexError):
            # This handles Windows where sensors_temperatures() is often not supported
            self.temp_label.setText("CPU Temperature: Not supported on this OS")
        except Exception as e:
            self.temp_label.setText(f"Temperature Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SysMonitor()
    window.show()
    sys.exit(app.exec())