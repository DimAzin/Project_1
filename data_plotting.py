import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def plot_with_indicators(data, ticker, period, style='default'):
    """
    Визуализирует данные с индикаторами RSI и MACD с заданным стилем графика.

    :param data: DataFrame с колонками 'Close', 'RSI', 'MACD', 'Signal_Line'
    :param ticker: Тикер акций
    :param period: Период данных
    :param style: Стиль графика (например, 'ggplot', 'seaborn', 'default')
    """
    # Применение стиля
    try:
        plt.style.use(style)
    except ValueError:
        print(f"Предупреждение: Стиль '{style}' не найден. Используется стиль по умолчанию.")
        plt.style.use('default')

    plt.figure(figsize=(14, 10))

    # График цены закрытия
    plt.subplot(3, 1, 1)
    plt.plot(data['Close'], label='Цена закрытия', color='blue')
    plt.title(f'Цена закрытия {ticker} за период {period}')
    plt.legend()

    # График RSI
    plt.subplot(3, 1, 2)
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Перекупленность (70)')
    plt.axhline(30, color='green', linestyle='--', label='Перепроданность (30)')
    plt.title('Индикатор RSI')
    plt.legend()

    # График MACD
    plt.subplot(3, 1, 3)
    plt.plot(data['MACD'], label='MACD', color='magenta')
    plt.plot(data['Signal_Line'], label='Сигнальная линия', color='orange')
    plt.axhline(0, color='black', linestyle='--')
    plt.title('Индикатор MACD')
    plt.legend()

    plt.tight_layout()
    filename = f"{ticker}_{period}_indicators.png"
    plt.savefig(filename)
    print(f"График сохранен как {filename}")
    plt.show()


def plot_with_statistics(data, ticker, period, statistics, style='default'):
    """
    Визуализирует данные с дополнительными статистическими индикаторами.

    :param data: DataFrame с колонкой 'Close'
    :param ticker: Тикер акций
    :param period: Период данных
    :param statistics: Словарь со статистическими показателями
    :param style: Стиль графика (например, 'ggplot', 'seaborn', 'default')
    """
    try:
        plt.style.use(style)
    except ValueError:
        print(f"Предупреждение: Стиль '{style}' не найден. Используется стиль по умолчанию.")
        plt.style.use('default')

    plt.figure(figsize=(10, 6))

    # График цены закрытия
    plt.plot(data['Close'], label='Цена закрытия', color='blue')

    # Линии статистических индикаторов
    mean = statistics['mean_close']
    std_dev = statistics['std_dev_close']
    plt.axhline(mean, color='orange', linestyle='--', label=f'Средняя цена ({mean:.2f})')
    plt.axhline(mean + std_dev, color='red', linestyle='--', label=f'Средняя + std ({mean + std_dev:.2f})')
    plt.axhline(mean - std_dev, color='green', linestyle='--', label=f'Средняя - std ({mean - std_dev:.2f})')

    plt.title(f"Цена закрытия и статистика {ticker} за период {period}")
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.legend()
    plt.tight_layout()

    filename = f"{ticker}_{period}_statistics.png"
    plt.savefig(filename)
    print(f"График с индикаторами сохранен как {filename}")
    plt.show()