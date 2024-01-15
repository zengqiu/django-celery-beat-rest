from django_filters import rest_framework as filters
from django_celery_beat.models import (
    ClockedSchedule, SolarSchedule, SOLAR_SCHEDULES, CrontabSchedule, IntervalSchedule, PeriodicTask
)


class ClockedScheduleFilter(filters.FilterSet):
    clocked_time = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = ClockedSchedule
        fields = ['clocked_time']


class SolarScheduleFilter(filters.FilterSet):
    event = filters.ChoiceFilter(choices=SOLAR_SCHEDULES)

    class Meta:
        model = SolarSchedule
        fields = ['event']


class CrontabScheduleFilter(filters.FilterSet):
    timezone = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class IntervalScheduleFilter(filters.FilterSet):
    period = filters.ChoiceFilter(choices=IntervalSchedule.PERIOD_CHOICES)

    class Meta:
        model = IntervalSchedule
        fields = '__all__'


class PeriodicTaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    task = filters.CharFilter(lookup_expr='icontains')
    start_time = filters.DateTimeFromToRangeFilter()
    last_run_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = PeriodicTask
        fields = ['enabled', 'one_off']
