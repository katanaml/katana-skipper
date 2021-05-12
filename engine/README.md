# Workflow engine

## Instructions

* **uvicorn endpoint:app --reload**

* **celery -A api.worker worker --loglevel=INFO**

* URL: http://127.0.0.1:8000/api/v1/skipper/tasks/docs