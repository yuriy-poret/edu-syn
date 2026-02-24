from worker import Worker


def main():

    num_workers = int(input("\nВведите количество работников: "))
    if num_workers <= 0:
        print("Ошибка: неверное количество работников.")
        return

    workers_list = []

    for i in range(num_workers):
        worker = Worker()
        worker.input_data()
        workers_list.append(worker)

    min_years_experience = int(input("\nВведите количество лет стажа: "))

    print("Следующие работники имеют стаж превышающий введённое значение:")
    has_found = False
    for worker in workers_list:
        seniority = worker.calculate_seniority()
        if seniority > min_years_experience:
            print(f"{worker.full_name}, стаж: {seniority}.")
            has_found = True

    if not has_found:
        print("Таких работников нет.")


if __name__ == "__main__":
    main()
