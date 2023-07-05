from cdktf_cdktf_provider_aws.dynamodb_table import DynamodbTable, DynamodbTableAttribute
from constructs import Construct

class SwiftStorage(Construct):

    table: DynamodbTable

    def __init__(self, scope: Construct, id: str):
        super().__init__(scope,id)

        self.table = DynamodbTable(self, "table",
            name = "SwiftSongs",
            billing_mode = "PAY_PER_REQUEST",
            hash_key = "id",
            attribute = [
                DynamodbTableAttribute(
                    name = "id",
                    type = "S"
                )
            ]
        )