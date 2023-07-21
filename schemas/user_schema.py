import json


def user_serializer(user) -> dict:
    return {
        'id': str(user["_id"]),
        'name': user["name"],
        'cv': user["cv"],
        'lastName': user["lastName"],
        'surName': user["surName"],
        'rfc': user["rfc"],
        'birthday': user["birthday"],
        'profilePicture': user["profilePicture"],
        'created_at': user["created_at"],
        'updated_at': user["updated_at"],
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
