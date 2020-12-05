from rest_framework.schemas.openapi import AutoSchema


class DishSchema(AutoSchema):
    def get_operation(self, path, method):
        op = super().get_operation(path, method)
        if method == 'GET' and path == '/api/dishes/':
            op['parameters'].extend([
                {
                    "name": "sortBy",
                    "in": "query",
                    "description": "Сортировка",
                    'schema': {'type': 'string'}
                },
                {
                    "name": "ingredient_list",
                    "in": "query",
                    "description": "Вернуть только те блюда, в которые входят переднные ингредиенты",
                    'schema': {
                        'type': 'array',
                        'items': {'type': 'integer'}}
                },
                {
                    "name": "favourite",
                    "in": "query",
                    "description": "Отобразить только избранное",
                    'schema': {'type': 'string'}
                }])
        return op
