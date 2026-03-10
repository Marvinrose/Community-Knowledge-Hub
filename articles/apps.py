from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "articles"


    def ready(self):
        import os
        if os.environ.get("RENDER") != "true":
            return

        from django.contrib.auth import get_user_model

        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password=os.environ.get("ADMIN_PASSWORD", "changeme"),
            )
