from django.http import JsonResponse

from data.models import AgeRanges, Genders


def metadata():
    age_ranges = [{"id": row.id, "range": row.range} for row in AgeRanges.objects.all()]
    genders = [{"id": row.id, "range": row.title} for row in Genders.objects.all()]

    return JsonResponse({"age_ranges": age_ranges, 'genders': genders})
