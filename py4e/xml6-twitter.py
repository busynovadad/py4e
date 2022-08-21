from twarc import Twarc2, expansions
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAAKjfewEAAAAAfHj5al5EjNl4yibLJ4VYdWYgdcg%3DdPn20JMLg8pAbN6uI1o1Fyrr72BAHv2UIeUYo4iSqdFp2NLc3c")


def main():
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2022, 7, 15, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2022, 7, 19, 0, 0, 0, 0, datetime.timezone.utc)

    # This is where we specify our query as discussed in module 5
    query = "from:brento"  # -is:retweet"

    # The search_recent method call the recent search endpoint to get Tweets based on the query, start and end times
    search_results = client.search_recent(query=query, start_time=start_time, end_time=end_time, max_results=100)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        print(page, '\r\n\r\n\r\n')
        result = expansions.flatten(page)
        print('page', type(page))
        print('result', type(result))
        # print(page["entities"])
        print('========================================================')
        print(result[0])
        # for tweet in result:
        #     # Here we are printing the recent Tweet object JSON to the console
        #     print(json.dumps(tweet, indent=4))
            # js = json.dumps(tweet)
            # for u in tweet['entities']['mentions']:
            #      print(u)


if __name__ == "__main__":
    main()

