# Heroku setup

1. Pull slack-imgur code from GitHub
2. Install and configure the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command)
3. `cd` to the local slack-imgur repo
4. Run "heroku create" to create a new app. Note the URL (eg. `http://falling-wind-1624.herokuapp.com/` or something similar). This will be used when configuring the Slack webhook.
5. Get [API keys for imgur](https://api.imgur.com/)
6. Set the API key environment variables

    ```bash
    $ heroku config:set IMGUR_CLIENT_ID=xxxxxxx
    $ heroku config:set IMGUR_CLIENT_SECRET=xxxxxxx
    ```

7. Deploy to Heroku

    ```bash
    $ git push heroku master
    ```

8. Profit!
