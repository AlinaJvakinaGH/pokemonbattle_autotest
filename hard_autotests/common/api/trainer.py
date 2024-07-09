import allure

from common.api.basic import Api

class TrainerApi(Api):
    def get_trainers(self, trainer_id: int = None):
        url=f'{self.url}/trainers'
        return self.get(url=url, params={'trainer_id': trainer_id}, token="your token")



