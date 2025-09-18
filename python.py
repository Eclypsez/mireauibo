def list_example():
    
    # 1. Создание и инициализация списка
    my_list = [5, 2, 8, 1, 3, 'hello']  # Может содержать разные типы
    print(f"Исходный список: {my_list}")

    # 2. Добавление элементов
    my_list.append(10)          # Добавление в конец
    my_list.insert(2, 77)       # Вставка 77 по индексу 2
    print(f"После добавления: {my_list}")

    # 3. Доступ к элементам
    print(f"Первый элемент: {my_list[0]}")
    print(f"Последний элемент: {my_list[-1]}")  # Отрицательная индексация
    print(f"Срез [1:4]: {my_list[1:4]}")        # Срезы (slicing)

    # 4. Удаление элементов
    removed = my_list.pop()      # Удаляет и возвращает последний элемент
    print(f"Удален последний: {removed}")
    
    removed = my_list.pop(3)     # Удаляет по индексу
    print(f"Удален элемент с индексом 3: {removed}")
    
    my_list.remove(8)           # Удаляет первое вхождение значения 8
    print(f"После удалений: {my_list}")

    # 5. Размер списка и проверка на пустоту
    print(f"Длина списка: {len(my_list)}")
    print(f"Пустой ли список? {len(my_list) == 0}")  # или not my_list

    # 6. Итерация по списку
    print("Элементы списка:")
    for i, item in enumerate(my_list):  # enumerate возвращает (индекс, значение)
        print(f"  Индекс {i}: {item}")

    # 7. Сортировка (работает только для comparable типов)
    try:
        # Создадим список только из чисел для сортировки
        num_list = [5, 2, 8, 1, 3]
        num_list.sort()                    # Сортировка на месте
        print(f"Отсортированный список: {num_list}")
        
        num_list.sort(reverse=True)        # Обратная сортировка
        print(f"Обратная сортировка: {num_list}")
    except TypeError as e:
        print(f"Ошибка сортировки: {e}")

    # 8. Поиск
    if 5 in my_list:
        print("Число 5 найдено в списке")
    print(f"Индекс элемента 'hello': {my_list.index('hello')}")

# Запуск примера со списками
list_example()

def stack_example():
    print("\n=== РЕАЛИЗАЦИЯ СТЕКА ЧЕРЕЗ LIST ===")
    
    # Создание стека
    stack = []

    # 1. Проверка на пустоту
    print(f"Стек пустой? {len(stack) == 0}")  # или not stack

    # 2. Добавление элементов в стек (push)
    print("Добавляем элементы...")
    stack.append("First")
    stack.append("Second") 
    stack.append("Third")
    # Стек сейчас: ['First', 'Second', 'Third'] где 'Third' - вершина
    
    print(f"Стек после добавления: {stack}")

    # 3. Размер стека
    print(f"Размер стека: {len(stack)}")

    # 4. Просмотр верхнего элемента без удаления (peek)
    if stack:
        top_element = stack[-1]  # Индекс -1 означает последний элемент
        print(f"Верхний элемент: {top_element}")

    # 5. Извлечение верхнего элемента с удалением (pop)
    if stack:
        popped = stack.pop()
        print(f"Извлеченный элемент: {popped}")
        print(f"Стек после извлечения: {stack}")

    # 6. Демонстрация принципа LIFO
    print("Извлекаем все элементы (порядок LIFO):")
    while stack:
        element = stack.pop()
        print(f"  Извлечено: {element}")
    
    print(f"Стек пустой? {len(stack) == 0}")

# Запуск примера со стеком
stack_example()

# Дополнительно: можно использовать collections.deque для более эффективной реализации
from collections import deque

def deque_stack_example():
    print("\n=== РЕАЛИЗАЦИЯ СТЕКА ЧЕРЕЗ DEQUE (более эффективно) ===")
    
    stack = deque()

    # Операции аналогичны списку
    stack.append("First")
    stack.append("Second")
    stack.append("Third")
    
    print(f"Стек: {stack}")
    print(f"Верхний элемент: {stack[-1]}")
    print(f"Извлеченный: {stack.pop()}")
    print(f"Осталось: {stack}")

# Запуск примера с deque
deque_stack_example()
