from celery import shared_task

from poll.models import PollingUnitLGAResult, Lga, AnnouncedLgaResults


def check_to_create_instance():
    announced_lga_results = 0
    polling_unit_lga_result = 0
    for item in AnnouncedLgaResults.objects.all():
        announced_lga_results = item.party_score
    for item in PollingUnitLGAResult.objects.all():
        polling_unit_lga_result = item.total_lga_result
    if (
            polling_unit_lga_result != announced_lga_results
            and Lga.objects.count() != PollingUnitLGAResult.objects.count()):
        return True
    return False

@shared_task
def create_total_polling_unit_result():
    # only run this loop if count is not equal.
    if check_to_create_instance():
        for item in Lga.objects.all():
            try:
                for polls in AnnouncedLgaResults.objects.filter(lga_name=item.lga_id):
                    polling_unit_lga_result = PollingUnitLGAResult.objects.filter(lga_id=polls.lga_name).first()
                    if polling_unit_lga_result:
                        polling_unit_lga_result.total_lga_result += polls.party_score
                        polling_unit_lga_result.total_lga_polls += 1
                        polling_unit_lga_result.save()
                    else:
                        PollingUnitLGAResult.objects.create(
                            lga_id=item.lga_id, lga_name=item.lga_name, total_lga=1,
                            total_lga_result=polls.party_score)
            except Exception as a:
                print(a)
                pass
