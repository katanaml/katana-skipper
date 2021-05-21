# Workflow engine

## Instructions

* **pip install -r requirements.txt**

* **uvicorn endpoint:app --reload**

* **celery -A api.worker worker --loglevel=INFO**

* **python event_receiver_test.py**

* URL: http://127.0.0.1:8000/docs
