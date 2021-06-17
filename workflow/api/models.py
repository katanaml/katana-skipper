from pydantic import BaseModel


class ServiceInfo(BaseModel):
    service_id: str
    queue_name: str
