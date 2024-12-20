Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.

Структура и модули проекта

1. data_download.py:

- Отвечает за загрузку данных об акциях.

- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.


2. main.py:

- Является точкой входа в программу.

- Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в виде графика.


3. data_plotting.py:

- Отвечает за визуализацию данных.

- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.


Описание функций


1. data_download.py:

- fetch_stock_data(ticker, start_date=start_date, end_date=end_date, period=period): Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.

- add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

- calculate_and_display_average_price(data): Вычисляет и выводит в консоль среднюю цену закрытия акций за заданный период.

- notify_if_strong_fluctuations(data, threshold): Находит максимальную и минимальную цену закрытия (max_price и min_price).
    Вычисляет разницу между ними в процентах.
    Сравнивает разницу с заданным порогом (threshold).
    Уведомляет пользователя, если колебания превышают порог.

- calculate_rsi(data, window=14): Вычисляет индикатор RSI (Relative Strength Index) и добавляет в DataFrame колонку с данными RSI.

- calculate_macd(data, short_window=12, long_window=26, signal_window=9): Вычисляет индикатор MACD (Moving Average Convergence Divergence) и добавляет в DataFrame колонку с данными MACD.

- calculate_statistics(data): Рассчитывает статистические индикаторы для данных акций.

- display_statistics(statistics): Выводит статистические показатели в консоль.

- export_data_to_csv(data, filename): Позволяет сохранять загруженные данные об акциях в CSV файл.
 
2. main.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию.


3. data_plotting.py:

- create_and_save_plot(data, ticker, period, filename): Создаёт график, отображающий цены закрытия и скользящие средние. Предоставляет возможность сохранения графика в файл. Параметр filename опционален; если он не указан, имя файла генерируется автоматически.

- plot_with_indicators(data, ticker, period, style='default'): Визуализирует данные с индикаторами RSI и MACD с заданным стилем графика.

- plot_with_statistics(data, ticker, period, statistics, style='default'): Визуализирует данные с дополнительными статистическими индикаторами.

- create_interactive_plot(data, ticker, period, statistics): Создаёт интерактивный график с Plotly.

Пошаговое использование

1. Запустите main.py.

2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).

3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц или диапазон дат).

4. Введите порог колебаний в процентах (например, 5).

5. Введите стиль графика.

6. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее, RSI, MACD, отобразит графики, выгрузит данные в CSV файл.


В дальнейшем планируется расширение аналитических возможностей проекта, предоставляя глубокие и настраиваемые инструменты для анализа данных об акциях.
