# A blog

This simple blgo application integrates [Esmerald][esmerald], [Saffier][saffier] and
[Esmerald Admin][esmerald_admin] making it simpler to show case any PoC needed.

## Requirements

* Python 3.8+
* Python virtual environment at your choice
* Docker

## Installation

1. There are two ways you can install the requirements:

    ```shell
    $ pip install -r development.txt
    ```

    Or you can simply run:

    ```shell
    $ make requirements
    ```
2. Start docker for local development.

   ```shell
   $ docker compose up
   ```
3. Export environment variables to make your development easier.

    ```shell
    $ export ESMERALD_SETTINGS_MODULE=blog.configs.development.settings.DevelopmentAppSettings
    $ export SAFFIER_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/blog
    ```
4. Run the existing migrations

    ```shell
    $ saffier migrate
    ```
5. Start the local development.
   
    ```shell
    esmerald runserver
    ```
6. Access the local documentation.

    ```shell
    http://localhost:8000/docs/swagger # for swagger
    http://localhost:8000/docs/redoc # for redoc
    http://localhost:8000/docs/stoplight # for stoplight
    ```

## Testing

To run the tests tou can simply

[esmerald]: https://esmerald.dev
[saffier]: https://saffier.tarsild.io
[esmerald_admin]: https://esmerald-admin.tarsild.io
