# Создание и тестирование приложения для работы с API 
---

Перейдя на сайт Flasgger, я стала изучать API для сайта PetFriends. Указанные ниже функции я реализовала на Python 3.8 (они находятся в папке API) и все функции указанные в ТЗ, используя библиотеку request.

Код каждой функции вы можете увидеть в директории **API**.

Результаты функций:

GET API key (Получение ключа API):

![image](https://user-images.githubusercontent.com/83708760/147490218-73dec3c2-d4e5-4eb9-bacc-94db62ba36c9.png)

POST new pet:
![image](https://user-images.githubusercontent.com/83708760/147490445-1c18ebe9-a714-43fa-92e6-ae5fa44523f2.png)

GET pet list (Получение списка My_Pets):

![image](https://user-images.githubusercontent.com/83708760/147490524-d8e9182c-7d1c-4753-b373-fb04a504799e.png)

POST create pet simple:

![image](https://user-images.githubusercontent.com/83708760/147490605-58c0060d-9d74-4e26-b947-ce7a6df7aca5.png)

PUT info:

![image](https://user-images.githubusercontent.com/83708760/147490649-c2089ad0-c27c-474f-9046-d5c1b192deec.png)

DELETE pet:

![image](https://user-images.githubusercontent.com/83708760/147490703-8015174d-3a6c-42f6-b199-c8f377687eec.png)

Фикстуры я буду использовать для всех функций, а параметризация подойдет для функции "POST".

Параметризация для функции POST: 

![image](https://user-images.githubusercontent.com/83708760/147490871-0811b6a6-b63a-48a4-82b4-e7570c1f3d22.png)
![image](https://user-images.githubusercontent.com/83708760/147490898-c26c7967-98e0-477b-884a-e03908f90f79.png)

Oтрицательные кейсы - marks=pytest.mark.xfail

![image](https://user-images.githubusercontent.com/83708760/147491015-2643b09e-9b5b-45cf-8bcb-d6483013b288.png)

Фикстура для удаления питомца: 

![image](https://user-images.githubusercontent.com/83708760/147491104-f6e5b7dd-21a7-49d6-9415-138404661c7f.png)












