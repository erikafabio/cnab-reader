from django.shortcuts import render
from .form import UploadFileForm
from .models import FileModel
from django.http import HttpResponse

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = dict(request.FILES)['file'][0] 

        if form.is_valid():
            transations = []
            line = file.readline()
            decoded_line = line.decode("utf8")

            while line:
                type_of_transition = decoded_line[0:1]
                date = decoded_line[2:10]
                value = decoded_line[10:20]
                cpf = decoded_line[20:31]
                card = decoded_line[31:43]
                hour = decoded_line[42:48]
                market_owner = decoded_line[48:62]
                market_name = decoded_line[62:80]
                transations.append({
                    'type_of_transition' : type_of_transition,
                    'date' : date,
                    'value' : value,
                    'cpf' : cpf,
                    'card' : card,
                    'hour' : hour,
                    'market_owner' : market_owner, 
                    'market_name' : market_name
                })
                line = file.readline()
                decoded_line = line.decode("utf8")
            
            for transation in transations:
                model_file = FileModel(
                    type_of_transition = transation['type_of_transition'],
                    date = transation['date'],
                    value = transation['value'],
                    cpf = transation['cpf'],
                    card = transation['card'],
                    hour = transation['hour'],
                    market_owner = transation['market_owner'],
                    market_name = transation['market_name']
                )
                model_file.save()
            
            return HttpResponse("File uploaded:" + str(file))
    else:
        form = UploadFileForm()
        return render(request, 'reader/index.html', {'form': form})

def transations_table(request):
    transations = []
    file = FileModel.objects.all()

    for transation in file:
        if transation.type_of_transition == "1":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "debito", 'flow': "Saída", 'sign': "-", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name })
        elif transation.type_of_transition == "2":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "boleto", 'flow': "Saída", 'sign': "-", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})
        elif transation.type_of_transition == "3":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "financiamento", 'flow': "Saída", 'sign': "-", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})    
        elif transation.type_of_transition == "4":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "credito", 'flow': "Entrada", 'sign': "+", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})
        elif transation.type_of_transition == "5":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "recebimento emprestimo", 'flow': "Entrada", 'sign': "+", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})
        elif transation.type_of_transition == "6":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "vendas", 'flow': "Entrada", 'sign': "+", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})
        elif transation.type_of_transition == "7":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "recebimento TED", 'flow': "Entrada", 'sign': "+", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})  
        elif transation.type_of_transition == "8":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "recebimento DOC", 'flow': "Entrada", 'sign': "+", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name})    
        elif transation.type_of_transition == "9":
            transations.append({'type_of_transition': transation.type_of_transition, 'description': "aluguel", 'flow': "Saída", 'sign': "-", 'value' : transation.value, 'date' : transation.date, 'cpf' : transation.cpf, 'card' : transation.card, 'hour' : transation.hour, 'market_owner' : transation.market_owner, 'market_name' : transation.market_name}) 
                         
    return render(request, 'reader/transations_table.html', {'transations': transations})


