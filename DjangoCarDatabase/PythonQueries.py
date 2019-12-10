from .models import Part, Customer, Car, fitsCar, purchasedBy, carMake
from loremipsum import get_sentences
import json
import random
import datetime


def gen_cars_makes():
    with open('make-models.json','r') as f:
        json_data = json.loads(f.read())

    for make, models in json_data.items():
        m = carMake(manufacturer=make)
        m.save()
        for model_name in models:
            for year in range(2015,2019):
                 c = Car(model=model_name, year=year,manufacturer=m)
                 c.save()


def gen_parts(num=0):
    partList = []

    with open('parts.txt', 'r') as f:
        for line in f:
            strip = line.rstrip('\n')
            partList.append(strip)

    rand_sentences = get_sentences(len(partList))

    for i in range(num):
        part_name = partList[random.randint(1,len(partList)-1)]
        part_num = random.randint(1,10000)
        rand_desc = rand_sentences[random.randint(1,len(rand_sentences)- 1)]
        p = Part(number=part_num, name=part_name, description=rand_desc)
        p.save()


def gen_fits_car():
    parts = Part.objects.all()
    cars = Car.objects.all()

    for i in parts:
        num_parts = random.randint(1,6)
        rand_car = cars[random.randint(0,cars.count()-1)]
        for j in range(num_parts):
            fc = fitsCar(part=i, car=rand_car)
            fc.save()


def gen_customers(t_customers,num_purchases):
    with open('users.json','r') as f:
        json_data = json.loads(f.read())

    for i in json_data:
        fn = i['first_name']
        c = Customer(first_name=fn)
        c.save()

    cust = Customer.objects.all()
    parts = Part.objects.all()

    for customer in range(t_customers):
        for i in range(num_purchases):
            time = datetime.datetime.now()
            random_part = random.randint = (0,parts.count()-1)
            cp = purchasedBy(customer=cust[customer], part=parts[i])
            cp.save()


def gen_queries():
    car_fit = fitsCar.objects.all()
    pb = purchasedBy.objects.all()

    '''
    Query 1
    '''
    for i in car_fit:
        if i.part == 6414: #battery plate
            print("Cars he use carburetor parts:",i.car)
    '''
    Query 2
    '''
    for i in car_fit:
        if i.car.model == "STS":
            print("Parts the YARIS:",i.parts)

    '''
    Query 3
    '''
    for j in pb:
        print j.customer, j.part, j.date
