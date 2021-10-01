import requests
from django.http import JsonResponse

from oauth2.utils import get_accounts_info


class Authentication:
    def oauth2(self, access_token: str):
        url = f"https://www.googleapis.com/drive/v3/about?fields=user&access_token={access_token}"
        response = requests.get(url)

        get_accounts_info(access_token)

        if response.status_code == 200:
            JsonResponse.status_code = 200
            return JsonResponse(response.json())
        else:
            JsonResponse.status_code = 401
            return JsonResponse({})
from django.http import HttpResponse


class Test:
    def as_view(self):
        return HttpResponse("""
            <button onclick="oauth2SignIn()">Continue with Google</button>
            <hr />
            <img id='img' />
            <div id='name'></div>
            <div id='email'></div>
            <script>
             var fragmentString = location.hash.substring(1);

      // Parse query string to see if page request is coming from OAuth 2.0 server.
      var params = {};
      var regex = /([^&=]+)=([^&]*)/g,
        m;
      while ((m = regex.exec(fragmentString))) {
        params[decodeURIComponent(m[1])] = decodeURIComponent(m[2]);
      }
      if (Object.keys(params).length > 0) {
        localStorage.setItem("oauth2-test-params", JSON.stringify(params));
        if (params["state"] && params["state"] == "try_sample_request") {
//           trySampleRequest();

    fetch('auth/google/' + params["access_token"]).then(res => res.json()).then(userInfo => {


  img.src=  userInfo.img
    name.textContent = userInfo.name
email.textContent = userInfo.email
})
        }
      }
            
          var YOUR_CLIENT_ID =
        "213873025360-dk75b6uhmd2h67mfdphg3usn8bktcer6.apps.googleusercontent.com";
      var YOUR_REDIRECT_URI =
        "http://127.0.0.1:8000";
             function oauth2SignIn() {
        // Google's OAuth 2.0 endpoint for requesting an access token
        var oauth2Endpoint = "https://accounts.google.com/o/oauth2/v2/auth";

        // Create element to open OAuth 2.0 endpoint in new window.
        var form = document.createElement("form");
        form.setAttribute("method", "GET"); // Send as a GET request.
        form.setAttribute("action", oauth2Endpoint);

        // Parameters to pass to OAuth 2.0 endpoint.
        var params = {
          client_id: YOUR_CLIENT_ID,
          redirect_uri: YOUR_REDIRECT_URI,
          scope: "https://www.googleapis.com/auth/drive.metadata.readonly",
          state: "try_sample_request",
          include_granted_scopes: "true",
          response_type: "token",
        };

        // Add form parameters as hidden input values.
        for (var p in params) {
          var input = document.createElement("input");
          input.setAttribute("type", "hidden");
          input.setAttribute("name", p);
          input.setAttribute("value", params[p]);
          form.appendChild(input);
        }

        // Add form to page and submit it to open the OAuth 2.0 endpoint.
        document.body.appendChild(form);
        form.submit();
      }</script>
        """)
