# Domain Analyzer #

Domain Analyzer is a web application that provides detailed information about a domain name. It includes registration details, DNS records, IP address, location, and security analysis.

## Features

- **Domain Information**: Retrieves information such as registrar, creation date, expiration date, name servers, and more.
- **IP and Location Information**: Provides the IP address and geographical location of the domain.
- **VirusTotal Analysis**: Fetches security information from VirusTotal, including malicious, suspicious, harmless, and undetected status.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS
- **APIs**: Whois API, IP Geolocation API, VirusTotal API

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/domain-analyzer.git
   cd domain-analyzer
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
    ```
  3. Run the application:  
    
        ```
        python app.py
        ```
