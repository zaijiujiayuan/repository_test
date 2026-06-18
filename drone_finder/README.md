# Drone Finder - RTL-SDR Radio Detection and Localization System

A comprehensive Python-based system for detecting and localizing drone radio signals using RTL-SDR (software-defined radio) hardware.

## Features

- **Dual-Channel Synchronous Sampling**: Real-time IQ data capture from two antennas
- **Spectrum Analysis**: Automatic frequency scanning and peak detection
- **Direction Finding**: Phase-based interferometric and multi-point triangulation methods
- **Positioning Algorithms**: Forward intersection, Kalman filtering, and triangulation
- **Visualization**: Radar UI, signal heatmaps, and interactive maps
- **Data Logging**: Complete audit trail with timestamps and raw IQ data storage

## Project Structure

```
drone_finder/
├── hardware/              # Hardware abstraction layer (SDR, GPS, antenna control)
├── signal_processing/     # Spectrum analysis and phase detection
├── localization/          # Positioning algorithms
├── visualization/         # UI and map rendering
├── data/                  # Data storage (raw IQ, processed results, logs)
├── utils/                 # Shared utilities
├── tests/                 # Unit test suite
├── scripts/               # Calibration and utility scripts
└── docs/                  # Documentation
```

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Hardware**:
   - Edit `config.yaml` with your antenna spacing and frequency settings
   - Run antenna calibration: `python scripts/calibrate_antennas.py`

3. **Run the System**:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- RTL-SDR hardware
- Dual antenna system with electronic switch (optional)
- GPS module (optional, for geo-tagging)

## Legal Notice

This system is designed for **receive-only** operation. No RF signals are transmitted. 
Ensure compliance with local regulations before use.

## Documentation

- [Setup Guide](docs/setup_guide.md) - Hardware installation and configuration
- [Algorithm Theory](docs/algorithm_theory.md) - Mathematical foundations
- [Legal Disclaimer](docs/legal_disclaimer.md) - Usage guidelines

## License

See LICENSE file for details.
