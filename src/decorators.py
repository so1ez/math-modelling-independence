from time import time


def repeat(n: int):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f"Start repeating {n} times...")
            for _ in range(n):
                func(*args, **kwargs)
            print("Stop repeating")
            
        return wrapper
    return outer

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        print(f"Функция выполнялась {time() - t1} секунд")
    
    return wrapper
