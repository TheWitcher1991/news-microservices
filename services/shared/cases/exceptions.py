from services.shared.kernel.errors import Errors
from services.shared.kernel.result import Result


def InternalErrorResult():
    return Result.failure(Errors.internal().to_list())
