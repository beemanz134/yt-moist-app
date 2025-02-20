from flask import jsonify

from .browser_sel import check_url, sel_take
from .panda_worker import get_datap

def main(user_url: str) -> None:
    duration = 0
    if check_url(user_url):
        duration = sel_take(user_url)
        rise_fall_data = get_datap(duration)
        return rise_fall_data
    return None



if __name__ == "__main__":
    pass
