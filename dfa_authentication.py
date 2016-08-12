import sys
import urllib

from oauthlib import oauth2

# Your OAuth 2.0 Client ID and Secret. If you do not have an ID and Secret yet,
# please go to https://console.developers.google.com and create a set.
CLIENT_ID = '764995533921-koh5npjud7so21lpi844l4c6v8ulpdtt.apps.googleusercontent.com'
CLIENT_SECRET = '4vAv2EdlV5hNy8TGI6d9xHrW'

# You may optionally provide an HTTPS proxy.
HTTPS_PROXY = None

# The AdWords API OAuth 2.0 scope.
SCOPE = 'https://www.googleapis.com/auth/dfareporting'
# This callback URL will allow you to copy the token from the success screen.
CALLBACK_URL = 'urn:ietf:wg:oauth:2.0:oob'
# The HTTP headers needed on OAuth 2.0 refresh requests.
OAUTH2_REFRESH_HEADERS = {'content-type':
                          'application/x-www-form-urlencoded'}
# The web address for generating new OAuth 2.0 credentials at Google.
GOOGLE_OAUTH2_AUTH_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_OAUTH2_GEN_ENDPOINT = 'https://accounts.google.com/o/oauth2/token'


def main():
  oauthlib_client = oauth2.WebApplicationClient(CLIENT_ID)

  authorize_url = oauthlib_client.prepare_request_uri(
      GOOGLE_OAUTH2_AUTH_ENDPOINT, redirect_uri=CALLBACK_URL, scope=SCOPE)
  print ('Log in to your AdWords account and open the following URL: \n%s\n' %
         authorize_url)
  print ('After approving the token enter the verification code (if specified).')
  code = input('Code: ').strip()

  post_body = oauthlib_client.prepare_request_body(
      client_secret=CLIENT_SECRET, code=code, redirect_uri=CALLBACK_URL)
  if sys.version_info[0] == 3:
    post_body = bytes(post_body, 'utf8')
  request = urllib2.Request(GOOGLE_OAUTH2_GEN_ENDPOINT, post_body,
                            OAUTH2_REFRESH_HEADERS)
  if HTTPS_PROXY:
    request.set_proxy(HTTPS_PROXY, 'https')
  raw_response = urllib2.urlopen(request).read().decode()
  oauth2_credentials = oauthlib_client.parse_request_body_response(raw_response)

  print ('Your access token is %s and your refresh token is %s'
         % (oauth2_credentials['access_token'],
            oauth2_credentials['refresh_token']))
  print ('You can cache these credentials into a yaml file with the '
         'following keys:\nadwords:\n  client_id: %s\n  client_secret: %s\n'
         '  refresh_token: %s\n'
         % (CLIENT_ID, CLIENT_SECRET, oauth2_credentials['refresh_token']))


if __name__ == '__main__':
  main()