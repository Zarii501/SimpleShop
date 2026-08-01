from django.core.management.base import BaseCommand

import subprocess


class Command(BaseCommand):

    help = "Update Vector Database"

    def handle(self, *args, **kwargs):

        subprocess.run(
            ["python", "rag/update_vectorstore.py"]
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Vector Database Updated."
            )
        )