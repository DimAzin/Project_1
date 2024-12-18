import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, start_date=None, end_date=None, period='1mo'):
    """
    Загружает данные акций за указанный период или между заданными датами.

    :param ticker: Тикер акций
    :param start_date: Дата начала анализа (формат 'YYYY-MM-DD')
    :param end_date: Дата окончания анализа (формат 'YYYY-MM-DD')
    :param period: Предустановленный период (например, '1mo')
    :return: DataFrame с историческими данными
    """
    stock = yf.Ticker(ticker)

    if start_date and end_date:
        data = stock.history(start=start_date, end=end_date)
    else:
        data = stock.history(period=period)

    if data.empty:
        raise ValueError("Не удалось загрузить данные. Проверьте параметры.")

    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет скользящее среднее в DataFrame.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия за заданный период.

    :param data: DataFrame с данными акций
    """
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за период: {average_price:.2f}")
    else:
        print("Колонка 'Close' отсутствует в данных.")


def notify_if_strong_fluctuations(data, threshold):
    """
    Уведомляет пользователя, если цена акций колебалась более чем на threshold% за период.

    :param data: DataFrame с данными акций
    :param threshold: Порог колебаний в процентах
    """
    if 'Close' in data.columns:
        max_price = data['Close'].max()
        min_price = data['Close'].min()

        # Вычисление разницы в процентах
        fluctuation = ((max_price - min_price) / min_price) * 100

        if fluctuation > threshold:
            print(f"⚠️ Внимание! Цена акций колебалась более чем на {threshold}% за период.")
            print(f"Максимальная цена: {max_price:.2f}, Минимальная цена: {min_price:.2f}")
            print(f"Колебания составили: {fluctuation:.2f}%")
        else:
            print(f"Цена акций колебалась менее чем на {threshold}%.")
    else:
        print("Колонка 'Close' отсутствует в данных.")


def export_data_to_csv(data, filename):
    """
    Экспортирует данные о ценах акций в CSV файл.

    :param data: DataFrame с данными акций
    :param filename: Имя файла, в который нужно сохранить данные (с расширением .csv)
    """
    if isinstance(data, pd.DataFrame):
        try:
            data.to_csv(filename, index=True)  # Сохранение данных с индексами
            print(f"Данные успешно сохранены в файл: {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")
    else:
        print("Ошибка: данные должны быть в формате DataFrame.")


def calculate_rsi(data, window=14):
    """
    Вычисляет индикатор RSI (Relative Strength Index).

    :param data: DataFrame с колонкой 'Close'
    :param window: Период для расчёта RSI
    :return: DataFrame с добавленной колонкой 'RSI'
    """
    if 'Close' not in data.columns:
        raise ValueError("Колонка 'Close' отсутствует в данных.")

    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Вычисляет индикатор MACD (Moving Average Convergence Divergence).

    :param data: DataFrame с колонкой 'Close'
    :param short_window: Короткий период EMA
    :param long_window: Длинный период EMA
    :param signal_window: Период для сигнальной линии
    :return: DataFrame с добавленными колонками 'MACD' и 'Signal_Line'
    """
    if 'Close' not in data.columns:
        raise ValueError("Колонка 'Close' отсутствует в данных.")

    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data


def calculate_statistics(data):
    """
    Рассчитывает статистические индикаторы для данных акций.

    :param data: DataFrame с колонкой 'Close'
    :return: Словарь со статистическими показателями
    """
    statistics = {
        "mean_close": data['Close'].mean(),
        "std_dev_close": data['Close'].std(),
        "min_close": data['Close'].min(),
        "max_close": data['Close'].max(),
        "median_close": data['Close'].median(),
    }
    return statistics


def display_statistics(statistics):
    """
    Выводит статистические показатели в консоль.

    :param statistics: Словарь со статистическими показателями
    """
    print("\nСтатистический анализ данных:")
    print(f"Средняя цена закрытия: {statistics['mean_close']:.2f}")
    print(f"Стандартное отклонение цены закрытия: {statistics['std_dev_close']:.2f}")
    print(f"Минимальная цена закрытия: {statistics['min_close']:.2f}")
    print(f"Максимальная цена закрытия: {statistics['max_close']:.2f}")
    print(f"Медианная цена закрытия: {statistics['median_close']:.2f}")