def calculate_call_cost ( call_cost, operator_from, operator_to):
    tariff_rates = {
        "МТС": 1.5,
        "Билайн": 1.2,
        "Мегафон": 1.8,
        "Теле2": 1.0
    }
    if operator_from not in tariff_rates:
        print("Ошибка! Неправильно указан оператор звонящего.")
        return None
    if operator_to not in tariff_rates:
        print("Ошибка! Неправильно указан оператор принимающего звонок.")
    return None