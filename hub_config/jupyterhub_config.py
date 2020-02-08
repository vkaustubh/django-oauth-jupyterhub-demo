# This is how we tell Jupyter to use OAuth instead of the default
# authentication which is done using local Linux user accounts.
c.JupyterHub.authenticator_class = 'oauthenticator.generic.GenericOAuthenticator'

# Where should Django pass the authentication results back to?
c.GenericOAuthenticator.oauth_callback_url = 'http://localhost:8010/hub/oauth_callback'

# What is the client ID and client secret for Jupyterhub provided Django?

c.GenericOAuthenticator.client_id = 'LEljnQrKwybZaFiS6Ee5YrkMAm1tYWTI0oLJpS2x'
c.GenericOAuthenticator.client_secret = 'ydIWGfdWLlqwIsIbg9VSOCVvBymysVKT649gaABTdcVLLvrRYMr2u4OqHnrSbSwkjQ0r5nZ5qFmnJXBgjxVBblGGe3k0UI5wQMyznUj651wTaTqVTYN7QwNFEnO7FN2S'

# Where can Jupyterhub get the token from?
c.GenericOAuthenticator.token_url = 'http://localhost:8000/o/token/'

# Where can it get the user name from? What method shall it use?
# What key in the JSON output is the username?
c.GenericOAuthenticator.userdata_url = 'http://localhost:8000/userdata'
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.userdata_params = {}
c.GenericOAuthenticator.username_key = 'username'

# What address will Jupyterhub be accessed from?
c.JupyterHub.bind_url = 'http://localhost:8010'

# By default Jupyterhub requires that a Linux user exist for every
# authenticated user. For testing, we are going to trick JupyterHub
# to merely pretend that such a user exists and launch notebook servers
# for the same user running the hub process itself!
from jupyterhub.spawner import LocalProcessSpawner

class SameUserSpawner(LocalProcessSpawner):
    """Local spawner that runs single-user servers as the same user as the Hub itself.

    Overrides user-specific env setup with no-ops.
    """

    def make_preexec_fn(self, name):
        """no-op to avoid setuid"""
        return lambda : None

    def user_env(self, env):
        """no-op to avoid setting HOME dir, etc.""" 
        return env

c.JupyterHub.spawner_class = SameUserSpawner
