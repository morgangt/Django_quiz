Django Quiz
===========

Задача 1
--------

Заказчик хочет вести базу данных транспортных средств и их категорий. Он хочет вводить модель ТС и то, какой категории это ТС принадлежит. Набор категорий задан строго:

 > A “Мотоцикл”
 > B “Легковая”
 > С “Грузовая”
 > D “Автобус”

Например, пользователь вводит Audi A4 и выбирает категорию B, вводит Kawasaki Z1000 и выбирает А. После ввода он может посмотреть список всех ТС с категориями в виде таблицы:

Дата внесения   Модель    Категория
22.08.2016      Audi A4   B “Легковая”
23.08.2016      Kawasaki Z1000   A “Мотоцикл”

* Дата внесения не редактируется, а проставляется автоматически.

Составьте Django модель соответствующую задаче, а также напишите отрывок HTML шаблона, выводящего эту таблицу. Модель должна быть printable. В БД колонка категории должна хранить только одну букву.

# Описание
### LINK localhost/task-one/

Задача 2
--------

На АЭС действует строгая система безопасности. Все сотрудники должны ежедневно выполнять некоторый набор процедур. Таких как: “одеть антирад. костюм”, “снять антирад. костюм”, “проверить уровень облучения” и т.д. Администратор может добавлять новые процедуры и удалять ненужные. Каждая процедура может быть выполнена только один раз в день каждым сотрудником. Сотрудники сами являются пользователями системы и при выполнении каждой процедуры вносят это в систему. Система сохраняет дату и время выполнения процедуры.

 > Составьте Django модель соответствующую задаче.
 > Как вывести на экран последнюю выполненную процедуру определенным сотрудником?
 > Получить количество выполнений каждой процедуры за все время.
 > Вывести на экран (print) все выполнения процедур отсортированные в обратном хронологическом порядке.
 > Количество выполнений процедур за последние 2 дня.
 > Суммарное кол-во выполнений процедур procedure1 и procedure2.
 > Суммарное кол-во выполнений всех процедур за любой день за исключением определенного.
 > Напишите админку для этих моделей.
 > Напишите view с формой для выполнения процедуры текущим пользователем.

# Описание:
Для исользования необходимо быть авторизованным (в скором времени добавлю форму авторизации и регистрации).

### LINK:
 >  localhost/task-two/

### USERS:
 > login/password - admin/adminadmin (пользователь имеет рание записи)
 > login/password - user/useruser  (пользователь не имеет записей)
