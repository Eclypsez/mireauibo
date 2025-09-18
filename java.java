import java.util.Arrays; // Для удобных методов работы с массивами

public class ArrayExample {
    public static void main(String[] args) {

        // 1. Объявление и инициализация массива
        // Способ 1: с известными значениями
        int[] numbers = {5, 2, 8, 1, 3};
        
        // Способ 2: с указанием размера (элементы получат значения по умолчанию, для int - 0)
        String[] words = new String[3]; // Массив из 3 null-ов
        words[0] = "Hello";
        words[1] = "World";
        words[2] = "Java";

        // 2. Доступ к элементам и изменение
        System.out.println("First number: " + numbers[0]); // Чтение
        numbers[1] = 10; // Запись. Теперь массив: {5, 10, 8, 1, 3}

        // 3. Длина массива
        System.out.println("Length of 'numbers' array: " + numbers.length); // .length - свойство, не метод

        // 4. Итерация по массиву
        System.out.print("Numbers: ");
        // Цикл for
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();

        System.out.print("Words: ");
        // Цикл for-each (упрощенный)
        for (String word : words) {
            System.out.print(word + " ");
        }
        System.out.println();

        // 5. Многомерные массивы
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println("Element [1][2]: " + matrix[1][2]); // Доступ к элементу 6

        // 6. Полезные методы класса Arrays
        System.out.println("Original array: " + Arrays.toString(numbers));

        Arrays.sort(numbers); // Сортировка массива (изменяет исходный)
        System.out.println("Sorted array: " + Arrays.toString(numbers));

        int[] numbersCopy = Arrays.copyOf(numbers, numbers.length); // Копирование массива
        System.out.println("Copied array: " + Arrays.toString(numbersCopy));

        // 7. Попытка выйти за границы массива
        try {
            System.out.println(numbers[100]); // Вызовет исключение
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: " + e.getMessage()); // Безопасная обработка
        }

        // Создание стека
        Stack<Integer> oldStack = new Stack<>();

        // Добавление элементов
        oldStack.push(10);
        oldStack.push(20);

        // Методы аналогичны, но класс считается устаревшим.
        System.out.println("Top: " + oldStack.peek());
        System.out.println("Popped: " + oldStack.pop());
    }
}

