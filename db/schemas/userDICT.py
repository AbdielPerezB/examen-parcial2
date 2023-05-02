def user_schema(user) -> dict:
    return {"id":str(user["_id"]),
            "username":user["username"],
            "email":user["email"]}
#De objeto a JSON (JSON y diccionario de python es lo mismo)