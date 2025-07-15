from django.shortcuts import render
from MiniCopro.models import Annonce
import numpy as np

def stats_view(request):
    result = None

    # filter_type = request.GET.get("type")
    # value = request.GET.get("value")

    filter_type = request.GET("type")
    value = request.GET("value")

    if filter_type and value:
        annonces = Annonce.objects.filter(**{filter_type: value})
        expenses = [a.condominium_expenses for a in annonces if a.condominium_expenses is not None]

        if expenses:
            result = {
                "average": round(np.mean(expenses), 2),
                "q10": round(np.percentile(expenses, 10), 2),
                "q90": round(np.percentile(expenses, 90), 2)
            }

    return render(request, "dashboard.html", {"result": result})