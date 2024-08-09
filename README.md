
# Basic-Port-Scanner

<a>
  <img src="https://github.com/VincentRitchie/Basic-Port-Scanner/blob/main/portscannerpython.png" alt="Logo" width="650" />
</a>

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Description
This repository contains a Python implementation of a basic port scanner. The port scanner allows users to scan a specified range of ports on a target IP address to identify open ports. The program utilizes sockets to attempt connections to the specified ports and reports which ports are open.

## Features
- **Port Scanning:** Scan a range of ports on a target IP address to identify open ports.
- **Socket Programming:** Utilizes Python's socket library for network communication.
- **Customizable Port Range:** Specify the start and end ports for the scanning range.

## Installation
To install and run this project, follow these steps:

```sh
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

## Usage
To use this project, run the following command:

```sh
python port_scanner.py
```
Follow the prompts to input the target IP address and the range of ports to scan.

## Screenshot

<a>
  <img src="https://github.com/VincentRitchie/Basic-Port-Scanner/blob/main/Simple%20Port%20Scanner%20Screenshot.png" alt="Logo" width="650" />
</a>

## Future Enhancements

### 1. **Multi-threaded Scanning**
   - **Description**: Implement multi-threading to improve the scanning speed by scanning multiple ports concurrently.
   - **Benefit**: Faster scanning results, especially when scanning a large range of ports.

### 2. **Service Detection**
   - **Description**: Add functionality to detect and display the service running on each open port (e.g., HTTP, FTP).
   - **Benefit**: Provides more detailed information about open ports, helping to identify potential vulnerabilities.

### 3. **Banner Grabbing**
   - **Description**: Implement banner grabbing to retrieve and display information about the service running on an open port.
   - **Benefit**: Offers insights into the software and version running on open ports, aiding in vulnerability assessments.

### 4. **Output to File**
   - **Description**: Add an option to save the scan results to a file (e.g., TXT, CSV, JSON) for later analysis.
   - **Benefit**: Enables easier documentation and further analysis of scan results.

### 5. **Command-line Arguments**
   - **Description**: Allow users to specify the target IP address, start port, and end port through command-line arguments instead of interactive prompts.
   - **Benefit**: Streamlines usage, making the tool more flexible for advanced users.

### 6. **Logging**
   - **Description**: Implement logging to keep track of scan progress and errors in a log file.
   - **Benefit**: Provides a record of the scanning process, useful for debugging and record-keeping.

### 7. **Improved Exception Handling**
   - **Description**: Enhance exception handling to provide more informative error messages and handle edge cases more gracefully.
   - **Benefit**: Improves the user experience by making the tool more robust and user-friendly.

### 8. **Interactive Progress Bar**
   - **Description**: Add a progress bar to visually indicate the scanning progress.
   - **Benefit**: Enhances the user interface by giving real-time feedback on the scan's progress.

## Contributing

Feel free to submit issues and enhancement requests. Pull requests are also welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/VincentRitchie/Basic-Port-Scanner/blob/main/LICENSE) file for details.

## Author

#### Vincent Chimaobi (CyberGhoxt)

Connect with me on 
- [GitHub](https://www.github.com/VincentRitchie/VincentRitchie)
- [LinkedIn](https://www.linkedin.com/in/vincent-chimaobi-53b458216?trk=contact-info)
- [X](https://x.com/vin_chimaobi042)
