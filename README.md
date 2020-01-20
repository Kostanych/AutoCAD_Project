#AutoCad_project

  Предназначено для ускорения работы с конструкторскими чертежами. Машинное обучение позволит убрать рутинные операции. Программа должна проставлять размеры на точки крепления к приборам, с учётом всех требований. Это первая задача. С имеющейся базой можно расширить применение на другие задачи работы с dwg чертежами.

  Проект читает хорошие чертежи, обучается на существующих позициях размеров. Фичи - линии в слое с точками крепления, пересечение с линиями прибора, и т. д. Target - базовые точки размеров, положение текста размера

  "Демонстрационная" первая версия: будет один вид, нужно проставить все размеры на 1 виде.

  Работа тестируется на файле train.dwg. Нужно открыть его у автокаде, т.к. возможно читать только активный документ автокада.
  
    Начальные условия:
  -Размеры линейные, aligned dimensions.
  
    Решённые на данный момент задачи:  
  - Чтение dwg файла средствами python, через com объекты.
  - Возможность взрывать блоки.
  - Извлечение координат точек крепления приборов, формирование датафрейма с данными для каждого прибора.
  
    Необходимо реализовать:
   - Извлечение данных размеров
   - Модель машинного обучения по собранным координатам объектов
