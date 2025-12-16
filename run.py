from src.load_data import load_data
from src.analyze import analyze
from src.generate_text import generate_text


if __name__ == '__main__':
 df = load_data('data/sample.csv')
summary = analyze(df)
report = generate_text(summary)


with open('outputs/report.txt', 'w', encoding='utf-8') as f:
 f.write(report)


print('Звіт згенеровано → outputs/report.txt')

print("Report generation finished successfully.")
