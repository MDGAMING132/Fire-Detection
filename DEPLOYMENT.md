# Deployment Guide for Cognitive Fire-Grid

This repository contains the full source code for the Cognitive Fire-Grid system.

## 1. Deploying the Backend (Web Web) to Azure

You can deploy this Flask app to Azure App Service.

1.  **Create an App Service** in Azure (Python 3.9+).
2.  **Connect GitHub**: Connect this repository to the App Service.
3.  **Startup Command**: Set the startup command to:
    ```bash
    gunicorn --bind=0.0.0.0:8000 backend.app:app
    ```
    *(Note: You may need to add `gunicorn` to `requirements.txt`)*

## 2. Connecting the Local Monitor (Camera)

The `live_feed_monitor.py` script runs on your **local machine** (where the drone/camera is) and sends alerts to the Cloud.

1.  Open `backend/live_feed_monitor.py`.
2.  Find the configuration section.
3.  Set the `API_URL` to your deployed Azure domain:

    ```python
    # Example
    API_URL = "https://your-fire-app-name.azurewebsites.net/api/vision-trigger"
    ```

    *Alternatively, set the `FIRE_BACKEND_URL` environment variable on your PC.*

4.  Run the monitor:
    ```bash
    python backend/live_feed_monitor.py
    ```

## 3. Optimizations Included
- **UI/UX**: Glassmorphism design, Skeleton Loading, Responsive Layout.
- **Performance**: Smart Rate Limiting, Exponential Smoothing for sensor data.
- **Reliability**: Auto-reconnect logic and robust error handling.
