import data_download as dd
import data_plotting as dplt


def main():
    # Запрос параметров от пользователя
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")

    threshold = float(input("Введите порог колебаний в процентах (например, 5): ").strip())

    print("\nУкажите временной период:")
    print("1. Предустановленный период (например, '1mo', '3mo', '1y').")
    print("2. Задать конкретные даты начала и окончания.")

    choice = input("Выберите 1 или 2: ").strip()
    start_date, end_date, period = None, None, None

    if choice == '2':
        start_date = input("Введите дату начала анализа (в формате 'YYYY-MM-DD'): ").strip()
        end_date = input("Введите дату окончания анализа (в формате 'YYYY-MM-DD'): ").strip()
    else:
        period = input("Введите предустановленный период (например, '1mo', '3mo', '1y'): ").strip()

        # Выбор стиля графика
        print("\nДоступные стили графика: ['default', 'ggplot', 'seaborn', 'fivethirtyeight', 'bmh', 'grayscale']")
        style = input("Введите стиль графика (по умолчанию 'default'): ").strip() or 'default'

    # Загрузка данных
    try:
        stock_data = dd.fetch_stock_data(ticker, start_date=start_date, end_date=end_date, period=period)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Расчёт индикаторов
    stock_data = dd.calculate_rsi(stock_data)
    stock_data = dd.calculate_macd(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Визуализация с индикаторами
    dplt.plot_with_indicators(stock_data, ticker, period or f"{start_date}_to_{end_date}", style)

    # Вывод средней цены за период
    dd.calculate_and_display_average_price(stock_data)

    # Уведомление о сильных колебаниях
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Сохранение данных в CSV
    filename = f"{ticker}_{period}_stock_data.csv"
    dd.export_data_to_csv(stock_data, filename)

if __name__ == "__main__":
    main()
