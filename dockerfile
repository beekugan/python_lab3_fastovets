FROM python:3.12-slim

# Користувацькі назви згідно завдання
ARG STUDENT_SURNAME=fastovets
ENV PROJECT_DIR=/${STUDENT_SURNAME}

# Створюємо робочий каталог (ім'я папки — прізвище студента)
RUN mkdir -p ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

# Копіюємо весь вміст проєкту в контейнер (з місцевої папки)
COPY . ${PROJECT_DIR}

# Встановлюємо залежності (якщо є requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt


CMD tail -f /dev/null
