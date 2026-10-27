# Storefront — Django REST API

> REST API for an online store built with Django and Django REST Framework.
> واجهة برمجية (REST API) لمتجر إلكتروني مبنية بـ Django و Django REST Framework.

## Features / المزايا

- Products and collections endpoints with full CRUD (DRF `ModelViewSet` + router)
- Store data model: products, collections, promotions, customers, orders, order items, addresses, carts
- Generic apps for **tags** and **likes** using Django content types
- Customised Django admin
- Django Debug Toolbar for development

## Tech stack

Python 3.10 · Django 4 · Django REST Framework · MySQL · Pipenv

## Project structure

```
storefront/     # project settings and root URLs
store/          # products, collections, orders, carts + API (views, serializers, urls)
store_custom/   # admin customisations
tags/           # generic tagging (Tag, TaggedItem)
likes/          # generic likes (LikedItem)
```

## Getting started / التشغيل

```bash
pipenv install
pipenv shell

cp .env.example .env        # then edit DB_* and DJANGO_SECRET_KEY
# export the variables in .env to your shell (or use a tool such as direnv)

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API

| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/store/products/` | List / create products |
| GET / PUT / PATCH / DELETE | `/store/products/<id>/` | Product details |
| GET / POST | `/store/collections/` | List / create collections |
| GET / PUT / PATCH / DELETE | `/store/collections/<id>/` | Collection details |

Admin panel: `/admin/`

## License

MIT
