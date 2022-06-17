Configuration of the breeze
=============================

breeze has a configuration class in :class:`breeze.config.Config` but we can't edit
this file because in that case our keys are placed in the code and this is not a good practice.
So we have to create a file `.env` at the root of the project and we can edit it.

``.env`` file is a file that contains environment variables. It is a file that is used to store
configuration variables. python dotenv is a library that allows us to read and write environment
variables from a file for more information visit `here <https://github.com/theskumar/python-dotenv>`_.

.. warning::
    ``.env`` file not commited to the repository because it's name in the `.gitignore` file.
    we not suggest to commit this file because it's not a good practice.

for example `.env` file contains the following::

    RECAPTCHA_PUBLIC_KEY=<your_recaptcha_public_key>
    RECAPTCHA_PRIVATE_KEY=<your_recaptcha_private_key>
    GITHUB_CLIENT_ID=<your_github_client_id>
    GITHUB_CLIENT_SECRET=<your_github_client_secret>
    DISCORD_CLIENT_ID=<your_discord_client_id>
    DISCORD_CLIENT_SECRET=<your_discord_client_secret>
