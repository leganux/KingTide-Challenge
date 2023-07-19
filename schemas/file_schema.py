def file_serializer(file) -> dict:
    return {
        'id': str(file["_id"]),
        'file': file["file"],
        'user_id': str(file["user_id"]),
        'created_at': file["created_at"],
        'updated_at': file["updated_at"],
    }


def files_serializer(files) -> list:
    return [file_serializer(file) for file in files]
