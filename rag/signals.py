from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from products.models import Product


@receiver(post_save, sender=Product)
def sync_product_to_vectorstore(sender, instance, **kwargs):
    from rag.vectorstore import upsert_product
    try:
        upsert_product(instance)
        print(f"[rag-sync] محصول '{instance.name}' در vectorstore آپدیت شد.")
    except Exception as e:
        print(f"[rag-sync] خطا در آپدیت محصول {instance.id}: {e}")


@receiver(post_delete, sender=Product)
def remove_product_from_vectorstore(sender, instance, **kwargs):
    from rag.vectorstore import delete_product
    try:
        delete_product(instance.id)
        print(f"[rag-sync] محصول '{instance.name}' از vectorstore حذف شد.")
    except Exception as e:
        print(f"[rag-sync] خطا در حذف محصول {instance.id}: {e}")