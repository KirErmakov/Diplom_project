<h1> Проект Web/Mobile тестирования онлайн-кинотеатра Okko + API reqres.in  </h1>

> <a target="_blank" href="https://okko.tv/">Okko</a>
<a target="_blank" href="https://reqres.in/">Reqres</a>

![This is an image](images/okko_tv.jpg)
<!-- Технологии -->

### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/requests.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
   <code><img width="5%" title="Appium" src="images/appium.png"></code>
   <code><img width="5%" title="Browserstack" src="images/browserstack.png"></code>
   <code><img width="5%" title="PyCharm" src="images/pycharm.png"></code>
  <code><img width="5%" title="Android Studio" src="images/android_studio.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>


<!-- Тест кейсы -->
UI:
* ✅ Проверка доступности вариантов регистрации
* ✅ Регистрация пользователя с корректным email
* ✅ Регистрация пользователя с некорректным email
* ✅ Переход в выбранный раздел сайта
* ✅ Поиск фильма по названию
* ✅ Выбор фильмов по определенной категории
* ✅ Выбор фильмв по определенному жанру

Mobile:
* ✅ Регистрация пользователя через email
* ✅ Поиск фильма по названию
* ✅ Покупка фильма

 API:
* ✅ Cоздание пользователя
* ✅ Логин пользователя
* ✅ Получение ифнормации о пользователе
* ✅ Обновление ифнормации о пользователе
* ✅ Удаление пользователя


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Запуск проекта в Jenkins

### [Задача в jenkins](https://jenkins.autotests.cloud/job/Okko-reqres-project/)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

##### Результаты выполнения тестова можно посмотреть в Allure-отчете
![This is an image](images/allure_dashboard.jpg)
![This is an image](images/allure-api.jpg)

##### Видео прохождение теста на мобильном устройстве
![This is an image](images/mobile_test.gif)



<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/4221/dashboards)

![This is an image](images/allure_testops_dash.jpg)




<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Интеграция с Jira

![This is an image](images/jira_okko.jpg)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Оповещения в Telegram
##### После выполнения тестов, в Telegram bot приходит сообщение с графиком и информацией о тестовом прогоне.

![This is an image](images/bot_mobile_result.png)
![This is an image](images/bot_api_result.png)
