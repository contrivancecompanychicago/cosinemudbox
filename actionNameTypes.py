from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import json

@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
        values = request.get("input")
        return cls(**values)

    def to_json(self):
        return json.dumps(asdict(self))

@dataclass
class ApiRestQOLocationsFictional5Input(RequestMixin):
  locationId: Optional[Any]
  object: Optional[QOLocationsFictionalSetInputInput]

@dataclass
class QOLocationsFictionalSetInputInput(RequestMixin):
  latitude: Optional[Any]
  locationId: Optional[Any]
  longitude: Optional[Any]
  playableActivity: Optional[str]
  playableArea: Optional[Any]
  playableDifficulty: Optional[str]
  playableDuration: Optional[Any]
  playableEquipment: Optional[str]
  playableSurface: Optional[str]
  playableTime: Optional[str]
  playableWeather: Optional[str]
  terrainType: Optional[str]

@dataclass
class ApiRestQOLocationsFictional3Input(RequestMixin):
  locationId: Optional[Any]

@dataclass
class SampleInput(RequestMixin):
  username: str
  password: str

@dataclass
class ApiRestQOLocationsFictional6(RequestMixin):
  updateQOLocationsFictionalByPk: Optional[UpdateQOLocationsFictionalByPk]

@dataclass
class UpdateQOLocationsFictionalByPk(RequestMixin):
  latitude: Optional[Any]
  locationId: Optional[Any]
  longitude: Optional[Any]
  playableActivity: Optional[str]
  playableArea: Optional[Any]
  playableDifficulty: Optional[str]
  playableDuration: Optional[Any]
  playableEquipment: Optional[str]
  playableSurface: Optional[str]
  playableTime: Optional[str]
  playableWeather: Optional[str]
  terrainType: Optional[str]

@dataclass
class ApiRestQOLocationsFictional4(RequestMixin):
  qOLocationsFictionalByPk: Optional[QOLocationsFictionalByPk]

@dataclass
class QOLocationsFictionalByPk(RequestMixin):
  latitude: Optional[Any]
  locationId: Optional[Any]
  longitude: Optional[Any]
  playableActivity: Optional[str]
  playableArea: Optional[Any]
  playableDifficulty: Optional[str]
  playableDuration: Optional[Any]
  playableEquipment: Optional[str]
  playableSurface: Optional[str]
  playableTime: Optional[str]
  playableWeather: Optional[str]
  terrainType: Optional[str]

@dataclass
class SampleOutput(RequestMixin):
  accessToken: str

@dataclass
class Mutation(RequestMixin):
  actionName: Optional[SampleOutput]

@dataclass
class actionNameArgs(RequestMixin):
  arg1: SampleInput
