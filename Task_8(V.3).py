import datetime


def log(func):
    def wrapper(distance):
        print(f"Function {func.__name__} started at {datetime.datetime.now()}")
        print(f"Input distance: {distance}")
        result = func(distance)
        print(f"Output result: {result}")
        return result
    return wrapper


@log
def total_taxi_fare(distance):
    base = 4.0
    total_fare = base + (distance * 1000 / 140) * 0.25  # Рассчитываем итоговою стоимость
    return round(total_fare, 2)


distance = 9.6 #Километров
total_taxi_fare(distance)

