from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "priority", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_title(self, value):
        cleaned = value.strip()
        if not cleaned:
            raise serializers.ValidationError("Название не может быть пустым.")
        return cleaned

    def validate_description(self, value):
        cleaned = value.strip()
        if len(cleaned) < 10:
            raise serializers.ValidationError(
                "Описание должно содержать минимум 10 символов."
            )
        return cleaned

    def validate_priority(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Приоритет должен быть от 1 до 5.")
        return value