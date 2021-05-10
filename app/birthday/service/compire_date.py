from ..models import BirthdayData
from datetime import date
from loguru import logger


def today_birthday(user_dates, some_list):

    for birthday_date in user_dates:
        tmp_list = list()
        if birthday_date.birthday.day == date.today().day and birthday_date.birthday.month == date.today().month:
            tmp_list.append(birthday_date.name)
            tmp_list.append(date.today().year - birthday_date.birthday.year)
            some_list.append(tmp_list)
            logger.debug(f"Today is B-Day for: {birthday_date.name}")
    return some_list


def run_compare(current_user):
    users_bdays = BirthdayData.objects.filter(user=current_user)
    list_of_list = list()
    result = today_birthday(users_bdays, list_of_list)
    return result


if __name__ == '__main__':
    run_compare(x)
