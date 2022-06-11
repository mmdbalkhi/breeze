API
===

.. module:: breeze


.. autoclass:: breeze.Config

.. autofunction:: breeze.create_app

Authentication
------------------

Auth is a module that provides a simple authentication system for Flask.

auth base class
~~~~~~~~~~~~~~~~

.. autoclass:: breeze.Auth
   :members:

Auth with other ways(e.g. github, etc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: breeze.GithubOAuth2
   :members:

Blueprints
------------------
This section lists our Blueprint APIs. A Blueprint is a way to organize a group
of related views and other codes. Rather than registering views and other code
directly with an application, they are registered with a blueprint. Then the blueprint
is registered with the application when it is available in the factory function.

For more information see `Modular Applications with Blueprints <https://flask.palletsprojects.com/en/2.1.x/blueprints>`_

Authentication
------------------

.. automodule:: breeze.blueprints.auth
   :members:

Index
------------------

.. automodule:: breeze.blueprints.index
   :members:


Posts
------------------

.. automodule:: breeze.blueprints.posts
   :members:


Config
------------------

.. automodule:: breeze.config
   :members:



Exception
------------------

.. automodule:: breeze.exc
   :members:



Models
------------------
.. automodule:: breeze.models
   :members:



Utils
------------------
.. automodule:: breeze.utils
   :members:
