from services.news.src.presentation.request import WritablePostRequest
from services.shared.interface.validator import AbstractValidator
from services.shared.kernel.errors import Errors
from services.shared.kernel.validation_result import ValidationResult


class UpdatePostValidator(AbstractValidator[WritablePostRequest]):

    def validate(self, command: WritablePostRequest) -> ValidationResult[WritablePostRequest]:

        if not command.title:
            self.errors.add(Errors.null("title"))

        if len(command.title) < 3:
            self.errors.add(Errors.value_is_invalid("title"))

        return self.execute()
