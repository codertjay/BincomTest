from django.urls import path
from .views import AnnouncedPuResultsView, PollingUnitView, AnnouncedLGAResultsView, PollingUnitLGAResultView

urlpatterns = [
    path('announced_pu_result/', AnnouncedPuResultsView.as_view(), name='announced_pu_result'),
    path('announced_lga_result/', AnnouncedLGAResultsView.as_view(), name='announced_lga_result'),
    path('polling_unit_lga_result/', PollingUnitLGAResultView.as_view(), name='polling_unit_lga_result'),
    path('', PollingUnitView.as_view(), name='polling_unit'),
]
