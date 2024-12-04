import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    Загружает данные о ценах акций за заданный период.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
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