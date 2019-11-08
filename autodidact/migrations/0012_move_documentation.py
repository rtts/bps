from django.db import migrations

def movedoc(apps, schema_editor):
    from autodidact.models import Page
    try:
        homepage = Page.objects.get(slug='')
        docs = Page.objects.get(slug='docs')
        homepage.content = docs.content
        homepage.save()
        docs.delete()
    except:
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('autodidact', '0011_clear_obsolete_cdns_from_pandocfields'),
    ]

    operations = [
        migrations.RunPython(movedoc, migrations.RunPython.noop),
    ]
