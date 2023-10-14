from .atm import AtmSerializer, DetailAtmSerializer
from .atm_services import AtmServiceSerializer
from .offices import OfficeSerializer,DetailOfficeSerializer
from .schedules import ScheduleSerializer

__all__= (
    AtmSerializer,
    DetailAtmSerializer,
    AtmServiceSerializer,
    OfficeSerializer, DetailOfficeSerializer,
    ScheduleSerializer
)