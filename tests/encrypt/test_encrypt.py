from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    message = 'myMessage'
    reversed_message = 'egasseMym'
    message_with_even_key = 'egass_eMym'
    message_with_odd_key = 'Mym_egasse'

    assert encrypt_message(message, 99) == reversed_message
    assert encrypt_message(message, 4) == message_with_even_key
    assert encrypt_message(message, 3) == message_with_odd_key

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, '3')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(9999, 3)
