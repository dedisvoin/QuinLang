<p align="center">
  <img src="https://github.com/dedisvoin/QuinLang/blob/add-basik-number-parser/logo.png" />
</p>

# QuinLang
Простой, быстрый интерпретируемый язык, полностью написанный на python.

# Базовые конструкции

## Присваивание переменной какого либо выражения.
~~~py
       тип   значение
        |       | 
  let (int) a = 10
            |
           имя
~~~

создание константных переменных происхожит при помощи ключевого слова (const)
~~~py
    
  const (str) a = 'Hello World'
      
~~~

Возможно присваивание значений сразу нескольким переменным одного типа доступа. Вот пример.
~~~py
   
  let (str, int, list) a, b, c =
    'hello!', 10-20*5, [1,2,3,['ded',true]]
       
~~~

## Конструкции if, else, (else if).
## простейшая конструкция if-else.
~~~py
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
~~~py

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

