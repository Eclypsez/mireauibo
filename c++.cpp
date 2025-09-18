#include <iostream>
#include <list>     
#include <algorithm> 
#include <stack>

using namespace std;

int main() {
    // 1. Создание и инициализация списка
    list<int> myList = {5, 2, 8, 1, 3}; // Создали список с элементами

    // 2. Добавление элементов
    myList.push_back(10);   // Добавление в конец: {5, 2, 8, 1, 3, 10}
    myList.push_front(0);   // Добавление в начало: {0, 5, 2, 8, 1, 3, 10}

    // 3. Вставка элемента в середину 
    // Найдем итератор на элемент со значением 8
    auto it = find(myList.begin(), myList.end(), 8);
    if (it != myList.end()) {
        myList.insert(it, 77); // Вставляем 77 перед 8
        // Список теперь: {0, 5, 2, 77, 8, 1, 3, 10}
    }

    // 4. Удаление элементов
    myList.pop_front();     // Удаляем первый элемент (0)
    myList.pop_back();      // Удаляем последний элемент (10)
    myList.remove(2);       // Удаляем все элементы со значением 2

    // 5. Размер списка и проверка на пустоту
    cout << "Size of list: " << myList.size() << endl;
    cout << "Is list empty? " << (myList.empty() ? "Yes" : "No") << endl;

    // 6. Доступ к элементам (только к первому и последнему напрямую)
    cout << "First element: " << myList.front() << endl;
    cout << "Last element: " << myList.back() << endl;

    // 7. Итерация по списку (так как нет оператора [])
    cout << "List elements: ";
    for (int num : myList) { // Range-based for loop (C++11)
        cout << num << " ";
    }
    cout << endl;

    // Или с помощью итератора
    cout << "List elements (using iterator): ";
    for (auto it = myList.begin(); it != myList.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // 8. Сортировка списка (у списка есть собственная эффективная функция sort)
    myList.sort();
    cout << "Sorted list: ";
    for (int num : myList) {
        cout << num << " ";
    }
    cout << endl;

     // 1. Создание стека
    // tack<int> myStack; // По умолчанию на основе deque
    stack<int, list<int>> myStack; // Явно указываем использовать list

    // 2. Проверка на пустоту
    cout << "Is stack empty? " << (myStack.empty() ? "Yes" : "No") << endl;

    // 3. Добавление элементов в стек (push)
    cout << "Pushing elements..." << endl;
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    myStack.push(40);
    // Стек сейчас: [40] (верх) -> [30] -> [20] -> [10] (низ)

    // 4. Размер стека
    cout << "Stack size: " << myStack.size() << endl;

    // 5. Доступ к верхнему элементу (без его удаления)
    cout << "Top element: " << myStack.top() << endl; // Выведет 40

    // 6. Удаление верхнего элемента (pop)
    cout << "Popping the top element..." << endl;
    myStack.pop(); // Удаляем 40
    cout << "New top element after pop: " << myStack.top() << endl; // Выведет 30

    // 7. Демонстрация принципа LIFO
    cout << "Popping all elements (LIFO order): ";
    while (!myStack.empty()) {
        cout << myStack.top() << " "; // Смотрим на верхний элемент
        myStack.pop();                     // Удаляем его
    } // Выведет: 30 20 10
    cout << endl;

    cout << "Is stack empty now? " << (myStack.empty() ? "Yes" : "No") << endl;

    return 0;
    
}
