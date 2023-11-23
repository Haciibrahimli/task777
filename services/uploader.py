class Uploader:


    @staticmethod
    def upload_photo_to_blog(instance, filename):
        return f"blogs/{instance.slug}/{filename}"