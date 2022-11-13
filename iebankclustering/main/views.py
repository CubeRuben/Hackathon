from django.shortcuts import render
from django.db.models import Q
from .models import IndividualEntrepreneur, IECluster

def index(request):

    query = request.GET.get('q')

    if query == None:
        return render(request, "main/index.html", {'show_result': False})

    try:
        ie = IndividualEntrepreneur.objects.get(INN=query)
        cluster = IECluster.objects.get(INN=query)
    except Exception:
        return render(request, "main/index.html", {'show_result': True, 'found': False})

    return render(request, "main/index.html", {'show_result': True, 'found': True, 'INN': ie.INN, 'registration_date': ie.registration_date, 'region': ie.region, 'okved': ie.okved, 'industry': ie.industry, 'cluster_id': cluster.cluster_id})