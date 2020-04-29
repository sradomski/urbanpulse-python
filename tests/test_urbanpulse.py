#!/usr/bin/env python

"""Tests for `urbanpulse` package."""

import pytest
import urbanpulse.historic as up_hist
import urbanpulse.mgmt as up_mgmt

@pytest.fixture
def urbanpulse_credentials():
	import os
	assert("UP_HOST" in os.environ)
	assert("UP_USERNAME" in os.environ)
	assert("UP_PASSWORD" in os.environ)
	return dict({
		"host": os.environ["UP_HOST"],
		"username": os.environ["UP_USERNAME"],
		"password": os.environ["UP_PASSWORD"]
		})

def test_mgmt_event_types(urbanpulse_credentials):
	up_mgmt.get_event_types(credentials=urbanpulse_credentials)

def test_historic(urbanpulse_credentials):
	import datetime
	hist = up_hist.fetch_csv(
		sid="",
		credentials=urbanpulse_credentials, 
		start_date=datetime.datetime.now() - datetime.timedelta(days=1), 
		end_date=datetime.datetime.now())
