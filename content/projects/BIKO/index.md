---
title: BIKO
date: 2025-03-11
description: Vehicular Networks course final project
tags:
  - Networks
  - "#python"
  - Wireless
---

## **Vehicular Networks and Cooperative Mobility Systems**

This course explored the technologies behind intelligent mobility, focusing on **wireless communication**, **autonomous cooperative systems**, and **vehicular networks**. I worked with concepts like **V2X communication**, **network architecture**, **protocol stacks**, and **Internet integration**.

We studied **cooperative applications** for mobility, their **network requirements**, and how to support them using **event-driven and periodic services**. At the transport level, I learned about **MANET routing**, **location-based addressing**, **IPv6**, and **Mobile IP**, gaining hands-on knowledge of how real-time communication and data flow are managed in dynamic, mobile environments.

---
## Problem to solve

For the final project we had to solve a **mobility problem** we found from queering people on the streets around our faculty. We choose bike theft.

**Bike theft** is a widespread issue in urban areas, **discouraging people from using personal mobility devices like bicycles and scooters**. 

Despite physical locks, theft remains common and often goes unreported or unresolved, leading to **low public trust** and **reduced adoption of eco-friendly transport**. 

Existing solutions **lack real-time responsiveness** and integration with smart city infrastructure.



---

## BIKO

Traditional anti-theft measures (locks, GPS trackers) are isolated and ineffective in real time. Urban areas lack **decentralized, cooperative systems** capable of detecting and responding to theft dynamically. BIKO addresses this by creating a **local ad hoc network** where devices communicate to monitor, detect, and report suspicious activity collectively.




<div style="width: 100%; max-width: 1200px; position: relative;">
	<iframe src="https://drive.google.com/file/d/1Y5JWTMZTVr-n5ZawNSPBwZmdhqnxDdKd/preview" width="640" height="380" allow="autoplay"></iframe>
</div>






**Key Technologies & Architecture:**

- **RSU-OBU Communication (Ad Hoc Network):**  
    BIKO creates a **wireless communication link** between On-Board Units (OBUs) on bikes and Road Side Units (RSUs) deployed in bike parking zones. This **V2I (Vehicle-to-Infrastructure)** setup allows:
    
    - Authentication via RFID when entering or leaving a monitored zone.
    - Detection of stolen bikes.
    - Low-latency alerts to nearby RSUs in the absence of Internet.

- **OBU (On-Board Unit):**
    
    - Embedded with RFID tag for user authentication and Raspberry pico for V2I communication.
    - Designed to be **low-power**, small, and easy to deploy.

- **RSU (Road Side Unit):**
    
    - Raspberry Pi-based node with RFID reader, camera, and network interface.
    
    - Acts as a **communication relay**, interfacing with both the OBU locally and the centralized web system via Wi-Fi or Ethernet.
    
- **Network Protocol Design:**
    
    - Initial prototype uses **Wi-Fi-based ad hoc communication** to establish peer-to-peer discovery between RSUs and OBUs.
    
    - Supports future enhancements using **MANET routing**, **location-based addressing**, and **V2X stack integration**.
    
- **Web Application & Back-end:**
    
    - Developed with **Python (Flask)** for user registration, theft alerts, and data visualization.
    
    - **Alerts** are pushed in **real time** to users and admins.


### Important Links

- [Web app](https://biko-02-01.vercel.app/) (Demo version)

<div style="width: 100%; max-width: 1200px; aspect-ratio: 16 / 9; position: relative;">
	  <iframe src="https://drive.google.com/file/d/1Qwr_KkDbNtwPCptsXnJ-1d0rMPFziPW6/preview" width="640" height="380" allow="autoplay"></iframe>
</div>

