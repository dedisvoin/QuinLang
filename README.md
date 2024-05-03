<p align="center">
  <img src="https://github.com/dedisvoin/QuinLang/blob/add-basik-number-parser/logo.png" />
</p>

# QuinLang
Простой, быстрый интерпретируемый язык, полностью написанный на python.

# Базовые конструкции

## Присваивание переменной какого либо выражения.
~~~js
       тип   значение
        |       | 
  let (int) a = 10
            |
           имя
~~~

создание константных переменных происхожит при помощи ключевого слова (const)
~~~js
    
  const (str) a = 'Hello World'
      
~~~

Возможно присваивание значений сразу нескольким переменным одного типа доступа. Вот пример.
~~~js
   
  let (str, int, list) a, b, c =
    'hello!', 10-20*5, [1,2,3,['ded',true]]
       
~~~

## Конструкции if, else, (else if).
## простейшая конструкция if-else.
~~~js
  ключевое слово для автаматичаского определения типа
         |
  let (auto) expr = (10-20)*2

  if (expr <= 0) {
    out(true)
  }
  else {
    out(false)
  }
~~~
метод (out) выводит в консоль все передаваемые ему через запятую значения и разделяет их пробелами, после переходит на другую строку.

## пример конструкции if-(else if).
~~~js

  let (int, str, int) n1, oper, n2 =
    int(input('input number1 -> ')),
    input('input operation -> '),
    int(input('input number1 -> ')),


  if (oper == '+') {
    out(m1+n2)
  } else if (oper == '-') {
    out(m1 - n2)
  } else if (oper == '*') {
    out(m1 * n2)
  } else if (oper == '/') {
    out(m1 / n2)
  }
  
~~~
метод (int) приводит значение в к типу (int).

метод (input) ожидает ввода данных пользователем в терминал и возвращает значение типа (str).

## Конструкции match-case.

~~~js
сравнимаемое выражение            case выражения и состояния
        |                                     |
  match 20 -> {                               |
    case 10 -> out('yes it is 10')           -|
    case 20 -> out('no it is 20')            -|
    case _ -> out('error value')             -|
  }      |
         |
  устанавливает состояние которое срабатывает, когда остальные состояния являются ложными
~~~

# Циклы
## Цикл For.
этот пример по очереди выводит элементы списка.
~~~js
  let (list) arr = [1,2,3,4,5,'true', false, 'NOOOO']

                  ограничивающее выражение
                             |
         начальное значение  |
                 |           |
  for (let (int) i = 0; i < len(arr); i = ++i){
    out(arr[i])
  }
~~~

## Цикл Forin.
этот тоже пример по очереди выводит элементы списка но не позвалает отследить индекс каждого элемента.
~~~js
  let (list) arr = [1,2,3,4,5,'true', false, 'NOOOO']

 в эту переменную попадает значение списка
                |
       список   |
          |     |
  forin (arr :-> n){
    out(n)
  }
~~~

## Цикл while.
пока проверочное выражение истинно, цикл будет повоторяться.
~~~js
  
  let (int) i = 0

   логическое выражение
             |    
  while (i < 20){
    out(i)
    i = ++i
  }
~~~
# Генераторы диапазонов.
~~~js
       выражение начального значение
                     |
  let (auto) arr = ~[0->10]
                        |
           выражение конечного значение
  out(arr)
~~~
пример выведет [0,1,2,3,4,5,6,7,8,9,10]

пример генератора диапазона с установленным шагом.
~~~js
                          шаг
                           |
  let (auto) arr = ~[0->10:2]
                        
           
  out(arr)
~~~
пример выведет [0,2,4,6,8,10]

# Создание пользовательских методов и функций.
создание метода.
~~~js
          название функции
                  |
 тип функции      |    аргумент
       |          |       |
  fn (void) print_value(value: int){
    out(value)                  |
  }                             |
                                |
                          тип аргумента

  print_value(10)
  print_value(20-40)
~~~
создание функции.
~~~js
возвращаемый тип  
       |          
  fn (str) str_repeat(value: str, count: int){
    return -> value * count       
  }                             
                                
  out(str_repeat('Hello', 4))
~~~

# Lambda выражения.
создание lambda выражений, присваивание lambda выражения какой-либо переменной, и ее последующий вызов.
~~~js
  let (call) a = lambda (a: int, b: int) -> {(a + b) / 2}

  out(
    a~(10,20) + 10
  )  |
     |
так вызываются lambda выражения
~~~

lambda выражения также поддерживают динамический вызов, тоесть вызов сразу при создании.
~~~js
  let (auto) val_a = true
  let (auto) val_b = false

  if (
      lambda (a: bool, b: bool) -> {a || b} : (val_a, val_b)
  ) {
    out('yes!')
  }
~~~

# Напиание сторонних модулей на python
базовая конструкция модуля.

~~~py
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type, test_instance

const_names = [] # имена констант и возвращаемые ими типы

function_names = [] # имена функций и возвращаемые ими типы

version = '0.0.1' # Версия вашей библиотеки.

~~~
дальше идут сам функции и константы.

~~~py
  первым в имени функции должно идти название модуля
      |
      |                типы принимаемых значений        атрибут необходимый для отслеживания ошибок в коде
      |                    |               |               | 
def math_cos(_value: Values.ValInt | Values.ValFloat, _stroke: int = 0):
    if test_type(_value, ['int', 'float'], 'cos', _stroke):             # проверка на тип вводимых значений
        return Values.ValFloat(math.cos(_value.get_value()))            # конвертация возвращаемого типа, в тип поддерживаемый языком
~~~

Функции используемые для проеврки типов
~~~py
             имя функции в которой происходит проверка
                                 |
    проверяемое значение         |
              |                  |
test_type( _value, _types, _funct_name, _stroke )
                      |                     |
              валидативные типы          атрибут необходимый для отслеживания ошибок в коде
~~~

класс ```Values``` содержит классы для конвертации базовых питоновских значений в значения моего языка.
~~~py
class Values:
    class ValInt(BasicValue):
        def __init__(self, _value: int) -> None:
            super().__init__(ValueTypes.INT, _value)
    
    class ValFloat(BasicValue):
        def __init__(self, _value: float) -> None:
            super().__init__(ValueTypes.FLOAT, _value)
    
    class ValStr(BasicValue):
        def __init__(self, _value: str) -> None:
            super().__init__(ValueTypes.STR, _value)
    
    class ValBool(BasicValue):
        def __init__(self, _value: bool) -> None:
            super().__init__(ValueTypes.BOOL, _value)

    class ValList(BasicValue):
        def __init__(self, _value: list) -> None:
            super().__init__(ValueTypes.LIST, _value)

    class ValFn(BasicValue):
        def __init__(self, _fn) -> None:
            super().__init__(ValueTypes.LIST, _fn)

    class ValNone(BasicValue):
        def __init__(self) -> None:
            super().__init__(ValueTypes.NONE)
~~~
после создания функции ее нужно добавить в список инициализируемых функций.

~~~py
                 имя функции
                      |        возвращаемый тип
function_names = [    |          |
                ['math_cos', 'float'],
                ['math_sin', 'float'],
                ['math_tan', 'float'],
                ['math_degrees', 'float']
]
~~~
создание модульных констант.
~~~py
имя аонстанты обязательно спереди с именем модуля
  |
math_pi = Values.ValFloat( math.pi )
                              |
                     значение константы
~~~                          
не забудим конвертировать значение.
после добавил информацю о константе в ```const_names```
~~~py
const_names = [
                ['math_pi', 'float']
]
~~~
