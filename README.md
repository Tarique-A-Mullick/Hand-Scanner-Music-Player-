# 🎶 HandScan Music Player

> Play music with just a wave of your hand ✋🎵  
> A futuristic, touchless music experience using gesture recognition.

![Banner](assets/banner.gif) <!-- Replace with your animated demo or logo -->


<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZ3bHFzNmdvcWkxdXV5ZzMyMHJmNzU3N2I3ZGxjMWNjaWN2N2Q2MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KovJk52xZxvKw/giphy.gif" width="300"/>
  <br/>
  <b>👋 Big Update Loading...</b><br/>
  New features arriving tomorrow!
</p>


---

## 🌟 Project Overview

**HandScan Music Player** is an innovative application that transforms your hand movements into music controls. No clicks, no taps — just gestures. Using hand tracking technology and a smart algorithm, this system detects your hand's position and triggers musical notes or playlists.

Whether you're an artist, a tech enthusiast, or just someone who loves cool interactive gadgets, this project brings the magic of touchless control to music.

---

## 🖼️ Demo Preview

| Gesture | Action |  
|--------|--------|  
| ✋ Palm Open | Play Music |  
| 🤚 Palm Away | Pause |  
| 👉 Pointing Right | Next Track |  
| 👈 Pointing Left | Previous Track |  

<p align="center">
  <img src="assets/hand-scan-demo.gif" alt="Demo" width="600"/>
</p>

---

## ⚙️ How It Works

1. **Camera Input**: Captures real-time hand movement.
2. **Hand Tracking**: Uses a hand detection model (e.g., Mediapipe).
3. **Gesture Mapping**: Maps gestures to specific music actions.
4. **Audio Playback**: Plays or changes music based on recognized gesture.

---

## 🧰 Tech Stack

- 🔍 **Mediapipe** – for hand gesture detection  
- 🎵 **Python + Pygame / PyDub** – for music control  
- 🎥 **OpenCV** – for camera input and UI feedback  
- 🚀 Future Plan: Integrate with Spotify API for real-time streaming  

---

## 📸 Screenshots

<p float="left">
  <img src="assets/ui-1.png" width="300"/>
  <img src="assets/ui-2.png" width="300"/>
  <img src="assets/ui-3.png" width="300"/>
</p>

---

## 🔮 Coming Soon

- 🧠 Custom gesture training  
- 🎶 Spotify playlist integration  
- 🎤 Voice + Gesture combo control  
- 🌐 Web-based version  

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/your-username/handscan-music-player.git
cd handscan-music-player
pip install -r requirements.txt
python main.py
