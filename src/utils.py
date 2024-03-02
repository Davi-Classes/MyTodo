def get_new_id(array: list[dict]) -> int:
    maior_id = None
    for item in array:
        if maior_id is None or item.get("id") > maior_id:
            maior_id = item.get("id")

    return maior_id + 1
