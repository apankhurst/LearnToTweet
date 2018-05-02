The fields available in each JSON item are listed below:
    - 'text'
    - 'created_at'
    - 'source'
    - 'id_str'
    - 'retweet_count'
    - 'in_reply_to_user_id_str'
    - 'favorite_count'-
    - 'is_retweet'
The only fields we care about for this project are 'text' and'is_retweet'. We may care about 'created_at' if we wish to segment data based off of time.
Also, we need to be careful about URLs and emojis appearing in Tweets and need to ensure that we don't include text that was created after the character limit was increased to 280.
