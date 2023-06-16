import time


def calculate_taxi_payment(distance):
    meters = distance * 1000
    base_fee = 4.00
    additional_fee = (meters // 140) * 0.25
    total_fee = base_fee + additional_fee
    return total_fee


def log_execution_time(func):
    def wrapper(distance):
        print(f"Function '{func.__name__}' was called at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Input parameters: {distance} km")
        result = func(distance)
        print(f"Result: {result} USD")
        return result
    return wrapper


@log_execution_time
def calculate_taxi_payment_with_log(distance):
    meters = distance * 1000
    base_fee = 4.00
    additional_fee = (meters // 140) * 0.25
    total_fee = base_fee + additional_fee
    return total_fee


if __name__ == "__main__":
    distance = 10
    print(f"The taxi payment for {distance} km is {calculate_taxi_payment(distance)} USD")
    print()
    calculate_taxi_payment_with_log(distance)

