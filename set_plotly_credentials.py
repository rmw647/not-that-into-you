def set_plotly_credentials(credential_json):
    with open(credential_json) as data_file:
        cred_data = json.load(data_file)
    username = cred_data['username']
    api_key = cred_data['api_key']
    plotly.tools.set_credentials_file(username=username, api_key=api_key)
    py.sign_in(username, api_key)
