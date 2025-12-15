def email_prompt(summary: dict) -> str:
    return f"""
Створи короткий email-звіт для менеджера.


Показники:
- Кількість записів: {summary['total_rows']}
- Середні продажі: {summary['avg_sales']:.2f}
- Максимальні продажі: {summary['max_sales']}
- Мінімальні продажі: {summary['min_sales']}


Тон: професійний, діловий, стислий.
"""