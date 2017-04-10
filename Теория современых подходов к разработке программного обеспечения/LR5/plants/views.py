from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import PlantForm
from .models import *


def index(request):
    divisions = Division.objects.all()
    context = {'divisions': divisions}
    return render(request, 'plants/index.html', context)


def plants_in_division(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    divisions = Division.objects.all()
    plants = Plant.objects.filter(division=division_id)[:2]
    statuses = Status.objects.all()
    reservations = Reservation.objects.all()
    context = {'divisions': divisions,
               'dvs': division,
               'plants': plants,
               'statuses': statuses,
               'reservations': reservations
               }
    return render(request, 'plants/plants_in_division.html', context)


def plant_add(request, division_id):
    plant = Plant(rus_name=request.GET['rus_name'],
                  lat_name=request.GET['lat_name'],
                  info=request.GET['info'],
                  sec_measures=request.GET['sec_measures'],
                  status=Status.objects.get(name=request.GET['status']),
                  division=Division.objects.get(pk=division_id)
                  )
    plant.save()
    return redirect('plants_in_division', division_id=division_id)


def plant_edit(request, plant_id):
    divisions = Division.objects.all()
    plant = Plant.objects.get(pk=plant_id)
    statuses = Status.objects.all()
    reservations = Reservation.objects.all()
    context = {'divisions': divisions,
               'plant': plant,
               'statuses': statuses,
               'reservations': reservations
                }
    return render(request, 'plants/edit_plant.html', context)


def plant_put(request, division_id, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    plant.rus_name = request.GET['rus_name']
    plant.lat_name = request.GET['lat_name']
    plant.info = request.GET['info']
    plant.sec_measures = request.GET['sec_measures']
    plant.status = Status.objects.get(name=request.GET['status'])
    plant.save()
    return redirect('plants_in_division', division_id=division_id)


def plant_delete(request, division_id, plant_id):
    Plant.objects.get(pk=plant_id).delete()
    return redirect('plants_in_division', division_id=division_id)


def ajax_plant_delete(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    data = dict()
    if request.method == 'POST':
        division = plant.division
        plant.delete()
        divisions = Division.objects.all()
        plants = Plant.objects.filter(division=division.id)
        statuses = Status.objects.all()
        reservations = Reservation.objects.all()
        data['form_is_valid'] = True
        data['html_plants_blog'] = render_to_string('plants/partial_plants_blog.html', {
            'plants': plants,
            'dvs': division,
            'divisions': divisions,
            'reservations': reservations,
            'statuses': statuses
        })
    else:
        context = {'plant': plant}
        data['html_form'] = render_to_string('plants/partial_plant_delete.html', context, request=request)
    return JsonResponse(data)


def ajax_partial_load(request, division_id):
    num = int(request.GET['num'])
    data = dict()
    division = Division.objects.get(pk=division_id)
    plants = Plant.objects.filter(division=division.id)[num:num+2]
    statuses = Status.objects.all()
    reservations = Reservation.objects.all()
    if (plants):
        data['form_is_valid'] = True
        data['html_plants_blog'] = render_to_string('plants/partial_plants_blog.html', {
            'plants': plants,
            'dvs': division,
            'reservations': reservations,
            'statuses': statuses
        })
    else:
        data['none'] = True
    return JsonResponse(data)
