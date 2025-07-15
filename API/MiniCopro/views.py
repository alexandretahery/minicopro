from django.shortcuts import render
from MiniCopro.models import Annonce
import requests
import numpy 

def MiniApi(request):
    result = None
    message = None

    if request.method == "GET":
        filter_type = request.GET.get("type")
        value = request.GET.get("value")

        if filter_type and value:
            annonces = Annonce.objects.filter(**{filter_type: value})
            expenses = []
            for annonce in annonces:
                if annonce.condominium_expenses is not None:
                    expenses.append(annonce.condominium_expenses)

            if expenses:
                result = {
                    "average": round(numpy.mean(expenses), 2),
                    "q10": round(numpy.percentile(expenses, 10), 2),
                    "q90": round(numpy.percentile(expenses, 90), 2)
                }
    elif request.method == "POST":
        url = request.POST.get("url")
        try:
            annonceId = url.split("/")[-1]
            apiUrl  = f"https://www.bienici.com/realEstateAd.json?id={annonceId}"
            response = requests.get(apiUrl)
            if response.status_code == 200:
                data = response.json()
                annonce = Annonce(
                    zip_code=data.get("postalCode"),
                    city=data.get("city"),
                    dept_code=data.get("departmentCode"),
                    condominium_expenses=data.get("annualCondominiumFees"))
                annonce.save()
                message = "Annonce ajoutée avec succès."
        except Exception as e:
            message = f"Erreur : {e}"
    
    return render(request, "dashboard.html", {"result": result, "message": message})