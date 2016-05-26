from channels import Group


def message_ws(message):
    """
    :param message: message sent through the websocket with its text and information
    :return:
    """
    Group("django_channels_group").send({
        "text": "My group message",
    })


def listener_add(message):
    """
    :param message: message sent through the websocket with its text and information
    :return:
    """
    Group("django_channels_group").add(message.reply_channel)


def listener_discconect(message):
    """
    :param message: message sent through the websocket with its text and information
    :return:
     """
    Group("django_channels_group").discard(message.reply_channel)
