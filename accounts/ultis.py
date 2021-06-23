def get_api_actions() -> list:
    from OauthToolkit_RestFramework import api_router
    from rest_framework.routers import SimpleRouter
    from api_base.permissions.token_permission import TokenPermissionWithAction

    registry = api_router.router.registry
    res_dict = {r[1].__name__: r[2] for r in registry}
    api_actions = []
    for res in registry:
        if TokenPermissionWithAction in res[1].permission_classes:
            router = SimpleRouter()
            routes = router.get_routes(res[1])
            action_list = []
            for route in routes:
                action_list += list(route.mapping.values())
            distinct_action_list = list(set(action_list))
            basename = res_dict.get(res[1].__name__)
            api_actions.extend(
                [f"{basename}:{action}" for action in distinct_action_list]
            )
    api_actions = list(set(api_actions))
    return api_actions


def read_file_json(file_path: str) -> dict:
    """
    Read file.json and return a dict of data
    """
    import json
    with open(file_path, "r") as json_file:
        data: dict = json.load(json_file)
    return data
