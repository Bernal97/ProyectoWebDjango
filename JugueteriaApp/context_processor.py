def importe_total_carro (request):
    total = float(0)
    for key, value in request.session["products"].items():
        total = total + float(value["precio"])    
    return {"importe_total_carro":total}