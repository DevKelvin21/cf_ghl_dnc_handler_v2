import os
import functions_framework
from flask import jsonify, Request
from .apps import VICI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

@functions_framework.http
def prime_to_dnc(request: Request):
    # Get the request data
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Get the phone number
    phone_number = request_json['phone'] if request_json else request_args['phone']
    # campaign = request_json['campaign'] if request_json else request_args['campaign']
    # Get the user and password
    user = os.getenv('VICI_USER')
    password = os.getenv('VICI_PASSWORD')

    # Initialize the VICI object
    vici = VICI("Rowena", user, password)

    # Add the phone number to the DNC list
    response = vici.add_dnc(phone_number)

    # Return the response
    return jsonify(response)