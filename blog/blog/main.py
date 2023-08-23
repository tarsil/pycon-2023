#!/usr/bin/env python
"""
Generated by 'esmerald createproject' using Esmerald 2.0.5.
"""
import os
import sys
from typing import Optional

from esmerald import Esmerald, Include, settings
from esmerald.exception_handlers import value_error_handler
from esmerald_admin import Admin
from esmerald_admin.backends.saffier.email import EmailAdminAuth
from saffier import Database, Migrate, Registry

database, registry = settings.db_access


def build_path():
    """
    Builds the path of the project and project root.
    """
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

    if SITE_ROOT not in sys.path:
        sys.path.append(SITE_ROOT)
        sys.path.append(os.path.join(SITE_ROOT, "apps"))


def get_migrations(app: "Esmerald", registry: "Registry") -> None:
    """
    Activates the migration system of Saffier with Esmerald
    """
    Migrate(app=app, registry=registry)


def get_admin(app: Esmerald, registry: Registry) -> None:
    """
    Starts the admin
    """
    from accounts.models import User

    from .admin import get_views

    auth_backend = EmailAdminAuth(
        secret_key=settings.secret_key, auth_model=User, config=settings.jwt_config
    )

    admin = Admin(app, registry.engine, authentication_backend=auth_backend)

    # Get the views function from the "admin.py"
    get_views(admin)


def get_application(connection: Optional[Database] = None, models: Optional[Registry] = None):
    """
    This is optional. The function is only used for organisation purposes.
    """
    build_path()

    db = connection or database
    app = Esmerald(
        routes=[Include(namespace="blog.urls")],
        on_startup=[db.connect],
        on_shutdown=[db.disconnect],
        exception_handlers={ValueError: value_error_handler},
    )

    # Migrations
    db_registry = models or registry
    get_migrations(app=app, registry=db_registry)

    # Admin
    get_admin(app=app, registry=db_registry)
    return app


app = get_application()
