from tortoise import fields, models


class BaseModel(models.Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    status = fields.BooleanField(default=True)

    class Meta:
        abstract = True
