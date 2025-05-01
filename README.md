# Uplift prediction
1. Data and Methodology
  * Data: Artificially generated purchase data and information from a previous campaign with offer mailings were used.
  * Customer Offer: Discount on the first purchase.
  * Profit Calculation: The calculations took into account the cost price, the cost of sending the offer, and the discount losses.
2. Technologies and Tools
  * Modeling: The Pylift library and LGBRegressor were used to build the model.
  * Data Analysis: Exploratory data analysis was conducted.
  * Transformers: Transformers were developed and proposed for use in the pipeline.
  * Data Processing: The PySpark framework was used for data analysis and transformation.
3. Model Features
  * Customer age.
  * Purchase amount.
  * Average, maximum, and minimum purchase amounts within a 100-day and 5-day window from the reference date.
  * Number of purchases.
  * Time since the last purchase.
  * Average interval between purchases.
4. Results
  * Output: A list of customers to whom it is most profitable to send a discount offer for the next purchase.
  * Evaluation: The result was assessed by the educational system and deemed successful.

Проект посвящен разработке uplift-модели для определения наиболее подходящих клиентов для рассылки предложений о покупке со скидкой с целью максимизации прибыли.

1. Данные и методология
  * Данные: Использовались искусственно созданные данные о покупках и информация о ранее проведенной кампании с рассылкой предложений.
  * Клиентское предложение: Скидка на первую покупку.
  * Учет прибыли: В расчетах учитывались себестоимость, стоимость рассылки и потери на скидку.
2. Технологии и инструменты
  * Моделирование: Для построения модели использовались библиотека Pylift и LGBRegressor.
  * Анализ данных: Проведен разведочный анализ данных.
  * Трансформеры: Разработаны и предложены трансформеры для использования в пайплайне.
  * Обработка данных: Применялся фреймворк PySpark для анализа и преобразования данных.
3. Признаки модели
  * Возраст клиента.
  * Сумма покупок.
  * Средняя, максимальная и минимальная сумма покупок в окне 100 и 5 дней от отчетной даты.
  * Количество покупок.
  * Время с последней покупки.
  * Средний интервал между покупками.
4. Результаты
  * Выходные данные: Список клиентов, которым наиболее выгодно отправить предложение со скидкой на следующую покупку.
  * Оценка: Результат был оценен учебной системой и признан успешным.
