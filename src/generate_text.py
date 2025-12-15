from src.prompts import email_prompt


def generate_text(summary: dict) -> str:
    prompt = email_prompt(summary)
# mock AI (без API)
    text = (
        f"Шановний менеджере,"
        f"За звітний період було оброблено {summary['total_rows']} записів. "
        f"Середній обсяг продажів склав {summary['avg_sales']:.2f}, "
        f"максимальне значення — {summary['max_sales']}."
f"Рекомендується звернути увагу на періоди з мінімальними показниками."
    )
    return text