import pytest
import json
import requests
from config import KEYS


@pytest.mark.usefixtures("test_setup")
class TestAPIToken:
    SUCCESS_CODE = 201
    OK_CODE = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400
    UNAUTHORIZED = 401

    api_token = "/internal/account/info"

    # User Info endpoints
    def test_valid_key(self):
        headers = {"api-key": KEYS.api_key}
        status_code, res = pytest.actions.get_method(self.api_token, headers)
        assert status_code == self.OK_CODE

    def test_invalid_key(self):
        headers = {"api-key": KEYS.invalid_key}
        status_code, res = pytest.actions.get_method(self.api_token, headers)
        assert status_code == self.BAD_REQUEST

    #  Advertiser User Info
    def test_api_key(self):
        headers = {"api-key": KEYS.api_key}
        status_code, res = pytest.actions.get_method(self.api_token, headers)
        assert status_code == self.OK_CODE
        assert len(res["data"]) == 4
        assert (res['success']) == True
        assert (res['message']) is None
        assert "data" in res, "Key 'data' does not exist in the response"
        assert "isConfigured" in res["data"], "Key 'isConfigured' does not exist under 'data' in the response"
        assert "user" in res["data"], "Key 'user' does not exist under 'data' in the response"
        assert "_id" in res["data"]["user"], "Key '_id' does not exist under 'user' in the response"
        assert "displayId" in res["data"]["user"], "Key 'displayId' does not exist under 'user' in the response"
        assert "oid" in res["data"]["user"], "Key 'oid' does not exist under 'user' in the response"
        assert "name" in res["data"]["user"], "Key 'name' does not exist under 'user' in the response"
        assert "email" in res["data"]["user"], "Key 'email' does not exist under 'user' in the response"
        assert "role" in res["data"]["user"], "Key 'role' does not exist under 'user' in the response"
        assert "status" in res["data"]["user"], "Key 'status' does not exist under 'user' in the response"
        assert "contact" in res["data"]["user"], "Key 'contact' does not exist under 'user' in the response"
        assert "skype" in res["data"]["user"]["contact"], "Key 'skype' does not exist under 'contact' in the response"
        assert "phone" in res["data"]["user"]["contact"], "Key 'phone' does not exist under 'contact' in the response"
        assert "address" in res["data"]["user"]["contact"], "Key 'address' does not exist under 'contact' in the response"
        assert "permissions" in res["data"]["user"], "Key 'permissions' does not exist under 'user' in the response"
        assert "appCrud" in res["data"]["user"]["permissions"], "Key 'appCrud' does not exist under 'permissions' in the response"
        assert "teamCrud" in res["data"]["user"]["permissions"], "Key 'teamCrud' does not exist under 'permissions' in the response"
        assert "payment" in res["data"]["user"]["permissions"], "Key 'payment' does not exist under 'permissions' in the response"
        assert "partnerCrud" in res["data"]["user"]["permissions"], "Key 'partnerCrud' does not exist under 'permissions' in the response"
        assert "eventCrud" in res["data"]["user"]["permissions"], "Key 'eventCrud' does not exist under 'permissions' in the response"
        assert "postbackCrud" in res["data"]["user"]["permissions"], "Key 'postbackCrud' does not exist under 'permissions' in the response"
        assert "appIdList" in res["data"]["user"], "Key 'appIdList' does not exist under 'user' in the response"
        assert "apiKey" in res["data"]["user"], "Key 'apiKey' does not exist under 'user' in the response"
        assert "lang" in res["data"]["user"], "Key 'lang' does not exist under 'user' in the response"
        assert "created" in res["data"]["user"], "Key 'created' does not exist under 'user' in the response"
        assert "lastAccess" in res["data"]["user"], "Key 'lastAccess' does not exist under 'user' in the response"
        assert "time" in res["data"]["user"]["lastAccess"], "Key 'time' does not exist under 'lastAccess' in the response"
        assert "ip" in res["data"]["user"]["lastAccess"], "Key 'ip' does not exist under 'lastAccess' in the response"
        assert "city" in res["data"]["user"]["lastAccess"], "Key 'city' does not exist under 'lastAccess' in the response"
        assert "country" in res["data"]["user"]["lastAccess"], "Key 'country' does not exist under 'lastAccess' in the response"
        assert "org" in res["data"], "Key 'org' does not exist under 'data' in the response"
        assert "_id" in res["data"]["org"], "Key '_id' does not exist under 'org' in the response"
        assert "name" in res["data"]["org"], "Key 'name' does not exist under 'org' in the response"
        assert "type" in res["data"]["org"], "Key 'type' does not exist under 'org' in the response"
        assert "status" in res["data"]["org"], "Key 'status' does not exist under 'org' in the response"
        assert "desc" in res["data"]["org"], "Key 'desc' does not exist under 'org' in the response"
        assert "ts" in res["data"]["org"], "Key 'ts' does not exist under 'org' in the response"
        assert "region" in res["data"]["org"], "Key 'region' does not exist under 'org' in the response"
        assert "signUpIp" in res["data"]["org"]["region"], "Key 'signUpIp' does not exist under 'region' in the response"
        assert "timezone" in res["data"]["org"]["region"], "Key 'timezone' does not exist under 'region' in the response"
        assert "country" in res["data"]["org"]["region"], "Key 'country' does not exist under 'region' in the response"
        assert "city" in res["data"]["org"]["region"], "Key 'city' does not exist under 'region' in the response"
        assert "state" in res["data"]["org"]["region"], "Key 'state' does not exist under 'region' in the response"
        assert "currency" in res["data"]["org"]["region"], "Key 'currency' does not exist under 'region' in the response"
        assert "meta" in res["data"]["org"], "Key 'meta' does not exist under 'org' in the response"
        assert "phone" in res["data"]["org"]["meta"], "Key 'phone' does not exist under 'meta' in the response"
        assert "website" in res["data"]["org"]["meta"], "Key 'website' does not exist under 'meta' in the response"
        assert "linkedin" in res["data"]["org"]["meta"], "Key 'linkedin' does not exist under 'meta' in the response"
        assert "twitter" in res["data"]["org"]["meta"], "Key 'twitter' does not exist under 'meta' in the response"
        assert "facebook" in res["data"]["org"]["meta"], "Key 'facebook' does not exist under 'meta' in the response"
        assert "address" in res["data"]["org"]["meta"], "Key 'address' does not exist under 'meta' in the response"
        assert "blog" in res["data"]["org"]["meta"], "Key 'blog' does not exist under 'meta' in the response"
        assert "instagram" in res["data"]["org"]["meta"], "Key 'instagram' does not exist under 'meta' in the response"
        assert "platform" in res["data"]["org"]["meta"], "Key 'platform' does not exist under 'meta' in the response"
        assert "image" in res["data"]["org"], "Key 'image' does not exist under 'org' in the response"
        assert "managerId" in res["data"]["org"], "Key 'managerId' does not exist under 'org' in the response"
        assert "created" in res["data"]["org"], "Key 'created' does not exist under 'org' in the response"
        assert "trialExpire" in res["data"]["org"], "Key 'trialExpire' does not exist under 'org' in the response"
        assert "expired" in res["data"]["org"], "Key 'expired' does not exist under 'org' in the response"
        assert "bid" in res["data"]["org"], "Key 'bid' does not exist under 'org' in the response"
        assert "features" in res["data"]["org"], "Key 'features' does not exist under 'org' in the response"
        assert "antifraud" in res["data"]["org"]["features"], "Key 'antifraud' does not exist under 'features' in the response"
        assert "targeting" in res["data"]["org"]["features"], "Key 'targeting' does not exist under 'features' in the response"
        assert "unilink" in res["data"]["org"]["features"], "Key 'unilink' does not exist under 'features' in the response"
        assert "brandedDomain" in res["data"]["org"]["features"], "Key 'brandedDomain' does not exist under 'features' in the response"
        assert "s2sTracking" in res["data"]["org"]["features"], "Key 's2sTracking' does not exist under 'features' in the response"
        assert "uninstall" in res["data"]["org"]["features"], "Key 'uninstall' does not exist under 'features' in the response"
        assert "uniqueEvent" in res["data"]["org"]["features"], "Key 'uniqueEvent' does not exist under 'features' in the response"
        assert "customerReport" in res["data"]["org"]["features"], "Key 'customerReport' does not exist under 'features' in the response"
        assert "audience" in res["data"]["org"]["features"], "Key 'audience' does not exist under 'features' in the response"
        assert "domain" in res["data"]["org"], "Key 'domain' does not exist under 'org' in the response"
        assert "advSetting" in res["data"]["org"], "Key 'advSetting' does not exist under 'org' in the response"
        assert "billing" in res["data"]["org"]["advSetting"], "Key 'billing' does not exist under 'advSetting' in the response"
        assert "disableWrite" in res["data"]["org"]["advSetting"], "Key 'disableWrite' does not exist under 'advSetting' in the response"
        assert "primaryAM" in res["data"]["org"]["advSetting"], "Key 'primaryAM' does not exist under 'advSetting' in the response"
        assert "secondaryAM" in res["data"]["org"]["advSetting"], "Key 'secondaryAM' does not exist under 'advSetting' in the response"
        assert "sdr" in res["data"]["org"]["advSetting"], "Key 'sdr' does not exist under 'advSetting' in the response"
        assert "manager" in res["data"], "Key 'manager' does not exist under 'data' in the response"
        assert "name" in res["data"]["manager"], "Key 'name' does not exist under 'manager' in the response"
        assert "skype" in res["data"]["manager"], "Key 'skype' does not exist under 'manager' in the response"
        assert "email" in res["data"]["manager"], "Key 'email' does not exist under 'manager' in the response"
        assert "phone" in res["data"]["manager"], "Key 'phone' does not exist under 'manager' in the response"
