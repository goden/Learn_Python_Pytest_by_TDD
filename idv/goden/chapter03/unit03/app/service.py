from idv.goden.chapter03.unit03.app import api, db


def sync_user(user_id):
    """商業邏輯：呼叫 API → 存 DB"""
    user_data = api.fetch_user(user_id)  # 外部 API
    database = db.Database()
    result = database.save_user(user_data)
    return result
