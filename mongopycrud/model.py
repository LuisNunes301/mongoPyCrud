from typing import Optional
from odmantic import Field, Model


class Constumers(Model):
    name: str
    location: Optional[str] =None

instances = [
    Constumers(name='Luis', location='BR')
    Constumers(name='Vini', location='NA')
    Constumers(name='Nunes', location='BR')
]