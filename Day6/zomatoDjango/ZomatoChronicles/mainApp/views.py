from django.shortcuts import render, redirect
from django.http import JsonResponse

menu_items = [
    {
        'id': 1,
        'name': 'Burger',
        'price': 8.99,
        'availability': True,
    },
    {
        'id': 2,
        'name': 'Pizza',
        'price': 12.99,
        'availability': True,
    },
    # Add more menu items as needed
]

def home(request):
    return render(request, 'home.html', {'menu_items': menu_items})


def menu_list(request):
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)

def add_menu_item(request):
    if request.method == 'POST':
        new_item = {
            'id': len(menu_items) + 1,
            'name': request.POST['name'],
            'price': float(request.POST['price']),
            'availability': request.POST.get('availability') == 'on',
        }
        menu_items.append(new_item)
        return redirect('menu_list')
    return render(request, 'menu.html', {'menu_items': menu_items})

def update_availability(request, item_id):
    print(item_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        for item in menu_items:
            if item['id'] == item_id:
                if action == 'toggle_availability':
                    item['availability'] = not item['availability']
                    return redirect('menu_list')
        return JsonResponse({'error': 'Menu item not found'}, status=404)

def delete_dish(request, item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            for item in menu_items:
                if item['id'] == item_id:
                    menu_items.remove(item)
                    return redirect('menu_list')
        return JsonResponse({'error': 'Menu item not found'}, status=404)

cart_items_list = []

def add_to_cart(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        selected_item = next((item for item in menu_items if item['id'] == item_id), None)

        if selected_item:
            cart_items_list.append(selected_item)
    print(cart_items_list)
    return redirect('home')

def cart(request):
    return render(request, 'cart.html', {'cart_items_list': cart_items_list})
