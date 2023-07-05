from constructs import Construct
from swift.api.index import SwiftApi
from swift.storage import SwiftStorage

class Swift(Construct):

    apiEndPoint: str

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        storage = SwiftStorage(self, "storage",)

        swiftApi = SwiftApi(self, "api", table = storage.table,)

        self.apiEndPoint = swiftApi.apiEndPoint