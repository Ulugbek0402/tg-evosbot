import logging

from core.database_settings import execute_query


def register(data: dict):
    try:
        query = """
                INSERT INTO users
                    (full_name, phone_number, longitude, latitude, language, chat_id)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
        params = (
            data.get('full_name'), data.get('phone_number'),
            data.get('longitude'), data.get('latitude'),
            data.get('language'), data.get('chat_id')
        )

        execute_query(query=query, params=params)
        return True
    except Exception as exc:
        logging.error(exc)
        return None


def get_user(chat_id: int):
    try:
        query = """SELECT *
                   FROM users
                   WHERE chat_id = %s"""
        params = (chat_id,)

        return execute_query(query=query, params=params, fetch="one")
    except Exception as exc:
        logging.error(exc)
        return None
