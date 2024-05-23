from django.core.files.images import get_image_dimensions
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


def generate_thumbnail_urls(image, request, sizes=(("small", "3"), ("medium", "2"), ("large", "1.5")), quality=90):
    if not image:
        return None

    width, height = get_image_dimensions(image)
    thumbnail_urls = {}

    for key, size in sizes:
        try:
            thumbnail = get_thumbnail(
                image, f"{int(width // float(size))}x{int(height // float(size))}", quality=quality, format="WEBP"
            )
            thumbnail_urls[key] = request.build_absolute_uri(thumbnail.url)
        except Exception as ex:
            print(f"Error generating thumbnail for size {size}: {ex}")

    return thumbnail_urls


class ThumbnailImageSerializer(serializers.Serializer):
    def to_representation(self, image):
        thumbnail_urls = generate_thumbnail_urls(image, self.context["request"])
        return thumbnail_urls


class ThumbnailMediaSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None

        image_url = media.url  # Assuming media is a Django ImageField or FileField
        thumbnail_urls = None

        if image_url.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            try:
                thumbnail_urls = generate_thumbnail_urls(media, self.context["request"])
            except Exception as ex:
                print(f"Error generating thumbnails: {ex}")

        if image_url:
            image_url = self.context["request"].build_absolute_uri(image_url)

        return {
            "original": image_url,
            "thumbnail": thumbnail_urls,
        }
