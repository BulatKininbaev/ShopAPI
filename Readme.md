1. Домашнее задание знакомство с Django.
2. Создание проекта
3. Запуск проекта
4. Создание модели (таблиц)
5. Заполнение таблиц с помощью комманд


ВТОРАЯ часть задания 
1. Основная часть приложения
    запуск url  = 'http://127.0.0.1:8000/index'
2. Админка url = 'http://127.0.0.1:8000/admin' 
3. Команда заполнения данных из простора сети gen_inital.py

Третья часть задания
1. Перевод всех view на CBV CRUD
2. Тесты для pytest django - проверил model , forms , view


Четвертая часть.
1.  docker run --name redis -p 6379:6379 -d redis  
2.  для celery из doker windows нужно app.conf.worker_pool = 'gevent'
3.  Запуск  celery -A config worker --loglevel=info -P solo
4. 

[//]: # (список Shell комманд для заполнения справочников. )


[//]: # (category = Category&#40;name="Электроника",description="Приборы 220 В"&#41;)

[//]: # (category.save&#40;&#41;)

[//]: # (tovar=Product&#40;name="Телевизор",description="Samsung TV 20/48",price=1078.25,category=category&#41;)

[//]: # (tovar.save&#40;&#41;)

[//]: # (tovar2=Product&#40;name="Утюг",description="Dyson 450",price=154.54,category=category&#41;             )

[//]: # (tovar.save&#40;&#41;)

[//]: # (tovar2.save&#40;&#41;)

[//]: # (category = Category.objects.create&#40;name="Бытовая техника",description="Помошник в доме"&#41;)

[//]: # (tovar=Product&#40;name="Холодильник",description="libher 160x70x45",price=2305.77,category=category&#41;)

[//]: # (tovar.save&#40;&#41;)

[//]: # (tovar=Product.objects.create&#40;name="Стиральная машина",description="Aristone 880 об.мин.",price=756.04,category=category&#41;)

[//]: # (Category.objects.all&#40;&#41;)

[//]: # (tovar=Product.objects.get&#40;name="Телевизор"&#41;)

[//]: # (tovar.price=1278.25)

[//]: # (tovar.save&#40;&#41;)