import pytest
import json
import requests
from config import KEYS


@pytest.mark.usefixtures("test_setup")
class TestAgencyIntegration:
    SUCCESS_CODE = 201
    OK_CODE = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    UNAUTHORIZED = 401

    agency_integration = "/internal/app/ksxhy8bPSF/agency/list"

    # Agency_Integration endpoints
    def test_agency_integration_key(self):
        headers = {"api-key": KEYS.api_key}
        params = {"status": "active"}
        status_code, res = pytest.actions.get_method(self.agency_integration, headers, params)
        assert status_code == self.OK_CODE

    def test_agency_integration_invalid_key(self):
        headers = {"api-key": KEYS.invalid_key}
        params = {"status": "active"}
        status_code, res = pytest.actions.get_method(self.agency_integration, headers, params)
        assert status_code == self.BAD_REQUEST

    def test_active_agency(self):
        headers = {"api-key": KEYS.api_key}
        params = {"status": "active"}
        status_code, res = pytest.actions.get_method(self.agency_integration, headers, params)
        assert status_code == self.OK_CODE
        assert len(res["data"]) == 4
        assert (res['success']) == True
        assert (res['message']) is None
        assert "data" in res, "Key 'data' does not exist in the response"
        assert (res['data']['pagination']['page']) == 1
        assert (res['data']['pagination']['limit']) == 10
        assert "filter" in res["data"], "Key 'filter' does not exist under 'data' in the response"
        assert "agencies" in res["data"], "Key 'agencies' does not exist under 'data' in the response"
        assert "_id" in res["data"]["agencies"][0], "Key '_id' does not exist under 'agencies' in the response"
        assert "name" in res["data"]["agencies"][0], "Key 'name' does not exist under 'agencies' in the response"
        assert "desc" in res["data"]["agencies"][0], "Key 'desc' does not exist under 'agencies' in the response"
        assert "status" in res["data"]["agencies"][0], "Key 'status' does not exist under 'agencies' in the response"
        assert "type" in res["data"]["agencies"][0], "Key 'type' does not exist under 'agencies' in the response"
        assert "pc" in res["data"]["agencies"][0], "Key 'pc' does not exist under 'agencies' in the response"
        assert "retargeting" in res["data"]["agencies"][0]["pc"], "Key 'retargeting' does not exist under 'pc' in the response"
        assert "cost" in res["data"]["agencies"][0]["pc"], "Key 'cost' does not exist under 'pc' in the response"
        assert "adrev" in res["data"]["agencies"][0]["pc"], "Key 'adrev' does not exist under 'pc' in the response"
        assert "impression" in res["data"]["agencies"][0]["pc"], "Key 'impression' does not exist under 'pc' in the response"
        assert "attribution" in res["data"]["agencies"][0]["pc"], "Key 'attribution' does not exist under 'pc' in the response"
        assert "skan" in res["data"]["agencies"][0]["pc"], "Key 'skan' does not exist under 'pc' in the response"
        assert "preload" in res["data"]["agencies"][0]["pc"], "Key 'preload' does not exist under 'pc' in the response"
        assert "ptype" in res["data"]["agencies"][0], "Key 'ptype' does not exist under 'agencies' in the response"
        assert "pvertical" in res["data"]["agencies"][0], "Key 'pvertical' does not exist under 'agencies' in the response"
        assert "image" in res["data"]["agencies"][0], "Key 'image' does not exist under 'agencies' in the response"
        assert "created" in res["data"]["agencies"][0], "Key 'created' does not exist under 'agencies' in the response"
        assert "appAccessList" in res["data"], "Key 'appAccessList' does not exist under 'data' in the response"
        assert "integrationStatus" in res["data"]["appAccessList"][0], "Key 'integrationStatus' does not exist under 'appAccessList' in the response"
        assert "oid" in res["data"]["appAccessList"][0], "Key 'oid' does not exist under 'appAccessList' in the response"
        assert "agencyPermission" in res["data"]["appAccessList"][0], "Key 'agencyPermission' does not exist under 'appAccessList' in the response"
        assert "uninstall" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'uninstall' does not exist under 'agencyPermission' in the response"
        assert "antiFraud" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'antiFraud' does not exist under 'agencyPermission' in the response"
        assert "cfgPartner" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'cfgPartner' does not exist under 'agencyPermission' in the response"
        assert "logAccess" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'logAccess' does not exist under 'agencyPermission' in the response"
        assert "allPartnerDataAccess" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'allPartnerDataAccess' does not exist under 'agencyPermission' in the response"
        assert "organicDataAccess" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'organicDataAccess' does not exist under 'agencyPermission' in the response"
        assert "revenueDataAccess" in res["data"]["appAccessList"][0]["agencyPermission"], "Key 'revenueDataAccess' does not exist under 'agencyPermission' in the response"
