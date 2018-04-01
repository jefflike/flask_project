import requests


class get_data:
    @staticmethod
    def get(url, is_json = True):
        """
        这里我们把代码简化了许多，没有使用大段的if/else，除了三元表达式我们还使用function简化代码
        提高可读性
        :param url:
        :param is_json:
        :return:
        """
        r = requests.get(url)
        if r.status_code != 200:
            return {} if is_json else ''
        return r.json() if is_json else r.text
