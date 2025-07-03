class PostNotFoundError(Exception):

    message = 'Post not found'

    def __str__(self):
        return PostNotFoundError.message
