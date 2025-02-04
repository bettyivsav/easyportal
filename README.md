# EasyPortal

## Overview

EasyPortal is a Python application designed to monitor the health and performance of hard drives on Windows systems. It provides valuable maintenance recommendations to help users optimize their computer's storage performance and reliability.

## Features

- **Disk Information**: Retrieves and displays detailed information about each mounted disk, including total, used, and free space.
- **Disk Health Status**: Utilizes Windows Management Instrumentation (WMI) to check the health status of connected disk drives.
- **Maintenance Recommendations**: Offers suggestions for maintaining disk health, such as cleaning up files on disks that are nearing capacity and defragmenting NTFS drives.

## Requirements

- Windows operating system
- Python 3.x
- `psutil` library

## Installation

1. Ensure that Python 3.x is installed on your Windows system.
2. Install the required Python library by running:
   ```bash
   pip install psutil
   ```

## Usage

1. Clone the repository or download the `easy_portal.py` file.
2. Open a command prompt and navigate to the directory containing the `easy_portal.py` file.
3. Run the script using Python:
   ```bash
   python easy_portal.py
   ```

## Notes

- This tool is specifically designed for Windows environments and may not function correctly on other operating systems.
- Regularly monitoring and maintaining your hard drives can help prevent data loss and improve system performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.