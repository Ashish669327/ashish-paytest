import pytest
import json
import requests
from test.config import KEYS
import os
@pytest.mark.usefixtures("test_setup")
class TestAddApp:
    SUCCESS_CODE = 201
    OK_CODE = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    UNAUTHORIZED = 401

    app_list = "/internal/app/list"
    add_app = "/internal/app/create"

    api_key = os.getenv("api_key")

    # App_endpoints
    def test_add_valid_key(self):
        headers = {"api-key": KEYS.api_key}
        status_code, res = pytest.actions.get_method(self.app_list, headers)
        assert status_code == self.OK_CODE
        assert len(res["data"]) == 3

    def test_add_invalid_key(self):
        headers = {"api-key": KEYS.invalid_key}
        status_code, res = pytest.actions.get_method(self.app_list, headers)
        assert status_code == self.BAD_REQUEST

    def test_app_mapping_filed(self):
        headers = {"api-key": KEYS.api_key}
        status_code, res = pytest.actions.get_method(self.app_list, headers)
        assert (res['success']) == True
        assert "data" in res, "Key 'data' does not exist in the response"
        assert (res['data']['pagination']['page']) == 1
        assert (res['data']['pagination']['limit']) == 10
        assert "applicationList" in res["data"], "Key 'applicationList' does not exist under 'data' in the response"
        assert "_id" in res["data"]["applicationList"][0], "Key '_id' does not exist under in the response"
        assert "oid" in res["data"]["applicationList"][0], "Key 'oid' does not exist under 'applicationList' in the response"
        assert "name" in res["data"]["applicationList"][0], "Key 'name' does not exist under 'applicationList' in the response"
        assert "os" in res["data"]["applicationList"][0], "Key 'os' does not exist under 'applicationList' in the response"
        assert "status" in res["data"]["applicationList"][0], "Key 'status' does not exist under 'applicationList' in the response"
        assert "packageId" in res["data"]["applicationList"][0], "Key 'packageId' does not exist under 'applicationList' in the response"
        assert "surl" in res["data"]["applicationList"][0], "Key 'surl' does not exist under 'applicationList' in the response"
        assert "timezone" in res["data"]["applicationList"][
            0], "Key 'timezone' does not exist under 'applicationList' in the response"
        assert "currency" in res["data"]["applicationList"][
            0], "Key 'currency' does not exist under 'applicationList' in the response"
        assert "genre" in res["data"]["applicationList"][
            0], "Key 'genre' does not exist under 'applicationList' in the response"
        assert "appKey" in res["data"]["applicationList"][
            0], "Key 'appKey' does not exist under 'applicationList' in the response"
        assert "minSessDuration" in res["data"]["applicationList"][
            0], "Key 'minSessDuration' does not exist under 'applicationList' in the response"
        assert "mode" in res["data"]["applicationList"][
            0], "Key 'mode' does not exist under 'applicationList' in the response"
        assert "hideOrganic" in res["data"]["applicationList"][
            0], "Key 'hideOrganic' does not exist under 'applicationList' in the response"
        assert "reatrw" in res["data"]["applicationList"][
            0], "Key 'reatrw' does not exist under 'applicationList' in the response"
        assert "ips" in res["data"]["applicationList"][
            0], "Key 'ips' does not exist under 'applicationList' in the response"
        assert "ute" in res["data"]["applicationList"][
            0], "Key 'ute' does not exist under 'applicationList' in the response"
        assert "deeplink" in res["data"]["applicationList"][
            0], "Key 'deeplink' does not exist under 'applicationList' in the response"
        assert "cnvMapping" in res["data"]["applicationList"][
            0], "Key 'cnvMapping' does not exist under 'applicationList' in the response"
        assert "whlDvIds" in res["data"]["applicationList"][
            0], "Key 'whlDvIds' does not exist under 'applicationList' in the response"
        assert "debug" in res["data"]["applicationList"][
            0], "Key 'debug' does not exist under 'applicationList' in the response"
        assert "storeInfo" in res["data"]["applicationList"][
            0], "Key 'storeInfo' does not exist under 'applicationList' in the response"
        assert "debug" in res["data"]["applicationList"][
            0], "Key 'debug' does not exist under 'applicationList' in the response"
        assert "hasSDKSigned" in res["data"]["applicationList"][
            0], "Key 'hasSDKSigned' does not exist under 'applicationList' in the response"
        assert "reng" in res["data"]["applicationList"][
            0], "Key 'reng' does not exist under 'applicationList' in the response"
        assert "organicfc" in res["data"]["applicationList"][
            0], "Key 'organicfc' does not exist under 'applicationList' in the response"
        assert "fea" in res["data"]["applicationList"][0], "Key 'fea' does not exist under 'applicationList' in the response"
        assert "s2sKey" in res["data"]["applicationList"][0], "Key 's2sKey' does not exist under 'applicationList' in the response"
        assert "created" in res["data"]["applicationList"][0], "Key 'created' does not exist under 'applicationList' in the response"
        assert "orgMap" in res["data"], "Key 'orgMap' does not exist under 'data' in the response"
