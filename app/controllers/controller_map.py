from flask import render_template, flash, redirect, url_for, request as flask_request, jsonify, Response
from flask_login import current_user
from sqlalchemy import and_
from app.models import Request
from app.utils import login_required
from app.constants import RequestStatuses, Roles
from app import db
from datetime import datetime, timedelta
import requests as outer_requests
import json


@login_required
def ShowMap():
    user = current_user        

    return render_template('map.html', user=user)

def GetCoords():
    result = {
       "type": "FeatureCollection", 
        "features": [],
    }
    requests = Request.query.filter(and_(Request.auctionEndDate>=datetime.now(), Request.status_id==RequestStatuses.auctionStarted)).all()
    for request in requests:
        r = outer_requests.get("https://geocode-maps.yandex.ru/1.x/?format=json&geocode=" + request.address)
        json_response = json.loads(r.content)
        coords = (json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']).split()
        temp = float(coords[0])
        coords[0] = float(coords[1])
        coords[1] = temp
        current_bet_amount = request.startingPrice
        if request.lowest_bet().summ < 2147483647:
            current_bet_amount = request.lowest_bet().summ
        result['features'].append({
            "type": "Feature",
            "id": request.id,
            "geometry": {
                "type": "Point",
                "coordinates": coords
            },
            "properties": {
                "balloonContentHeader": "<div class='info_h1'><h1>Кличка собаки: " + request.pets[0].pet.name + "</h1></div>",
                "balloonContentBody": " <div class='info__spans'>" +
                                            "<span>Время создания заявки: " + request.creationDate.strftime('%d.%m.%Y %H:%M') + "</span><br/>" +
                                            "<span>Время взятия заявки: " + request.walkStartDate.strftime('%d.%m.%Y %H:%M') + "</span><br/>" +
                                            "<span>Длительность прогулки: " + str(request.walkDuration) + " мин</span><br/>" +
                                            "<span>Время начала аукциона: " + request.auctionStartDate.strftime('%d.%m.%Y %H:%M') + "</span><br/>" +
                                            "<span>Время конца аукциона: " + request.auctionEndDate.strftime('%d.%m.%Y %H:%M') + "</span><br/>" +
                                            "<span>Текущая цена: " + str(current_bet_amount) + " руб.</span><br/>" +
                                            "<span>Адресс клиента: " + request.address + "</span><br/>" +
                                            "<span><a href='/pets/" + str(request.pets[0].pet_id) + "/requests/" + str(request.id) + "/-1?return_to=map' role='button' class='btn btn-primary waves-effect waves-light' name=" + str(request.id) + " id='takeBTN'>Сделать ставку</a></span>" +
                                       "</div>",
                "clusterCaption": "<h4>" + request.pets[0].pet.name + "</h4>"
            }
        })
    return jsonify(result)