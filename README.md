# SAVI_WOMEN_SAFETY
---
# SAVI - Safe and Vigilant Initiative

SAVI is a comprehensive, AI-powered mobile application designed to enhance personal safety, especially for women. The app integrates real-time location tracking, automated SOS signaling, and advanced AI-driven features to detect threats, notify emergency contacts, and provide immediate assistance when users need it most.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Contributing](#contributing)

---

## Features

1. **Immediate Help Access**: Instant connection to nearby helpers, emergency contacts, or the police in times of need.
2. **AI-based Threat Detection**: Uses object detection to monitor surroundings, alerting users if they are in a risky situation (e.g., surrounded by unfamiliar individuals).
3. **Real-time Location Sharing**: Users can share their live location with selected contacts for added safety and peace of mind.
4. **Voice-Activated SOS**: Recognizes distress words or phrases like "help" or "bachao" and triggers an emergency alert.
5. **Shake-to-Alert**: Alerts emergency contacts when the phone is shaken multiple times.
6. **Route Safety Guidance**: Identifies and recommends safer routes based on historical safety data.
7. **Geotagged Alerts**: Notifies users when they enter high-risk areas based on crowd-sourced data and prior reports.
8. **Offline Availability**: Core features work offline, ensuring continuous protection even without internet connectivity.
9. **Voice Recording**: Automatically records audio when a threat is detected to provide evidence if needed.

## Installation

To install SAVI on your Android or iOS device:

1. Clone this repository:
   ```bash
   git clone https://github.com/username/SAVI.git
   cd SAVI
   ```
2. For Android: 
   - Open the project in Android Studio.
   - Connect an Android device/emulator.
   - Build and run the app.

3. For iOS:
   - Open the project in Xcode.
   - Connect an iOS device/simulator.
   - Build and run the app.

_Note_: Ensure you have Android Studio or Xcode installed for the respective platform.

## Usage

1. **Account Setup**: Register using your phone number and set up trusted contacts.
2. **Enabling Features**:
   - **Location**: Allow location access for real-time tracking and route guidance.
   - **Microphone**: Enable microphone access for SOS voice activation.
3. **Setting Up Emergency Contacts**: Add trusted contacts to notify them automatically when an alert is triggered.
4. **Testing SOS Features**: Try the shake or voice-activated SOS to familiarize yourself with emergency responses.

## Technology Stack

- **Frontend**: React Native for cross-platform mobile support
- **Backend**: Node.js, Express for server-side processing
- **Database**: MongoDB for storing user profiles, geotags, and incident reports
- **AI and ML**: TensorFlow Lite for on-device threat detection using object and voice recognition
- **Geolocation Services**: Google Maps API for route safety guidance and live location sharing

## Architecture

SAVI follows a modular architecture to ensure scalability and maintainability:
- **User Interface**: React Native components for mobile app interactions.
- **AI Modules**: TensorFlow Lite models deployed for object and voice recognition.
- **Backend**: RESTful API developed with Express, handling SOS requests, contact notifications, and route safety data.
- **Database**: MongoDB stores user profiles, safety reports, and geotagged data.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/YourFeatureName`).
3. Commit your changes.
4. Open a pull request with a detailed description.



---

For questions or feedback, feel free to reach out or open an issue. Together, let’s make the world a safer place with SAVI!
