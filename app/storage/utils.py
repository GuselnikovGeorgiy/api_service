from datetime import datetime, timedelta


def split_query(filter_params: dict) -> dict:
    filter_query = {}

    ip_address = filter_params.get("ip_address")
    user_agent = filter_params.get("user_agent")
    os_info = filter_params.get("os_info")
    min_longitude = filter_params.get("min_longitude")
    max_longitude = filter_params.get("max_longitude")
    min_latitude = filter_params.get("min_latitude")
    max_latitude = filter_params.get("max_latitude")
    connect_time_from = filter_params.get("connect_time_from")
    connect_time_to = filter_params.get("connect_time_to")
    disconnect_time_from = filter_params.get("disconnect_time_from")
    disconnect_time_to = filter_params.get("disconnect_time_to")
    connection_duration_from = filter_params.get("connection_duration_from")
    connection_duration_to = filter_params.get("connection_duration_to")

    if ip_address:
        filter_query["ip_address"] = ip_address
    if user_agent:
        filter_query["user_agent"] = {"$regex": user_agent, "$options": "i"}
    if os_info:
        filter_query["os_info"] = os_info
    if min_longitude is not None or max_longitude is not None:
        filter_query["geo_position.longitude"] = {}
        if min_longitude is not None:
            filter_query["geo_position.longitude"]["$gte"] = min_longitude
        if max_longitude is not None:
            filter_query["geo_position.longitude"]["$lte"] = max_longitude
    if min_latitude is not None or max_latitude is not None:
        filter_query["geo_position.latitude"] = {}
        if min_latitude is not None:
            filter_query["geo_position.latitude"]["$gte"] = min_latitude
        if max_latitude is not None:
            filter_query["geo_position.latitude"]["$lte"] = max_latitude
    if connect_time_from:
        if "connect_time" not in filter_query:
            filter_query["connect_time"] = {}
        filter_query["connect_time"]["$gte"] = connect_time_from
    if connect_time_to:
        if "connect_time" not in filter_query:
            filter_query["connect_time"] = {}
        filter_query["connect_time"]["$lte"] = connect_time_to
    if disconnect_time_from:
        if "disconnect_time" not in filter_query:
            filter_query["disconnect_time"] = {}
        filter_query["disconnect_time"]["$gte"] = disconnect_time_from
    if disconnect_time_to:
        if "disconnect_time" not in filter_query:
            filter_query["disconnect_time"] = {}
        filter_query["disconnect_time"]["$lte"] = disconnect_time_to
    if connection_duration_from:
        if "connection_duration" not in filter_query:
            filter_query["connection_duration"] = {}
        filter_query["connection_duration"]["$gte"] = connection_duration_from
    if connection_duration_to:
        if "connection_duration" not in filter_query:
            filter_query["connection_duration"] = {}
        filter_query["connection_duration"]["$lte"] = connection_duration_to

    return filter_query


def calculate_connection_duration(document: dict) -> dict:
    if "connect_time" in document and "disconnect_time" in document:
        if isinstance(document["connect_time"], str):
            document["connect_time"] = datetime.fromisoformat(document["connect_time"])
        if isinstance(document["disconnect_time"], str):
            document["disconnect_time"] = datetime.fromisoformat(document["disconnect_time"])
        document["connection_duration"] = (document["disconnect_time"] - document["connect_time"]).total_seconds()
    return document
