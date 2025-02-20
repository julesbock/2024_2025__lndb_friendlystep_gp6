import os

BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

message_object = {
    "invitation_to_a_tournament": "You are invited to a tournament!",
    "tournament_entry_request": "Tournament entry request",
    "friend_request": "New friend request"
}

message_content = {
    "invitation_to_a_tournament": "has invited you to join a tournament.",
    "tournament_entry_request": "is requesting to participate in your tournament.",
    "friend_request": "has sent you a friend request."
}

first_file_name = "personnal_data"
second_file_name = "user_data"
third_file_name = "user_notifications"
first_folder_name = "conversations"