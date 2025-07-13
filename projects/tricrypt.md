---
layout: default
title: TriCrypt Authentication System
permalink: /projects/tricrypt/
---

# 🔐 TriCrypt Authentication System

## Overview

**TriCrypt** is a multi-layered authentication system I developed as part of my academic research and security project work. The system is designed to enhance user authentication by introducing three independent but complementary verification layers, making it suitable for use in high-security applications such as banking, healthcare, and enterprise environments.

---

## 🔑 Key Features

1. **Level 1 – Passphrase Authentication**  
   Users input a strong text-based passphrase for basic access verification.

2. **Level 2 – Image-Based Puzzle Pattern**  
   During registration, the user arranges a grid-based pattern using drag-and-drop interaction. During login, the same pattern must be re-assembled even when tiles are shuffled.

3. **Level 3 – Gesture + Face Recognition**  
   Using a webcam, the system verifies the user's identity through a combination of facial recognition and unique hand gestures captured via OpenCV and MediaPipe.

---

## 💡 Technologies Used

- **Python** (Core backend logic)
- **OpenCV** (Face & gesture recognition)
- **MediaPipe** (Hand tracking)
- **Tkinter / PyQt** (GUI interactions)
- **SQLite** (User data storage)
- **Jekyll + GitHub Pages** (Project documentation site)

---

## 📸 Screenshots / Demo

> _Add demo GIFs or images if available. You can upload them to `assets/img/tricrypt/` and embed like this:_

```html
<img src="{{ '/assets/img/tricrypt/puzzle-demo.png' | relative_url }}" alt="Puzzle Demo" style="max-width:100%; border-radius:8px;" />
