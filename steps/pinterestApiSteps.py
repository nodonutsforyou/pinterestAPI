import requests
from behave import *
import json


@given(u'we are authenticated')
@given(u'we get authenticated user info')
def step_impl(context):
    context.url = "%s/%s/me/?access_token=%s" % (context.host, context.apiVersion, context.authCode)
    context.response = requests.get(context.url)
    print('response status code: ', context.response.status_code)
    assert context.response.status_code == 200, "response code %s. response: %s" (context.response.status_code,
                                                                                  context.response.text)


@then(u'responce should contain user id')
def step_impl(context):
    context.jsonObject = json.loads(context.response.text)
    assert str(context.jsonObject['data']['id']) == str(context.userId), "user id is %s and not equals %s" % (context.jsonObject['data']['id'], context.userId)


@then(u'we should not see {board_name} in our boards list')
@given(u'we are not following board {board_name}')
def step_impl(context, board_name):
    context.url = "%s/%s/me/following/boards/?access_token=%s" % (context.host, context.apiVersion, context.authCode)
    context.response = requests.get(context.url)
    assert context.response.status_code == 200, "response code %s. response: %s"(context.response.status_code,
                                                                                 context.response.text)
    assert board_name not in context.response.text, "we are following %s but should not. Response: %s" % (board_name, context.response.text)


@then(u'we follow {board_name}')
def step_impl(context, board_name):
    context.url = "%s/%s/me/following/boards/?access_token=%s&board=%s" % (context.host, context.apiVersion, context.authCode, board_name)
    context.response = requests.get(context.url)
    assert context.response.status_code == 200, "response code %s. response: %s"(context.response.status_code,
                                                                                 context.response.text)
    #TODO - did not understood how to follow board. should change validation
    assert board_name not in context.response.text, "we are following %s but should not. Response: %s" % (board_name, context.response.text)


@then(u'we should see {board_name} in our boards list')
def step_impl(context, board_name):
    context.url = "%s/%s/me/following/boards/?access_token=%s" % (context.host, context.apiVersion, context.authCode)
    context.response = requests.get(context.url)
    assert context.response.status_code == 200, "response code %s. response: %s"(context.response.status_code,
                                                                                 context.response.text)
    assert board_name in context.response.text, "we are following %s but should not. Response: %s" % (board_name, context.response.text)


@then(u'we unfollow {board_name}')
def step_impl(context, board_name):
    context.url = "%s/%s/me/following/boards/$s?access_token=%s" % (context.host, context.apiVersion, board_name, context.authCode)
    context.response = requests.get(context.url)
    assert context.response.status_code == 200, "response code %s. response: %s"(context.response.status_code,
                                                                                 context.response.text)
    #TODO - did not understood how to follow board. should change validation
    assert board_name not in context.response.text, "we are following %s but should not. Response: %s" % (board_name, context.response.text)


