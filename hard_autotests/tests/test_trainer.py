from pytest_voluptuous import S
import pytest
from common.api.trainer import TrainerApi
from common.helper.schema.trainer import valid_trainer, invalid_intager_trainer, invalid_string_trainer

class TestTrainers():
    CASE = [
        {"id": 'your id', "status_code": 200, "schema" : valid_trainer},
        {"id": -'your id', "status_code": 200, "schema" : invalid_intager_trainer},
        {"id": "qwerty", "status_code": 422, "schema" : invalid_string_trainer}
    ]

    @pytest.mark.parametrize("case", CASE)
    def test_get_trainers(self, case):
        trainer_api = TrainerApi()

        response = trainer_api.get_trainers(trainer_id=case["id"])
        trainer_api.status_code_should_be(expected_code=case["status_code"])
        
        assert S(case["schema"]) == response.response.json()