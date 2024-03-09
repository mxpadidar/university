from fastapi import Depends, Request

from backbone.service_layer.dtos import UserDto


def get_token(request: Request) -> str:
    """Get token from request."""
    return "USER_ID=1; PHONE=1234567890; UNIVERSITY_ID=1"


def get_current_user_info(token: str = Depends(get_token)) -> UserDto:
    """Decode token and get user from database.
    Returns a user dto."""
    user_data = token.split(";")
    user_id = int(user_data[0].split("=")[1])
    phone = user_data[1].split("=")[1]
    university_id = int(user_data[2].split("=")[1])
    return UserDto(id=user_id, phone=phone, university_id=university_id)
