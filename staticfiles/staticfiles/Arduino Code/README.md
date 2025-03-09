
# Health Monitoring System with Edge AI

![Project Banner](https://images.unsplash.com/photo-1721114989769-0423619f03d2?q=80&w=3566&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)  
*Remote patient monitoring system with heart disease risk prediction*

## Overview
This Arduino-based system collects vital health metrics, analyzes them using an Edge Impulse machine learning model, and transmits data to a remote server for medical monitoring. The device features offline capabilities with local data storage when internet connectivity is unavailable.
Th device too has the ability to make prediction on the device since a machine learning is directly connected and deployed on the device.

## Key Features
- **Multi-Sensor Integration** - Collects 7 vital health parameters
- **Real-Time Risk Prediction** - ML model analyzes heart disease risk (High/Low)
- **Offline Resilience** - Local storage for 100+ records using SPIFFS
- **Secure Sync** - Encrypted HTTPS transmission with duplicate prevention
- **Smart Connectivity** - Automatic WiFi reconnection and data retries

## Hardware Requirements
| Component | Specification | Purpose |
|-----------|---------------|---------|
| **Main Board** | ESP32-WROOM-32 | Data processing & connectivity |
| **ECG Sensor** | AD8232 Heart Monitor | Cardiac electrical activity |
| **BP Sensor** | MAX30102 Pulse Oximeter | Blood pressure monitoring |
| **HR Sensor** | SEN-11574 Pulse Sensor | Heart rate measurement |
| **Storage** | SPIFFS (Internal) | Local data storage |
| **Power** | 3.7V 2000mAh LiPo | Mobile operation |

## Software Requirements
- Arduino IDE 2.3+
- Edge Impulse CLI
- Required Libraries:
  - `WiFi.h`
  - `HTTPClient.h`
  - `SPIFFS.h`
  - `ArduinoJSON 6.21+`
  - Edge Impulse Inference Library

## 🚀 Installation
1. **Arduino Setup**
   ```bash
        # Install required libraries
        arduino-cli lib install "WiFi" 
        arduino-cli lib install "ArduinoJSON"
    ```

2. **Edge Impulse Setup**
   ```bash
        # Install Edge Impulse CLI

        ### Arduino Library Usage 
        Built Arduino library
        - Add this library through the Arduino IDE via:
        - `Sketch` > `Include Library` > Add .ZIP Library...

        ## Examples can then be found under:
        - File > Examples > heart_inferencing
   ```

3. **Configuration**
    ```bash
        // Set in code:
        const char* ssid = "YOUR_WIFI_SSID";
        const char* password = "YOUR_WIFI_PASS";
        int patient_id = 123; // Unique patient ID
        String serverUrl = "https://your-server.com/api/...";
    ```

4. **Build and Upload**
    ```bash
        # Build the project
        arduino-cli compile --fqbn esp32:esp32:esp32-wroom-32

        # Upload to ESP32
        arduino-cli upload -p /dev/ttyUSB0
    ```


##  Usage
1. ### Data Collection Cycle
    Every 60 seconds:
    - Collects sensor readings
    - Runs ML inference
    - Stores data locally if offline
    - Transmits via WiFi when available


2. ### ML Prediction Output
    ```bash
        High Risk: 82.3%
        Low Risk: 17.7%
    ```

3. ### Data Transmission Format
    ```json
   {
     "patient": 123,
     "blood_pressure": 120.5,
     "heart_rate": 75,
     "risk_score": 82.3,
     "timestamp": 1717025603
   }


## Machine Learning Model
**Model Architecture**  
- Input Features: 7 health parameters
- Output Classes: High Risk (≥60%) / Low Risk
- Training Accuracy: 94.2% (Edge Impulse)

**Input Features**:
1. Age
2. Sex 
3. Blood Pressure
4. Heart Rate
5. Resting ECG
6. Exercise-Induced Angina
7. ST Depression

##  Troubleshooting
| Issue | Solution |
|-------|----------|
| WiFi Connection Failed | Check credentials & signal strength |
| Data Sync Issues | Verify server endpoint & check SPIFFS |
| Inaccurate Readings | Recalibrate sensors & check placements |
| Storage Full | Increase MAX_STORED_RECORDS value |

##  Future Enhancements
- Add OTA model updates
- Implement BLE emergency alerts
- Add OLED display for local readouts
- Power optimization for battery mode
- Multi-patient support via device pairing

## License
Apache 2.0 - See [LICENSE](LICENSE) for details

## Acknowledgments
- Edge Impulse for ML tooling
- Arduino ecosystem
- ESP32 developer community


This README provides comprehensive documentation while highlighting:
1. The ML integration and sensor requirements
2. Clear setup instructions for medical IoT deployment
3. Data flow explanations for clinical staff
4. Troubleshooting for field maintenance
5. Future directions for technical contributors



### Authors 
- [Kayongo Johnson Brian](https://github.com/kaybrian)