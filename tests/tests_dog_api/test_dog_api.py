import pytest


class TestDogApi:

    def test_list_all_breeds(self, dog_api_obj):
        r = dog_api_obj.request("list_all_breeds")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    @pytest.mark.parametrize("number_of_photos", ("1", "10", "30"))
    def test_random_image(self, dog_api_obj, number_of_photos):
        r = dog_api_obj.request("random_image", number_of_photos=number_of_photos)
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"
    #
    def test_by_breed(self, dog_api_obj):
        r = dog_api_obj.request("by_breed")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    def test_list_all_sub_breeds(self, dog_api_obj):
        r = dog_api_obj.request("list_all_sub_breeds")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"
    #
    @pytest.mark.parametrize("number_of_photos", ("3", "4", "5"))
    def test_multiple_images_from_a_sub_breed(self, dog_api_obj, number_of_photos):
        r = dog_api_obj.request("multiple_images_from_a_sub_breed", number_of_photos=number_of_photos)
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"