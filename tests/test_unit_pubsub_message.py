from presentation.schemas.pubsub_request import PubsubMessage


def test_pubsub_message_with_plain_json():
    a = {
        "message": {
            "data": '{"field": "Arielincho Test ñó"}',
            "messageId": "2182476073861316",
            "message_id": "2182476073861316",
            "publishTime": "2025-04-08T23:14:37.789Z",
            "publish_time": "2025-04-08T23:14:37.789Z",
        },
        "subscription": "projects/project-name/subscriptions/subscription-name",
    }

    parsed_a = PubsubMessage(**a["message"])

    assert isinstance(parsed_a.decoded_data, dict)
    assert parsed_a.decoded_data == {"field": "Arielincho Test ñó"}


def test_pubsub_message_with_b64_str():
    a = {
        "message": {
            "data": "ewogICAgImZpZWxkIjogIkFyaWVsaW5jaG8gVGVzdCDDscOzIgp9",
            "messageId": "2182476073861316",
            "message_id": "2182476073861316",
            "publishTime": "2025-04-08T23:14:37.789Z",
            "publish_time": "2025-04-08T23:14:37.789Z",
        },
        "subscription": "projects/project-name/subscriptions/subscription-name",
    }

    parsed_a = PubsubMessage(**a["message"])

    assert isinstance(parsed_a.decoded_data, dict)
    assert parsed_a.decoded_data == {"field": "Arielincho Test ñó"}
