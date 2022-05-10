import json

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import AnnouncedPuResults, PollingUnit, AnnouncedLgaResults, PollingUnitLGAResult
from .tasks import create_total_polling_unit_result


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncedPuResultsView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        if data.get('result_id'):
            announced_pu_results = AnnouncedPuResults.objects.get(result_id=data.get('result_id'))
            if data.get('party_score'):
                announced_pu_results.party_score = int(data.get('party_score'))
                create_total_polling_unit_result.delay()
        return redirect('announced_pu_result')

    def get(self, request):
        polling_unit_result = AnnouncedPuResults.objects.all()

        context = {
            'polling_unit_result': polling_unit_result
        }
        return render(request, 'announced_pu_results.html', context=context)


class AnnouncedLGAResultsView(View):

    def get(self, request, *args, **kwargs):
        announced_lga_results = AnnouncedLgaResults.objects.all()

        context = {
            'announced_lga_results': announced_lga_results
        }
        return render(request, 'announced_lga_results.html', context=context)


class PollingUnitView(View):

    def get(self, request, *args, **kwargs):
        polling_unit = PollingUnit.objects.all()

        context = {
            'polling_unit': polling_unit
        }
        return render(request, 'polling_unit.html', context=context)


class PollingUnitLGAResultView(View):
    def get(self, request):
        polling_unit_lga_result = PollingUnitLGAResult.objects.all()
        # celery task
        create_total_polling_unit_result.delay()
        context = {
            'polling_unit_lga_result': polling_unit_lga_result
        }
        return render(request, 'polling_unit_total_result.html', context=context)