'''
    def test_cud_app(self):
        headers = {"api-key": KEYS.api_key}
        body = {
            "appStatus": "instore",
            "currency": "INR",
            "genre": "TOOLS",
            "name": "test_autoamtion",
            "os": "android",
            "packageId": "in.gov.uidai.test_autoamtion",
            "storeUrl": "https://play.google.com/store/apps/details?id=in.gov.uidai.test_autoamtion",
            "timezone": "Asia/Kolkata"
        }
        status_code, res = pytest.actions.post_method(self.add_app, headers, json=body)
        assert status_code == 200
        assert len(res["data"]) == 1
        assert (res['success']) == True
        assert (res['message']) == "Application added successfully"
        assert "data" in res, "Key 'data' does not exist in the response"
        assert "displayId" in res["data"]["application"], "Key 'displayId' does not exist in the response"
        assert "status" in res["data"]["application"], "Key 'status' does not exist in the response"
        assert "timezone" in res["data"]["application"], "Key 'timezone' does not exist in the response"
        assert "currency" in res["data"]["application"], "Key 'currency' does not exist in the response"
        assert "s2sKey" in res["data"]["application"], "Key 's2sKey' does not exist in the response"
        assert "imagePath" in res["data"]["application"], "Key 'imagePath' does not exist in the response"
        assert "mode" in res["data"]["application"], "Key 'mode' does not exist in the response"
        assert "hideOrganic" in res["data"]["application"], "Key 'hideOrganic' does not exist in the response"
        assert "reatrw" in res["data"]["application"], "Key 'reatrw' does not exist in the response"
        assert "ips" in res["data"]["application"], "Key 'ips' does not exist in the response"
        assert "ute" in res["data"]["application"], "Key 'ute' does not exist in the response"
        assert "whlDvIds" in res["data"]["application"], "Key 'whlDvIds' does not exist in the response"
        assert "isConfigured" in res["data"]["application"], "Key 'isConfigured' does not exist in the response"
        assert "debug" in res["data"]["application"], "Key 'debug' does not exist in the response"
        assert "hasSDKSigned" in res["data"]["application"], "Key 'hasSDKSigned' does not exist in the response"
        assert "_id" in res["data"]["application"], "Key '_id' does not exist in the response"
        assert "oid" in res["data"]["application"], "Key 'oid' does not exist in the response"
        assert "name" in res["data"]["application"], "Key 'name' does not exist in the response"
        assert "os" in res["data"]["application"], "Key 'os' does not exist in the response"
        assert "surl" in res["data"]["application"], "Key 'surl' does not exist in the response"
        assert "packageId" in res["data"]["application"], "Key 'packageId' does not exist in the response"
        assert "genre" in res["data"]["application"], "Key 'genre' does not exist in the response"
        assert "appKey" in res["data"]["application"], "Key 'appKey' does not exist in the response"
        assert "minSessDuration" in res["data"]["application"], "Key 'minSessDuration' does not exist in the response"
        assert "storeInfo" in res["data"]["application"], "Key 'storeInfo' does not exist in the response"
        assert "cnvMapping" in res["data"]["application"], "Key 'cnvMapping' does not exist in the response"
        assert "fea" in res["data"]["application"], "Key 'fea' does not exist in the response"
        assert "reng" in res["data"]["application"], "Key 'reng' does not exist in the response"
        assert "created" in res["data"]["application"], "Key 'created' does not exist in the response"
        assert "modified" in res["data"]["application"], "Key 'modified' does not exist in the response"
        t1 = res["data"]["application"]["_id"]
        edit_app = "/internal/app/" + t1
        body_edit = {
            "currency": "USD",
            "genre": "FINANCE",
            "name": "muvin-1demo",
            "reatrw": 90,
            "minSessUnit": "minute",
            "minSessDuration": 5,
            "mode": "testing",
            "status": "active",
        }
        status_code_edit, res_edit = pytest.actions.patch_method(edit_app, headers, json=body_edit)
        assert status_code_edit == 200
        assert len(res["data"]) == 1
        assert (res_edit['success']) == True
        assert (res_edit['message']) == "Application updated successfully."
        assert "data" in res_edit, "Key 'data' does not exist in the response"
        assert "displayId" in res_edit["data"]["application"], "Key 'displayId' does not exist in the response"
        assert "status" in res_edit["data"]["application"], "Key 'status' does not exist in the response"
        assert "timezone" in res_edit["data"]["application"], "Key 'timezone' does not exist in the response"
        assert "currency" in res_edit["data"]["application"], "Key 'currency' does not exist in the response"
        assert "s2sKey" in res_edit["data"]["application"], "Key 's2sKey' does not exist in the response"
        assert "imagePath" in res_edit["data"]["application"], "Key 'imagePath' does not exist in the response"
        assert "mode" in res_edit["data"]["application"], "Key 'mode' does not exist in the response"
        assert "hideOrganic" in res_edit["data"]["application"], "Key 'hideOrganic' does not exist in the response"
        assert "reatrw" in res_edit["data"]["application"], "Key 'reatrw' does not exist in the response"
        assert "ips" in res_edit["data"]["application"], "Key 'ips' does not exist in the response"
        assert "ute" in res_edit["data"]["application"], "Key 'ute' does not exist in the response"
        assert "isConfigured" in res_edit["data"]["application"], "Key 'isConfigured' does not exist in the response"
        assert "debug" in res_edit["data"]["application"], "Key 'debug' does not exist in the response"
        assert "hasSDKSigned" in res_edit["data"]["application"], "Key 'hasSDKSigned' does not exist in the response"
        assert "_id" in res_edit["data"]["application"], "Key '_id' does not exist in the response"
        assert "oid" in res_edit["data"]["application"], "Key 'oid' does not exist in the response"
        assert "name" in res_edit["data"]["application"], "Key 'name' does not exist in the response"
        assert "os" in res_edit["data"]["application"], "Key 'os' does not exist in the response"
        assert "surl" in res_edit["data"]["application"], "Key 'surl' does not exist in the response"
        assert "packageId" in res_edit["data"]["application"], "Key 'packageId' does not exist in the response"
        assert "genre" in res_edit["data"]["application"], "Key 'genre' does not exist in the response"
        # assert "image" in res_edit["data"]["application"], "Key 'image' does not exist in the response"
        assert "appKey" in res_edit["data"]["application"], "Key 'appKey' does not exist in the response"
        assert "minSessDuration" in res_edit["data"]["application"], "Key 'minSessDuration' does not exist in the response"
        assert "duration" in res_edit["data"]["application"]["minSessDuration"], "Key 'duration' does not exist in the response"
        assert "unit" in res_edit["data"]["application"]["minSessDuration"], "Key 'unit' does not exist in the response"
        assert "created" in res_edit["data"]["application"], "Key 'created' does not exist in the response"
        assert "modified" in res_edit["data"]["application"], "Key 'modified' does not exist in the response"
        assert "storeInfo" in res_edit["data"]["application"], "Key 'storeInfo' does not exist in the response"
        assert "version" in res_edit["data"]["application"]["storeInfo"], "Key 'version' does not exist in the response"
        assert "updatedAt" in res_edit["data"]["application"]["storeInfo"], "Key 'updatedAt' does not exist in the response"
        assert "cnvMapping" in res_edit["data"]["application"], "Key 'cnvMapping' does not exist in the response"
        assert "fea" in res_edit["data"]["application"], "Key 'fea' does not exist in the response"
        assert "organicfc" in res_edit["data"]["application"], "Key 'organicfc' does not exist in the response"
        assert "app_version_mismatch" in res_edit["data"]["application"]["organicfc"], "Key 'app_version_mismatch' does not exist in the response"
        assert "blacklist_ip" in res_edit["data"]["application"]["organicfc"], "Key 'blacklist_ip' does not exist in the response"
        assert "duplicate_ip" in res_edit["data"]["application"]["organicfc"], "Key 'duplicate_ip' does not exist in the response"
        assert "duplicate_install" in res_edit["data"]["application"]["organicfc"], "Key 'duplicate_install' does not exist in the response"
        assert "duplicate_event" in res_edit["data"]["application"]["organicfc"], "Key 'duplicate_event' does not exist in the response"
        assert "emulator" in res_edit["data"]["application"]["organicfc"], "Key 'emulator' does not exist in the response"
        assert "sdk_spoofing" in res_edit["data"]["application"]["organicfc"], "Key 'sdk_spoofing' does not exist in the response"
        assert "signature_mismatch" in res_edit["data"]["application"]["organicfc"], "Key 'signature_mismatch' does not exist in the response"
        assert "untrusted_device" in res_edit["data"]["application"]["organicfc"], "Key 'untrusted_device' does not exist in the response"
        assert "validation_rule_block" in res_edit["data"]["application"]["organicfc"], "Key 'validation_rule_block' does not exist in the response"
        assert "fake_device" in res_edit["data"]["application"]["organicfc"], "Key 'fake_device' does not exist in the response"
        assert "reng" in res_edit["data"]["application"], "Key 'reng' does not exist in the response"
        t3 = res["data"]["application"]["_id"]
        delete_app = "/internal/app/" + t3
        status_code_delete, res_delete = pytest.actions.delete_method(delete_app, headers, json=delete_app)
        assert status_code_delete == 200
        assert (res_delete['success']) == True
        assert (res_delete['message']) == "Application deleted successfully"

'''
