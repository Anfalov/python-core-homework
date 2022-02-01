def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    return {
        "categories": [
            {
                "id": "category-" + mapping["categories"][category_id]["id"],
                "text": mapping["categories"][category_id]["name"],
                "items": [
                    {
                        "id": mapping["roles"][role_id]["id"],
                        "text": mapping["roles"][role_id]["name"]
                    }
                    for role_id in mapping["categories"][category_id]["roleIds"]
                ]
            }
            for category_id in mapping["categoryIdsSorted"]
        ]
    }
