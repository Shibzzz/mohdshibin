---
layout: default
title: WiFi DoS Detection
permalink: /projects/wifi-dos/
---

# 📶 WiFi DoS Detection Tool

## Overview

This project focuses on detecting **Denial of Service (DoS)** attacks targeting wireless networks, specifically WiFi-based infrastructure. These types of attacks aim to disconnect or disrupt legitimate clients by exploiting weaknesses in the 802.11 protocol.

The tool passively listens to network traffic using a wireless interface in monitor mode, identifies high volumes of deauthentication packets, and raises alerts when thresholds are breached — indicating a potential DoS attempt.

---

## 🔧 Features

- 📡 Monitors WiFi traffic in real-time
- 🚨 Detects excessive deauthentication/disassociation frames
- 💬 Provides CLI-based alerts and packet summaries
- 📁 Saves logs of suspicious activities for later forensic analysis

---

## 💡 Technologies Used

- **Python**  
- **Scapy** (packet sniffing and parsing)
- **Monitor Mode Interface** (via tools like `airmon-ng`)
- **Linux-based Environment** (tested on Kali and Ubuntu)

---

## 📸 Screenshot / Terminal Output Example

> *(Replace this with a real screenshot if available)*

```text
[!] High DeAuth packet rate detected from MAC: 78:XX:XX:XX:YY:ZZ
    Possible DoS Attack in progress targeting: FF:FF:FF:FF:FF:FF (broadcast)
    Packets captured: 142 in 10 seconds
