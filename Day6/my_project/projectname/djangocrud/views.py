from django.shortcuts import render, redirect

data_dict = {}  

def create_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data_dict[key] = value
        return redirect('/read')
    return render(request, 'create.html')

def read_view(request):
    return render(request, 'read.html', {'data_dict': data_dict})

def update_view(request):
    print(data_dict)
    if request.method == 'POST':
        key = request.POST['key']
        if key in data_dict:
            new_value = request.POST['new_value']
            data_dict[key] = new_value
            return redirect('/read')
    return render(request, 'update.html', {'data_dict': data_dict})

def delete_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data_dict:
            del data_dict[key]
            return redirect('/read')
    return render(request, 'delete.html', {'data_dict': data_dict})
