![](docs/assets/logo.png)

# thinking

Machine learning made easy 💗⚡

The following are supported:

- Data Annotation PLatform (Lablestudio)
- Invoice OCR [Coming soon]
- ...
- Want to suggest a new service? Submit a feature request.

More services will be added on popular demand.

### How to run?

Install docker and run `docker compose up --build -d`. That is all you have to do.

> *More information will be added soon.*

#### Port information

| Port | Name | User interface | Short description |
--- | --- | --- | --- |
| `8989` | Label studio | http://127.0.0.1:8989 | Data annotation platform |
| `1572` | RabbitMQ | http://127.0.0.1:15672 | Transient message broker. `username:skipper` `password:welcome1`|
| `8000` | Celery API | http://127.0.0.1:8000/docs | Post tasks to task queues and view their status |
| `5000` | Wrokflow API | http://127.0.0.1:5000/docs | Get names of queues using task service IDs |
| `5001` | Logger API |  http://127.0.0.1:5001/docs | Log all infomation in background |
| `5432` | Postgres DB | Coming soon | Persistent database |
| `5432` | PgAdmin | Coming soon | Web UI for postgres DB |
| `7777` | Web app | Coming soon | Web app for everything here |   
| `9999` | backend  | Coming soon | Backend for app at port `s7777` |
| `8080` | NGINX |-| Reverse proxy for tasks API  |
| `5672` | RabbitMQ port | - | Port for event producer and receiver |  


--- 

### Credits

- Our contributors (you can be one of them to. Go to issues section and see if you can send a PR)
- Built on top of [katana-skipper workflow engine](https://github.com/katanaml/katana-skipper).
- OCR powered by [MMOCR](https://github.com/open-mmlab/mmocr)
- Data annotation with [Label Studio](https://github.com/heartexlabs/label-studio)

### Licence

[Apache License 2.0](./LICENSE)
