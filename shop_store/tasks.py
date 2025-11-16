from celery import shared_task
import time

@shared_task
def log_new_product(new_prod: str):
    """Лог создания нового товара в консоль"""
    return f"Добавлен новый товар {new_prod}"

@shared_task
def add(x,y):
    """Для проверки постановки задачи"""
    time.sleep(2)
    return x+y