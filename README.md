# ASCII Motion

A Python project for creating ASCII art animations.

## Prerequisites

-   Python 3.x
-   uv package manager

## Installation

1. Clone this repository:

```bash
git clone https://github.com/dnafolayan/ascii-motion.git
cd ascii-motion
```

2. Install dependencies using uv:

```bash
uv sync
```

3. Activate the virtual environment

```bash
source .venv/bin/activate # Linux / WSL / macOS
.venv\Scripts\activate # Windows (PowerShell / CMD)
```

## Usage

Run the main script:

```bash
uv run main.py --source <"camera" / "video">
```

> **Note**: When using WSL on Windows, the `--source camera` option may not work due to limited webcam access in WSL. Consider using PowerShell/CMD or native Linux for camera functionality.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

-   Divine Afolayan

## Acknowledgments

-   [`ascii-media` by John Afolayan](https://github.com/jnafolayan/ascii-media)
