# Industry 4.0 Project

![Industry 4.0](image.png)

## Overview
This project focuses on implementing Industry 4.0 principles by integrating data acquisition, automation, and smart monitoring solutions. It leverages LabVIEW, Python, and various sensors to collect, process, and visualize data in an industrial setting.
![image](https://github.com/user-attachments/assets/55633bb1-3b64-4cf6-a1a3-336be46863a7)

## Features
- **Real-time Data Acquisition**: Collects temperature and humidity data.
- **Smart Monitoring**: Uses LabVIEW VIs for data visualization and processing.
- **Email Notifications**: Python script for automated email alerts.
- **Data Logging**: Stores sensor data in CSV format for analysis.
- ![image](https://github.com/user-attachments/assets/d8c318d1-2151-446b-8a78-34784dcf1ac6)

- **Integration with External Devices**: Communicates with microcontrollers and sensors.
![image](https://github.com/user-attachments/assets/a4c77b4c-a82f-4177-99f4-3683cff84533)

## Project Structure
```
/industrie_4_0_project
│── LIFA DHT11 LV9.rar      # LabVIEW Interface for Arduino (LIFA) library
│── README.md               # Project documentation
│── Untitled Project 1.lvproj  # LabVIEW project file
│── read_courbe.vi          # Visualization VI
│── smart_temp_humid.vi     # Main VI for smart monitoring
│── temp_humid.csv          # Logged sensor data
│── read_email.py           # Python script for email notifications
│── action_python.txt       # Notes on Python integration
│── data_email.txt          # Sample email data
```

## Installation & Setup
1. **Install Required Software**:
   - [LabVIEW](https://www.ni.com/en-us/shop/labview.html)
   - [LabVIEW Interface for Arduino (LIFA)](https://www.ni.com/)
   - Python 3.x (if using email automation)
   - Required Python libraries: `pip install smtplib pandas`

2. **Hardware Requirements**:
   - DHT11 temperature & humidity sensor
   - Arduino board
   - Computer running LabVIEW

3. **Clone Repository**:
   ```sh
   git clone https://github.com/dhia06-dridi/industrie_4_0_project.git
   cd industrie_4_0_project
   ```

4. **Run LabVIEW VIs**:
   - Open `Untitled Project 1.lvproj` in LabVIEW.
   - Execute `smart_temp_humid.vi` to start data collection.

5. **Enable Email Notifications (Optional)**:
   - Configure `read_email.py` with your SMTP settings.
   - Run `python read_email.py` to test email alerts.

## Usage
- Connect the Arduino and sensors to your PC.
- Open the LabVIEW project and run the VIs.
- Monitor real-time sensor data.
- Review logged data in `temp_humid.csv`.
- Receive email alerts when thresholds are exceeded.

## Future Enhancements
- Add cloud-based data storage.
- Implement machine learning for predictive maintenance.
- Develop a web dashboard for remote monitoring.

## License
This project is licensed under the MIT License.

## Author
[dhia06-dridi](https://github.com/dhia06-dridi)

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests.


https://github.com/user-attachments/assets/51ddb235-90aa-4507-a7a9-56a8765cc418


