# Django REST API
Этот проект представляет собой простой REST API, созданный с использованием Django, для управления категориями и объявлениями (ads).
Откройте браузер и перейдите по URL-адресу http://localhost:8000/ для проверки, работает ли API. Вы должны увидеть {"status": "ok"}.
GET /categories/ - Получить список всех категорий.
POST /categories/ - Создать новую категорию. Отправьте JSON-объект с ключом "name" для создания категории.


2) Базу данных в формате CSV переделали в Json

3)Реализовали для /cat метод GET и POST.
Реализовали для /ad метод GET POST.

4)Реализовали для /cat/:id метод GET.
Реализовали для /ad/:id метод GET.
